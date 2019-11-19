"""Scape various news sources for information on events about sustainability.

Logan Czernel
logan.czernel@ucdconnect.ie

Nikita Skobelevs
nikita.skobelevs@ucdconnect.ie

7/11/2019
"""
from src.fetcher import Fetcher
from src.mappers import Mapper
from src.pages_packet import PagesPacket
from src.printer import Printer
from src.scrapers.nienvironmentlink import NiEnvironmentLink
from src.scrapers.eventbrite import EventBrite
from src.source_manager import SourceManager
from src.urls import Urls

from time import time


def main():

    packet = PagesPacket()

    packet.add_entry(Urls.EVENTBRITE, Mapper.eventbrite)
    packet.add_entry(Urls.NIENVIRONMENTLINK, Mapper.nienvironmentlink)

    # Get all HTML asynchronously.
    t1 = time()
    fetcher = Fetcher(packet)
    results = fetcher.get_results()
    t2 = time()

    # Temporary for development purposes.
    print(f"Time taken: {t2-t1}")

    # TODO: check for places where exceptions may need to be handled.
    # TODO: write unit tests.

    manager = SourceManager(results=results,
                            sources=[EventBrite, NiEnvironmentLink])
    manager.all_events()

    # Print events (for simple testing purposes).
    printer = Printer()
    printer.print_event_list(manager.all_events())


if __name__ == '__main__':
    main()
