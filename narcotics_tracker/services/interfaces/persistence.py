"""Defines the protocol for communication with data repositories.

Classes:
    PersistenceService: Protocol for communicating with a data repository.
    """

from typing import Protocol


class PersistenceService(Protocol):
    """Protocol for communicating with a data repository.

    Classes using this protocol must be able to store and retrieve data from
    the data repository using the methods declared below.

    Methods:
        add: Adds new data to the repository.

        remove: Deletes data from the repository.

        read: Returns data from the repository.

        update: Updates data in the repository.
    """

    def add():
        ...

    def remove():
        ...

    def read():
        ...

    def update():
        ...
