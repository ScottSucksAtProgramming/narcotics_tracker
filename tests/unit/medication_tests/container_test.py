"""Contains the TestContainer class."""

import pytest

from narcotics_tracker.medication.containers import Container
from narcotics_tracker.units.units import Unit
from narcotics_tracker.medication.medication import Medication


class TestContainer:
    """Test the Container class."""

    def test_VIAL_returns_correct_string(self):
        """Check that VIAL returns the correct string."""

        assert Container.VIAL.value == "Vial"

    def test_AMPULE_returns_correct_string(self):
        """Check that AMPULE returns the correct string."""

        assert Container.AMPULE.value == "Ampule"

    def test_PRE_FILLED_SYRINGE_returns_correct_string(self):
        """Check that PRE_FILLED_SYRINGE returns the correct string."""

        assert Container.PRE_FILLED_SYRINGE.value == "Pre-filled Syringe"

    def test_PRE_MIXED_BAG_returns_correct_string(self):
        """Check that PRE_MIXED_BAG returns the correct string."""

        assert Container.PRE_MIXED_BAG.value == "Pre-mixed Bag"
