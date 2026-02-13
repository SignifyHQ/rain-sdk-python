# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    cursor: str
    """The ID of the resource after which to start fetching"""

    limit: int
    """The number of resources to fetch"""
