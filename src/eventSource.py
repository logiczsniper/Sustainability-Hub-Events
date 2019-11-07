"""An object for operations using an event source.

All event sources should be represented using this class.
"""

from requests import get
from bs4 import BeautifulSoup


class EventSource:

    def __init__(self, url):
        """
        Construct an EventHub object
        :param url: the url to the location's web page
        :type: str
        """

        self.url = url
        self.page = get(url)
        self.html = BeautifulSoup(self.page.content, 'html5lib')
        # self.events =
