# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CardRetrieveSecretsResponse", "EncryptedCvc", "EncryptedPan"]


class EncryptedCvc(BaseModel):
    """The encrypted CVC"""

    data: str
    """The encrypted data"""

    iv: str
    """The initialization vector"""


class EncryptedPan(BaseModel):
    """The encrypted PAN"""

    data: str
    """The encrypted data"""

    iv: str
    """The initialization vector"""


class CardRetrieveSecretsResponse(BaseModel):
    """The encrypted data for the card"""

    encrypted_cvc: EncryptedCvc = FieldInfo(alias="encryptedCvc")
    """The encrypted CVC"""

    encrypted_pan: EncryptedPan = FieldInfo(alias="encryptedPan")
    """The encrypted PAN"""
