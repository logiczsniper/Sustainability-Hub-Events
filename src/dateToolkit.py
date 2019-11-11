""" Assisting the conversion to a date object.

Individual web scrapers (subclasses of EventSource) should have methods in this toolkit
to convert their date format to a more consistent date object.
"""
from datetime import datetime


class DateToolkit:

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
