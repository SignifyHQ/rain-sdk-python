# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .issuing_card_status import IssuingCardStatus
from .issuing_card_limit_param import IssuingCardLimitParam
from .applications.physical_address_param import PhysicalAddressParam

__all__ = ["CardUpdateParams", "Configuration"]


class CardUpdateParams(TypedDict, total=False):
    billing: PhysicalAddressParam
    """The billing address associated with the card."""

    configuration: Configuration
    """Configuration for the card, such as virtual card art"""

    limit: IssuingCardLimitParam
    """The limit associated with the card"""

    status: IssuingCardStatus
    """The current status of the card"""


class Configuration(TypedDict, total=False):
    """Configuration for the card, such as virtual card art"""

    virtual_card_art: Annotated[str, PropertyInfo(alias="virtualCardArt")]
    """The virtual card art ID used to customize the card's appearance, if applicable"""
