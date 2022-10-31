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
