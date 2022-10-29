"""This module handles the validation of DataItem attributes."""


from typing import Union

from narcotics_tracker.services.service_provider import ServiceProvider


class ValidationManager:
    """Evaluates and fixes incorrect Dataitem attributes prior to storage."""

    service_provider = ServiceProvider()
