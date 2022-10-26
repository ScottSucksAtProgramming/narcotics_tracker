"""Handles unit testing of the service provider module.

Classes:
    Test_ServiceProvider: Unit tests the ServiceProvider Class.
"""

from narcotics_tracker.services.conversion_interface import ConversionService
from narcotics_tracker.services.datetime_interface import DateTimeService
from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.persistence_interface import PersistenceService
from narcotics_tracker.services.service_provider import ServiceProvider


class Test_ServiceProvider:
    """Unit tests the ServiceProvider Class.

    Behaviors Tested:
        - Returns usable PersistenceManager.
        - Returns usable DateTimeManager.
        - Returns usable UnitConverter.
    """

    def test_ServiceProvider_returns_persistence_service(self) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        assert isinstance(db, PersistenceService)

    def test_ServiceProvider_returns_datetime_service(self) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        assert isinstance(dt, DateTimeService)

    def test_ServiceProvider_returns_conversion_service(self) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        assert isinstance(converter, ConversionService)

    def test_persistence_service_returns_expected_results(self, reset_database) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        db.create_table("test_table", {"data": "TEXT"})

        db.add("test_table", {"data": "Hello"})

        cursor = db.read("test_table")
        data = cursor.fetchall()[0][0]

        assert data == "Hello"

    def test_datetime_service_returns_expected_result(self) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        assert dt.convert_to_timestamp("01-02-1986 14:10:00") == 505077000

    def test_conversion_service_returns_expected_results(self) -> None:
        service_provider = ServiceProvider()
        db, dt, converter = service_provider.start_services()

        answer = converter.to_standard(1, "mg")

        assert answer == 1000
