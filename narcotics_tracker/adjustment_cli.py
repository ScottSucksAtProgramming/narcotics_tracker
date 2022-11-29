"""Playing around with a command line interface for the Narcotics Tracker."""

from typing import TYPE_CHECKING

import typer
from rich import print

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.items.adjustments import Adjustment

if TYPE_CHECKING:
    from narcotics_tracker.builders.interfaces.builder import Builder

app = typer.Typer()


@app.command()
def log(
    adjustment_date: str = typer.Argument(
        ...,
        help="Date of the adjustment. Format: MM-DD-YYYY",
        show_default=False,
    ),
    adjustment_time: str = typer.Argument(
        ..., help="Time of the adjustment. Format: HH:MM:SS"
    ),
    event_code: str = typer.Argument(..., show_default=False),
    medication_code: str = typer.Argument(..., show_default=False),
    adjustment_amount: float = typer.Argument(..., show_default=False),
    reference_id: str = typer.Argument(..., show_default=False),
    reporting_period_id: int = typer.Argument(..., show_default=False),
    modified_by: str = typer.Argument(..., help="User initials."),
):
    """Logs an inventory adjustment to the database."""
    full_date = adjustment_date + " " + adjustment_time
    adj_builder: "Builder" = AdjustmentBuilder()
    adj_builder.set_adjustment_date(full_date)
    adj_builder.set_event_code(event_code)
    adj_builder.set_medication_code(medication_code)
    adj_builder.set_adjustment_amount(adjustment_amount)
    adj_builder.set_reference_id(reference_id)
    adj_builder.set_reporting_period_id(reporting_period_id)
    adj_builder.set_modified_by(modified_by)

    adjustment = adj_builder.build()

    result: str = commands.AddAdjustment().execute(adjustment)

    print(result)


@app.command()
def show():
    """Prints the Adjustments currently in the inventory table."""
    adjustment_data: list[tuple["Adjustment"]] = commands.ListAdjustments().execute()
    for adjustment in adjustment_data:
        print(adjustment)


if __name__ == "__main__":
    app()
