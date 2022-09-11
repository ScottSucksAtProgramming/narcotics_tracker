"""Contains the concrete builder for the Medication class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    MedicationBuilder: Builds and returns Medication objects.
"""
from narcotics_tracker import database, medications
from narcotics_tracker.builders import medication_builder_template
from narcotics_tracker.utils import unit_converter


class MedicationBuilder(medication_builder_template.Medication):
    """Builds and returns medication objects.

    There are two types of methods: 'set' methods can be called to manually
    set attributes for the object; 'assign' methods perform calculations and
    are used as part of the build method to assign other attributes like the
    created date, or unit conversions.

    Look at the Medication Class documentation in the Medications Module for
    more information on how to use the Medication objects.

    How To Use:

        1. Create a database connection using the database.Database() context
        manager.

        2. Initialize the builder by assigning it to a variable and passing a
        database connection:
            ```e_builder = medication_builder.MedicationBuilder(database_connection)```

        3. Call the following methods and pass the required values:
        ```set_medication_name()```; ```set_medication_code()```;
        ```set_container()```; ```set_fill_amount()```;
        ```set_dose_and_unit()```; ```set_medication_status()``` and
        ```set_modified_by()```;

        4. Call the `build()` method to return an Medication object.

    Initializer:

        def __init__(self) -> None:
        ```Initializes the medication builder. Sets all attributes to None.```

    Instance Methods:

        build: Returns the medication object. Assigns the medication's
            attributes.

        set_medication_name: Sets the medication's name.

        set_medication_code: Sets the unique code of the medication.

        set_container: Sets the container the medication comes in.

        set_fill_amount: Sets the medication's fill amount.

        set_dose_and_unit: Sets the medication's dose and its preferred unit.

        set_medication_status: Sets the medication's status.

        set_modified_by: Sets the identifier of the user who modified the
            Medication.

        calculate_concentration: Calculates the concentration of the
            medication.

        assign_all_attributes: Assigns all attributes of the Medication.

        assign_medication_id: Manually sets the Medication's id. Should not be
            called by the user.

        assign_concentration: Manually sets the concentration. Should not be
             called by the user.

        assign_created_date: Manually sets the created_date attribute.

        assign_modified_date: Manually sets the modified_date attribute.

    """

    def __init__(self) -> None:
        """Initializes the medication builder. Sets all attributes to None."""
        self.medication_id = None
        self.medication_code = None
        self.name = None
        self.container_type = None
        self.fill_amount = None
        self.dose = None
        self.preferred_unit = None
        self.concentration = None
        self.status = None
        self.created_date = None
        self.modified_date = None
        self.modified_by = None

    def build(self) -> "medications.Medication":
        """Returns the medication object. Assigns the medication's attributes.

        This is the last method to be called as part of the building process.
        It will return the medication object with all of its attributes set.
        The concentration is calculated using the calculate_concentration
        method.

        Returns:
            medication.Medication: The medication object.
        """
        self.calculate_concentration()

        return medications.Medication(self)

    def set_medication_name(self, name: str) -> None:
        """Sets the medication's name.

        Args:
            name (str): The medication's name.
        """
        self.name = name

    def set_medication_code(self, code: str) -> None:
        """Sets the unique code of the medication.

        The medications unique code is used to identify the medication within
        the database and the Narcotics Tracker. This code is set by the user
        as an easy reference to the medication. Medications without a code are
        not retrievable from the database.

        Args:
            code (str): Identifier for this specific medication.
        """
        self.medication_code = code

    def set_container(self, container_type: str) -> None:
        """Sets the container the medication comes in.

        Containers are defined in the containers table of the database as well
        as the Containers Module and class.

        The Narcotics Tracker comes with the following pre-defined containers
        for medications:
            Vial -  Container Code: 'vial'
            Pre-filled Syringe - Container Code: 'pfs'
            Pre-mixed Bag - Container Code: 'pmb'


        Args:
            container_type (str): The type of container the
                medication comes in. Defaults to None.
        """
        self.container_type = container_type

    def set_fill_amount(self, fill_amount: float) -> None:
        """Sets the medication's fill amount.

        Each comes dissolved within a liquid (solvent). The fill amount is the
        measurement of that liquid in the container measured in milliliters
        (ml).

        Args:
            fill_amount (float): The amount of medication in the container.
                Defaults to None.
        """
        self.fill_amount = fill_amount

    def set_dose_and_unit(self, dose: float, preferred_unit: str) -> None:
        """Sets the medication's dose and its preferred unit.

        The dose is converted into micrograms which is how the Narcotics
        Tracker stores all medication amounts. The preferred unit is saved so
        the amounts can be converted back when being shown to the user.

        Look at the Unit Converter Module for more information on converting
        between units.

        Args:
            dose (float): The amount of medication dissolved in the container.

            preferred_unit (str): The unit the medication is commonly measured
                in.
        """
        self.dose = unit_converter.UnitConverter.to_mcg(dose, preferred_unit)
        self.unit = preferred_unit

    def set_medication_status(self, status: str) -> None:
        """Sets the medication's status.

        Statuses determine when objects can and cannot be used. They are
        defined in the statuses table of the database as well as the Statuses
        module and class.

        The Narcotics Tracker comes with pre-defined statuses for medications:
            ACTIVE
            INACTIVE

        Args:
            status (str): The status of the medication.
        """
        self.status = status

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who modified the Medication.

        This method will set the Medication's modified by attribute.

        Args:
            modified_by (str): Identifier of the user who modified the
                Medication.
        """
        self.modified_by = modified_by

    def calculate_concentration(self) -> None:
        """Calculates the concentration of the medication.

        Will calculate the concentration of the medications as a decimal by
        diving the dose by the fill amount. This is useful when converting
        medication amounts into milliliters for reports.
        """
        self.concentration = self.dose / self.fill_amount

    def assign_all_attributes(self, attributes: dict) -> None:
        """Assigns all attributes of the Medication.

        This method is intended to be called when loading an Medication from
        the database.

        Args:
            attributes (dict): The attributes of the Medication. Dictionary
                keys are formatted as the Medication attribute names.
        """
        self.assign_medication_id(attributes["medication_id"])
        self.set_medication_name(attributes["name"])
        self.set_medication_code(attributes["medication_code"])
        self.set_container(attributes["container_type"])
        self.set_fill_amount(attributes["fill_amount"])
        self.set_dose_and_unit(attributes["dose"], attributes["unit"])
        self.assign_concentration(attributes["concentration"])
        self.set_medication_status(attributes["status"])
        self.assign_created_date(attributes["created_date"])
        self.assign_modified_date(attributes["modified_date"])
        self.set_modified_by(attributes["modified_by"])

    def assign_medication_id(self, medication_id: int) -> None:
        """Manually sets the Medication's id. Should not be called by the user.

        This method will set the Medication's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the Medication is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            medication_id (int): The Medication's numeric id.
        """
        self.medication_id = medication_id

    def assign_concentration(self, concentration: float) -> None:
        """Manually sets the concentration. Should not be called by the user.

        This method will set the Medications's concentration number. This
        method is useful in setting the concentration when the Medications is
        loaded from the database. It will override any id number that is
        already set and may cause errors in the within the database table.
        Users should not call this method.

        Args:
            concentration (float): The Medication's concentration.
        """
        self.concentration = concentration

    def assign_created_date(self, created_date: str) -> None:
        """Manually sets the created_date attribute.

        Note: This method is not intended to be called when building an Medication.

        Args:
            created_date (str): The date the Medication object was created.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.created_date = database.return_datetime(created_date)

    def assign_modified_date(self, modified_date: str) -> None:
        """Manually sets the modified_date attribute.

        Note: This method is not intended to be called when building an Medication.

        Args:
            modified_date (str): The date the Medication was last modified.
                Must be in the format 'YYYY-MM-DD HH:MM:SS'.
        """
        self.modified_date = database.return_datetime(modified_date)
