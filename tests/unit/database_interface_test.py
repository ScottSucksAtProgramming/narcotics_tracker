"""Contains tests for the Database Interface Module."""

from abc import ABC

import pytest

from narcotics_tracker import database_interface


class Test_DatabaseInterface_Module:
    """Tests the behaviors of the Database Interface Module.

    Behaviors Tested:
        - Database Interface Module can be accessed.
    """

    def test_database_interface_module_is_accessible(self) -> None:
        """Test that the Database Interface module is accessible."""
        assert database_interface.__doc__ != None


class Test_DatabaseInterface_Class:
    """Tests the behaviors of the Database Interface Class.

    Behaviors Tested:
        - Database Interface Class can be accessed.
        - Database Interface Class inherits from ABC Class."""

    def test_database_interface_class_exists(self) -> None:
        """Tests that the Database Interface class can be accessed."""
        assert database_interface.DatabaseInterface.__doc__ != None

    def test_database_interface_class_inherits(self) -> None:
        """Tests that Database Interface class inherits from the ABC Class.

        Test will pass if a TypeError is raised.
        """
        with pytest.raises(TypeError):
            isinstance(database_interface.DatabaseInterface(), ABC)
