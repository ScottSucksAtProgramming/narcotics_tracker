"""Contains various utility functions."""


from enum import Enum


class Utilities:
    """Contains various utility functions."""

    @staticmethod
    def enum_from_string(
        enum_class: type[Enum],
        string: str,
    ) -> Enum:
        """Returns the enum value from a string.

        Args:
            enum_class: The enum class to use.
            string: The string to convert to an enum value.

            Returns:
                The enum value.
        """

        string = string.replace(" ", "_")
        string = string.replace("-", "_")

        return enum_class[string.upper()]
