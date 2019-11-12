""" Scraping from eventbrite.

"""
from datetime import datetime

from src.attributes import Attrs
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

        event_datetime = datetime.strptime(date_string, "%a, %b %d, %I:%M%p")
        # Doesn't know year in case of EventBrite
        event_datetime = event_datetime.replace(
            year=self.toolkit.get_year(event_datetime.month))

        return event_datetime.date()

    def get_events(self):
        """
        See EventSource.get_events
        """

        entries_class = "eds-media-card-content__content__principal"
        date_class = "eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1"
        title_class = "eds-is-hidden-accessible"
        link_class = "eds-media-card-content__action-link"

        entries = self.html.find_all(name=Tags.DIV.value, attrs={
                                     Attrs.CLASS: entries_class})

        for entry in entries:
            title = entry.find(name=Tags.DIV.value, attrs={
                Attrs.CLASS: title_class}).contents[0]

            event = Event.eventbrite(
                title=title,
                date=self._convert_date(entry.find(name=Tags.DIV.value, attrs={
                                        Attrs.CLASS: date_class}).contents[0]),
                link=entry.find(name=Tags.A.value, attrs={
                                Attrs.CLASS: link_class}).get(Attrs.HREF),
                scope=EventScope.NATIONAL)

        return set(self.events)
