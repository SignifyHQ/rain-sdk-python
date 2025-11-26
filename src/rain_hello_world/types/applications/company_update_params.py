# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .physical_address_param import PhysicalAddressParam

__all__ = ["CompanyUpdateParams", "Entity"]


class CompanyUpdateParams(TypedDict, total=False):
    address: PhysicalAddressParam
    """The company's physical address"""

    entity: Entity
    """The company's legal entity details."""

    name: str
    """The name of the company for the corporate application"""


class Entity(TypedDict, total=False):
    description: str
    """A brief description of the legal entity and its activities"""

    expected_spend: Annotated[str, PropertyInfo(alias="expectedSpend")]
    """The estimated monthly spending by the legal entity"""

    registration_number: Annotated[str, PropertyInfo(alias="registrationNumber")]
    """The legal entity's registration number"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The legal entity's national tax ID"""

    type: str
    """The type of legal entity (e.g., LLC, S Corp)"""

    website: str
    """The legal entity's website"""
