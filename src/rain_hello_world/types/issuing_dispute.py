# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IssuingDispute"]


class IssuingDispute(BaseModel):
    id: str
    """The dispute's unique identifier"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the dispute was created"""

    status: Literal["pending", "inReview", "accepted", "rejected", "canceled"]
    """The current status of the dispute"""

    transaction_id: str = FieldInfo(alias="transactionId")
    """The transaction's unique identifier"""

    resolved_at: Optional[datetime] = FieldInfo(alias="resolvedAt", default=None)
    """The date and time when the dispute was resolved, if applicable"""

    text_evidence: Optional[str] = FieldInfo(alias="textEvidence", default=None)
    """Textual evidence provided by the parties involved in the dispute"""
