"""Defines the protocol for providing services within the narcotics tracker.

Classes:
    ServiceProvider: Protocol for providing services.
"""

from typing import Protocol

from narcotics_tracker.services.interfaces.conversion import ConversionService
from narcotics_tracker.services.interfaces.datetime import DateTimeService
from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ServiceProvider(Protocol):
    """Protocol for providing services.

    ServiceProviders are intended to offer a simple way to provide the various
    utilities used by the Narcotics Tracker while allowing flexibility to add
    or change objects which provide the functionality.

    Classes using this protocol must be able to store the services and return
    instances of them using the methods and attributes declared below.

    Methods:
        persistence: Returns an instance of the object which communicates with
            the data repository.

        datetime:
            Returns an instance of the object which handles datetimes.

        conversion: Returns an instance of the object which handles unit
            conversion.
    """

    def persistence(self) -> "PersistenceService":
        """Returns an instance of the persistence service."""

        return PersistenceService

    def datetime(self) -> "DateTimeService":
        """Returns an instance of the datetime service."""

        return DateTimeService

    def conversion(self) -> "ConversionService":
        """Returns an instance of the unit conversion service."""

        return "ConversionService"
