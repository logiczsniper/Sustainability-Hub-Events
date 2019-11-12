"""Scape various news sources for information on events about sustainability.

Logan Czernel
logan.czernel@ucdconnect.ie

Nikita Skobelevs
nikita.skobelevs@ucdconnect.ie

TODO: FILL OUT SIMILAR DETAILS HERE (whoever else is working on this)

7/11/2019
"""
from src.fetcher import Fetcher
from src.printer import Printer
from src.scrapers.nienvironmentlink import NiEnvironmentLink
from src.scrapers.eventbrite import EventBrite
from src.urls import Urls

from time import time


def main():

    # Get all HTML asynchronously.
    t1 = time()
    fetcher = Fetcher()
    results = fetcher.get_results()
    t2 = time()

    # Temporary for development purposes.
    print(f"Time taken: {t2-t1}")

    # TODO: check for places where exceptions may need to be handled.
    # TODO: write unit tests.

    # event_source = NiEnvironmentLink(
    # page=results.get(Urls.NIENVIRONMENTLINK.name))

    event_source = EventBrite(
        page=results.get(Urls.EVENTBRITE.name))

    # Print events (for simple testing purposes).
    printer = Printer()
    printer.print_event_list(event_source.get_events())


if __name__ == '__main__':
    main()
