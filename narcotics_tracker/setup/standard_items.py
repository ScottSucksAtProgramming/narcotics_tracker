"""Contains a library of database items which come packaged with the program.

The builders and modules allow for the creation of new items to be saved into 
the database. There are some common items which come built in with the 
Narcotics Tracker. They are contained in this module.

The setup.py script makes use of the items in this module.

Classes:


Functions:

"""

# Standard Event Types

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

# Standard Units

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

# Standard Containers

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

# Standard Statuses

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
