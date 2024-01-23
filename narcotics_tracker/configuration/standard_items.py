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

    _standard_events: list["Event"] = []
    _standard_statuses: list["Status"] = []
    _standard_units: list["Unit"] = []

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

    def _create_standard_events(self):
        """Builds the standard events and returns in a list."""
        events_list = []

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("DESTROY")
        event_builder.set_event_name("Destroyed")
        event_builder.set_description(
            "Used when subtracting medication which was destroyed through a reverse distributor."
        )
        event_builder.set_modifier(-1)
        destroy_event = event_builder.build()

        events_list.append(destroy_event)

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("IMPORT")
        event_builder.set_event_name("Imported")
        event_builder.set_description(
            "Used when adding pre-existing stock to the inventory."
        )
        event_builder.set_modifier(+1)

        import_event = event_builder.build()
        events_list.append(import_event)

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("LOSS")
        event_builder.set_event_name("Lost")
        event_builder.set_description(
            "Used when subtracting medication which were lost or stolen."
        )
        event_builder.set_modifier(-1)

        loss_event = event_builder.build()
        events_list.append(loss_event)

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("ORDER")
        event_builder.set_event_name("Ordered")
        event_builder.set_description(
            "Used when adding new stock from a purchase order."
        )
        event_builder.set_modifier(+1)

        order_event = event_builder.build()
        events_list.append(order_event)

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("USE")
        event_builder.set_event_name("Used")
        event_builder.set_description(
            "Used when subtracting medication that was administered to a patient."
        )
        event_builder.set_modifier(-1)

        use_event = event_builder.build()
        events_list.append(use_event)

        event_builder = EventBuilder()
        event_builder.set_table("events")
        event_builder.set_id(None)
        event_builder.set_created_date()
        event_builder.set_modified_date()
        event_builder.set_modified_by("System")
        event_builder.set_event_code("WASTE")
        event_builder.set_event_name("Wasted")
        event_builder.set_description(
            "Used when subtracting medication which was wasted."
        )
        event_builder.set_modifier(-1)

        waste_event = event_builder.build()
        events_list.append(waste_event)

        self._standard_events = events_list

    def _create_standard_units(self):
        """Builds the standard units and returns in a list."""
        unit_builder = UnitBuilder()
        unit_builder.set_table("units")
        unit_builder.set_id()
        unit_builder.set_created_date()
        unit_builder.set_modified_date()
        unit_builder.set_modified_by("Setup")
        unit_builder.set_unit_code("mcg")
        unit_builder.set_unit_name("microgram")
        unit_builder.set_decimals(-6)

        microgram = unit_builder.build()
        self._standard_units.append(microgram)

        unit_builder = UnitBuilder()
        unit_builder.set_table("units")
        unit_builder.set_id()
        unit_builder.set_created_date()
        unit_builder.set_modified_date()
        unit_builder.set_modified_by("Setup")
        unit_builder.set_unit_code("mg")
        unit_builder.set_unit_name("milligram")
        unit_builder.set_decimals(-3)

        milligram = unit_builder.build()
        self._standard_units.append(milligram)

        unit_builder = UnitBuilder()
        unit_builder.set_table("units")
        unit_builder.set_id()
        unit_builder.set_created_date()
        unit_builder.set_modified_date()
        unit_builder.set_modified_by("Setup")
        unit_builder.set_unit_code("g")
        unit_builder.set_unit_name("gram")
        unit_builder.set_decimals(0)

        gram = unit_builder.build()
        self._standard_units.append(gram)

        unit_builder = UnitBuilder()
        unit_builder.set_table("units")
        unit_builder.set_id()
        unit_builder.set_created_date()
        unit_builder.set_modified_date()
        unit_builder.set_modified_by("Setup")
        unit_builder.set_unit_code("ml")
        unit_builder.set_unit_name("milliliter")
        unit_builder.set_decimals(-3)

        milliliter = unit_builder.build()
        self._standard_units.append(milliliter)

        unit_builder = UnitBuilder()
        unit_builder.set_table("units")
        unit_builder.set_id()
        unit_builder.set_created_date()
        unit_builder.set_modified_date()
        unit_builder.set_modified_by("Setup")
        unit_builder.set_unit_code("std")
        unit_builder.set_unit_name("standard")
        unit_builder.set_decimals(-8)

        standard_unit = unit_builder.build()
        self._standard_units.append(standard_unit)

    def _create_standard_statuses(self):
        """Builds the standard statuses and returns in a list."""
        status_list = []

        status_builder = StatusBuilder()
        status_builder.set_table("statuses")
        status_builder.set_id(None)
        status_builder.set_created_date()
        status_builder.set_modified_date()
        status_builder.set_modified_by("System")
        status_builder.set_status_code("ACTIVE")
        status_builder.set_status_name("Active")
        status_builder.set_description("Used for items which are still being used.")

        active_status = status_builder.build()
        status_list.append(active_status)

        status_builder = StatusBuilder()
        status_builder.set_table("statuses")
        status_builder.set_id(None)
        status_builder.set_created_date()
        status_builder.set_modified_date()
        status_builder.set_modified_by("System")
        status_builder.set_status_code("INACTIVE")
        status_builder.set_status_name("Inactive")
        status_builder.set_description("Used for items which are no longer being used.")

        inactive_status = status_builder.build()
        status_list.append(inactive_status)

        status_builder = StatusBuilder()
        status_builder.set_table("statuses")
        status_builder.set_id(None)
        status_builder.set_created_date()
        status_builder.set_modified_date()
        status_builder.set_modified_by("System")
        status_builder.set_status_code("OPEN")
        status_builder.set_status_name("Open")
        status_builder.set_description("Used for items which have not been completed.")

        open_status = status_builder.build()
        status_list.append(open_status)

        status_builder = StatusBuilder()
        status_builder.set_table("statuses")
        status_builder.set_id(None)
        status_builder.set_created_date()
        status_builder.set_modified_date()
        status_builder.set_modified_by("System")
        status_builder.set_status_code("CLOSED")
        status_builder.set_status_name("Closed")
        status_builder.set_description("Used for items which have been completed.")

        closed_status = status_builder.build()
        status_list.append(closed_status)

        status_builder = StatusBuilder()
        status_builder.set_table("statuses")
        status_builder.set_id(None)
        status_builder.set_created_date()
        status_builder.set_modified_date()
        status_builder.set_modified_by("System")
        status_builder.set_status_code("CANCELLED")
        status_builder.set_status_name("Cancelled")
        status_builder.set_description("Used for items which have been cancelled.")

        cancelled_status = status_builder.build()
        status_list.append(cancelled_status)

        self._standard_statuses = status_list
