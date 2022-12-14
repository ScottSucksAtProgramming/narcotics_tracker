"""Contains the classes which unit tests the report."""

from pytest import Function

from narcotics_tracker import commands
from narcotics_tracker.items.medications import Medication
from narcotics_tracker.reports import BiAnnualNarcoticsInventory
from narcotics_tracker.services.sqlite_manager import SQLiteManager

# pylint: disable=protected-access, missing-function-docstring, unused-argument
# pyright: reportPrivateUsage=false


class TestBiAnnualNarcoticsInventory:
    """Unit tests the report.

    Behaviors Tested:/microsoft/pyright/blob/main/docs/configuration.md
        -
    """

    def test_can_return_current_reporting_period(
        self, setup_integration_db: Function
    ) -> None:
        sq_man = SQLiteManager("integration_test.db")

        bi_annual_inventory = BiAnnualNarcoticsInventory(sq_man)
        result = bi_annual_inventory._get_current_reporting_period()
        assert result.id == 2200001

    def test_can_get_active_medications(self, setup_integration_db: Function) -> None:
        sq_man = SQLiteManager("integration_test.db")
        bi_annual_inventory = BiAnnualNarcoticsInventory(sq_man)
        med_list: list["Medication"] = bi_annual_inventory._get_active_medications()

        assert (
            med_list[0].medication_code == "fentanyl"
            and med_list[1].medication_code == "midazolam"
            and med_list[2].medication_code == "morphine"
        )

    def test_can_add_initial_report_data(self, setup_integration_db: Function) -> None:
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._medications = report._get_active_medications()

        report_dict = report._build_report_dictionary(medications)

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                },
            }
        }

        assert report_dict == expected_dict

    def test_can_return_medication_starting_amount(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        amount = report._get_starting_amount(fentanyl)

        assert amount == 149

    def test_can_add_starting_amount_to_report_dict(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            starting_amount = report._get_starting_amount(medication)
            report._report[report._period.id][medication.medication_code][
                "starting_amount"
            ] = starting_amount

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "concentration": 50.0,
                    "starting_amount": 149.0,
                },
                "midazolam": {
                    "name": "Midazolam",
                    "unit": "mg",
                    "concentration": 5.0,
                    "starting_amount": 132.68,
                },
                "morphine": {
                    "name": "Morphine",
                    "unit": "mg",
                    "concentration": 10.0,
                    "starting_amount": 69.0,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_get_total_amount_received(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        result = report._get_amount_received(fentanyl)

        assert result == 0

    def test_can_add_amount_received_to_report_dict(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            amount_received = report._get_amount_received(medication)
            report._report[report._period.id][medication.medication_code][
                "amount_received"
            ] = amount_received

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "amount_received": 0,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "amount_received": 0,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "amount_received": 0,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_get_total_amount_used(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        result = report._get_amount_used(fentanyl)

        assert result == 4.2

    def test_can_add_amount_used_to_report_dict(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            amount_used = report._get_amount_used(medication)
            report._report[report._period.id][medication.medication_code][
                "amount_used"
            ] = amount_used

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "amount_used": 4.2,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "amount_used": 2.32,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "amount_used": 0,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_get_total_amount_wasted(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        result = report._get_amount_wasted(fentanyl)

        assert result == 0

    def test_can_add_amount_wasted_to_report_dict(self, setup_integration_db: Function):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            amount_wasted = report._get_amount_wasted(medication)
            report._report[report._period.id][medication.medication_code][
                "amount_wasted"
            ] = amount_wasted

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "amount_wasted": 0,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "amount_wasted": 0,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "amount_wasted": 0,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_get_total_amount_destroyed(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        result = report._get_amount_destroyed(fentanyl)

        assert result == 69

    def test_can_add_amount_destroyed_to_report_dict(
        self, setup_integration_db: Function
    ):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            amount_destroyed = report._get_amount_destroyed(medication)
            report._report[report._period.id][medication.medication_code][
                "amount_destroyed"
            ] = amount_destroyed

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "amount_destroyed": 69,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "amount_destroyed": 72.68,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "amount_destroyed": 44,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_get_total_amount_lost(self, setup_integration_db: Function):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        fentanyl = (
            commands.ListMedications(sq_man).set_parameters({"id": 1}).execute()[0]
        )

        result = report._get_amount_lost(fentanyl)

        assert result == 0

    def test_can_add_amount_lost_to_report_dict(self, setup_integration_db: Function):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man)
        report._period = report._get_current_reporting_period()
        medications = report._get_active_medications()
        report._report = report._build_report_dictionary(medications)

        for medication in medications:
            amount_lost = report._get_amount_lost(medication)
            report._report[report._period.id][medication.medication_code][
                "amount_lost"
            ] = amount_lost

        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "amount_lost": 0,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "amount_lost": 0,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "amount_lost": 0,
                },
            }
        }

        assert report._report == expected_dict

    def test_can_calculate_ending_amount(self):
        sq_man = SQLiteManager("integration_test.db")
        report = BiAnnualNarcoticsInventory(sq_man).run()
        result = report[2200001]["fentanyl"]["ending_amount"]  # type: ignore
        assert result == 75.8

    def test_can_create_full_report_dict(self, setup_integration_db: Function):
        sq_man = SQLiteManager("integration_test.db")
        expected_dict = {
            2200001: {
                "fentanyl": {
                    "concentration": 50.0,
                    "name": "Fentanyl",
                    "unit": "mcg",
                    "starting_amount": 149.0,
                    "amount_received": 0,
                    "amount_used": 4.2,
                    "amount_wasted": 0,
                    "amount_destroyed": 69.0,
                    "amount_lost": 0,
                    "ending_amount": 75.8,
                },
                "midazolam": {
                    "concentration": 5.0,
                    "name": "Midazolam",
                    "unit": "mg",
                    "starting_amount": 132.68,
                    "amount_received": 0,
                    "amount_used": 2.32,
                    "amount_wasted": 0,
                    "amount_destroyed": 72.68,
                    "amount_lost": 0,
                    "ending_amount": 57.68,
                },
                "morphine": {
                    "concentration": 10.0,
                    "name": "Morphine",
                    "unit": "mg",
                    "starting_amount": 69.0,
                    "amount_received": 0,
                    "amount_used": 0,
                    "amount_wasted": 0,
                    "amount_destroyed": 44,
                    "amount_lost": 0,
                    "ending_amount": 25,
                },
            }
        }

        # print(BiAnnualNarcoticsInventory(sq_man).run())
        assert BiAnnualNarcoticsInventory(sq_man).run() == expected_dict
