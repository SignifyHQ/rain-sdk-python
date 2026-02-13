# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IssuingSignature", "IfSignatureIsPending", "IfSignatureIsReady", "IfSignatureIsReadySignature"]


class IfSignatureIsPending(BaseModel):
    """
    Indicates the signature is pending and provides the time after which a retry is possible.
    """

    retry_after: int = FieldInfo(alias="retryAfter")
    """The number of seconds after which the signature can be retried"""

    status: Literal["pending"]
    """The status of the signature"""


class IfSignatureIsReadySignature(BaseModel):
    data: str
    """The actual signature data"""

    salt: str
    """The salt used to generate the signature"""


class IfSignatureIsReady(BaseModel):
    """
    Indicates that the signature is ready and includes the signature data and expiration time.
    """

    signature: IfSignatureIsReadySignature

    status: Literal["ready"]
    """The status of the signature"""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """The time at which the signature will expire"""


IssuingSignature: TypeAlias = Union[IfSignatureIsPending, IfSignatureIsReady]
