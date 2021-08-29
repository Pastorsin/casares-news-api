from .scrapper import Scrapper, Article, Newspaper
from datetime import datetime
from bs4 import BeautifulSoup

import requests


class NuevaImagenNewspaper(Newspaper):
    def name(self):
        return "Nueva Imagen"

    def url(self):
        return "https://www.periodiconuevaimagen.com.ar"


class NuevaImagenArticle(Article):
    def __init__(self, soup):
        self.soup = soup

    def __section_soup(self):
        request = requests.get(self.url())
        return BeautifulSoup(request.content, "html.parser")

    def date(self):
        format_date = "%A, %d de %B de %Y · %H:%M"
        return datetime.strptime(self.__date_text(), format_date)

    def __date_text(self):
        selector = self.__section_soup().select(".fecha")[0]
        return selector.text.strip()

    def title(self):
        return self.__title_selector().text.strip()

    def __title_selector(self):
        return self.soup.select(".titulo")[0]

    def __domain(self):
        return self.source().url()

    def url(self):
        href = self.__title_selector().a.get("href")
        return self.__domain() + href

    def photo(self):
        selector = self.soup.img
        url = self.__domain() + selector.get("src") if selector else ""

        return url

    def description(self):
        selector = self.__section_soup().find("meta", {"name": "description"})
        return selector.get("content").strip()

    def source(self):
        return NuevaImagenNewspaper()


class NuevaImagenScrapper(Scrapper):
    @property
    def url(self):
        return "https://www.periodiconuevaimagen.com.ar/locales/"

    def scrap_articles(self):
        soups = self.articles_soup()
        return [NuevaImagenArticle(article) for article in soups]

    def articles_soup(self):
        return self.soup.find_all("article")
