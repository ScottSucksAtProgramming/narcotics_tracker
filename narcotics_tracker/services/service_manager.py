from typing import TYPE_CHECKING

from narcotics_tracker.services.conversion_manager import (
    ConversionManager,
    ConversionService,
)
from narcotics_tracker.services.datetime_manager import DateTimeManager, DateTimeService
from narcotics_tracker.services.interfaces.service_provider import ServiceProvider
from narcotics_tracker.services.sqlite_manager import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.datetime_service import DateTimeService
    from narcotics_tracker.services.interfaces.persistence_service import (
        PersistenceService,
    )


class ServiceManager(ServiceProvider):

    _persistence: "PersistenceService" = SQLiteManager
    _database: str = "inventory.db"
    _datetime: "DateTimeService" = DateTimeManager
    _conversion: "ConversionService" = ConversionManager

    @property
    def persistence(self) -> "PersistenceService":
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
        return self._datetime()

    @datetime.setter
    def datetime(self, value: "DateTimeService"):
        self._datetime = value

    @property
    def conversion(self) -> "ConversionService":
        return self._conversion()

    @conversion.setter
    def conversion(self, value: "ConversionService"):
        self._conversion = value
