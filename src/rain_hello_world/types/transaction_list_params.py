# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    authorized_after: Annotated[Union[str, datetime], PropertyInfo(alias="authorizedAfter", format="iso8601")]
    """Filter transactions authorized after a specific date"""

    authorized_before: Annotated[Union[str, datetime], PropertyInfo(alias="authorizedBefore", format="iso8601")]
    """Filter transactions authorized before a specific date"""

    card_id: Annotated[str, PropertyInfo(alias="cardId")]
    """The ID of the card to get transactions for"""

    company_id: Annotated[str, PropertyInfo(alias="companyId")]
    """For corporate cards, the identifier of the company to get transactions for"""

    cursor: str
    """The ID of the resource after which to start fetching"""

    limit: int
    """The number of resources to fetch"""

    posted_after: Annotated[Union[str, datetime], PropertyInfo(alias="postedAfter", format="iso8601")]
    """Filter transactions posted after a specific date"""

    posted_before: Annotated[Union[str, datetime], PropertyInfo(alias="postedBefore", format="iso8601")]
    """Filter transactions posted before a specific date"""

    transaction_hash: Annotated[str, PropertyInfo(alias="transactionHash")]
    """The hash of the transaction to retrieve"""

    type: List[Literal["spend", "collateral", "payment", "fee"]]
    """The type of transactions to retrieve"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """The ID of the user to get transactions for"""
