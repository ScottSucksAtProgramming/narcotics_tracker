"""Unit tests the Statuses Module.

Classes:

    Test_Status: Unit tests the Status Class.
"""

from narcotics_tracker.items.statuses import Status


class Test_Status:
    """Unit tests the Status Class.

    Behaviors Tested:
        - Statuses class can be accessed.
        - Statuses return expected id.
        - Statuses return expected status_code.
        - Statuses return expected status_name.
        - Statuses return expected description.
        - Statuses return expected string.
        - Statuses return expected dictionary.
    """

    test_status = Status(
        table="statuses",
        id=-1,
        status_code="BROKEN",
        status_name="Broken",
        description="Used for testing purposes.",
        created_date=1666061200,
        modified_date=1666061200,
        modified_by="Systems",
    )

    def test_status_class_can_be_accessed(self) -> None:
        assert Status.__doc__ != None

    def test_status_returned_expected_id(self) -> None:
        assert self.test_status.id == -1

    def test_statuses_return_expected_status_code(self) -> None:
        assert self.test_status.status_code == "BROKEN"

    def test_statuses_return_expected_status_name(self) -> None:
        assert self.test_status.status_name == "Broken"

    def test_statuses_return_expected_description(self) -> None:
        assert self.test_status.description == "Used for testing purposes."

    def test_adjustments_return_expected_string(self) -> None:
        assert (
            str(self.test_status)
            == "Status #-1: Broken (BROKEN) Used for testing purposes."
        )

    def test_adjustments_return_expected_dictionary(self) -> None:
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
