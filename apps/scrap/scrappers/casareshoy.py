import requests
import dateutil.parser
from bs4 import BeautifulSoup
from .scrapper import Scrapper, Article, Newspaper


class CasaresHoyNewspaper(Newspaper):
    def name(self):
        return "Casares Hoy"

    def url(self):
        return "https://casareshoy.com.ar/"


class CasaresHoyArticle(Article):
    def __init__(self, soup):
        self.soup = soup

    def date(self):
        return dateutil.parser.parse(self.__date_text())

    def __date_text(self):
        """Date format is: "%Y-%m-%dT%H:%M:%S+00:00"
        Example: "2019-08-12T18:10:08+00:00"
        """
        selector = self.__date_soup().find(
            "meta", {"property": "article:published_time"}
        )
        return self.__cleaned_date(date_text=selector.get("content"))

    def __date_soup(self):
        request = requests.get(self.url())
        return BeautifulSoup(request.content, "html.parser")

    def __cleaned_date(self, date_text):
        return date_text.split("+")[0]

    def title(self):
        return self.__title_section().text

    def __title_section(self):
        return self.soup.find("h2", {"class": "entry-title"})

    def url(self):
        return self.__title_section().a.get("href")

    def photo(self):
        selector = self.soup.find("img")
        return selector.get("src") if selector else ""

    def description(self):
        selector = self.soup.find("div", "entry-content")
        return selector.text if selector else ""

    def source(self):
        return CasaresHoyNewspaper()


class CasaresHoyScrapper(Scrapper):
    @property
    def url(self):
        return "https://casareshoy.com.ar/"

    def scrap_articles(self):
        blog_posts = self.soup.find("div", {"id": "main-box-7"})
        articles_soup = blog_posts.find_all("article")
        return [CasaresHoyArticle(soup) for soup in articles_soup]
