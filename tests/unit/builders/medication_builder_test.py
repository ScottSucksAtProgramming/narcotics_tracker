"""Contains the unit tests for the MedicationBuilder.

Classes:
    Test_MedicationBuilder: Unit tests the MedicationBuilder.
"""


from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.items.medications import Medication


class Test_MedicationBuilder:
    """Unit tests the MedicationBuilder.

    Behaviors Tested:
        - Can be accessed.
        - Returns a Medication Object.
        - Returned object has expected attribute values.
    """

    test_medication = (
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
        .set_preferred_unit("mcg")
        .set_concentration()
        .set_status("unknown")
        .build()
    )

    def test_MedicationBuilder_can_be_accessed(self) -> None:
        assert MedicationBuilder.__doc__ != None

    def test_returned_object_is_an_Medication(self) -> None:
        assert isinstance(self.test_medication, Medication)

    def test_returned_object_had_expected_attributes(self) -> None:
        assert vars(self.test_medication) == {
            "table": "medications",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "SRK",
            "medication_code": "apap",
            "medication_name": "Acetaminophen",
            "fill_amount": 10,
            "medication_amount": 1,
            "preferred_unit": "mcg",
            "concentration": 0.1,
            "status": "unknown",
        }
