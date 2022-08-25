"""Contains the fixtures and configuration for the tests.

Fixtures:
    test_med: Return's a medication object for testing.
"""
from pytest import fixture
from typing import TYPE_CHECKING

from narcotics_tracker import database, order
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder

if TYPE_CHECKING:
    from narcotics_tracker import medication, order


@fixture
def test_med() -> "medication.Medication":
    """Return a Medication object for testing.

    The test_med fixture uses the builder to create a medication object for
    testing. All the medication attributes are set with values which would not
    be valid for a medication in a real system.

    Returns:
        test_med (medication.Medication): A medication object for testing.
    """
    med_builder = medication_builder.MedicationBuilder()
    med_builder.set_medication_id(1)
    med_builder.set_name("Unobtanium")
    med_builder.set_code("Un-69420-9001")
    med_builder.set_container(containers.Container.VIAL)
    med_builder.set_dose_and_unit(69_420, units.Unit.MCG)
    med_builder.set_fill_amount(9_001)
    med_builder.set_status(medication_statuses.MedicationStatus.DISCONTINUED)
    med_builder.set_created_date("01-02-1986")
    med_builder.set_modified_date("08-09-2022")
    med_builder.set_modified_by("Kvothe")

    test_med = med_builder.build()

    return test_med


@fixture
def test_order() -> "order.Order":
    """Return an order object for testing.

    The test_order fixture uses the builder to create an order object for
    testing. All the order attributes are set with values which would not
    be valid for an order in a real system.

    Returns:
        test_med (order.Order): An order object for testing.
    """
    test_order = order.Order()

    test_order.order_id = 69_420
    test_order.po_number = "2022-ThisOne"
    test_order.date_ordered = "01-02-1986"
    test_order.medication_code = "Un-69420-9001"
    test_order.containers_amount = 3_000_001
    test_order.supplier = "Mystical Medicine"
    test_order.supplier_order_number = "BoundTree-999999"
    test_order.dea_form_number = "11223344556677889900"
    test_order.date_received = "13-44-2022"
    test_order.packages_received = 300
    test_order.comments = "Best Order Ever."
    test_order.status = "Forgotten"
    test_order.created_date = "13-44-2022"
    test_order.modified_date = "34-44-2022"
    test_order.modified_by = "Navi"

    return test_order


@fixture
def test_db() -> str:
    """Return the name of the testing database file.

    The test_db fixture returns the name of the testing database file.
    This is used in the tests to connect to the database.

    Returns:
        test_db (str): The path to the database file.
    """
    return "test_database.db"


@fixture
def database_test_set_up():
    """Resets test_database.db"""
    db = database.Database()
    db.connect("test_database.db")
    db.delete_database("test_database.db")
