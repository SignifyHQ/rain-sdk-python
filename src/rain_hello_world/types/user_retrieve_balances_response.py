# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserRetrieveBalancesResponse"]


class UserRetrieveBalancesResponse(BaseModel):
    balance_due: int = FieldInfo(alias="balanceDue")
    """Balance due of the user, in cents"""

    credit_limit: int = FieldInfo(alias="creditLimit")
    """Credit limit of the user, in cents"""

    pending_charges: int = FieldInfo(alias="pendingCharges")
    """Pending charges of the user, in cents"""

    posted_charges: int = FieldInfo(alias="postedCharges")
    """Posted charges of the user, in cents"""

    spending_power: int = FieldInfo(alias="spendingPower")
    """The amount of money the user can spend, in cents"""
