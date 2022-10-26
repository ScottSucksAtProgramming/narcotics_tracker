"""Defines the standard DataItems used for inventory tracking.

Classes:

    StandardItemCreator: Creates and returns all

Items:

    Events:

        Destroyed (DESTROY) Used when subtracting medication which was 
            destroyed through a reverse distributor.
        
        Imported (IMPORT) Used when adding pre-existing stock to the inventory.
        
        Lost (LOSS) Used when subtracting medication which were lost or stolen.
        
        Ordered (ORDER) Used when adding new stock from a purchase order.
        
        Used (USE) Used when subtracting medication that was administered to a 
            patient.
        
        Wasted (WASTE) Used when subtracting medication which was wasted.

    Units:

        microgram (mcg).
        
        milligram (mg).
        
        gram (g).
        
        milliliter (ml).

    Statuses:
        
        Active (ACTIVE) Used for items which are still being used.
        
        Inactive (INACTIVE) Used for items which are no longer being used.
        
        Open (OPEN) Used for items which have not been completed.
        
        Closed (CLOSED) Used for items which have been completed.
        
        Cancelled (CANCELLED) Used for items which have been cancelled.
"""
from typing import TYPE_CHECKING

from narcotics_tracker.items.events import Event
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.items.units import Unit

if TYPE_CHECKING:
    from narcotics_tracker.items.interfaces.dataitem_interface import DataItem


class StandardItemCreator:
    """Creates standard DataItems for the Narcotics Tracker."""

    standard_events = []
    standard_statuses = []
    standard_units = []

    def create_events(self) -> list["Event"]:
        """Creates standard events and returns them in a list."""

        self._create_standard_events()

        return self.standard_events

    def create_statuses(self) -> list["Status"]:
        """Creates standard statuses and returns them in a list."""

        self._create_standard_statuses()

        return self.standard_statuses

    def create_units(self) -> list["Unit"]:
        """Creates standard units and returns them in a list."""

        self._create_standard_units()

        return self.standard_units

    def _create_standard_events(self) -> None:

        destroy_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "DESTROY",
            "Destroyed",
            "Used when subtracting medication which was destroyed through a reverse distributor.",
            -1,
        )
        self.standard_events.append(destroy_event)

        import_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "IMPORT",
            "Imported",
            "Used when adding pre-existing stock to the inventory.",
            +1,
        )
        self.standard_events.append(import_event)

        loss_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "LOSS",
            "Lost",
            "Used when subtracting medication which were lost or stolen.",
            -1,
        )
        self.standard_events.append(loss_event)

        order_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "ORDER",
            "Ordered",
            "Used when adding new stock from a purchase order.",
            +1,
        )
        self.standard_events.append(order_event)

        use_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "USE",
            "Used",
            "Used when subtracting medication that was administered to a patient.",
            -1,
        )
        self.standard_events.append(use_event)

        waste_event = Event(
            "events",
            None,
            1666746384,
            1666746384,
            "Setup",
            "WASTE",
            "Wasted",
            "Used when subtracting medication which was wasted.",
            -1,
        )
        self.standard_events.append(waste_event)

    def _create_standard_units(self) -> None:

        microgram = Unit(
            "units", None, 1666746384, 1666746384, "Setup", "mcg", "microgram", 6
        )
        self.standard_units.append(microgram)

        milligram = Unit(
            "units", None, 1666746384, 1666746384, "Setup", "mg", "milligram", 3
        )
        self.standard_units.append(milligram)

        gram = Unit("units", None, 1666746384, 1666746384, "Setup", "g", "gram", 0)
        self.standard_units.append(gram)

        milliliter = Unit(
            "units", 1666746384, 1666746384, None, "Setup", "ml", "milliliter", 3
        )
        self.standard_units.append(milliliter)

    def _create_standard_statuses(self):

        active_status = Status(
            "statuses",
            None,
            1666746384,
            1666746384,
            "Setup",
            "ACTIVE",
            "Active",
            "Used for items which are still being used.",
        )
        self.standard_units.append(active_status)

        inactive_status = Status(
            "statuses",
            None,
            1666746384,
            1666746384,
            "Setup",
            "INACTIVE",
            "Inactive",
            "Used for items which are no longer being used.",
        )
        self.standard_units.append(inactive_status)

        open_status = Status(
            "statuses",
            None,
            1666746384,
            1666746384,
            "Setup",
            "OPEN",
            "Open",
            "Used for items which have not been completed.",
        )
        self.standard_units.append(open_status)

        closed_status = Status(
            "statuses",
            None,
            1666746384,
            1666746384,
            "Setup",
            "CLOSED",
            "Closed",
            "Used for items which have been completed.",
        )
        self.standard_units.append(closed_status)

        cancelled_status = Status(
            "statuses",
            None,
            1666746384,
            1666746384,
            "Setup",
            "CANCELLED",
            "Cancelled",
            "Used for items which have been cancelled.",
        )
        self.standard_units.append(cancelled_status)
