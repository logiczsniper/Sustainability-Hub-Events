"""Scape various news sources for information on events about sustainability.

Logan Czernel
logan.czernel@ucdconnect.ie

TODO: FILL OUT SIMILAR DETAILS HERE (whoever else is working on this)

7/11/2019
"""
from src.scrapers.nienvironmentlink import NiEnvironmentLink
from src.urls import Urls
from src.scrapers.eventbrite import EventBrite


def main():
    event_source = NiEnvironmentLink(url=Urls.NIENVIRONMENTLINK)

    print(event_source.get_events())


if __name__ == '__main__':
    main()
