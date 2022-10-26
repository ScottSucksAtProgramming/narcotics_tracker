"""Defines the interface for persistent storage."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class PersistenceService(Protocol):
    """Interface for objects managing persistent storage."""

    def add() -> None:
        ...

    def remove() -> None:
        ...

    def read() -> None:
        ...

    def update() -> None:
        ...
