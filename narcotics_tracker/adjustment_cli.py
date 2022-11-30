"""Playing around with a command line interface for the Narcotics Tracker."""

from typing import TYPE_CHECKING

import rich
import typer

from narcotics_tracker import commands
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.items.adjustments import Adjustment

if TYPE_CHECKING:
    from narcotics_tracker.builders.interfaces.builder import Builder

app = typer.Typer()


@app.command()
def log(
    adjustment_date: str = typer.Argument(
        ..., help="Format: MM-DD-YYYY", show_default=False
    ),
    adjustment_time: str = typer.Argument(..., help="Format: HH:MM:SS"),
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

    result: str = commands.AddAdjustment().set_adjustment(adjustment).execute()

    rich.print(result)


@app.command()
def show():
    """Prints the Adjustments currently in the inventory table."""
    adjustment_data: list[tuple["Adjustment"]] = commands.ListAdjustments().execute()
    for adjustment in adjustment_data:
        rich.print(adjustment)


@app.command()
def delete(
    adjustment_id: int = typer.Argument(
        ..., help="ID Number of the Adjustment.", show_default=False
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Will not prompt for confirmation.",
        show_default=False,
    ),
):
    """Deletes an Adjustment from the inventory table by it's ID.

    Note: This is permanent and irreversible.
    """
    if force is False:
        adj_info = commands.ListAdjustments().execute(criteria={"id": adjustment_id})[0]
        rich.print(f"Attempting to delete {adj_info}.")
        confirmation: str = typer.prompt(
            "Please confirm deletion. This cannot be reversed. (y/n): "
        ).lower()

        if confirmation != "y":
            rich.print("Cancelling...")

    result: str = commands.DeleteAdjustment().set_id(adjustment_id).execute()

    rich.print(result)


if __name__ == "__main__":
    app()
