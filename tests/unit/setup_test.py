"""Contains unit tests for the Setup Package and it's modules.

Classes:

    Test_SetupPackage: Contains all unit tests for the Setup Package.
    
"""
from narcotics_tracker import setup


class Test_SetupPackage:
    """Contains all unit tests for the Setup Package.

    Behaviors Tested:
        - Setup Package exists and can be accessed.

    """

    def test_setup_package_exists_and_can_be_accessed(self) -> None:
        """Tests that the Setup Package exists and can be accessed.

        Asserts that setup.__doc__ does not return 'None.
        """
        assert setup.__doc__ != None
