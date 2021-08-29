from .scrapper import Scrapper, Article, Newspaper

import dateutil.parser


class ElOesteNewspaper(Newspaper):
    def name(self):
        return "El Oeste"

    def url(self):
        return "https://www.periodicoeloeste.com"


class ElOesteArticle(Article):
    def __init__(self, soup):
        self.soup = soup

    def date(self):
        return dateutil.parser.parse(self.__date_text())

    def __date_text(self):
        return self.soup.select("time")[0].get("datetime")

    def title(self):
        return self.__url_selector().get("title")

    def __url_selector(self):
        return self.__header_selector().a

    def __header_selector(self):
        return self.soup.select(".heading")[0]

    def url(self):
        return self.__url_selector().get("href")

    def photo(self):
        selector = self.soup.find("img")
        return selector.get("src") if selector else ""

    def description(self):
        description_soup = self.soup.select(".description > p")
        return description_soup[0].text.strip() if description_soup else ""

    def is_adversiment(self):
        return "publicidad" in self.title().lower()

    def source(self):
        return ElOesteNewspaper()


class ElOesteScrapper(Scrapper):
    @property
    def url(self):
        return "https://www.periodicoeloeste.com/"

    def scrap_articles(self):
        articles = [ElOesteArticle(soup) for soup in self.articles_soup()]
        
        return [article for article in articles if not article.is_adversiment()]

    def articles_soup(self):
        return self.soup.select("article")
