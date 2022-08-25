"""Contains the classes and test which test the periods module."""

from narcotics_tracker import periods


class Test_PeriodsModule:
    """Contains all unit tests for the periods module.

    Behaviors Tested:
        - Periods module can be accessed.
    """

    def test_periods_module_can_be_accessed(self):
        """Tests that the periods module exists and can be accessed.

        Asserts that calling periods.__doc__ does not return 'None'.
        """
        assert periods.__doc__ != None
