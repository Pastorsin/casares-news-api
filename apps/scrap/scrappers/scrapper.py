from abc import ABC, abstractmethod, abstractproperty

import requests
from bs4 import BeautifulSoup


class Newspaper(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def url(self):
        pass

    def __str__(self):
        return f"{self.name()}"

    def serialize(self):
        return {"name": self.name(), "url": self.url()}


class Article(ABC):

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    @abstractmethod
    def date(self):
        pass

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def photo(self):
        pass

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def source(self):
        pass

    def __str__(self):
        return f"{self.title()} - {self.source()}"


class Scrapper(ABC):
    def __init__(self):
        request = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(request.content, "html.parser")

    @property
    def headers(self):
        return {}

    @abstractproperty
    def url(self):
        pass

    @abstractmethod
    def scrap_articles(self):
        """Returns an Articles collection"""
        pass
