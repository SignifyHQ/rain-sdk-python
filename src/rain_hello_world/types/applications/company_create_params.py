# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam
from .issuing_application_person_param import IssuingApplicationPersonParam

__all__ = ["CompanyCreateParams", "Entity", "InitialUser"]


class CompanyCreateParams(TypedDict, total=False):
    address: Required[PhysicalAddressParam]
    """The company's physical address"""

    entity: Required[Entity]
    """The company's legal entity details."""

    initial_user: Required[Annotated[InitialUser, PropertyInfo(alias="initialUser")]]
    """The initial user of the company.

    This user must have a wallet address, and their wallet address will be
    associated as an owner on the company's Rain smart contract.
    """

    name: Required[str]
    """The name of the company requesting to create an account"""

    representatives: Required[Iterable[IssuingApplicationPersonParam]]
    """The company's representatives"""

    ultimate_beneficial_owners: Required[
        Annotated[Iterable[IssuingApplicationPersonParam], PropertyInfo(alias="ultimateBeneficialOwners")]
    ]
    """The company's ultimate beneficial owners (UBOs)"""

    chain_id: Annotated[str, PropertyInfo(alias="chainId")]
    """The chain ID of the external collateral contract, if used.

    Not required when using Rain's collateral contracts.
    """

    contract_address: Annotated[str, PropertyInfo(alias="contractAddress")]
    """The address of the external collateral contract, if used.

    Not required when using Rain's collateral contracts.
    """

    source_key: Annotated[str, PropertyInfo(alias="sourceKey")]
    """A unique identifier for the origin of the user"""


class Entity(TypedDict, total=False):
    """The company's legal entity details."""

    name: Required[str]
    """The legal entity's name"""

    registration_number: Required[Annotated[str, PropertyInfo(alias="registrationNumber")]]
    """The legal entity's registration number"""

    tax_id: Required[Annotated[str, PropertyInfo(alias="taxId")]]
    """The legal entity's national tax id"""

    website: Required[str]
    """The legal entity's website"""

    description: str
    """A brief description of the legal entity and its activities"""

    expected_spend: Annotated[str, PropertyInfo(alias="expectedSpend")]
    """The estimated monthly spending by the legal entity"""

    type: str
    """The type of legal entity (e.g., LLC, S Corp)"""


class InitialUser(IssuingApplicationPersonParam, total=False):
    """The initial user of the company.

    This user must have a wallet address, and their wallet address will be associated as an owner on the company's Rain smart contract.
    """

    ip_address: Required[Annotated[str, PropertyInfo(alias="ipAddress")]]
    """This user's IP address"""

    is_terms_of_service_accepted: Required[Annotated[Literal[True], PropertyInfo(alias="isTermsOfServiceAccepted")]]
    """Indicates whether the user has accepted the terms of service"""

    role: str
    """This user's role at their company (not their role on the Rain platform)"""

    solana_address: Annotated[str, PropertyInfo(alias="solanaAddress")]
    """The user's Solana address.

    Either this or a EVM address is required if using a Rain-managed solution, but
    optional otherwise.
    """

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's Ethereum Virtual Machine (EVM) address.

    Either this or a Solana address is required if using a Rain-managed solution,
    but optional otherwise.
    """
