from narcotics_tracker.builders.adjustment_builder import AdjustmentBuilder
from narcotics_tracker.services.service_manager import ServiceManager
import typer
from narcotics_tracker.commands import (
    adjustment_commands,
    medication_commands,
    # Import other command groups as needed
)


def add_adjustment():
    """
    Prompts the user for adjustment details and adds an adjustment to the database.
    """
    # Assuming the user input required matches the parameters in the `log` function
    adjustment_date = typer.prompt("Enter the adjustment date (Format: MM-DD-YYYY)")
    adjustment_time = typer.prompt("Enter the adjustment time (Format: HH:MM:SS)")
    event_code = typer.prompt("Enter the event code")
    medication_code = typer.prompt("Enter the medication code")
    adjustment_amount = typer.prompt("Enter the adjustment amount", type=float)
    reference_id = typer.prompt("Enter the reference ID")
    reporting_period_id = typer.prompt("Enter the reporting period ID", type=int)
    modified_by = typer.prompt("Enter your initials")

    # Create the full date combining date and time
    full_date = f"{adjustment_date} {adjustment_time}"
    
    # Build the Adjustment object
    adj_builder = AdjustmentBuilder()
    adj_builder.set_adjustment_date(full_date)
    adj_builder.set_event_code(event_code)
    adj_builder.set_medication_code(medication_code)
    adj_builder.set_adjustment_amount(adjustment_amount)
    adj_builder.set_reference_id(reference_id)
    adj_builder.set_reporting_period_id(reporting_period_id)
    adj_builder.set_modified_by(modified_by)
    adjustment = adj_builder.build()

    # Add the adjustment to the database using AddAdjustment command
    persistence_service = ServiceManager().persistence
    result = adjustment_commands.AddAdjustment(persistence_service).set_adjustment(adjustment).execute()

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

# You can define more functions for update, delete, list, etc.
# And similarly add top-level commands that delegate to these functions



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
    
@app.command("list")
def list(entity: str):
    """
    Updates an entity, where entity can be 'adjustment', 'medication', etc.
    """
    if entity == "adjustment":
        list_adjustment()
    elif entity == "medication":
        list_medication()
    # You can add more elif statements for other entities
    else:
        raise typer.BadParameter(f"Unknown entity '{entity}'")

if __name__ == "__main__":
    app()