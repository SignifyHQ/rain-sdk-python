# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PinRetrieveResponse", "EncryptedPin"]


class EncryptedPin(BaseModel):
    """The encrypted pin"""

    data: str
    """The encrypted pin in base64"""

    iv: str
    """The initialization vector in base64"""


class PinRetrieveResponse(BaseModel):
    """The encrypted pin"""

    encrypted_pin: EncryptedPin = FieldInfo(alias="encryptedPin")
    """The encrypted pin"""
