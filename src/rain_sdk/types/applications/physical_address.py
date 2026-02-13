# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PhysicalAddress"]


class PhysicalAddress(BaseModel):
    """
    Represents a physical address with components like street, city, region, postal code, and country.
    """

    city: str
    """The city of the address"""

    country: str
    """The full name of the country"""

    country_code: str = FieldInfo(alias="countryCode")
    """The 2-letter country code of the address"""

    line1: str
    """The first line of the street address"""

    postal_code: str = FieldInfo(alias="postalCode")
    """The postal or zip code of the address"""

    region: str
    """The region or state of the address"""

    line2: Optional[str] = None
    """The second line of the street address (optional)"""
