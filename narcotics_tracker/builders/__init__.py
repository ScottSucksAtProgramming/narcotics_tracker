"""Contains the builders for the DataItems used in the Narcotics Tracker.

#* Situation

    There are multiple DataItems in the Narcotics Tracker. Each one stores 
    various bits of information which enable inventory tracking. Each DataItem 
    also inherits from the DataItem class which adds more attributes. This 
    makes these items difficult to build with large constructors.

#* Background

    This Package implements the Builder Pattern which helps solve this problem 
    by separating the creation of these object from the objects themselves. 
    Instead of using a DataItem's initializer a Builder has been created which 
    constructs the object in a stepwise fashion. Each Builder implements the 
    interface defined in a DataItemBuilder superclass.

#* Intended Use

    When creating a DataItem, the builder for that item can be created and its 
    methods can be called to build the object piece by piece. When all pieces 
    have been constructed the `build` method will create return the object. 
    After calling the build method, the builder is reset with a fresh instance 
    of the DataItem object so it can be re-used if necessary.

    #* Example Usage:

        ```python

        med_builder = MedicationBuilder()
        med_builder.set_table("medications")
        med_builder.set_id()
        med_builder.set_created_date()
        med_builder.set_modified_date()
        med_builder.set_modified_by("Narcotics Administrator")
        med_builder.set_medication_code("fentanyl")
        med_builder.set_medication_name("Fentanyl")
        med_builder.set_fill_amount(2)
        med_builder.set_medication_amount(100)
        med_builder.set_preferred_unit("mcg")
        med_builder.set_concentration()
        med_builder.set_status("ACTIVE")

        fentanyl = med_builder.build()
        ```

    Review the documentation of specific builders for more information on 
    their usage and available methods.

#* Modules:
    Builder Interface: Contains the interface for concrete DataItem builders.
    Adjustment Builder: Contains the concrete builder for Adjustment DataItems.
    Event Builder: Contains the concrete builder for the Event DataItems.
    Medication Builder: Contains the concrete builder for Medication DataItems.
    Reporting Period Builder: Contains the concrete builder for ReportingPeriod 
        DataItems.
    Status Builder: Contains the concrete builder for the Status DataItems.
    Unit Builder: Contains the concrete builder for the Unit DataItems.
"""
