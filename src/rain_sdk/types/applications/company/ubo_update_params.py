# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..physical_address_param import PhysicalAddressParam

__all__ = ["UboUpdateParams"]


class UboUpdateParams(TypedDict, total=False):
    company_id: Required[Annotated[str, PropertyInfo(alias="companyId")]]

    address: PhysicalAddressParam
    """The UBO's address"""

    birth_date: Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]
    """The UBO's birth date"""

    country_of_issue: Annotated[str, PropertyInfo(alias="countryOfIssue")]
    """The 2-digit country code of the user's national ID issuer"""

    email: str
    """The UBO's email address"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The UBO's first name"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The UBO's last name"""

    national_id: Annotated[str, PropertyInfo(alias="nationalId")]
    """The UBO's national ID number. For the US, this is a 9-digit SSN"""
