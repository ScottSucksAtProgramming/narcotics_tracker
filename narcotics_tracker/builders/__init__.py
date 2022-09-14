"""Assists with building complex objects for the narcotics tracker.

Many objects in the narcotics tracker are complex and have a large number of 
attributes. The builder design pattern was used to separate the creation of 
the objects from their representations allowing objects to be created in a 
modular fashion.

The builder package contains two types of builders: Abstract builders, which 
serve as templates for the Concrete builders. The Concrete builders implement 
the building process. Abstract builders are postfixed with the word 
`template`.

Tests for the builders' package are located in the tests/unit/builders_test.py

Modules:

    Abstract Builder Templates:

        adjustment_builder_template: Contains the template for the Adjustment 
            Builder.
        
        container_builder_template: Contains the template for the Container 
            Builder.
        
        event_builder_template: Contains the template for the Event Builder.
        
        medication_builder_template: Contains the template for the Medication 
            Builder.
        
        reporting_period_builder_template: Contains the template for the 
            Reporting Period Builder.
        
        status_builder_template: Contains the template for the Status Builder.
        
        unit_builder_template: Contains the template for the Unit Builder.

    Concrete Builder Modules:

        adjustment_builder: Contains the concrete builder for the Adjustment 
            class.
        
        container_builder: Contains the concrete builder for the Container 
            class.
        
        event_builder: Contains the concrete builder for the Event class.
        
        medication_builder: Contains the concrete builder for the Medication 
            class.
        
        reporting_period_builder: ‌Contains the concrete builder for the 
            ReportingPeriod class
        
        status_builder: Contains the concrete builder for the Status class.
        
        unit_builder: Contains the concrete builder for the Unit class.


How to Use the Builders:
    
    1. Import the builder for the object you want to build.
    
    2. If needed make a connection with the database using the 
        database.Database() context manager. Review documentation of Database 
        Module for more information.
    
    3. Initialize the builder by assigning it to a variable and passing any
        information required by its __init__ method.

    4. Call the various 'set' methods and pass in the required information.

    5. Call the builder's `build()` method and assign it to a variable.

Example:

    ```python
    from narcotics_tracker.builders import medication_builder

    med_builder = medication_builder.MedicationBuilder()

    med_builder.set_medication_id(None)
    med_builder.set_name("Aspirin")
    med_builder.set_code("ASA")
    med_builder.set_fill_amount(10)
    med_builder.set_container(containers.Container.AMPULE)
    med_builder.set_dose_and_unit(10, units.Unit.MCG)
    med_builder.set_status(medication_statuses.MedicationStatus.ACTIVE)
    med_builder.set_created_date(None)
    med_builder.set_modified_date(None)
    med_builder.set_modified_by("SRK")

    aspirin = med_builder.build()
    ```
 """
