# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TransactionUpdateParams"]


class TransactionUpdateParams(TypedDict, total=False):
    memo: str
    """
    A memo or note to attach to the transaction, providing additional information or
    context
    """
