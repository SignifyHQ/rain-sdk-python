# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .issuing_application import IssuingApplication

__all__ = ["CompanyRetrieveResponse", "CompanyRetrieveResponseUltimateBeneficialOwner"]


class CompanyRetrieveResponseUltimateBeneficialOwner(IssuingApplication):
    id: str
    """The UBO's unique identifier"""

    email: Optional[str] = None
    """The UBO's email address"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The UBO's first name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The UBO's last name"""


class CompanyRetrieveResponse(IssuingApplication):
    id: str
    """The identifier of the company application"""

    ultimate_beneficial_owners: List[CompanyRetrieveResponseUltimateBeneficialOwner] = FieldInfo(
        alias="ultimateBeneficialOwners"
    )
    """The company's ultimate beneficial owners (UBOs)"""
