# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IssuingCardLimitParam"]


class IssuingCardLimitParam(TypedDict, total=False):
    """Represents the spending limit and frequency for a card."""

    amount: Required[int]
    """The maximum spending amount in cents"""

    frequency: Required[
        Literal["per24HourPeriod", "per7DayPeriod", "per30DayPeriod", "perYearPeriod", "allTime", "perAuthorization"]
    ]
    """The frequency at which the spending limit resets"""
