import locale
import logging
import time
from concurrent.futures import ThreadPoolExecutor

from scrap import reporter, scrappers
from scrap.serializers import ArticleSerializer

logger = logging.getLogger(__name__)

LOCALE = "es_ES.utf8"

TASKS = [
    scrappers.PortalElToroScrapper,
    scrappers.CasaresOnlineScrapper,
    scrappers.CasaresHoyScrapper,
    scrappers.NuevaImagenScrapper,
    scrappers.ElOesteScrapper,
]


def scrap(Scraper):
    scraped_articles = Scraper().scrap_articles()
    created_articles = []

    start_time = time.time()
    for scraped_article in scraped_articles:
        try:
            serializer = ArticleSerializer(scraped_article)
            article = serializer.save()

            if article is not None:
                created_articles.append(article)

        except Exception as e:
            logger.error(e, exc_info=True)
            continue
    end_time = time.time()

    return {
        "scraper": Scraper.__name__,
        "stats": {
            "scraped": len(scraped_articles),
            "created": len(created_articles),
            "time": end_time - start_time,
        },
    }


def run():
    locale.setlocale(locale.LC_ALL, LOCALE)

    with ThreadPoolExecutor() as executor:
        results = executor.map(scrap, TASKS)

    reporter.report(results)
