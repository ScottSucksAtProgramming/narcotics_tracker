from narcotics_tracker.medication import Medication


class TestMedication:

    def test_can_see_Medication_class(self):
        """Can we see the Medications class?"""
        assert type(Medication) == type(object)
