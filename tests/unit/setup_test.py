"""Contains unit tests for the Setup Package and it's modules.

Classes:

    Test_SetupPackage: Contains all unit tests for the Setup Package.
    
"""
from narcotics_tracker import configuration
from narcotics_tracker.configuration import standard_items


class Test_SetupPackage:
    """Contains all unit tests for the Setup Package.

    Behaviors Tested:
        - Setup Package exists and can be accessed.

    """

    def test_setup_package_exists_and_can_be_accessed(self) -> None:
        """Tests that the Setup Package exists and can be accessed.

        Asserts that setup.__doc__ does not return 'None.
        """
        assert configuration.__doc__ != None


class Test_StandardItemsModule:
    """Contains all unit tests for the Standard Items Module.

    Behaviors Tested:
        - Module exists can can be accessed.

    """

    def test_standard_items_module_exists_and_can_be_accessed(self) -> None:
        """Tests that the Standard Items Module exists and can be accessed.

        Asserts that setup.standard_items.__doc__ does not return None.
        """
        assert standard_items.__doc__ != None
