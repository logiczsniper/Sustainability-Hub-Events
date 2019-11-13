""" Scraping from nienvironmentlink.

"""
from datetime import date, datetime
import calendar

from src.attributes import Attrs
from src.event import Event
from src.eventScopes import EventScope
from src.eventSource import EventSource
from src.tags import Tags


class NiEnvironmentLink(EventSource):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "nienvironmentlink"

    def _convert_date(self, date_string):
        """
        See EventSource._convert_date
        e.g. Sunday 3 November 2019
        """
        event_date = datetime.strptime(date_string, "%A %d %B %Y")

        return event_date.date()

    def get_events(self):
        """
        See EventSource.get_events
        """

        entries_class = "eventBox"
        date_class = "date"
        location_class = "venue"

        entries = self.html.find_all(name=Tags.DIV.value, attrs={
                                     Attrs.CLASS: entries_class})

        for entry in entries:
            event = Event(
                title=entry.find(Tags.H3.value).contents[0].text,
                date=self._convert_date(entry.find(name=Tags.H4.value, attrs={
                                        Attrs.CLASS: date_class}).contents[0]),
                link="https://www.nienvironmentlink.org/" +
                entry.find(name=Tags.A.value).get(Attrs.HREF),
                scope=EventScope.NATIONAL,
                location=entry.find(name=Tags.H4.value,
                                    attrs={Attrs.CLASS: location_class}).contents[0])
            self.events.append(event)

        return self.events
