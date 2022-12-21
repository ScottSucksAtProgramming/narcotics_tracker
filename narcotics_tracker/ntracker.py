"""Playing around with a command line interface for the Narcotics Tracker."""

import rich
import typer

from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.commands import adjustment_commands
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.typings import NTTypes

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
) -> None:
    """Logs an inventory adjustment to the database."""
    full_date = adjustment_date + " " + adjustment_time
    adj_builder = AdjustmentBuilder()
    adj_builder.set_adjustment_date(full_date)
    adj_builder.set_event_code(event_code)
    adj_builder.set_medication_code(medication_code)
    adj_builder.set_adjustment_amount(adjustment_amount)
    adj_builder.set_reference_id(reference_id)
    adj_builder.set_reporting_period_id(reporting_period_id)
    adj_builder.set_modified_by(modified_by)

    adjustment = adj_builder.build()

    result: str = (
        adjustment_commands.AddAdjustment().set_adjustment(adjustment).execute()
    )

    rich.print(result)


@app.command()
def show(
    medication: str = typer.Option(
        None,
        "--medication",
        "-m",
        help="Returns adjustments for the specified medication only.",
    ),
    event: str = typer.Option(
        None, "--event", "-e", help="Returns adjustments for the specified event only."
    ),
) -> None:
    """Prints the Adjustments currently in the inventory table."""
    list_adjustments = adjustment_commands.ListAdjustments()
    criteria: NTTypes.sqlite_types = {}

    if medication:
        criteria["medication_code"] = medication

    if event:
        criteria["event_code"] = event.upper()

    if criteria:
        list_adjustments.set_parameters(criteria)

    adjustment_data: list["Adjustment"] = list_adjustments.execute()
    for adjustment in adjustment_data:
        rich.print(str(adjustment))


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
) -> None:
    """Deletes an Adjustment from the inventory table by it's ID.

    Note: This is permanent and irreversible.
    """
    if force is False:
        adj_info = adjustment_commands.ListAdjustments().execute(
            criteria={"id": adjustment_id}
        )[0]
        rich.print(f"Attempting to delete {adj_info}.")
        confirmation: str = typer.prompt(
            "Please confirm deletion. This cannot be reversed. (y/n): "
        ).lower()

        if confirmation != "y":
            rich.print("Cancelling...")

    result: str = adjustment_commands.DeleteAdjustment().set_id(adjustment_id).execute()

    rich.print(result)


if __name__ == "__main__":
    app()
