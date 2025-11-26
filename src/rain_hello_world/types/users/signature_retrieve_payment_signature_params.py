# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SignatureRetrievePaymentSignatureParams"]


class SignatureRetrievePaymentSignatureParams(TypedDict, total=False):
    token: Required[str]
    """
    The address of the token that the payment should be made in, as a hex string for
    EVM or base58 string for Solana
    """

    admin_address: Required[Annotated[str, PropertyInfo(alias="adminAddress")]]
    """
    The address of the admin making the payment, as a hex string for EVM or base58
    string for Solana
    """

    amount: Required[str]
    """The amount of token that is being paid"""

    chain_id: Annotated[int, PropertyInfo(alias="chainId")]
    """The chain ID (base-10 number) that the smart contract is deployed on"""
