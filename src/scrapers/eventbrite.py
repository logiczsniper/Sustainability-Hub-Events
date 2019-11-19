""" Scraping from eventbrite.

"""
from datetime import datetime

from src.attributes import Attrs
from src.event import Event
from src.eventScopes import EventScope
from src.eventSource import EventSource
from src.tags import Tags
from src.urls import Urls


class EventBrite(EventSource):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "eventbrite"

    @staticmethod
    def get_url():
        """
        See EventSource.get_url
        """
        return Urls.EVENTBRITE.name

    def _convert_date(self, date_string):
        """
        See EventSource._convert_date
        """
        if "+" in date_string:
            date_string = date_string.split("+")[0][:-1]

        event_datetime = datetime.strptime(date_string, "%a, %b %d, %I:%M%p")
        # Doesn't know year in case of EventBrite
        event_datetime = event_datetime.replace(
            year=self.get_year(event_datetime.month))

        return event_datetime.date()

    def get_events(self):
        """
        See EventSource.get_events
        """

        main_data_spec = "search-results"
        entries_class = "eds-media-card-content__content__principal"
        date_class = "eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1"
        title_class = "eds-is-hidden-accessible"
        link_class = "eds-media-card-content__action-link"
        location_class = "card-text--truncated__one"

        entries = self.html.find(name=Tags.MAIN.value, attrs={
            Attrs.DATA_SPEC: main_data_spec}).find(
            name=Tags.DIV.value).find_all(
            name=Tags.DIV.value, attrs={Attrs.CLASS: entries_class})

        for entry in entries:
            location_div = entry.find(name=Tags.DIV.value,
                                      attrs={Attrs.CLASS: location_class})
            event = Event(
                title=entry.find(name=Tags.DIV.value, attrs={
                    Attrs.CLASS: title_class}).contents[0],
                date=self._convert_date(entry.find(name=Tags.DIV.value, attrs={
                    Attrs.CLASS: date_class}).contents[0]),
                link=entry.find(name=Tags.A.value, attrs={
                    Attrs.CLASS: link_class}).get(Attrs.HREF),
                scope=EventScope.NATIONAL,
                location=location_div.contents[0] if location_div is not None else None)

            self.events.append(event)

        return self.events
