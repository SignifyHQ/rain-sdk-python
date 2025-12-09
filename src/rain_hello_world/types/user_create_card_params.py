# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .issuing_card_status import IssuingCardStatus
from .issuing_card_limit_param import IssuingCardLimitParam
from .applications.physical_address_param import PhysicalAddressParam

__all__ = ["UserCreateCardParams", "Configuration", "Shipping"]


class UserCreateCardParams(TypedDict, total=False):
    type: Required[Literal["physical", "virtual"]]

    billing: PhysicalAddressParam
    """The address that will serve as the billing address for the card.

    Defaults to the shipping address or team address if not explicitly provided.
    """

    configuration: Configuration
    """
    Configuration details for the card, including display name, product ID, and
    virtual card art
    """

    limit: IssuingCardLimitParam
    """The initial credit limit for the card, expressed in cents"""

    shipping: Shipping
    """The address to ship the card, if it is a physical card"""

    status: IssuingCardStatus
    """The initial status of the card"""


class Configuration(TypedDict, total=False):
    """
    Configuration details for the card, including display name, product ID, and virtual card art
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The name to display on the card.

    If omitted, it will be the user's full name trimmed to 30 characters.
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The product ID to use for the card, denoting its BIN range.

    Only relevant if custom product IDs or product references are part of the user's
    contract.
    """

    product_ref: Annotated[str, PropertyInfo(alias="productRef")]
    """The product reference to use for the card, denoting its appearance.

    Only relevant if custom product IDs or product references are part of the user's
    contract.
    """

    virtual_card_art: Annotated[str, PropertyInfo(alias="virtualCardArt")]
    """The virtual card art ID to use for the card, denoting its virtual appearance.

    Only relevant if custom virtual card art IDs are part of the user's contract.
    """


class Shipping(PhysicalAddressParam, total=False):
    """The address to ship the card, if it is a physical card"""

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """The phone number to use for shipping, if it is a physical card"""

    method: Literal["standard", "express", "international"]
    """The shipping method to use for the card.

    Standard and express are for US addresses, while international is for non-US
    addresses.
    """
