"""
This script contains a CLI application for adding various entities to the 
database including adjustments, events, medications, reporting periods, 
statuses, and units.
"""

import click
from datetime import datetime
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.builders.event_builder import EventBuilder
from narcotics_tracker.builders.medication_builder import MedicationBuilder
from narcotics_tracker.builders.reporting_period_builder import ReportingPeriodBuilder
from narcotics_tracker.builders.status_builder import StatusBuilder
from narcotics_tracker.builders.unit_builder import UnitBuilder
from narcotics_tracker.commands.adjustment_commands import AddAdjustment
from narcotics_tracker.commands.event_commands import AddEvent
from narcotics_tracker.commands.medication_commands import AddMedication
from narcotics_tracker.commands.reporting_period_commands import AddReportingPeriod
from narcotics_tracker.commands.status_commands import AddStatus
from narcotics_tracker.commands.unit_commands import AddUnit


@click.group()
def cli():
    """
    Define a command line group using Click.
    """
    pass


@click.group()
def add():
    """
    A decorator that creates a new Click group. The decorated function, instead 
    of being a command, will act as a container of subcommands.
    """
    pass


def get_current_timestamp():
    """
    Return the current timestamp as an integer.
    """
    return int(datetime.now().timestamp())


cli.add_command(add)


@add.command("adjustment")
@click.argument("adjustment_date", type=str)
@click.argument("adjustment_time", type=str)
@click.argument("event_code", type=str)
@click.argument("medication_code", type=str)
@click.argument("adjustment_amount", type=float)
@click.argument("reference_id", type=str)
@click.argument("reporting_period_id", type=int)
@click.argument("modified_by", type=str)
def add_adjustment(
    adjustment_date,
    adjustment_time,
    event_code,
    medication_code,
    adjustment_amount,
    reference_id,
    reporting_period_id,
    modified_by,
):
    """Logs an inventory adjustment to the database."""
    full_date = f"{adjustment_date} {adjustment_time}"
    adj_builder = AdjustmentBuilder()
    adj_builder.set_table("inventory")
    adj_builder.set_adjustment_date(full_date)
    adj_builder.set_event_code(event_code)
    adj_builder.set_medication_code(medication_code)
    adj_builder.set_adjustment_amount(adjustment_amount)
    adj_builder.set_reference_id(reference_id)
    adj_builder.set_reporting_period_id(reporting_period_id)
    adj_builder.set_created_date(get_current_timestamp())
    adj_builder.set_modified_date(get_current_timestamp())
    adj_builder.set_modified_by(modified_by)

    adjustment = adj_builder.build()

    result = AddAdjustment().set_adjustment(adjustment).execute()

    click.echo(result)


@add.command("event")
@click.argument("event_code", type=str)
@click.argument("event_name", type=str)
@click.argument("description", type=str)
@click.argument("modifier", type=int)
@click.argument("modified_by", type=str)
def add_event(event_code, event_name, description, modifier, modified_by):
    """Add a new event to the database.

    Args:
        event_code (str): Unique code identifying the event.
        event_name (str): Name of the event.
        description (str): Description of what the event is.
        modifier (int): Specifies if the event adds (1) or removes (-1) from the inventory.
        modified_by (str): The user who modified or created the event.

    Example:
        nbx add event "WASTE" "Wasted" "Event indicating that an item was wasted" -1 "jdoe"
    """
    # Instantiate an EventBuilder or similar from your codebase
    event_builder = EventBuilder()

    # Set the properties of the event
    event_builder.set_event_code(event_code)
    event_builder.set_event_name(event_name)
    event_builder.set_description(description)
    event_builder.set_modifier(modifier)
    event_builder.set_modified_by(modified_by)
    event_builder.set_created_date(get_current_timestamp())
    event_builder.set_modified_date(get_current_timestamp())

    # Build the event object
    event = event_builder.build()

    # Add the event to the database using your command class
    try:
        result = AddEvent().set_event(event).execute()
        click.echo(f"Event '{event_name}' added successfully.")
    except Exception as e:
        click.echo(f"Failed to add event: {e}")


