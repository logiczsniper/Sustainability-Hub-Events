""" Scraping from eventbrite.

"""
from datetime import date
import calendar

from src.event import Event
from src.eventScopes import EventScope
from src.eventSource import EventSource
from src.tags import Tags


class EventBrite(EventSource):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "eventbrite"

    def _convert_date(self, date_string):
        """
        See EventSource._convert_date
        """

        sliced_date = date_string.split(", ")

        try:
            month = (self.toolkit.date_to_int(sliced_date[1].split(" ")[0], calendar_type=calendar.month_abbr))
            day = int(sliced_date[1].split(" ")[1])
        except ValueError:
            print("ERROR:   Failed to create date object. Conversion to int failed.")
            return date(0, 0, 0)

        year = self.toolkit.get_year(month)

        return date(year, month, day)

    def get_events(self):
        """
        See EventSource.get_events
        """

        entries_class = "eds-media-card-content__content__principal"
        date_class = "eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1"
        title_class = "eds-is-hidden-accessible"
        link_class = "eds-media-card-content__action-link"

        entries = self.html.find_all(name=Tags.DIV, attrs={self.CLASS: entries_class})

        for entry in entries:
            event = Event.eventbrite(
                title=entry.find(name=Tags.DIV, attrs={self.CLASS: title_class}).contents[0],
                date=self._convert_date(entry.find(name=Tags.DIV, attrs={self.CLASS: date_class}).contents[0]),
                link=entry.find(name=Tags.A, attrs={self.CLASS: link_class}).get("href"),
                scope=EventScope.NATIONAL)
            self.events.append(event)

        return self.events
