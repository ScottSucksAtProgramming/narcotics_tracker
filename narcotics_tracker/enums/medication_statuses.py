"""Contains the class defining controlled substance statuses.

Classes:
    MedicationStatuses: Defines the acceptable values for medication status.
"""
from enum import Enum


class MedicationStatus(Enum):
    """Defines the acceptable values for medication status.

    Medications may be come unavailable, or discontinued. The medication
    status is used to determine if the medication is available for use.

    Available Statuses:
        - ACTIVE: Medication is available for use.
        - INACTIVE: Medication is unavailable for use.
        - DISCONTINUED: Medication is discontinued.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DISCONTINUED = "Discontinued"
