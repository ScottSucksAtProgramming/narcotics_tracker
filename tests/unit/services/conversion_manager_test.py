"""Contains tests for the Conversion Manager Module.

Classes: 
"""

from narcotics_tracker.services.unit_conversion import ConversionManager


class Test_ConversionManager:
    """Unit tests the ConversionManager.

    Behaviors Tested:

    - Converts from grams to the standard unit.

    - Converts from milligrams to the standard unit.

    - Converts from micrograms to the standard unit.

    - Converts from the standard unit to grams.

    - Converts from the standard unit to milligrams.

    - Converts from the standard unit to micrograms.

    - Converts from grams to milliliters.

    - Converts from milligrams to milliliters.

    - Converts from micrograms to milliliters.
    """


def test_convert_grams_to_standard() -> None:
    answer = ConversionManager().to_standard(1, "g")

    assert answer == 100000000


def test_convert_milligrams_to_standard() -> None:
    answer = ConversionManager().to_standard(1, "mg")

    assert answer == 100000


def test_convert_micrograms_to_standard() -> None:
    answer = ConversionManager().to_standard(1, "mcg")
    assert answer == 100


def test_convert_standard_to_gram():
    answer = ConversionManager().to_preferred(100000000, "g")

    assert answer == 1


def test_convert_standard_to_milligrams():
    answer = ConversionManager().to_preferred(100000, "mg")

    assert answer == 1


def test_converts_standard_to_micrograms():
    answer = ConversionManager().to_preferred(100, "mcg")

    assert answer == 1


def test_conversion_g_to_milliliters():
    answer = ConversionManager().to_milliliters(1500000000, "g", 5)

    assert answer == 3


def test_conversion_mg_to_milliliters():
    answer = ConversionManager().to_milliliters(1000000, "mg", 5)

    assert answer == 2


def test_conversion_mcg_to_milliliters():
    answer = ConversionManager().to_milliliters(10000, "mcg", 50)

    assert answer == 2
