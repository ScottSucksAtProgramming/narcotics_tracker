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
from narcotics_tracker.items.events import Event
from narcotics_tracker.items.units import Unit

STANDARD_EVENTS = []

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
STANDARD_EVENTS.append(import_event)

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
STANDARD_EVENTS.append(order_event)

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
STANDARD_EVENTS.append(use_event)

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
STANDARD_EVENTS.append(waste_event)

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
STANDARD_EVENTS.append(destroy_event)

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
STANDARD_EVENTS.append(loss_event)


STANDARD_UNITS = []
microgram = Unit("units", None, None, None, "Setup", "mcg", "microgram", 6)
STANDARD_UNITS.append(microgram)

milligram = Unit("units", None, None, None, "Setup", "mg", "milligram", 3)
STANDARD_UNITS.append(milligram)

gram = Unit("units", None, None, None, "Setup", "g", "gram", 0)
STANDARD_UNITS.append(gram)

milliliter = Unit("units", None, None, None, "Setup", "ml", "milliliter", 3)
STANDARD_UNITS.append(milliliter)


STANDARD_CONTAINERS = [
    {
        "container_id": None,
        "container_code": "vial",
        "container_name": "Vial",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "container_id": None,
        "container_code": "pfs",
        "container_name": "Pre-filled Syringe",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "container_id": None,
        "container_code": "pmb",
        "container_name": "Pre-mixed Bag",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
]

STANDARD_STATUSES = [
    {
        "status_id": None,
        "status_code": "ACTIVE",
        "status_name": "Active",
        "description": "Used for items which are still being used.",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "status_id": None,
        "status_code": "INACTIVE",
        "status_name": "Inactive",
        "description": "Used for items which are no longer being used.",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "status_id": None,
        "status_code": "OPEN",
        "status_name": "Open",
        "description": "Used for orders which have not been completed.",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "status_id": None,
        "status_code": "CANCELLED",
        "status_name": "Cancelled",
        "description": "Used for orders which have been cancelled.",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "status_id": None,
        "status_code": "CLOSED",
        "status_name": "Closed",
        "description": "Used for orders which have been completed.",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
]

print(STANDARD_EVENTS)
