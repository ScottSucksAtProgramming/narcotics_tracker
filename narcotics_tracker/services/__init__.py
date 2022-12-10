"""Contains the services which are used by the Narcotics Tracker.

The Narcotics Tracker makes use of various utilities which have been
implemented within the modules in this package.

These services are made available through the ServiceManager which provides
instances of each service to the other modules and classes which need them.
Additional services, or replacement services, should be added to the
ServiceManager and made available using a method named for the type of service
provided.

Packages:
    interfaces: Organizes the interfaces for utility services within the
        Narcotics Tracker.

Modules:
    service_manager: Provides access to the services used by the Narcotics
        Tracker.

    conversion_manager: Handles conversion between different units.

    datetime_manager: Handles datetime functions for the Narcotics Tracker.

    sqlite_manager: Manages Communication with the SQLite3 Database.

Accessing Services:
    When a service is needed they can be instantiated by accessing the
    appropriate property in the ServiceProvider.

    Example:

        ```python
        datetime_service = ServiceProvider().datetime

        persistence_service = ServiceProvider().persistence

        conversion_service = ServiceProvider().conversion
        ```

Changing The Database:
    The ServiceProvider's database property stores the filename of the
    database file as a string. It can be changed by specifying a different
    file using that property.

    Example:

        ```python
        services = ServiceProvider()

        services.database = 'new_filename.db'

        persistence_service = services.persistence
"""
