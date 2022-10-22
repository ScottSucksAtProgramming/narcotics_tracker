"""Contains a library of pre-defined database items for the Narcotics Tracker.

The builders and modules allow for the creation of new items to be saved into 
the database. The items defined in this module are used as part of the 
setup.py script to populate the database with the default items.

Classes:

    None

Functions:

    None

Items:

    Events:

        Common events which adjust the amount of medication in the inventory.

        Import Event

        Order Event

        Use Event

        Waste Event

        Destroy Event

        Loss Event

    Units:

        Common units which controlled substance medications are measured in.

        Micrograms (mcg)

        Milligrams (mg)

        Grams (g)

        Milliliters (ml)

    Containers:

        Common containers that controlled substance medications come in.

        Vial

        Pre-filled Syringe

        Pre-mixed Bag

    Statuses:

        Common statuses used for controlled substance medications and other 
            database items.

        Active (ACTIVE)

        Inactive (INACTIVE)

        Open (OPEN)

        Cancelled (CANCELLED)

        Closed (CLOSED)
"""
from typing import TYPE_CHECKING

from narcotics_tracker.items.events import Event
from narcotics_tracker.items.statuses import Status
from narcotics_tracker.items.units import Unit

if TYPE_CHECKING:
    from narcotics_tracker.items.data_items import DataItem


class StandardItemCreator:
    """Creates standard DataItems for the Narcotics Tracker."""

    standard_items = []

    def create(self) -> list["DataItem"]:
        """Creates all items and returns them in a list."""

        self._create_standard_events()
        self._create_standard_units()

        return self.standard_items

    def _create_standard_events(self) -> None:

        destroy_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "DESTROY",
            "Destroyed",
            "Used when subtracting medication which was destroyed through a reverse distributor.",
            -1,
        )
        self.standard_items.append(destroy_event)

        import_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "IMPORT",
            "Imported",
            "Used when adding pre-existing stock to the inventory.",
            +1,
        )
        self.standard_items.append(import_event)

        loss_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "LOSS",
            "Lost",
            "Used when subtracting medication which were lost or stolen.",
            -1,
        )
        self.standard_items.append(loss_event)

        order_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "ORDER",
            "Ordered",
            "Used when adding new stock from a purchase order.",
            +1,
        )
        self.standard_items.append(order_event)

        use_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "USE",
            "Used",
            "Used when subtracting medication that was administered to a patient.",
            -1,
        )
        self.standard_items.append(use_event)

        waste_event = Event(
            "events",
            None,
            None,
            None,
            "Setup",
            "WASTE",
            "Wasted",
            "Used when subtracting medication which was wasted.",
            -1,
        )
        self.standard_items.append(waste_event)

    def _create_standard_units(self) -> None:

        microgram = Unit("units", None, None, None, "Setup", "mcg", "microgram", 6)
        self.standard_items.append(microgram)

        milligram = Unit("units", None, None, None, "Setup", "mg", "milligram", 3)
        self.standard_items.append(milligram)

        gram = Unit("units", None, None, None, "Setup", "g", "gram", 0)
        self.standard_items.append(gram)

        milliliter = Unit("units", None, None, None, "Setup", "ml", "milliliter", 3)
        self.standard_items.append(milliliter)

    def _create_standard_statuses(self):

        active_status = Status(
            "statuses",
            None,
            None,
            None,
            "Setup",
            "ACTIVE",
            "Active",
            "Used for items which are still being used.",
        )
        self.standard_items.append(active_status)

        inactive_status = Status(
            "statuses",
            None,
            None,
            None,
            "Setup",
            "INACTIVE",
            "Inactive",
            "Used for items which are no longer being used.",
        )
        self.standard_items.append(inactive_status)

        open_status = Status(
            "statuses",
            None,
            None,
            None,
            "Setup",
            "OPEN",
            "Open",
            "Used for items which have not been completed.",
        )
        self.standard_items.append(open_status)

        closed_status = Status(
            "statuses",
            None,
            None,
            None,
            "Setup",
            "CLOSED",
            "Closed",
            "Used for items which have been completed.",
        )
        self.standard_items.append(closed_status)

        cancelled_status = Status(
            "statuses",
            None,
            None,
            None,
            "Setup",
            "CANCELLED",
            "Cancelled",
            "Used for items which have been cancelled.",
        )
        self.standard_items.append(cancelled_status)
