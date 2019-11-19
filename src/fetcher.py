""" Gets all of the HTML pages required asynchronously.

This should significantly increase the speed of the program.
"""
from requests_futures.sessions import FuturesSession

from src.urls import Urls


class Fetcher:

    def __init__(self, pages_packet):
        """
        Pages structure:
        {
            URL: (String base_url->[String individual_url]),
            ...
        }
        """

        # Singleton
        self.session = FuturesSession()
        self.pages_packet = pages_packet

    def _format_urls(self):
        output = list()

        for url in Urls:
            mapper = self.pages_packet.get(url)
            pages = mapper()
            output += pages

        return output

    def get_results(self):
        """
        Fetch all HTML pages asynchronously. Return object structure:

        {
            "URL_NAME": [HTML(page)],
            ...
        }

        Use get() to get the HTML of a given page.

        :return: each page name with it's corresponding result.
        :rtype: dict
        """

        results = list()
        urls = self._format_urls()

        for url in urls:
            request = self.session.get(url)
        for url in Urls:
            value = url.value
            request = self.session.get(value)
            results.append(request.result())

        output = dict(zip([url.name for url in Urls], results))

        return output
