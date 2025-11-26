# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    account_purpose: Annotated[str, PropertyInfo(alias="accountPurpose")]
    """The purpose of the user's account"""

    address: PhysicalAddressParam
    """The user's address"""

    annual_salary: Annotated[str, PropertyInfo(alias="annualSalary")]
    """The user's annual salary"""

    birth_date: Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]
    """The user's birth date"""

    country_of_issue: Annotated[str, PropertyInfo(alias="countryOfIssue")]
    """The 2-digit country code of the user's national ID issuer"""

    expected_monthly_volume: Annotated[str, PropertyInfo(alias="expectedMonthlyVolume")]
    """The estimated monthly spending amount for the user"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The user's first name"""

    has_existing_documents: Annotated[bool, PropertyInfo(alias="hasExistingDocuments")]
    """
    Indicates whether the user will use existing documents for additional
    verification
    """

    ip_address: Annotated[str, PropertyInfo(alias="ipAddress")]
    """The user's IP address"""

    is_terms_of_service_accepted: Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]
    """Indicates whether the user has accepted the terms of service"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The user's last name"""

    national_id: Annotated[str, PropertyInfo(alias="nationalId")]
    """The user's national ID number. For the US, this is a 9-digit SSN."""

    occupation: str
    """The user's occupation"""
