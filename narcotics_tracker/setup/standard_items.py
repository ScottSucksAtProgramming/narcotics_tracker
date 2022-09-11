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
STANDARD_EVENTS = [
    {
        "event_id": None,
        "event_code": "IMPORT",
        "event_name": "imported",
        "description": "Used when adding pre-existing stock to the table.",
        "operator": +1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "event_id": None,
        "event_code": "ORDER",
        "event_name": "ordered",
        "description": "Used when adding new stock from a purchase order.",
        "operator": +1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "event_id": None,
        "event_code": "USE",
        "event_name": "used",
        "description": "Used when subtracting medication that was administered to a patient.",
        "operator": -1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "event_id": None,
        "event_code": "WASTE",
        "event_name": "wasted",
        "description": "Used when subtracting medication which was wasted.",
        "operator": -1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "event_id": None,
        "event_code": "DESTROY",
        "event_name": "destroyed",
        "description": "Used when subtracting medication which was destroyed through a reverse distributor.",
        "operator": -1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "event_id": None,
        "event_code": "LOSS",
        "event_name": "lost",
        "description": "Used when subtracting medication which were lost or stolen.",
        "operator": -1,
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
]

STANDARD_UNITS = [
    {
        "unit_id": None,
        "unit_code": "mcg",
        "unit_name": "Micrograms",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "unit_id": None,
        "unit_code": "mg",
        "unit_name": "Milligrams",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "unit_id": None,
        "unit_code": "g",
        "unit_name": "Grams",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
    {
        "unit_id": None,
        "unit_code": "ml",
        "unit_name": "Milliliters",
        "created_date": None,
        "modified_date": None,
        "modified_by": "Setup",
    },
]

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
