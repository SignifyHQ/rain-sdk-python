# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .applications.physical_address_param import PhysicalAddressParam

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]
    """The user's email address"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The user's first name"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The user's last name"""

    address: PhysicalAddressParam
    """The user's address"""

    phone_country_code: Annotated[str, PropertyInfo(alias="phoneCountryCode")]
    """The user's phone country code"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The user's phone number"""

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's wallet address"""
