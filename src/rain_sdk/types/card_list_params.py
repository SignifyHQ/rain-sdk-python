# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .issuing_card_status import IssuingCardStatus

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    company_id: Annotated[str, PropertyInfo(alias="companyId")]
    """For corporate cards, the identifier of the company to get cards for"""

    cursor: str
    """The ID of the resource after which to start fetching"""

    limit: int
    """The number of resources to fetch"""

    status: IssuingCardStatus
    """Filter cards by status"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """The identifier of the user to get cards for"""
