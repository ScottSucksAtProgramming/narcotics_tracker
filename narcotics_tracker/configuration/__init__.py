"""Contains the modules needed to set up the Narcotics Tracker software.

The events, statuses, and units table serve as vocabulary control tables which 
provide the available events, statuses and units which can be used in other 
tables. This package and its modules create the standard items which are used 
at all EMS agencies. They can be returned in lists and easily added to the 
data repository.

Modules:

    standard_items: Defines the standard DataItems used for inventory tracking.

How To Use:

    The StandardItemCreator contains methods which build and return the 
    standard items as needed.

    ```python
    standard_events = StandardItemCreator().create_events()
    for event in standard_events:
        command.AddEvent().execute(event)

    standard_statuses = StandardItemCreator().create_statuses()
    for status in standard_statuses:
        command.AddStatus().execute(status)

    standard_events = StandardItemCreator().create_events()
    for unit in standard_units:
        command.AddUnit().execute(unit)
    ```
"""
