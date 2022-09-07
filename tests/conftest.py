"""Contains the fixtures and configuration used in the Testing Suite.

Testing for the Narcotics Tracker is done using pytest. This configuration 
file contains various fixtures and setting to help with testing.

Fixtures:
    test_adjustment: Builds and returns a test object from the Event Class.

    test_container: Builds and returns a test object from the Event Class.

    test_db: Connects to and returns the connection to 'test_database.db'.

    test_event: Builds and returns a test object from the Event Class.

    test_medication: Builds and returns a test object from the Medication Class.

    test_period: Builds and returns a test object from the Period Class.

    test_status: Builds and returns a test object from the Status Class.

    test_unit: Builds and returns a test object from the Unit Class.

    reset_database: Resets test_database.db for testing functions.
"""

from pytest import fixture
from typing import TYPE_CHECKING

from narcotics_tracker import (
    containers,
    database,
    events,
    inventory,
    reporting_periods,
    statuses,
    units,
)
from narcotics_tracker.builders import (
    adjustment_builder,
    container_builder,
    event_builder,
    medication_builder,
    reporting_period_builder,
    status_builder,
    unit_builder,
)

if TYPE_CHECKING:
    from narcotics_tracker import medications


@fixture
def test_adjustment() -> "inventory.Adjustment":
    """Builds and returns a test object from the Adjustment Class.

    Adjustments are used in the inventory module to make changes to the amount
    of controlled substance medications. This function uses the builder
    pattern to build a adjustment which can be used for testing.

    Review the Inventory Module for more information on adjustments and the
    inventory table.

    Review the Database Module for more information on interacting with the
    database.

    Review the Events Module for more information on Events and the event_code
    which is used as a foreign key within the inventory table.

    Review the Medications Module for more information on Medications and the
    medication_code which is used as a foreign key within the inventory table.

    How To Use:
        Pass 'test_adjustment' into the test function.

        Assign test_adjustment to a variable and use as needed.

    Returns:
        test_adjustment (inventory.Adjustment): An adjustment object for
            testing.
    """

    with database.Database("test_database_2.db") as db:

        adj_builder = adjustment_builder.AdjustmentBuilder()
        adj_builder.set_adjustment_id(-300)
        adj_builder.set_adjustment_date("2022-08-01 10:00:00")
        adj_builder.set_event_code("WASTE")
        adj_builder.set_medication_code("morphine")
        adj_builder.set_adjustment_amount(1)
        adj_builder.set_reference_id("TEST ID")
        adj_builder.set_created_date("2022-08-01 10:00:00")
        adj_builder.set_modified_date("2022-08-01 10:00:00")
        adj_builder.set_modified_by("Ambrose")

        test_adjustment = adj_builder.build(db)

        return test_adjustment


@fixture
def test_container() -> containers.Container:
    """Builds and returns a test object from the Container Class.

    Medications come in different containers. These objects are used in the
    containers vocabulary control table and the medications table. This
    function uses the builder pattern to build a adjustment which can be used
    for testing.

    Review the Database Module for more information on interacting with the
    database.

    Review the Medications Module for more information on Medications and the
    container_type attribute which uses containers.

    How To Use:
        Pass 'test_container' into the test function.

        Assign test_container to a variable and use as needed.

    Returns:
        test_container (container.Container): A container object for testing.
    """

    cont_builder = container_builder.ContainerBuilder()

    cont_builder.set_container_id(-7)
    cont_builder.set_container_code("supp")
    cont_builder.set_container_name("Suppository")
    cont_builder.set_created_date("2022-08-01 00:00:00")
    cont_builder.set_modified_date("2022-08-01 00:00:00")
    cont_builder.set_modified_by("Elodin")

    test_container = cont_builder.build()

    return test_container


@fixture
def test_event() -> events.Event:
    """Builds and returns a test object from the Event Class.

    Events are used in the events vocabulary control table and the inventory
    module to define the reason for the inventory change and select whether
    the adjustment adds or removes medication from the inventory. This
    function uses the builder pattern to build a adjustment which can be used
    for testing.

    Review the Inventory Module for more information on adjustments, the
    inventory table, and the even_code column which which uses the event_code
    as a foreign key from the events table.

    Review the Database Module for more information on interacting with the
     database.

    Review the Events Module for more information on Events and the
    event_code which is used as a foreign key within the inventory table.

    How To Use:
        Pass 'test_event' into the test function.

        Assign test_event to a variable and use as needed.

    Returns:
        test_event (event_type.EventType): An EventType object for
            testing.
    """
    e_builder = event_builder.EventBuilder()
    e_builder.set_event_id(2001)
    e_builder.set_event_code("TEST")
    e_builder.set_event_name("Test Event")
    e_builder.set_description("Used for testing the Event Class.")
    e_builder.set_operator(-1)
    e_builder.set_created_date("2022-08-26 00:00:00")
    e_builder.set_modified_date("2022-08-01 00:00:00")
    e_builder.set_modified_by("Bast")

    test_event = e_builder.build()
    return test_event


