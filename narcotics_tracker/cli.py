from pendulum import datetime
from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.services.service_manager import ServiceManager
import typer
from narcotics_tracker.commands import (
    adjustment_commands,
    medication_commands,
    # Import other command groups as needed
)


def add_adjustment(
    adjustment_date: str = typer.Argument(..., help="Enter the adjustment date (Format: MM-DD-YYYY)"),
    adjustment_time: str = typer.Argument(..., help="Enter the adjustment time (Format: HH:MM:SS)"),
    event_code: str = typer.Argument(..., help="Enter the event code"),
    medication_code: str = typer.Argument(..., help="Enter the medication code"),
    adjustment_amount: float = typer.Argument(..., help="Enter the adjustment amount"),
    reference_id: str = typer.Argument(..., help="Enter the reference ID"),
    reporting_period_id: int = typer.Argument(..., help="Enter the reporting period ID")
):

    # Create the full date combining date and time
    full_date = f"{adjustment_date} {adjustment_time}"
    
    # Build the Adjustment object
    adjustment = AdjustmentBuilder()\
        .set_adjustment_date(full_date)\
        .set_event_code(event_code)\
        .set_medication_code(medication_code)\
        .set_adjustment_amount(adjustment_amount)\
        .set_reference_id(reference_id)\
        .set_reporting_period_id(reporting_period_id)\
        .set_modified_by(modified_by)\
        .build()

    # Add the adjustment to the database
    persistence_service = ServiceManager().persistence
    result = adjustment_commands.AddAdjustment(persistence_service)\
        .set_adjustment(adjustment)\
        .execute()

    typer.echo(result)


app = typer.Typer()

# Define top-level 'add' command
@app.command("add")
def add(entity: str):
    """
    Add a new entity, where entity can be 'adjustment', 'medication', etc.
    """
    if entity == "adjustment":
        add_adjustment()
    elif entity == "medication":
        add_medication()
    # You can add more elif statements for other entities
    else:
        raise typer.BadParameter(f"Unknown entity '{entity}'")

def add_adjustment():
    # Implementation for adding an adjustment
    # Example: result = adjustment_commands.AddAdjustment().execute()
    pass

def add_medication():
    # Implementation for adding a medication
    pass


def remove_adjustment():
    """
    Prompts the user for the ID of the adjustment to remove and then removes it from the database.
    """
    adjustment_id = typer.prompt("Enter the ID of the adjustment to remove", type=int)
    
    # Get the persistence service
    persistence_service = ServiceManager().persistence
    
    # Use the DeleteAdjustment command to remove the adjustment
    result = adjustment_commands.DeleteAdjustment(persistence_service).set_id(adjustment_id).execute()
    
    typer.echo(f"Adjustment removed: {result}")



@app.command("remove")
def remove(entity: str):
    """
    Remove an entity, where entity can be 'adjustment', 'medication', etc.
    """
    if entity == "adjustment":
        remove_adjustment()
    elif entity == "medication":
        remove_medication()
    # You can add more elif statements for other entities
    else:
        raise typer.BadParameter(f"Unknown entity '{entity}'")
    
def update_adjustment():
    """
    Prompts the user for details about the adjustment to update and then updates it in the database.
    """
    adjustment_id = typer.prompt("Enter the ID of the adjustment to update", type=int)
    updated_data = {}  # Dictionary to hold the data for update
    
    # Example of updating the amount
    updated_amount = typer.prompt("Enter the new adjustment amount", type=float)
    updated_data['amount'] = updated_amount
    
    # Prompt for other fields you might want to update...
    
    # Get the persistence service
    persistence_service = ServiceManager().persistence
    
    # Use the UpdateAdjustment command to update the adjustment
    result = adjustment_commands.UpdateAdjustment(persistence_service).set_data(
        updated_data, {'id': adjustment_id}
    ).execute()
    
    typer.echo(f"Adjustment updated: {result}")


@app.command("update")
def update(entity: str):
    """
    Updates an entity, where entity can be 'adjustment', 'medication', etc.
    """
    if entity == "adjustment":
        update_adjustment()
    elif entity == "medication":
        update_medication()
    # You can add more elif statements for other entities
    else:
        raise typer.BadParameter(f"Unknown entity '{entity}'")
    


def list_adjustments():
    """
    Lists adjustments based on a date or ID.
    """
    # Get the persistence service
    persistence_service = ServiceManager().persistence
    
    selection_method = typer.prompt("List adjustments by (date/id):").lower()
    
    if selection_method == 'date':
        date_str = typer.prompt("Enter the date (Format: MM-DD-YYYY)")
        date = datetime.strptime(date_str, "%m-%d-%Y")
        # You'll need to implement a method in your persistence service to get adjustments by date
        adjustments = persistence_service.get_adjustments_by_date(date)
    elif selection_method == 'id':
        adjustment_id = typer.prompt("Enter the adjustment ID", type=int)
        # You'll need to implement a method in your persistence service to get an adjustment by ID
        adjustments = [persistence_service.get_adjustment_by_id(adjustment_id)]
    else:
        typer.echo("Invalid selection method.")
        return
    
    # Assuming adjustments is a list of Adjustment objects or similar
    for adj in adjustments:
        typer.echo(f"ID: {adj.id}, Date: {adj.date}, Amount: {adj.amount}, ...")  # Adapt the attributes to match your data model
    
@app.command("list")
def list(entity: str):
    """
    Updates an entity, where entity can be 'adjustment', 'medication', etc.
    """
    if entity == "adjustment":
        list_adjustments()
    elif entity == "medication":
        list_medication()
    # You can add more elif statements for other entities
    else:
        raise typer.BadParameter(f"Unknown entity '{entity}'")

if __name__ == "__main__":
    app()