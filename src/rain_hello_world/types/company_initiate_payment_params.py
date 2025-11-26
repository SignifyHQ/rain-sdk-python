# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyInitiatePaymentParams"]


class CompanyInitiatePaymentParams(TypedDict, total=False):
    amount: Required[int]
    """The amount of the payment, in cents"""

    wallet_address: Required[Annotated[str, PropertyInfo(alias="walletAddress")]]
    """The wallet address the payment is being sent from"""

    chain_id: Annotated[int, PropertyInfo(alias="chainId")]
    """The chain ID (base-10 number) that the payment transaction is on"""
