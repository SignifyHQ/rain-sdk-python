# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .applications.physical_address_param import PhysicalAddressParam

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    address: PhysicalAddressParam
    """The user's address"""

    email: str
    """The user's email address"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The user's first name"""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether the user is active"""

    is_terms_of_service_accepted: Annotated[bool, PropertyInfo(alias="isTermsOfServiceAccepted")]
    """Indicates whether the user has accepted the terms of service"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The user's last name"""

    phone_country_code: Annotated[str, PropertyInfo(alias="phoneCountryCode")]
    """The user's phone country code"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The user's phone number"""
