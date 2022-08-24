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
 medication_builder_template: Abstract builder for medication objects.

 medication_builder: Concrete builder for medication objects.

How to Use the Builders:
To use the builder import the builder for the object you want to build.

 ```python
 from narcotics_tracker.builders import medication_builder
 ```

Create an instance of the builder and set the attributes using the available 
methods. Methods are prefixed with `set_` and are listed in the documentation 
for the concrete builder.

 ```python
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
 ```

Once the attributes are set, call the `build` method to create the object. 
Once the build method has been called the object is created and all of its 
methods and attributes are available.

 ```python
 aspirin = med_builder.build()
 ```
 """
