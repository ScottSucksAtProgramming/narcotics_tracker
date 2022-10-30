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

    _persistence: "PersistenceService" = SQLiteManager
    _database: str = "inventory.db"
    _datetime: "DateTimeService" = DateTimeManager
    _conversion: "ConversionService" = ConversionManager

    @property
    def persistence(self) -> "PersistenceService":
        """Returns an instance of the persistence service."""
        return self._persistence(self._database)

    @persistence.setter
    def persistence(self, value: "PersistenceService"):
        self._persistence = value

    @property
    def database(self) -> str:
        return self._database

    @database.setter
    def database(self, value: str):
        self._database = value

    @property
    def datetime(self) -> "DateTimeService":
        """Returns an instance of the datetime service."""
        return self._datetime()

    @datetime.setter
    def datetime(self, value: "DateTimeService"):
        self._datetime = value

    @property
    def conversion(self) -> "ConversionService":
        """Returns an instance of the conversion service."""
        return self._conversion()

    @conversion.setter
    def conversion(self, value: "ConversionService"):
        self._conversion = value
