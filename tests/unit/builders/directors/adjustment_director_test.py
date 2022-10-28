"""Tests the Adjustment Director Module."""


from narcotics_tracker.builders.directors.adjustment_director import Director


class Test_AdjustmentDirector:
    """Unit tests the AdjustmentDirector.

    Behaviors Tested:
        - Converts Given Amount Correctly.
    """

    def test_AdjustmentDirector_converts_amount_correctly(self):
        adjustment_director = Director()

        adjusted_amount = adjustment_director._return_converted_amount(
            modifier=-1, amount=10, preferred_unit="mg"
        )

        assert adjusted_amount == -10000
