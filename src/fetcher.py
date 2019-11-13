""" Gets all of the HTML pages required asynchronously.

This should significantly increase the speed of the program.
"""
from requests_futures.sessions import FuturesSession

from src.urls import Urls


class Fetcher:

    def __init__(self):

        # Singleton
        self.session = FuturesSession()

    def get_results(self):
        """
        Fetch all HTML pages asynchronously. Return object structure:

        {
            "URL_NAME": HTML(page),
            ...
        }

        Use get() to get the HTML of a given page.

        :return: each page name with it's corresponding result.
        :rtype: dict
        """

        results = list()

        for url in Urls:
            value = url.value
            request = self.session.get(value)
            results.append(request.result())

        output = dict(zip([url.name for url in Urls], results))

        return output
