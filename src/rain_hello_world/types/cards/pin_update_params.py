# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PinUpdateParams", "EncryptedPin"]


class PinUpdateParams(TypedDict, total=False):
    encrypted_pin: Required[Annotated[EncryptedPin, PropertyInfo(alias="encryptedPin")]]
    """The encrypted pin"""

    session_id: Required[Annotated[str, PropertyInfo(alias="SessionId")]]


class EncryptedPin(TypedDict, total=False):
    data: Required[str]
    """The encrypted PIN data"""

    iv: Required[str]
    """The initialization vector for encryption"""
