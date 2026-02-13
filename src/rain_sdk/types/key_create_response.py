# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    """
    Represents a unique key used for issuing, typically used for authentication or encryption purposes.
    """

    id: str
    """The key's unique identifier"""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """The expiration date and time of the key"""

    key: str
    """The actual key used for the issuing process"""

    name: str
    """The name assigned to the key"""
