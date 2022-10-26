"""Defines the interface for datetime objects.

Classes:
    DateTimeService: Interface for date and time providers."""


from typing import Protocol, runtime_checkable


@runtime_checkable
class DateTimeService(Protocol):
    """Interface for date and time providers."""

    def return_current_datetime(self) -> int:
        ...

    def convert_to_timestamp(self) -> int:
        ...

    def convert_to_string(self) -> str:
        ...
