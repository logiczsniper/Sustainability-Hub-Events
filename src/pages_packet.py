""" Provides a structure for parameters of Fetcher.
"""
from src.urls import Urls


class PagesPacket(dict):

    def __init__(self):
        super().__init__()

    def add_entry(self, url, mapper):

        assert url in Urls
        assert callable(mapper)

        self[url] = mapper
