# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IssuingCardLimit"]


class IssuingCardLimit(BaseModel):
    """Represents the spending limit and frequency for a card."""

    amount: int
    """The maximum spending amount in cents"""

    frequency: Literal[
        "per24HourPeriod", "per7DayPeriod", "per30DayPeriod", "perYearPeriod", "allTime", "perAuthorization"
    ]
