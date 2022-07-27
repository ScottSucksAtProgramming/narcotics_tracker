from narcotics_tracker.medication import Medication


class TestMedication:

    def test_can_see_Medication_class(self):
        """Checks to see if Medication class is defined."""
        assert type(Medication) == type(object)

    def test_can_instantiate_Medication_object(self):
        """Check to see if Medication object can be instantiated."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert isinstance(fentanyl, Medication)

    def test_can_get_name(self):
        """Check to see if name can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.name == "Fentanyl"

    def test_can_get_dosage_in_mg(self):
        """Check to see if dosage_in_mg can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.dosage_in_mg == 0.1
