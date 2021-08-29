from .scrapper import Scrapper, Article, Newspaper
from bs4 import BeautifulSoup
import dateutil.parser
import requests
import re


class PortalElToroNewspaper(Newspaper):
    def name(self):
        return "Portal El Toro"

    def url(self):
        return "https://portaleltoro.com/"


class PortalElToroArticle(Article):
    def __init__(self, soup, scrap):
        self.soup = soup
        self.scrap = scrap

    def date(self):
        return dateutil.parser.parse(self.__date_text())

    def __date_text(self):
        return self.__date_selector().get("content")

    def __date_selector(self):
        return self.__date_soup().find(
            "meta", property="article:published_time"
        )

    def __date_soup(self):
        request = requests.get(self.url(), headers=self.scrap.headers)
        return BeautifulSoup(request.content, "html.parser")

    def title(self):
        return self.soup.h3.text

    def url(self):
        return self.soup.a.get("href")

    def photo(self):
        selector = self.soup.select(".post-img")

        if selector:
            style = selector[0]["style"]
            url = re.findall("(?<=')(.*)(?=')", style)[0]

            return url
        else:
            return ""

    def description(self):
        selector = self.soup.p
        return selector.text if selector else ""

    def source(self):
        return PortalElToroNewspaper()


class PortalElToroScrapper(Scrapper):
    @property
    def url(self):
        return "https://portaleltoro.com/"

    @property
    def headers(self):
        return {"User-Agent": "curl/7.58.0"}

    def scrap_articles(self):
        soups = self.articles_soup()
        return [PortalElToroArticle(article, self) for article in soups]

    def articles_soup(self):
        # main = self.soup.select("main")[0]
        return self.soup.select(".post-boxed")
