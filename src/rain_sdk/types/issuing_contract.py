# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IssuingContract", "Token"]


class Token(BaseModel):
    address: str
    """The address of the token contract"""

    advance_rate: Optional[float] = FieldInfo(alias="advanceRate", default=None)
    """The advance rate for the token"""

    balance: Optional[str] = None
    """The balance of the token"""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """The exchange rate for the token"""


class IssuingContract(BaseModel):
    """
    Represents an issuing contract with details about its deployment and token handling.
    """

    id: str
    """The contract's unique identifier"""

    chain_id: int = FieldInfo(alias="chainId")
    """The chain ID (base-10 number) that the smart contract is deployed on"""

    contract_version: int = FieldInfo(alias="contractVersion")
    """Version of the contract"""

    controller_address: str = FieldInfo(alias="controllerAddress")
    """The address of the contract's controller"""

    proxy_address: str = FieldInfo(alias="proxyAddress")
    """The proxy address of the contract"""

    tokens: List[Token]
    """Tokens that the contract accepts for transactions"""

    deposit_address: Optional[str] = FieldInfo(alias="depositAddress", default=None)
    """The address where funds should be deposited"""
