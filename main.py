"""Scape various news sources for information on events about sustainability.

Logan Czernel
logan.czernel@ucdconnect.ie

TODO: FILL OUT SIMILAR DETAILS HERE (whoever else is working on this)

7/11/2019
"""
from src.fetcher import Fetcher
from src.printer import Printer
from src.scrapers.nienvironmentlink import NiEnvironmentLink
from src.scrapers.eventbrite import EventBrite
from src.urls import Urls


def main():

    # Get all HTML asynchronously.
    fetcher = Fetcher()
    results = fetcher.get_results()

    # TODO: finish nienvironmentlink scraper
    # event_source = NiEnvironmentLink(url=Urls.NIENVIRONMENTLINK)

    event_source = EventBrite(page=results.get(Urls.EVENTBRITE.name))

    # Print events (for simple testing purposes).
    printer = Printer()
    printer.print_event_list(event_source.get_events())


if __name__ == '__main__':
    main()
