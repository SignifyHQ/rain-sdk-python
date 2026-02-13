# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam

__all__ = ["IssuingApplicationPersonParam"]


class IssuingApplicationPersonParam(TypedDict, total=False):
    address: Required[PhysicalAddressParam]
    """The person's address"""

    birth_date: Required[Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]]
    """The person's birth date"""

    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The 2-digit country code of the person's national ID issuer"""

    email: Required[str]
    """The user's email address"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The person's first name"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The person's last name"""

    national_id: Required[Annotated[str, PropertyInfo(alias="nationalId")]]
    """The person's national ID number. For the US, this is a 9-digit SSN"""

    id: str
    """The person's unique identifier"""

    phone_country_code: Annotated[str, PropertyInfo(alias="phoneCountryCode")]
    """The country code for the phone number"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the person"""
