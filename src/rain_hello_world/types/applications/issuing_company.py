# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .physical_address import PhysicalAddress
from .issuing_application import IssuingApplication

__all__ = ["IssuingCompany", "IssuingCompanyUltimateBeneficialOwner"]


class IssuingCompanyUltimateBeneficialOwner(IssuingApplication):
    """The details of an issuing application."""

    id: str
    """The UBO's unique identifier"""


class IssuingCompany(IssuingApplication):
    """The details of an issuing application."""

    id: str
    """The company's unique identifier"""

    address: PhysicalAddress
    """The company's physical address"""

    name: str
    """The company's name on the Rain platform"""

    ultimate_beneficial_owners: Optional[List[IssuingCompanyUltimateBeneficialOwner]] = FieldInfo(
        alias="ultimateBeneficialOwners", default=None
    )
    """The company's ultimate beneficial owners (UBOs)"""
