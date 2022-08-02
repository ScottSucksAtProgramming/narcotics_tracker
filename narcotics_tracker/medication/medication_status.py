"""Contains the status options for a medication."""

from enum import Enum


class MedicationStatus(Enum):
    """Enum for medication status.

    Medications may be come unavailable, or discontinued. The medication
    status is used to determine if the medication is available for use.

    Attributes:
        AVAILABLE: Medication is available for use.
        UNAVAILABLE: Medication is unavailable for use.
        DISCONTINUED: Medication is discontinued.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DISCONTINUED = "Discontinued"
