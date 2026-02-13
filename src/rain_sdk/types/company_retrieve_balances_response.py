# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CompanyRetrieveBalancesResponse"]


class CompanyRetrieveBalancesResponse(BaseModel):
    balance_due: int = FieldInfo(alias="balanceDue")
    """Balance due of the company, in cents"""

    credit_limit: int = FieldInfo(alias="creditLimit")
    """Credit limit of the company, in cents"""

    pending_charges: int = FieldInfo(alias="pendingCharges")
    """Pending charges of the company, in cents"""

    posted_charges: int = FieldInfo(alias="postedCharges")
    """Posted charges of the company, in cents"""

    spending_power: int = FieldInfo(alias="spendingPower")
    """The amount of money the company can spend, in cents"""
