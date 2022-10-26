"""Creates the services required to run the Narcotics Tracker.

    Classes: ServiceProvider: Instantiates the services required to run the 
        Narcotics Tracker.
"""

from narcotics_tracker.database import SQLiteManager
from narcotics_tracker.persistence_interface import PersistenceService
from narcotics_tracker.utils.datetime_manager import DateTimeManager
from narcotics_tracker.utils.unit_converter import UnitConverter


class ServiceProvider:
    """Instantiates the services required to run the Narcotics Tracker.

    Methods:
        start_services: Instantiates and returns all services.
    """

    def __init__(
        self,
        persistence_service: PersistenceService = SQLiteManager,
        datetime_service: DateTimeManager = DateTimeManager,
        conversion_service: UnitConverter = UnitConverter,
    ) -> None:
        """Initializes the ServiceProvider and sets the three services.

        Args:
            persistence_service (PersistenceManager, optional): The object
                which communicates with the data repository. Defaults to
                SQLiteManager.

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

    def start_services(
        self,
    ) -> tuple[PersistenceService, DateTimeManager, UnitConverter]:
        """Instantiates and returns all services.

        Returns:
            tuple(PersistenceManager, DateTimeManager, UnitConverter)
        """
        return (
            self.persistence_service("inventory.db"),
            self.datetime_service(),
            self.conversion_service(None, None, None),
        )
