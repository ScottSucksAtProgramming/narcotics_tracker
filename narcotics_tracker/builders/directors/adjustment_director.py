"""Directs the construction of Adjustment Objects."""

from typing import TYPE_CHECKING, Union

from narcotics_tracker import commands
from narcotics_tracker.builders import adjustment_builder
from narcotics_tracker.services.service_provider import ServiceProvider

if TYPE_CHECKING:
    from narcotics_tracker.items.adjustments import Adjustment


class Director:
    """Directs the construction of Data Items."""

    adjustment_builder = adjustment_builder.AdjustmentBuilder
    datetime_manager = ServiceProvider().start_services()[1]
    conversion_manager = ServiceProvider().start_services()[2]

    def new_adjustment(self) -> "Adjustment":
        datetime = self.datetime_manager.return_current_datetime()
        modified_by = self._get_string_input("your initials")
        adjustment_date = self._get_datetime_input("adjustment")
        event_code = self._get_string_input("the event code")
        medication_code = self._get_string_input("medication code")
        preferred_unit = commands.ReturnPreferredUnit().execute(medication_code)
        modifier = commands.ReturnEventModifier().execute(event_code)
        amount = self._get_numeric_input("the amount of medication to adjust")
        amount = self._return_converted_amount(modifier, amount, preferred_unit)
        reference_id = self._get_string_input("reference id")

        adjustment_builder = (
            self.adjustment_builder()
            .set_created_date(datetime)
            .set_modified_date(datetime)
            .set_modified_by(modified_by)
            .set_adjustment_date(adjustment_date)
            .set_event_code(event_code)
            .set_medication_code(medication_code)
            .set_adjustment_amount(amount)
            .set_reference_id(reference_id)
        )

        return adjustment_builder.build()

    def _return_converted_amount(
        self, modifier: int, amount: Union[float, int], preferred_unit: str
    ) -> float:
        """Converts amount to standard_unit applies modifier, and returns.

        Args:
            modifier (int): The event's modifier attribute.

            preferred_unit (str): The preferred unit of the medication.
        """
        converted_amount = self.conversion_manager.to_standard(amount, preferred_unit)
        return converted_amount * modifier

    def _get_string_input(self, prompt: str) -> str:
        """Requests and returns user input.

        Args:
            prompt (str): Prompt shown to the user.

            type (str, int, float): The type of input accepted.

        Returns:
            str, int, float: The requested user input.
        """
        user_input = input(f"Enter {prompt}: ")
        return str(user_input)

    def _get_numeric_input(self, prompt: str) -> float:
        """Requests and returns user input.

        Args:
            prompt (str): Prompt shown to the user.

            type (str, int, float): The type of input accepted.

        Returns:
            int, float: The requested user input.
        """
        user_input = input(f"Enter {prompt}: ")
        return float(user_input)

    def _get_datetime_input(self, prompt: str) -> int:
        """Requests a string datetime and returns a unix timestamp.

        Args:
            prompt (str): Prompt shown to the user.

        Returns:
            int: Converted date and time as a unix timestamp.
        """
        date = input(f"Enter the date on which the {prompt} happened (MM-DD-YYYY): ")
        time = input(f"Enter the time on which the {prompt} happened (HH:MM:SS): ")
        return self.datetime_manager.convert_to_timestamp(f"{date} {time}")
