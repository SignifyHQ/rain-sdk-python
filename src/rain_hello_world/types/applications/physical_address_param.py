# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhysicalAddressParam"]


class PhysicalAddressParam(TypedDict, total=False):
    city: Required[str]
    """The city of the address"""

    country: Required[str]
    """The full name of the country"""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The 2-letter country code of the address"""

    line1: Required[str]
    """The first line of the street address"""

    postal_code: Required[Annotated[str, PropertyInfo(alias="postalCode")]]
    """The postal or zip code of the address"""

    region: Required[str]
    """The region or state of the address"""

    line2: str
    """The second line of the street address (optional)"""