@fixture
def test_medication() -> "medications.Medication":
    """Builds and returns a test object from the Medication Class.

    Medications are used to specify medication properties in the medications
    table. They are also used in the inventory module where they're inventory
    amounts are adjusted. This function uses the builder pattern to build a
    medication object which can be used for testing.

    Review the Inventory Module for more information on adjustments, the
    inventory table, and the medication_code column which which uses the
    medication_code as a foreign key from the events table.

    Review the Database Module for more information on interacting with the
    database.

    How To Use:
        Pass 'test_med' into the test function.

        Assign test_med to a variable and use as needed.

    Returns:
        test_med (medication.Medication): A medication object for testing.
    """
    med_builder = medication_builder.MedicationBuilder()
    med_builder.set_medication_id(1)
    med_builder.set_name("Unobtanium")
    med_builder.set_code("Un-69420-9001")
    med_builder.set_container("Vial")
    med_builder.set_dose_and_unit(69.420, "mg")
    med_builder.set_fill_amount(9_001)
    med_builder.set_status("Discontinued")
    med_builder.set_created_date("01-02-1986")
    med_builder.set_modified_date("08-09-2022")
    med_builder.set_modified_by("Kvothe")

    test_med = med_builder.build()

    return test_med


@fixture
def test_period() -> reporting_periods.ReportingPeriod:
    """Builds and returns a test object from the Period Class.

    Reporting Periods are used in the reporting_periods vocabulary control
    table and the inventory module to organize adjustments into the different
    periods in which they must be reported to New York State. This function
    uses the builder pattern to build a reporting period object which can be
    used for testing.

    Review the Inventory Module for more information on adjustments, the
    inventory table, and the reporting_period column which which uses the
    reporting_period_id as a foreign key from this table.

    Review the Database Module for more information on interacting with the
    database.

    How To Use:
        Pass 'test_period' into the test function.

        Assign test_period to a variable and use as needed.

    Returns:
        test_period (period.Period): A period object for testing.
    """

    period_builder = reporting_period_builder.ReportingPeriodBuilder()

    period_builder.set_period_id(9001)
    period_builder.set_starting_date("2001-01-01 00:00:00")
    period_builder.set_ending_date("2100-06-30 00:00:00")
    period_builder.set_created_date("2022-08-01 00:00:00")
    period_builder.set_modified_date("2022-08-01 00:00:00")
    period_builder.set_modified_by("Cinder")

    test_period = period_builder.build()

    return test_period


@fixture
def test_status() -> statuses.Status:
    """Builds and returns a test object from the Status Class.

    Statuses are used in the statuses vocabulary control table and the
    Medications module to denote the status of a particular medication. This
    function uses the builder pattern to build a status object which can be
    used for testing.

    Review the Medication Module for more information on Medications, the
    medications table, and the status column which which uses the status_code
    as a foreign key from this table.

    Review the Database Module for more information on interacting with the
    database.

    How To Use:
        Pass 'test_status' into the test function.

        Assign test_status to a variable and use as needed.

    Returns:
        test_status (statuses.Status): A status object for testing.
    """

    stat_builder = status_builder.StatusBuilder()

    stat_builder.set_status_id(-19)
    stat_builder.set_status_code("ACTIVE")
    stat_builder.set_status_name("Active")
    stat_builder.set_description("Used for items which are currently in use.")
    stat_builder.set_created_date("2022-08-01 00:00:00")
    stat_builder.set_modified_date("2022-08-01 00:00:00")
    stat_builder.set_modified_by("Abenthy")

    test_status = stat_builder.build()

    return test_status


@fixture
def test_unit() -> units.Unit:
    """Builds and returns a test object from the Unit Class.

    Units are used in the units vocabulary control table, the Medication
    Module to denote the unit of measurement the medication is commonly
    measured in, the Unit Converter Module which converts between different
    units of measurements as well as the inventory module to set the amount by
    which the medication was changed. This function uses the builder pattern
    to build a unit object which can be used for testing.

    Review the Medication Module for information on medications, the
    medications table and the preferred_unit column which uses the unit_code
    as a foreign key from this table.

    Review the Inventory Module for more information on adjustments, the
    inventory table, and the amount_in_mcg column which which uses a
    medication's preferred_unit to convert the adjustment amount.

    Review the Database Module for more information on interacting with the
    database.

    How To Use:
        Pass 'test_uni' into the test function.

        Assign test_uni to a variable and use as needed.

    Returns:
        test_unit (units.unit): A unit object for testing.
    """

    u_builder = unit_builder.UnitBuilder()

    u_builder.set_unit_id(821)
    u_builder.set_unit_code("tn")
    u_builder.set_unit_name("Tina")
    u_builder.set_created_date("2022-08-01 00:00:00")
    u_builder.set_modified_date("2022-08-01 00:00:00")
    u_builder.set_modified_by("Denna")

    test_unit = u_builder.build()

    return test_unit


@fixture
def reset_database():
    """Resets test_database.db for testing functions.

    This function deletes 'data/test_database.db'.
    """
    with database.Database("test_database.db") as db:
        db.delete_database("test_database.db")
