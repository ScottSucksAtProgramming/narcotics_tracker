"""Contains the ServiceManager which sets and provides services.

Classes:
    ServiceManager: Provides access to the services used by the Narcotics
        Tracker.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.services.conversion_manager import ConversionManager
from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.interfaces.service_provider import ServiceProvider
from narcotics_tracker.services.sqlite_manager import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.conversion import ConversionService
    from narcotics_tracker.services.interfaces.datetime import DateTimeService
    from narcotics_tracker.services.interfaces.persistence import PersistenceService


class ServiceManager(ServiceProvider):
    """Provides access to the services used by the Narcotics Tracker.

    Properties:
        persistence: Assigns and returns an instance of the persistence
            service.

        database: Assigns and returns the filename of the database file if
            used.

        datetime: Assigns and returns an instance of the datetime service.

        conversion: Returns an instance of the conversion service.
    """

    _database: str = "inventory.db"
    _persistence = SQLiteManager(_database)
    _datetime = DateTimeManager()
    _conversion = ConversionManager()

    @property
    def persistence(self) -> "PersistenceService":
        """Returns an instance of the persistence service."""
        return self._persistence

    @persistence.setter
    def persistence(self, value: "PersistenceService"):
        self._persistence = value

    @property
    def database(self) -> str:
        """Assigns and returns the filename of the database file if used."""
        return self._database

    @database.setter
    def database(self, value: str):
        self._database: str = value

    @property
    def datetime(self) -> "DateTimeService":
        """Returns an instance of the datetime service."""
        return self._datetime

    @datetime.setter
    def datetime(self, value: "DateTimeService"):
        self._datetime = value

    @property
    def conversion(self) -> "ConversionService":
        """Returns an instance of the conversion service."""
        return self._conversion

    @conversion.setter
    def conversion(self, value: "ConversionService"):
        self._conversion = value
