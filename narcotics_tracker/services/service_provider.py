"""Creates the services required to run the Narcotics Tracker.

    Classes: 
        ServiceProvider: Instantiates the services required to run the 
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

    def start_services(
        self,
    ) -> tuple["PersistenceService", "DateTimeService", "ConversionService"]:
        """Instantiates and returns all services.

        Returns:
            tuple(PersistenceManager, DateTimeManager, UnitConverter)
        """
        return (SQLiteManager("inventory.db"), DateTimeManager(), ConversionManager())
