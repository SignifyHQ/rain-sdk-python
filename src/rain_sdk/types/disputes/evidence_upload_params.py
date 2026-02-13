# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["EvidenceUploadParams"]


class EvidenceUploadParams(TypedDict, total=False):
    evidence: Required[FileTypes]
    """The evidence to upload"""

    name: Required[str]
    """The name of the evidence"""

    type: Required[str]
    """The type of evidence"""
