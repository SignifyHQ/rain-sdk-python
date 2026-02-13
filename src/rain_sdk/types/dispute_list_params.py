# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeListParams"]


class DisputeListParams(TypedDict, total=False):
    company_id: Annotated[str, PropertyInfo(alias="companyId")]
    """For corporate cards, the identifier of the company to get disputes for"""

    cursor: str
    """The ID of the resource after which to start fetching"""

    limit: int
    """The number of resources to fetch"""

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
    """The ID of the transaction to get disputes for"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """The ID of the user to get disputes for"""
