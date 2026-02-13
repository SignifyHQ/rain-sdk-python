# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam

__all__ = ["UserCreateParams", "UsingSumsubShareToken", "UsingPersonaShareToken", "UsingAPI"]


class UsingSumsubShareToken(TypedDict, total=False):
    account_purpose: Required[Annotated[str, PropertyInfo(alias="accountPurpose")]]
    """The purpose of the user's account"""

    annual_salary: Required[Annotated[str, PropertyInfo(alias="annualSalary")]]
    """The user's annual salary"""

    expected_monthly_volume: Required[Annotated[str, PropertyInfo(alias="expectedMonthlyVolume")]]
    """The estimated monthly spending amount for the user"""

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """This user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    occupation: Required[str]
    """The user's occupation"""

    sumsub_share_token: Required[Annotated[str, PropertyInfo(alias="sumsubShareToken")]]
    """The Sumsub share token used for user verification"""

    chain_id: Annotated[str, PropertyInfo(alias="chainId")]
    """The chain ID of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    contract_address: Annotated[str, PropertyInfo(alias="contractAddress")]
    """The address of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    has_existing_documents: Annotated[bool, PropertyInfo(alias="hasExistingDocuments")]
    """
    Indicates whether the user will use existing documents for additional
    verification
    """

    solana_address: Annotated[str, PropertyInfo(alias="solanaAddress")]
    """The user's Solana address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """

    source_key: Annotated[str, PropertyInfo(alias="sourceKey")]
    """A unique identifier for the source of this user."""

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's Ethereum Virtual Machine (EVM) address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """


class UsingPersonaShareToken(TypedDict, total=False):
    account_purpose: Required[Annotated[str, PropertyInfo(alias="accountPurpose")]]
    """The purpose of the user's account"""

    annual_salary: Required[Annotated[str, PropertyInfo(alias="annualSalary")]]
    """The user's annual salary"""

    expected_monthly_volume: Required[Annotated[str, PropertyInfo(alias="expectedMonthlyVolume")]]
    """The estimated monthly spending amount for the user"""

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """This user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    occupation: Required[str]
    """The user's occupation"""

    persona_share_token: Required[Annotated[str, PropertyInfo(alias="personaShareToken")]]
    """The Persona inquiry ID"""

    chain_id: Annotated[str, PropertyInfo(alias="chainId")]
    """The chain ID of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    contract_address: Annotated[str, PropertyInfo(alias="contractAddress")]
    """The address of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    has_existing_documents: Annotated[bool, PropertyInfo(alias="hasExistingDocuments")]
    """
    Indicates whether the user will use existing documents for additional
    verification
    """

    solana_address: Annotated[str, PropertyInfo(alias="solanaAddress")]
    """The user's Solana address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """

    source_key: Annotated[str, PropertyInfo(alias="sourceKey")]
    """A unique identifier for the source of this user."""

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's Ethereum Virtual Machine (EVM) address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """


class UsingAPI(TypedDict, total=False):
    account_purpose: Required[Annotated[str, PropertyInfo(alias="accountPurpose")]]
    """The purpose of the user's account"""

    address: Required[PhysicalAddressParam]
    """The person's address"""

    annual_salary: Required[Annotated[str, PropertyInfo(alias="annualSalary")]]
    """The user's annual salary"""

    birth_date: Required[Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]]
    """The person's birth date"""

    country_of_issue: Required[Annotated[str, PropertyInfo(alias="countryOfIssue")]]
    """The 2-digit country code of the person's national ID issuer"""

    email: Required[str]
    """The user's email address"""

    expected_monthly_volume: Required[Annotated[str, PropertyInfo(alias="expectedMonthlyVolume")]]
    """The estimated monthly spending amount for the user"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The person's first name"""

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """This user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The person's last name"""

    national_id: Required[Annotated[str, PropertyInfo(alias="nationalId")]]
    """The person's national ID number. For the US, this is a 9-digit SSN"""

    occupation: Required[str]
    """The user's occupation"""

    id: str
    """The person's unique identifier"""

    chain_id: Annotated[str, PropertyInfo(alias="chainId")]
    """The chain ID of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    contract_address: Annotated[str, PropertyInfo(alias="contractAddress")]
    """The address of the user's external collateral contract, if applicable.

    Not required when using Rain's collateral contracts.
    """

    has_existing_documents: Annotated[bool, PropertyInfo(alias="hasExistingDocuments")]
    """
    Indicates whether the user will use existing documents for additional
    verification
    """

    phone_country_code: Annotated[str, PropertyInfo(alias="phoneCountryCode")]
    """The country code for the phone number"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the person"""

    solana_address: Annotated[str, PropertyInfo(alias="solanaAddress")]
    """The user's Solana address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """

    source_key: Annotated[str, PropertyInfo(alias="sourceKey")]
    """A unique identifier for the source of this user."""

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's Ethereum Virtual Machine (EVM) address.

    Either walletAddress or solanaAddress is required if using a Rain-managed
    solution, but optional otherwise.
    """


UserCreateParams: TypeAlias = Union[UsingSumsubShareToken, UsingPersonaShareToken, UsingAPI]
