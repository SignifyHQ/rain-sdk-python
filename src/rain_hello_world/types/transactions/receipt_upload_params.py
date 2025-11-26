# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ReceiptUploadParams"]


class ReceiptUploadParams(TypedDict, total=False):
    receipt: Required[FileTypes]
    """The receipt file to upload, typically in PDF or other binary formats"""
