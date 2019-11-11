"""An object for operations using an event source.

All event sources should be represented using this class.
"""
from abc import ABC, abstractmethod

from requests import get
from bs4 import BeautifulSoup

from src.dateToolkit import DateToolkit


class EventSource(ABC):

    def __init__(self, page):
        """
        Construct an EventHub object
        :param page: the response to the get request
        :type: str
        """

        self.page = page
        self.html = BeautifulSoup(self.page.content, "html.parser")
        self.toolkit = DateToolkit()
        self.events = list()

    @abstractmethod
    def _convert_date(self, date_string):
        """
        Every EventSource MUST override this method.
        :param date_string: the date as scraped from this particular EventSource.
        :type: str
        :return: the datetime object equivalent of the date string
        :rtype: datetime.date
        """
        pass

    @abstractmethod
    def get_events(self):
        """
        Every EventSource MUST override this method.
        :return: Event objects from the instance of EventSource.
        :rtype: list
        """
        pass
