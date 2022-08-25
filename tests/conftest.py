"""Contains the fixtures and configuration for the tests.

Fixtures:
    test_med: Return's a medication object for testing.
"""
from pytest import fixture
from typing import TYPE_CHECKING

from narcotics_tracker import database, order
from narcotics_tracker.enums import containers, medication_statuses, units
from narcotics_tracker.builders import medication_builder, order_builder

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
    ord_builder = order_builder.OrderBuilder()

    ord_builder.set_order_id(69_420)
    ord_builder.set_po_number("2022-ThisOne")
    ord_builder.set_date_ordered("01-02-1986")
    ord_builder.set_medication_code("Un-69420-9001")
    ord_builder.set_containers_amount(3_000_001)
    ord_builder.set_supplier("Mystical Medicine")
    ord_builder.set_supplier_order_number("BoundTree-999999")
    ord_builder.set_dea_form_number("11223344556677889900")
    ord_builder.set_date_received("13-44-2022")
    ord_builder.set_packages_received(300)
    ord_builder.set_comment("Best Order Ever.")
    ord_builder.set_status("Forgotten")
    ord_builder.set_created_date("13-44-2022")
    ord_builder.set_modified_date("34-44-2022")
    ord_builder.set_modified_by("Navi")

    test_order = ord_builder.build()
    print(test_order.order_id)

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
