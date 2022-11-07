"""Contains the unit tests for the ReturnMedicationStock Report.

Classes:
"""
from narcotics_tracker.reports import ReturnMedicationStock


class Test_ReturnMedicationStock:
    """Unit tests the ReturnMedicationStock Report.

    Behaviors Tested:

        - Class can be accessed.
        - Receiver can be set in initializer."""

    def test_can_access_class(self):
        assert ReturnMedicationStock().__doc__ != None

    def test_can_set_receiver(self):
        return_medication_stock = ReturnMedicationStock("FakePersistenceService")

        assert return_medication_stock._receiver == "FakePersistenceService"


def test_can_extract_amount_from_adjustment_data():
    test_adjustments = [
        (
            1,
            1658523600,
            "IMPORT",
            "fentanyl",
            1,
            2200001,
            "2200001",
            1667351782,
            1667351782,
            "SRK",
        ),
        (
            4,
            1659212760,
            "USE",
            "fentanyl",
            2,
            2200001,
            "2200001",
            1667351782,
            1667351782,
            "SRK",
        ),
        (
            7,
            1661027838,
            "DESTROY",
            "fentanyl",
            3,
            2200001,
            "2200001",
            1667351782,
            1667351782,
            "SRK",
        ),
        (
            9,
            1661701387,
            "USE",
            "fentanyl",
            4,
            2200001,
            "2200001",
            1667351782,
            1667351782,
            "SRK",
        ),
        (
            10,
            1662580020,
            "USE",
            "fentanyl",
            5,
            2200001,
            "2200001",
            1667351782,
            1667351782,
            "SRK",
        ),
    ]

    result = ReturnMedicationStock()._extract_adjustment_amounts(test_adjustments)

    assert result == [1, 2, 3, 4, 5]
