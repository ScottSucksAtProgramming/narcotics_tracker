"""Contains tests for the database_rf Module."""

from abc import ABC

import pytest

from narcotics_tracker import persistence_interface


class Test_PersistenceInterface_Module:
    """Tests the behaviors of the Persistence Module.

    Behaviors Tested:
        - Persistence Interface Module can be accessed.
    """

    def test_persistence_interface_module_is_accessible(self) -> None:
        """Test that the Persistence Interface module is accessible."""
        assert persistence_interface.__doc__ != None


class Test_PersistenceInterface_Class:
    """Tests the behaviors of the Persistence Interface Class.

    Behaviors Tested:
        - Persistence Interface Class can be accessed.
        - Persistence Interface Class inherits from ABC Class."""

    def test_persistence_interface_class_exists(self) -> None:
        """Tests that the Persistence Interface class can be accessed."""
        assert persistence_interface.PersistenceInterface.__doc__ != None

    def test_persistence_interface_class_inherits(self) -> None:
        """Tests that Persistence Interface class inherits from the ABC Class.

        Test will pass if a TypeError is raised.
        """
        with pytest.raises(TypeError):
            isinstance(persistence_interface.PersistenceInterface(), ABC)
