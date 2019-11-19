""" Manages all the event source classes.
"""


from src.keywords import Keywords


class SourceManager:

    def __init__(self, results, sources):

        self.results = results
        self.sources = sources
        self.scrapers = self.build_sources()

    def build_sources(self):

        scrapers = list()

        for source in self.sources:

            page = self.results.get(source.get_url())
            new_scraper = source(page=page)
            scrapers.append(new_scraper)

        return scrapers

    def _events(self):
        """
        Get unfiltered events from all scrapers.
        :rtype: list
        """

        return [scraper.get_events() for scraper in self.scrapers]

    def all_events(self):
        """
        Filtering out duplicate events by title and date,
        also removing events with none of the keywords.
        :return: Event objects from the instance of EventSource.
        :rtype: list
        """
        events = self._events()
        titles = [event.title for event in events]
        dates = [event.date for event in events]

        for event in events:
            title = event.title
            date = event.date

            if titles.count(title) > 1 and dates.count(date) > 1 or not self._check_title(title):
                events.remove(event)

        return events

    @staticmethod
    def _check_title(title):
        """
        Check whether or not the title is relevant.
        :param title: the title to check.
        :return: True if valid title, False else.
        :rtype: bool
        """

        # TODO: fix me

        overlaps = [word if word.value.lower() in title.lower() else None for word in Keywords]
        return overlaps != [None] * Keywords.__len__()
