"""Contains the concrete builder for the medication class.

Concrete builders contain the implementation of the builder interface defined 
in the abstract builder class. They are used to build objects for the 
Narcotics Tracker in a modular step-wise approach.

Classes:

    MedicationBuilder: Builds and returns medication objects.
"""

from narcotics_tracker import medications
from narcotics_tracker.builders import medication_builder_template
from narcotics_tracker.utils import unit_converter


class MedicationBuilder(medication_builder_template.Medication):
    """Builds and returns medication objects.

    Initializer:

        def __init__(self) -> None:

            Initializes the medication builder. Sets all attributes to None.

    Instance Methods:

        set_medication_id: Sets the medication's id number.

        set_name: Sets the medication's name.

        set_code: Sets the unique code for the medication.

        set_container: Sets the medication's container type.

        set_fill_amount: Sets the medication's fill amount.

        set_dose_and_unit: Sets the medication's dose and unit.

        set_concentration: Sets the medication's concentration.

        set_status: Sets the medication's status.

        set_created_date: Sets the medication's created date.

        set_modified_date: Sets the medication's modified date.

        set_modified_by: Sets the medication's modified by.

        calculate_concentration: Calculates medication's concentration.

    Exceptions:

        TypeError: Raised when an enum type is not valid.
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

    def set_medication_id(self, medication_id: int = None) -> None:
        """Sets the medication's id number. Should not be called by the user.

        This method will set the medication's id number. The id number is
        generally set by the database using its row id. This method is useful
        in setting the id number when the medication is loaded from the
        database. It will override any id number that is already set and may
        cause errors in the within the database table. Users should not call
        this method.

        Args:
            medication_id (int): The medication's unique id. Defaults to None.
        """
        self.medication_id = medication_id

    def set_name(self, name: str) -> None:
        """Sets the medication's name.

        Args:
            name (str): The medication's name. Defaults to None.
        """
        self.name = name

    def set_code(self, code: str) -> None:
        """Sets the unique code of the medication.

        The medications unique code is used to identify the medication within
        the database and the Narcotics Tracker. This code is set by the user
        as an easy reference to the medication. Medications without a code are
        not retrievable from the database.

        Recommended codes are short and easy to remember. For example,
        "Morphine1", or "Fentanyl100in2" referencing the dose and fill amount.

        Args:
            code (str): Identifier for this specific medication. Defaults to
                None.
        """
        self.medication_code = code

    def set_container(self, container_type: str) -> None:
        """Sets the medication's container type via the enum Container class.

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
        """Sets the medication's dose and its preferred preferred_.
        Args:
            dose (float): The amount of medication dissolved in the container.
                Defaults to None.

            preferred_unit (str): The unit the medication is commonly referred
                by.
        """
        self.dose = unit_converter.UnitConverter.to_mcg(dose, preferred_unit)
        self.unit = preferred_unit

    def set_concentration(self, concentration: float) -> None:
        """Sets the medication's concentration. Should not be set by the user.

        The concentration is the amount of medication dissolved in the
        solvent. It is required for calculating the amount of medication when
        completing periodic reporting.

        The concentration is automatically calculated when the medication is
        built using the calculate_concentration method. This method is helpful
        in setting the concentration when the medication is loaded from the
        database. It will override any concentration that is already set
        within the database table. Users should not call this method.

        Args:

            concentration (float): The medication's concentration.
        """
        self.concentration = concentration

    def set_status(self, status: str) -> None:
        """Sets the medication's status via the enum MedicationStatus class.

        Acceptable statuses are:
            MedicationStatus.ACTIVE,
            MedicationStatus.INACTIVE,
            MedicationStatus.DISCONTINUED,

        Args:
            status (medication_status.MedicationStatus): The status of the
                medication.

        Raises:
            TypeError: Raised if the status is not a valid type.
        """
        self.status = status

    def set_created_date(self, created_date: str) -> None:
        """Sets the medication's created date. Should not be called users.

        This method will set the medication's created date. The created date
        is set automatically when the medication is saved in the database.
        This method is useful in setting the created date when loading a
        medication from the database. It will override any created date set in
        the database table. Users should not call this method.

        Args:
            created_date (str): The date the medication was created.
        """
        self.created_date = created_date

    def set_modified_date(self, modified_date: str) -> None:
        """Sets the medication's modified date. Should not be called the user.

        This method will set the medication's modified by date. The modified
        by date is set automatically when the medication is updated in the
        database. This method is useful in setting the modified_by date when
        loading a medication from the database. It will override any modified
        by date set in the database table. Users should not call this method.

        Args:
            modified_date (str): The date the medication was last modified.
        """
        self.modified_date = modified_date

    def set_modified_by(self, modified_by: str) -> None:
        """Sets the identifier of the user who last modified the medication.

        Args:
            modified_by (str): The identifier of the user who last modified
                the medication."""
        self.modified_by = modified_by

    def calculate_concentration(self) -> None:
        """Calculates the concentration of the medication.

        Formula: dose/fill_amount
        """
        self.concentration = self.dose / self.fill_amount

    def set_all_properties(self, properties: dict) -> None:
        """Sets all properties of the medication.

        Args:
            properties (dict): The properties of the medication. Dictionary
                keys are formatted as the medication property names.
        """
        self.set_medication_id(properties["medication_id"])
        self.set_name(properties["name"])
        self.set_code(properties["medication_code"])
        self.set_container(properties["container_type"])
        self.set_fill_amount(properties["fill_amount"])
        self.set_dose_and_unit(properties["dose"], properties["unit"])
        self.set_concentration(properties["concentration"])
        self.set_status(properties["status"])
        self.set_created_date(properties["created_date"])
        self.set_modified_date(properties["modified_date"])
        self.set_modified_by(properties["modified_by"])

    def reset(self) -> None:
        """Resets the medication to its default values."""
        self._medication = medications.Medication()

    def build(self) -> "medications.Medication":
        """Returns the medication object. Assigns the medication's properties.

        This is the last method to be called as part of the building process.
        It will return the medication object with all of its properties set.
        The concentration is calculated using the calculate_concentration
        method.

        Returns:
            medication.Medication: The medication object.
        """
        self.calculate_concentration()

        return medications.Medication(self)
