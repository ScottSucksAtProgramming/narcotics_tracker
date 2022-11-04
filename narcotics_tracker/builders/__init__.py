"""Contains the builders for the DataItems used in the Narcotics Tracker.

There are multiple DataItems in the Narcotics Tracker. Each one stores various 
bits of information which enable inventory tracking. Each DataItem also 
inherits from the DataItem class which adds more attributes. This makes these 
items difficult to build with large constructors.

This Package implements the Builder Pattern which helps solve this problem by 
separating the creation of these object from the objects themselves. Instead 
of using a DataItem's initializer a Builder has been created which constructs 
the object in a stepwise fashion. Each Builder implements the interface 
defined in a DataItemBuilder superclass.

Interfaces:

    Builder: Contains the interface for concrete DataItem builders.

Modules:
    
    DataItemBuilder: Defines the builder for generic DataItems. Only meant to 
        be inherited from.
    
    Adjustment Builder: Handles the defining and building of Adjustment 
        Objects.
    
    Event Builder: Handles the defining and building of Event Objects.
    
    Medication Builder: Handles the defining and building of Medication 
        Objects.
    
    Reporting Period Builder: Handles the defining and building of Reporting 
        Period Objects.

    Status Builder: Handles the defining and building of Status Objects.
    
    Unit Builder: Handles the defining and building of Unit Objects.

How To Use:

    When creating a DataItem, the builder for that item can be created and its 
    methods can be called to build the object piece by piece. When all pieces have 
    been constructed the `build` method will create return the object. After 
    calling the build method, the builder is reset with a fresh instance of the 
    DataItem object so it can be re-used if necessary.

    Example:

        ```python
        fentanyl = (
            MedicationBuilder()
            .set_table("medications")
            .set_id(None)
            .set_created_date(1666932094)
            .set_modified_date(1666932094)
            .set_modified_by("SRK")
            .set_medication_code("fentanyl")
            .set_medication_name("Fentanyl")
            .set_fill_amount(2)
            .set_medication_amount(100)
            .set_preferred_unit("mcg")
            .set_concentration(0.05)
            .set_status("ACTIVE")
            .build()
        )
        ```

    Review the documentation of specific builders for more information on 
    their usage and available methods.
"""
from narcotics_tracker.builders.medication_builder import MedicationBuilder
