# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .applications.physical_address_param import PhysicalAddressParam

__all__ = ["CompanyUpdateParams"]


class CompanyUpdateParams(TypedDict, total=False):
    address: PhysicalAddressParam
    """The company's physical address"""

    name: str
    """The company's name on the Rain platform"""
