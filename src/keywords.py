""" Holds words which, if found in the the title, the event is deemed
relevant.
"""
from enum import Enum


class Keywords(Enum):

    SUSTAIN = "sustain"
    RENEWABLE = "renewable"
    ENVIRONMENT = "environment"
    CARBON = "carbon"
    CLIMATE = "climate"
    WASTE = "waste"
    RECYCLE = "recycle"
    ECO = "eco"
    EMISSIONS = "emissions"
