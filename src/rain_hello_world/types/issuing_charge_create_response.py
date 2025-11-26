# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IssuingChargeCreateResponse"]


class IssuingChargeCreateResponse(BaseModel):
    id: str
    """The identifier of the charge"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the charge was created"""

    amount: Optional[int] = None
    """The amount of the charge, in cents"""

    description: Optional[str] = None
    """The description of the charge"""
