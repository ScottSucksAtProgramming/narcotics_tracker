"""Creates the services required to run the Narcotics Tracker.

    Classes: ServiceProvider: Instantiates the services required to run the 
        Narcotics Tracker.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.services.conversion_manager import ConversionManager
from narcotics_tracker.services.datetime_manager import DateTimeManager
from narcotics_tracker.services.sqlite_manager import SQLiteManager

if TYPE_CHECKING:
    from narcotics_tracker.services.interfaces.conversion_interface import (
        ConversionService,
    )
    from narcotics_tracker.services.interfaces.datetime_interface import DateTimeService
    from narcotics_tracker.services.interfaces.persistence_interface import (
        PersistenceService,
    )


class ServiceProvider:
    """Instantiates the services required to run the Narcotics Tracker.

    Methods:
        start_services: Instantiates and returns all services.
    """

    def __init__(
        self,
        persistence_service: "PersistenceService" = SQLiteManager,
        repository: any = "inventory.db",
        datetime_service: "DateTimeService" = DateTimeManager,
        conversion_service: "ConversionService" = ConversionManager,
    ) -> None:
        """Initializes the ServiceProvider and sets the three services.

        Args:
            persistence_service (PersistenceManager, optional): The object
                which communicates with the data repository. Defaults to
                SQLiteManager.

            repository (any, optional): Path to the data repository. Defaults
                to "inventory.db"

            datetime_service (DateTimeManager, optional): The object which
                provides datetimes and datetime conversions. Defaults to
                DateTimeManager.

            converter_service (UnitConverter, optional): The object which
                provides conversion between different units. Defaults to
                UnitConverter.
        """
        self.persistence_service = persistence_service
        self.datetime_service = datetime_service
        self.conversion_service = conversion_service
        self.database_filename = repository

    def start_services(
        self,
    ) -> tuple["PersistenceService", "DateTimeService", "ConversionService"]:
        """Instantiates and returns all services.

        Returns:
            tuple(PersistenceManager, DateTimeManager, UnitConverter)
        """
        return (
            self.persistence_service(self.database_filename),
            self.datetime_service(),
            self.conversion_service(),
        )
