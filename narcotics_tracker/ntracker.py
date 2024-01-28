"""Playing around with a command line interface for the Narcotics Tracker."""

from datetime import datetime
from typing import Union

import click

from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.commands import adjustment_commands
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes, SQLiteDict

@click.group()
def cli():
    pass

@click.group()
def add ():
    pass

def get_current_timestamp():
    return int(datetime.now().timestamp())

@add.command('adjustment')
@click.argument('adjustment_date', type=str)
@click.argument('adjustment_time', type=str)
@click.argument('event_code', type=str)
@click.argument('medication_code', type=str)
@click.argument('adjustment_amount', type=float)
@click.argument('reference_id', type=str)
@click.argument('reporting_period_id', type=int)
@click.argument('modified_by', type=str)
def add_adjustment(adjustment_date, adjustment_time, event_code, medication_code, adjustment_amount, reference_id, reporting_period_id, modified_by):
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

    result = adjustment_commands.AddAdjustment().set_adjustment(adjustment).execute()

    click.echo(result)

cli.add_command(add)

if __name__ == "__main__":
    cli()
