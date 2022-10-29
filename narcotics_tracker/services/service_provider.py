from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.sqlite_manager import SQLiteManager
from narcotics_tracker.services.unit_conversion import ConversionManager


class ServiceProvider:

    _persistence = SQLiteManager
    _database = "inventory.db"
    _datetime = DateTimeManager
    _conversion = ConversionManager

    @property
    def persistence(self) -> object:
        return self._persistence(self._database)

    @persistence.setter
    def persistence(self, value: object):
        self._persistence = value

    @property
    def database(self) -> str:
        return self._database

    @database.setter
    def database(self, value: str):
        self._database = value

    @property
    def datetime(self: object) -> object:
        return self._datetime()

    @datetime.setter
    def datetime(self, value: object):
        self._datetime = value

    @property
    def conversion(self) -> object:
        return self._conversion()

    @conversion.setter
    def conversion(self, value: object):
        self._conversion = value
