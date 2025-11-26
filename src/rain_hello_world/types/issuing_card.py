# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .issuing_card_limit import IssuingCardLimit
from .issuing_card_status import IssuingCardStatus

__all__ = ["IssuingCard"]


class IssuingCard(BaseModel):
    id: str
    """The card's ID"""

    company_id: str = FieldInfo(alias="companyId")
    """The ID of the company that issued the card"""

    expiration_month: str = FieldInfo(alias="expirationMonth")
    """The expiration month of the card"""

    expiration_year: str = FieldInfo(alias="expirationYear")
    """The expiration year of the card"""

    last4: str
    """The last four digits of the card number"""

    status: IssuingCardStatus
    """The card's current status"""

    type: Literal["physical", "virtual"]
    """The type of the card (physical or virtual)"""

    user_id: str = FieldInfo(alias="userId")
    """The userID to whom the card was issued"""

    limit: Optional[IssuingCardLimit] = None
    """The card's spending limit"""

    token_wallets: Optional[List[str]] = FieldInfo(alias="tokenWallets", default=None)
