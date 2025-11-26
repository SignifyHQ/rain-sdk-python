# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam

__all__ = ["UserReapplyParams"]


class UserReapplyParams(TypedDict, total=False):
    account_purpose: Required[Annotated[str, PropertyInfo(alias="accountPurpose")]]
    """The purpose of the user's account"""

    address: Required[PhysicalAddressParam]
    """The user's address"""

    annual_salary: Required[Annotated[str, PropertyInfo(alias="annualSalary")]]
    """The user's annual salary"""

    birth_date: Required[Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]]
    """The user's birth date"""

    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The 2-digit country code of the user's national ID issuer"""

    expected_monthly_volume: Required[Annotated[str, PropertyInfo(alias="expectedMonthlyVolume")]]
    """The estimated monthly spending amount for the user"""

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """The user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    national_id: Required[Annotated[str, PropertyInfo(alias="nationalId")]]
    """The user's national ID number. For the US, this is a 9-digit SSN"""

    occupation: Required[str]
    """The user's occupation"""

    has_existing_documents: Annotated[bool, PropertyInfo(alias="hasExistingDocuments")]
    """
    Indicates whether the user will use existing documents for additional
    verification
    """
