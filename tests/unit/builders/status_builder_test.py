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

    test_status = (
        StatusBuilder()
        .set_table("statuses")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("Systems")
        .set_status_code("BROKEN")
        .set_status_name("Broken")
        .set_description("Used for testing purposes.")
        .build()
    )

    def test_StatusBuilder_can_be_accessed(self) -> None:
        assert StatusBuilder.__doc__ != None

    def test_returned_object_is_an_reporting_period(self) -> None:
        assert isinstance(self.test_status, Status)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_status) == {
            "table": "statuses",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "Systems",
            "status_code": "BROKEN",
            "status_name": "Broken",
            "description": "Used for testing purposes.",
        }
