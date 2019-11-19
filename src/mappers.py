""" Contains mapping functions for each of the Urls.
"""
from src.urls import Urls


class Mapper:
    """
    Each method must have the same parameters and output.
    """

    @staticmethod
    def eventbrite():
        """
        Create a list of urls for all eventbrite variants.
        :return: all variants of eventbrite urls.
        :rtype: list
        """

        url = Urls.EVENTBRITE

        return [url.value.format(i) for i in range(1, 2)]

    @staticmethod
    def nienvironmentlink():
        """
        Create a list of urls for all nienvironmentlink variants.
        :return: all variants of nienvironmentlink urls.
        :rtype: list
        """

        url = Urls.NIENVIRONMENTLINK

        return [url.value]
