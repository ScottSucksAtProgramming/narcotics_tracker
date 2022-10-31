"""Defines the standard DataItems used for inventory tracking.

Classes:

    StandardItemCreator: Creates standard DataItems for the Narcotics Tracker.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.builders.event_builder import EventBuilder
from narcotics_tracker.builders.status_builder import StatusBuilder
from narcotics_tracker.builders.unit_builder import UnitBuilder

if TYPE_CHECKING:
    from narcotics_tracker.items.events import Event
    from narcotics_tracker.items.statuses import Status
    from narcotics_tracker.items.units import Unit


class StandardItemCreator:
    """Creates standard DataItems for the Narcotics Tracker.

    Methods:

        create_events: Creates standard events and returns them in a list.

        create_statuses: Creates standard statuses and returns them in a list.

        create_units: Creates standard units and returns them in a list.
    """

    _standard_events = []
    _standard_statuses = []
    _standard_units = []

    def create_events(self) -> list["Event"]:
        """Creates standard events and returns them in a list."""
        self._create_standard_events()

        return self._standard_events

    def create_statuses(self) -> list["Status"]:
        """Creates standard statuses and returns them in a list."""
        self._create_standard_statuses()

        return self._standard_statuses

    def create_units(self) -> list["Unit"]:
        """Creates standard units and returns them in a list."""
        self._create_standard_units()

        return self._standard_units

    def _create_standard_events(self) -> list["Event"]:
        """Builds the standard events and returns in a list."""
        destroy_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("DESTROY")
            .set_event_name("Destroyed")
            .set_description(
                "Used when subtracting medication which was destroyed through a reverse distributor."
            )
            .set_modifier(-1)
            .build()
        )
        self._standard_events.append(destroy_event)

        import_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("IMPORT")
            .set_event_name("Imported")
            .set_description("Used when adding pre-existing stock to the inventory.")
            .set_modifier(+1)
            .build()
        )
        self._standard_events.append(import_event)

        loss_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("LOSS")
            .set_event_name("Lost")
            .set_description(
                "Used when subtracting medication which were lost or stolen."
            )
            .set_modifier(-1)
            .build()
        )
        self._standard_events.append(loss_event)

        order_event = loss_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("ORDER")
            .set_event_name("Ordered")
            .set_description("Used when adding new stock from a purchase order.")
            .set_modifier(+1)
            .build()
        )
        self._standard_events.append(order_event)

        use_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("USE")
            .set_event_name("Used")
            .set_description(
                "Used when subtracting medication that was administered to a patient."
            )
            .set_modifier(-1)
            .build()
        )
        self._standard_events.append(use_event)

        waste_event = (
            EventBuilder()
            .set_table("events")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_event_code("WASTE")
            .set_event_name("Wasted")
            .set_description("Used when subtracting medication which was wasted.")
            .set_modifier(-1)
            .build()
        )
        self._standard_events.append(waste_event)

    def _create_standard_units(self) -> list["Unit"]:
        """Builds the standard units and returns in a list."""
        microgram = (
            UnitBuilder()
            .set_id()
            .set_table("units")
            .set_created_date()
            .set_modified_date()
            .set_modified_by("Setup")
            .set_unit_code("mcg")
            .set_unit_name("microgram")
            .set_decimals(-6)
            .build()
        )
        self._standard_units.append(microgram)

        milligram = (
            UnitBuilder()
            .set_id()
            .set_table("units")
            .set_created_date()
            .set_modified_date()
            .set_modified_by("Setup")
            .set_unit_code("mg")
            .set_unit_name("milligram")
            .set_decimals(-3)
            .build()
        )
        self._standard_units.append(milligram)

        gram = (
            UnitBuilder()
            .set_id()
            .set_table("units")
            .set_created_date()
            .set_modified_date()
            .set_modified_by("Setup")
            .set_unit_code("g")
            .set_unit_name("gram")
            .set_decimals(0)
            .build()
        )
        self._standard_units.append(gram)

        milliliter = (
            UnitBuilder()
            .set_id()
            .set_table("units")
            .set_created_date()
            .set_modified_date()
            .set_modified_by("Setup")
            .set_unit_code("ml")
            .set_unit_name("milliliter")
            .set_decimals(-3)
            .build()
        )
        self._standard_units.append(milliliter)

        standard_unit = (
            UnitBuilder()
            .set_id()
            .set_table("units")
            .set_created_date()
            .set_modified_date()
            .set_modified_by("Setup")
            .set_unit_code("std")
            .set_unit_name("standard")
            .set_decimals(-8)
            .build()
        )
        self._standard_units.append(standard_unit)

    def _create_standard_statuses(self) -> list["Status"]:
        """Builds the standard statuses and returns in a list."""
        active_status = (
            StatusBuilder()
            .set_table("statuses")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_status_code("ACTIVE")
            .set_status_name("Active")
            .set_description("Used for items which are still being used.")
            .build()
        )
        self._standard_statuses.append(active_status)

        inactive_status = (
            StatusBuilder()
            .set_table("statuses")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_status_code("INACTIVE")
            .set_status_name("Inactive")
            .set_description("Used for items which are no longer being used.")
            .build()
        )
        self._standard_statuses.append(inactive_status)

        open_status = (
            StatusBuilder()
            .set_table("statuses")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_status_code("OPEN")
            .set_status_name("Open")
            .set_description("Used for items which have not been completed.")
            .build()
        )
        self._standard_statuses.append(open_status)

        closed_status = (
            StatusBuilder()
            .set_table("statuses")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_status_code("CLOSED")
            .set_status_name("Closed")
            .set_description("Used for items which have been completed.")
            .build()
        )
        self._standard_statuses.append(closed_status)

        cancelled_status = (
            StatusBuilder()
            .set_table("statuses")
            .set_id(None)
            .set_created_date()
            .set_modified_date()
            .set_modified_by("System")
            .set_status_code("CANCELLED")
            .set_status_name("Cancelled")
            .set_description("Used for items which have been cancelled.")
            .build()
        )
        self._standard_statuses.append(cancelled_status)
