"""Contains tests for the Conversion Manager Module.

Classes: 
"""

from narcotics_tracker.services.conversion_manager import ConversionManager


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

    assert answer == 100000000.0


def test_convert_milligrams_to_standard() -> None:
    answer = ConversionManager().to_standard(663.4, "mg")

    assert answer == 66340000.0


def test_convert_micrograms_to_standard() -> None:
    answer = ConversionManager().to_standard(7450, "mcg")
    assert answer == 745000.0


def test_convert_standard_to_gram():
    answer = ConversionManager().to_preferred(100000000.0, "g")

    assert answer == 1


def test_convert_standard_to_milligrams():
    answer = ConversionManager().to_preferred(66340000.0, "mg")

    assert answer == 663.4


def test_converts_standard_to_micrograms():
    answer = ConversionManager().to_preferred(745000.0, "mcg")

    assert answer == 7450


def test_conversion_g_to_milliliters():
    answer = ConversionManager().to_milliliters(100000000000.0, "g", 5)

    assert answer == 200


def test_conversion_mg_to_milliliters():
    answer = ConversionManager().to_milliliters(69000000.0, "mg", 10)

    assert answer == 69


def test_conversion_mcg_to_milliliters():
    answer = ConversionManager().to_milliliters(745000.0, "mcg", 50)

    assert answer == 149


def test_ml_to_mg():
    amount = 149
    concentration = 5
    amount_in_mg = amount * concentration

    assert amount_in_mg == 745


def test_2():
    assert 0 - -3 == 3
