# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam
from .issuing_application_person_param import IssuingApplicationPersonParam

__all__ = ["CompanyReapplyParams", "Entity", "InitialUser"]


class CompanyReapplyParams(TypedDict, total=False):
    address: Required[PhysicalAddressParam]
    """The company's physical address"""

    entity: Required[Entity]
    """The company's legal entity details."""

    initial_user: Required[Annotated[InitialUser, PropertyInfo(alias="initialUser")]]
    """The initial user of the company who will be the owner on the Rain smart
    contract.

    This user must provide various personal details.
    """

    name: Required[str]
    """The name of the company reapplying for the corporate application"""

    representatives: Required[Iterable[IssuingApplicationPersonParam]]
    """The company's representatives"""

    ultimate_beneficial_owners: Required[
        Annotated[Iterable[IssuingApplicationPersonParam], PropertyInfo(alias="ultimateBeneficialOwners")]
    ]
    """The company's ultimate beneficial owners (UBOs)"""


class Entity(TypedDict, total=False):
    website: Required[str]
    """The legal entity's website"""

    description: str
    """A brief description of the legal entity, and its activities"""

    expected_spend: Annotated[str, PropertyInfo(alias="expectedSpend")]
    """The estimated monthly spending by the legal entity"""

    type: str
    """The type of legal entity (e.g., LLC, S Corp)"""


class InitialUser(TypedDict, total=False):
    address: Required[PhysicalAddressParam]
    """The user's address"""

    birth_date: Required[Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]]
    """The user's birth date"""

    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The 2-digit country code of the user's national ID issuer"""

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """The user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    national_id: Required[Annotated[str, PropertyInfo(alias="nationalId")]]
    """The user's national ID number. For the US, this is a 9-digit SSN"""

    role: str
    """This user's role at their company (not their role on the Rain platform)"""
