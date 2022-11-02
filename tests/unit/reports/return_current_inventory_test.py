"""Contains the unit tests for the ReturnCurrentInventory Report.

Classes:
"""
from narcotics_tracker.reports.return_current_inventory import ReturnCurrentInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager


class Test_ReturnCurrentInventory:
    """Unit tests the ReturnCurrentInventory Report.

    Behaviors Tested:

        - Class can be accessed.
        - Receiver can be set in initializer.
    """

    def test_can_access_class(self):
        assert ReturnCurrentInventory().__doc__ != None

    def test_can_set_receiver(self):
        return_current_inventory = ReturnCurrentInventory("FakePersistenceService")

        assert return_current_inventory._receiver == "FakePersistenceService"

    def test_can_retrieve_active_medication_info(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")

        result = ReturnCurrentInventory(sq_man)._retrieve_medications()

        expected = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg"},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg"},
            {"code": "morphine", "name": "Morphine", "unit": "mg"},
        ]

        assert result == expected

    def test_can_add_amount_to_medication_dict(self, setup_integration_db):
        sq_man = SQLiteManager("integration_test.db")

        medication_info = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg"},
            {"code": "midazolam", "name": "Midazolam", "unit": "mg"},
            {"code": "morphine", "name": "Morphine", "unit": "mg"},
        ]

        result = ReturnCurrentInventory(sq_man)._add_amounts(medication_info)
        amounts = []

        for item in result:
            amounts.append(item["amount"])

        assert amounts == [19000.0, 28840000.0, 25000000.0]

    def test_can_convert_amount_to_preferred(self) -> None:
        medication_info = [
            {"code": "fentanyl", "name": "Fentanyl", "unit": "mcg", "amount": 19000.0},
            {
                "code": "midazolam",
                "name": "Midazolam",
                "unit": "mg",
                "amount": 28840000.0,
            },
            {
                "code": "morphine",
                "name": "Morphine",
                "unit": "mg",
                "amount": 25000000.0,
            },
        ]

        result = ReturnCurrentInventory()._convert_amounts_to_preferred(medication_info)
        converted_amounts = []
        for item in result:
            converted_amounts.append(item["amount"])

        assert converted_amounts == [190, 288.4, 250]
