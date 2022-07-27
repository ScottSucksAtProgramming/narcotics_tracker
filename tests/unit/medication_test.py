from narcotics_tracker import Medication


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

    def test_can_get_manufacturer(self):
        """Check to see if manufacturer can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.manufacturer == "Umbrella Corp"

    def test_can_get_ndc_number(self):
        """Check to see if ndc_number can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.ndc_number == "123456789"

    def test_can_get_box_quantity(self):
        """Check to see if box_quantity can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.box_quantity == 25

    def test_can_get_container_type(self):
        """Check to see if container_type can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.container_type == "Vial"

    def test_can_get_fill_amount_in_milliliters(self):
        """Check to see if fill_amount_in_milliliters can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.fill_amount_in_milliliters == 2

    def test_can_get_dosage_in_mg(self):
        """Check to see if dosage_in_mg can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.dosage_in_mg == 0.1

    def test_can_get_dose_unit(self):
        """Check to see if dose_unit can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.dose_unit == "mcg"

    def test_can_get_concentration(self):
        """Check to see if concentration can be retrieved."""

        fentanyl = Medication("Fentanyl", "Umbrella Corp", "123456789",
                              "Vial", 25, 2, 0.1, "mcg", 0.05)
        assert fentanyl.concentration == 0.05
