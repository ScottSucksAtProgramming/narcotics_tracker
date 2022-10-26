"""Handles unit testing of the service provider module.

Classes:
    Test_ServiceProvider: Unit tests the ServiceProvider Class.
"""

from narcotics_tracker.configuration.service_provider import ServiceProvider
from narcotics_tracker.conversion_interface import ConversionService
from narcotics_tracker.datetime_interface import DateTimeService
from narcotics_tracker.persistence_interface import PersistenceService
from narcotics_tracker.utils.datetime_manager import DateTimeManager


class Test_ServiceProvider:
    """Unit tests the ServiceProvider Class.

    Behaviors Tested:
        - Returns usable PersistenceManager.
        - Returns usable DateTimeManager.
        - Returns usable UnitConverter.
    """

    def test_ServiceProvider_returns_persistence_service(self) -> None:
        assert isinstance(ServiceProvider().start_services()[0], PersistenceService)

    def test_ServiceProvider_returns_datetime_service(self) -> None:
        assert isinstance(ServiceProvider().start_services()[1], DateTimeService)

    def test_ServiceProvider_returns_conversion_service(self) -> None:
        assert isinstance(ServiceProvider().start_services()[2], ConversionService)
