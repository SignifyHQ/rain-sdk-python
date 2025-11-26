# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .physical_address import PhysicalAddress
from .issuing_application import IssuingApplication

__all__ = ["IssuingUser"]


class IssuingUser(IssuingApplication):
    id: str
    """The user's unique identifier"""

    email: str
    """The user's email address"""

    first_name: str = FieldInfo(alias="firstName")
    """The user's first name"""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether the user account is active"""

    is_terms_of_service_accepted: bool = FieldInfo(alias="isTermsOfServiceAccepted")
    """Indicates whether the user has accepted the terms of service"""

    last_name: str = FieldInfo(alias="lastName")
    """The user's last name"""

    address: Optional[PhysicalAddress] = None
    """The user's address"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """The identifier of the company the user belongs to, if applicable"""

    phone_country_code: Optional[str] = FieldInfo(alias="phoneCountryCode", default=None)
    """The country code for the user's phone number"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The user's phone number"""
