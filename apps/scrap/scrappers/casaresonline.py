from datetime import datetime
from .scrapper import Scrapper, Article, Newspaper


class CasaresOnlineNewspaper(Newspaper):
    def name(self):
        return "Casares Online"

    def url(self):
        return "https://casaresonline.com.ar/"


class CasaresOnlineArticle(Article):
    def __init__(self, soup):
        self.soup = soup

    def date(self):
        selector = self.soup.find("span", {"class": "entry-meta-date"})
        format_date = "%d %B, %Y"
        return datetime.strptime(selector.text, format_date)

    def title(self):
        return self.title_section().text

    def title_section(self):
        return self.soup.find("h3")

    def url(self):
        return self.title_section().a.get("href")

    def photo(self):
        selector = self.soup.find("img")
        return selector.get("src") if selector else ""

    def description(self):
        selector = self.soup.find_all("p")[1]
        return selector.text

    def source(self):
        return CasaresOnlineNewspaper()


class CasaresOnlineScrapper(Scrapper):
    @property
    def url(self):
        return "https://casaresonline.com.ar/"

    def scrap_articles(self):
        articles_soup = self.soup.find_all("article")
        return [CasaresOnlineArticle(soup) for soup in articles_soup]
