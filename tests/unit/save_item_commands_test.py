"""Contains the unit tests for the Commands Module.

Classes:
    Test_AddMedication: Unit tests the AddMedication command.
"""


from typing import TYPE_CHECKING

import pytest

from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.commands import AddMedication

if TYPE_CHECKING:
    from narcotics_tracker.items.medications import Medication


@pytest.fixture
def test_med() -> "Medication":
    med_builder = (
        MedicationBuilder()
        .set_table("medications")
        .set_id(-1)
        .set_created_date(1666061200)
        .set_modified_date(1666061200)
        .set_modified_by("SRK")
        .set_medication_code("apap")
        .set_medication_name("Acetaminophen")
        .set_fill_amount(10)
        .set_medication_amount(1)
        .set_preferred_unit("dg")
        .set_concentration()
        .set_status("unknown")
    )

    return med_builder.build()


class Test_AddMedication:
    """Unit tests the AddMedication command.

    Behaviors Tested:
        - DataItem information is extracted correctly.
        - Table name is extracted correctly.
    """

    def test_AddMedication_extracts_medication_data_correctly(self, test_med) -> None:
        test_med = test_med
        command = AddMedication(None, test_med)

        command._extract_medication_info()

        assert command.medication_info == {
            "table": "medications",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "medication_code": "apap",
            "medication_name": "Acetaminophen",
            "fill_amount": 10,
            "medication_amount": 1,
            "preferred_unit": "dg",
            "concentration": 0.1,
            "status": "unknown",
        }

    def test_AddMedication_extracts_table_name_correctly(self, test_med) -> None:
        test_med = test_med
        command = AddMedication(None, test_med)
        command._extract_medication_info()
        table_name = command._pop_table_name()

        assert table_name == "medications"
