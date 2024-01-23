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

    def test_MedicationBuilder_can_be_accessed(self) -> None:
        assert MedicationBuilder.__doc__ != None

    def test_returned_object_is_an_Medication(self, test_medication) -> None:
        assert isinstance(test_medication, Medication)

    def test_returned_object_had_expected_attributes(self, test_medication) -> None:
        assert vars(test_medication) == {
            "table": "medications",
            "id": -1,
            "created_date": 1666061200,
            "modified_date": 1666061200,
            "modified_by": "System",
            "medication_code": "apap",
            "medication_name": "Acetaminophen",
            "fill_amount": 10,
            "medication_amount": 1,
            "preferred_unit": "mcg",
            "concentration": 0.1,
            "status": "BROKEN",
        }
