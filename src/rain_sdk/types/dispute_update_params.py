# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeUpdateParams"]


class DisputeUpdateParams(TypedDict, total=False):
    status: Literal["canceled"]
    """The new status of the dispute. Can only be set to 'canceled'."""

    text_evidence: Annotated[str, PropertyInfo(alias="textEvidence")]
    """The textual evidence to add to the dispute"""
