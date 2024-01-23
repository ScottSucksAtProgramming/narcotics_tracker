"""Playing around with a command line interface for the Narcotics Tracker."""

from typing import Union

import rich
import typer

from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.commands import adjustment_commands
from narcotics_tracker.items.adjustments import Adjustment
from narcotics_tracker.services.service_manager import ServiceManager
from narcotics_tracker.typings import NTTypes, SQLiteDict

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
    reference_id: str = typer.Option(
        None,
        "--reference",
        "-r",
        help="Returns adjustments for the specified reference id only.",
    ),
    adjustment_date: str = typer.Option(
        None,
        "--date",
        "-d",
        help="Returns adjustments for the specified date only.",
    ),
    reporting_period: str = typer.Option(
        None,
        "--period",
        "-p",
        help="Returns adjustments for the specified reporting period only.",
    ),
) -> None:
    """Prints the Adjustments currently in the inventory table."""
    command = adjustment_commands.ListAdjustments()
    criteria: SQLiteDict = {}

    if medication:
        criteria["medication_code"] = medication.lower()

    if event:
        criteria["event_code"] = event.upper()

    if reference_id:
        criteria["reference_id"] = reference_id

    if adjustment_date:
        date = ServiceManager().datetime.convert_to_timestamp(adjustment_date)
        criteria["adjustment_date"] = date

    if reporting_period:
        criteria["reporting_period"] = reporting_period

    if criteria:
        command.set_parameters(criteria)

    adjustment_data: list["Adjustment"] = command.execute()
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


@app.command()
def update(
    adjustment_id: int = typer.Argument(
        ..., help="ID Number of the Adjustment.", show_default=False
    ),
    user: str = typer.Argument(
        ..., help="Name of User Updating Adjustment.", show_default=False
    ),
    medication: str = typer.Option(
        None,
        "--medication",
        "-m",
        help="Update the medication code",
    ),
    event: str = typer.Option(None, "--event", "-e", help="Update the event code"),
    reference_id: str = typer.Option(
        None,
        "--reference",
        "-r",
        help="Update the reference ID.",
    ),
    adjustment_date: str = typer.Option(
        None,
        "--date",
        "-d",
        help="Update the adjustment date.",
    ),
    amount: float = typer.Option(
        None, "--amount", "-a", help="Update the adjustment amount."
    ),
    reporting_period: str = typer.Option(
        None,
        "--period",
        "-p",
        help="Update the reporting period.",
    ),
    created_date: str = typer.Option(
        None,
        "--created",
        "-c",
        help="Update the created date.",
    ),
) -> None:
    """Updates an adjustment's data."""
    command = adjustment_commands.UpdateAdjustment()
    datetime_service = ServiceManager().datetime
    data: dict[str, Union[float, str]] = {}
    criteria = {"id": adjustment_id}

    if medication:
        data["medication_code"] = medication.lower()

    if event:
        data["event_code"] = event.upper()

    if adjustment_date:
        date = datetime_service.convert_to_timestamp(adjustment_date)
        data["adjustment_date"] = date

    if amount:
        data["amount"] = amount

    if reporting_period:
        data["reporting_period_id"] = reporting_period

    if reference_id:
        data["reference_id"] = reference_id

    if created_date:
        data["created_date"] = created_date

    data["modified_date"] = datetime_service.return_current()
    data["modified_by"] = user

    adjustment = (
        adjustment_commands.ListAdjustments()
        .set_parameters({"id": adjustment_id})
        .execute()
    )
    print("This adjustment:")
    print(vars(adjustment))
    print("will be updated to:")
    print("--------------------------")
    print(data)

    response: str = input("Please confirm (y or yes): ").lower()

    if response != "y" or "yes":
        return

    command.set_data(data=data, criteria=criteria).execute()

    input("Adjustment updated. Press enter to exit.")


if __name__ == "__main__":
    app()

