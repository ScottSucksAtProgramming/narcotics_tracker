"""Contains the unit tests for the StatusBuilder.

Classes:
    Test_StatusBuilder: Unit tests the StatusBuilder.
"""


from narcotics_tracker.builders.status_builder import StatusBuilder
from narcotics_tracker.items.statuses import Status


class Test_StatusBuilder:
    """Unit tests the StatusBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns a Status Object.
        - Returned object has expected attribute values.
    """

    def test_StatusBuilder_can_be_accessed(self) -> None:
        assert StatusBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(self, test_status) -> None:
        assert isinstance(test_status, Status)

    def test_returned_object_had_expected_attributes(self, test_status) -> None:
        assert vars(test_status) == {
            "table": "statuses",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "Systems",
            "status_code": "BROKEN",
            "status_name": "Broken",
            "description": "Used for testing purposes.",
        }
