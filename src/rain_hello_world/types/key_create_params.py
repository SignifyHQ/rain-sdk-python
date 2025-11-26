# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    expires_at: Required[Annotated[str, PropertyInfo(alias="expiresAt")]]
    """The expiration timestamp of the key"""

    name: Required[str]
    """The name of the key being created"""