@add.command("medication")
@click.argument("medication_code", type=str)
@click.argument("medication_name", type=str)
@click.argument("med_amount", type=int)
@click.argument("unit", type=str)
@click.argument("fill_amount", type=int)
@click.argument("status", type=str)
@click.argument("modified_by", type=str)
def add_medication(
    medication_code, medication_name, med_amount, unit, fill_amount, status, modified_by
):
    """Add a new medication to the database.

    Args:
        medication_code (str): The code representing the medication.
        medication_name (str): The name of the medication.
        med_amount (int): The amount of medication.
        unit (str): The unit used for the medication amount.
        fill_amount (int): The amount to fill.
        status (str): The status of the medication.
        modified_by (str): The user who modified or created the medication.

    Example:
        nbx add medication "MED123" "Ibuprofen" 200 "MG" 50 "ACTIVE" "jdoe"
    """
    med_builder = MedicationBuilder()
    med_builder.set_medication_code(medication_code)
    med_builder.set_medication_name(medication_name)
    med_builder.set_medication_amount(med_amount)
    med_builder.set_fill_amount(fill_amount)
    med_builder.set_preferred_unit(unit)
    med_builder.set_status(status)
    med_builder.set_created_date(get_current_timestamp())
    med_builder.set_modified_date(get_current_timestamp())
    med_builder.set_modified_by(modified_by)
    medication = med_builder.build()

    try:
        add_medication_command = AddMedication()
        add_medication_command.set_medication(medication)
        result = add_medication_command.execute()
        click.echo(f"Medication '{medication_name}' added successfully.")
    except Exception as e:
        click.echo(f"Failed to add medication: {e}")


@add.command("period")
@click.argument("start_date", type=str)
@click.argument("end_date", type=str)
@click.argument("status", type=str)
@click.argument("modified_by", type=str)
def add_reporting_period(start_date, end_date, status, modified_by):
    """Add a new reporting period to the database.

    Args:
        start_date (str): The start date of the reporting period.
        end_date (str): The end date of the reporting period.
        status (str): The status of the reporting period.
        modified_by (str): The user who modified or created the reporting period.

    Example:
        nbx add period "2023-01-01" "2023-06-30" "OPEN" "jdoe"
    """
    rp_builder = ReportingPeriodBuilder()
    rp_builder.set_start_date(start_date)
    rp_builder.set_end_date(end_date)
    rp_builder.set_status(status)
    rp_builder.set_created_date(get_current_timestamp())
    rp_builder.set_modified_date(get_current_timestamp())
    rp_builder.set_modified_by(modified_by)
    reporting_period = rp_builder.build()

    try:
        add_reporting_period_command = AddReportingPeriod()
        add_reporting_period_command.set_reporting_period(reporting_period)
        result = add_reporting_period_command.execute()
        click.echo(
            f"Reporting period from '{start_date}' to '{end_date}' added successfully."
        )
    except Exception as e:
        click.echo(f"Failed to add reporting period: {e}")


@add.command("status")
@click.argument("status_code", type=str)
@click.argument("status_name", type=str)
@click.argument("description", type=str)
@click.argument("modified_by", type=str)
def add_status(status_code, status_name, description, modified_by):
    """Add a new status to the database.

    Args:
        status_code (str): The code representing the status.
        status_name (str): The name of the status.
        description (str): A description of what the status represents.
        modified_by (str): The user who modified or created the status.
    
    Example:
        nbx add status "ACTIVE" "Active" "The status of an item that is currently active" "jdoe"
    """
    status_builder = StatusBuilder()
    status_builder.set_status_code(status_code)
    status_builder.set_status_name(status_name)
    status_builder.set_description(description)
    status_builder.set_created_date(get_current_timestamp())
    status_builder.set_modified_date(get_current_timestamp())
    status_builder.set_modified_by(modified_by)
    status = status_builder.build()

    try:
        add_status_command = AddStatus()
        add_status_command.set_status(status)
        result = add_status_command.execute()
        click.echo(f"Status '{status_code}' added successfully.")
    except Exception as e:
        click.echo(f"Failed to add status: {e}")


@add.command("unit")
@click.argument("unit_code", type=str)
@click.argument("unit_name", type=str)
@click.argument("decimals", type=int)
@click.argument("modified_by", type=str)
def add_unit(unit_code, unit_name, decimals, modified_by):
    """Add a new unit to the database.

    Args:
        unit_code (str): The code of the unit.
        unit_name (str): The name of the unit.
        decimals (int): The decimal places for the unit.
        modified_by (str): The user who modified the unit.

    Example:
        nbx add unit "mg" "milligrams" 3 "jdoe"
    """
    unit_builder = UnitBuilder()
    unit_builder.set_unit_code(unit_code)
    unit_builder.set_unit_name(unit_name)
    unit_builder.set_decimals(decimals)
    unit_builder.set_created_date(get_current_timestamp())
    unit_builder.set_modified_date(get_current_timestamp())
    unit_builder.set_modified_by(modified_by)
    unit = unit_builder.build()

    try:
        add_unit_command = AddUnit().set_unit(unit)
        result = add_unit_command.execute()
        click.echo(f"Unit '{unit_name}' added successfully.")
    except Exception as e:
        click.echo(f"Failed to add unit: {e}")


if __name__ == "__main__":
    cli()
