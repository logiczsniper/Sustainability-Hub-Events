""" Assisting the conversion to a date object.

Individual web scrapers (subclasses of EventSource) should have methods in this toolkit
to convert their date format to a more consistent date object.
"""
from datetime import datetime


class DateToolkit:

    @staticmethod
    def date_to_int(date, calendar_type):
        """
        Converts a day or month (full or short) to an int representation.
        :param date: the full or short day or month name.
        :type: str
        :param calendar_type: one of the following ONLY: calendar.month_name
                                                         calendar.month_abbr
                                                         calendar.day_name
                                                         calendar.day_abbr
        :type: list
        :return: the int equivalent of the input_month, upon failure returns 0
        :rtype: int
        """
        mapping = {name: num for num, name in enumerate(calendar_type) if num}
        return mapping[date]

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
