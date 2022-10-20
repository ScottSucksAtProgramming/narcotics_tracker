"""Contains the unit tests for the Unit Converter.

Classes: 
"""

from narcotics_tracker.utils.unit_converter import UnitConverter


class Test_UnitConverter:
    """Unit tests the Unit Converter.

    Behaviors Tested:

    - Converts from grams to the standard unit.
    - Converts from milligrams to the standard unit.
    - Converts from micrograms to the standard unit.
    - Converts from the standard unit to grams.
    - Converts from the standard unit to milligrams.
    - Converts from the standard unit to micrograms.
    - Converts
    """


def test_convert_grams_to_standard() -> None:
    answer = UnitConverter(1, "g").to_standard()

    assert answer == 1000000


def test_convert_milligrams_to_standard() -> None:
    answer = UnitConverter(1, "mg").to_standard()

    assert answer == 1000


def test_convert_micrograms_to_standard() -> None:
    answer = UnitConverter(1, "mcg").to_standard()


def test_convert_standard_to_gram():
    answer = UnitConverter(1000000, "g").to_preferred()

    assert answer == 1


def test_convert_standard_to_milligrams():
    answer = UnitConverter(1000, "mg").to_preferred()

    assert answer == 1


def test_converts_standard_to_micrograms():
    answer = UnitConverter(1, "mcg").to_preferred()

    assert answer == 1


def test_conversion_g_to_milliliters():
    answer = UnitConverter(15000000, "g", 5).to_milliliters()

    assert answer == 3


def test_conversion_mg_to_milliliters():
    answer = UnitConverter(10000, "mg", 5).to_milliliters()

    assert answer == 2


def test_conversion_mcg_to_milliliters():
    answer = UnitConverter(100, "mcg", 50).to_milliliters()

    assert answer == 2
