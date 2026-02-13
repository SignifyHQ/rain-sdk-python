# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionCreateDisputeParams"]


class TransactionCreateDisputeParams(TypedDict, total=False):
    text_evidence: Annotated[str, PropertyInfo(alias="textEvidence")]
    """The textual evidence that supports the dispute"""
