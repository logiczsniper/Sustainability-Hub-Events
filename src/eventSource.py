"""An object for operations using an event source.

All event sources should be represented using this class.
"""
from abc import ABC, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup
from bs4.element import SoupStrainer

from src.tags import Tags


class EventSource(ABC):

    def __init__(self, page):
        """
        Construct an EventHub object
        :param page: the response to the get request
        :type: str
        """

        # Only fetch tags that are used by scrapers.
        strainer = SoupStrainer(name=[tag.value for tag in Tags])

        self.page = page
        self.html = BeautifulSoup(
            self.page.content, "html.parser", parse_only=strainer)
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

    @staticmethod
    def get_url():
        """
        :return: the url of this event source.
        :rtype: str
        """
        pass

    @staticmethod
    def get_year(month):
        """
        If the month of the event is between January and current month, it is next year.
        Otherwise, it is this year.
        :param month: the month of the event.
        :type: int
        :return: the year of the event.
        :rtype: int
        """
        current_month = datetime.now().month

        if 0 <= month < current_month:
            return datetime.now().year + 1
        return datetime.now().year
