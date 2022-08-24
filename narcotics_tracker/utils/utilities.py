"""Contains miscellaneous utility functions."""
from enum import Enum


def enum_from_string(enum_class: type[Enum], enum_literal: str) -> Enum:
    """Returns the object from a string.

    Args:
        enum_class (type[Enum]): The enum class to use.
        enum_literal (stg): The string to convert to an enum object.

    Returns:
        Enum: The enum object.
    """
    enum_literal = enum_literal.replace(" ", "_")
    enum_literal = enum_literal.replace("-", "_")

    return enum_class[enum_literal.upper()]
