# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "IssuingTransaction",
    "UnionMember0",
    "UnionMember0Spend",
    "UnionMember1",
    "UnionMember1Collateral",
    "UnionMember2",
    "UnionMember2Payment",
    "UnionMember3",
    "UnionMember3Fee",
]


class UnionMember0Spend(BaseModel):
    """
    Details specific to a spend transaction, including merchant, amount, and user information.
    """

    amount: int
    """The amount of the transaction, in cents"""

    authorized_at: str = FieldInfo(alias="authorizedAt")
    """The time at which the transaction was authorized"""

    card_id: str = FieldInfo(alias="cardId")
    """The unique identifier of the card used for the transaction"""

    card_type: Literal["physical", "virtual"] = FieldInfo(alias="cardType")
    """The type of card used for the transaction"""

    currency: str
    """The currency of the transaction"""

    merchant_category: str = FieldInfo(alias="merchantCategory")
    """The category of the merchant (e.g., electronics, food)"""

    merchant_category_code: str = FieldInfo(alias="merchantCategoryCode")
    """The merchant's category code"""

    merchant_name: str = FieldInfo(alias="merchantName")
    """The name of the merchant where the transaction took place"""

    receipt: bool
    """Indicates whether a receipt was generated for the transaction"""

    status: Literal["pending", "reversed", "declined", "completed"]
    """The status of the transaction"""

    user_email: str = FieldInfo(alias="userEmail")
    """The email address of the user who made the transaction"""

    user_first_name: str = FieldInfo(alias="userFirstName")
    """The first name of the user who made the transaction"""

    user_id: str = FieldInfo(alias="userId")
    """The identifier of the user who made the transaction"""

    user_last_name: str = FieldInfo(alias="userLastName")
    """The last name of the user who made the transaction"""

    authorization_method: Optional[str] = FieldInfo(alias="authorizationMethod", default=None)
    """The method used for authorization of the transaction"""

    authorized_amount: Optional[int] = FieldInfo(alias="authorizedAmount", default=None)
    """The authorized amount of the transaction, in cents"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """The identifier of the company under which the transaction was made"""

    declined_reason: Optional[str] = FieldInfo(alias="declinedReason", default=None)
    """The reason why the transaction was declined"""

    enriched_merchant_category: Optional[str] = FieldInfo(alias="enrichedMerchantCategory", default=None)
    """An enriched category of the merchant, providing further details"""

    enriched_merchant_icon: Optional[str] = FieldInfo(alias="enrichedMerchantIcon", default=None)
    """The enriched icon of the merchant"""

    enriched_merchant_name: Optional[str] = FieldInfo(alias="enrichedMerchantName", default=None)
    """An enriched name of the merchant, possibly with additional information"""

    local_amount: Optional[int] = FieldInfo(alias="localAmount", default=None)
    """The amount of the transaction in local currency, in cents"""

    local_currency: Optional[str] = FieldInfo(alias="localCurrency", default=None)
    """The local currency of the transaction"""

    memo: Optional[str] = None
    """A memo or note associated with the transaction"""

    posted_at: Optional[str] = FieldInfo(alias="postedAt", default=None)
    """The time at which the transaction was posted"""


class UnionMember0(BaseModel):
    """Represents a transaction of type 'spend'.

    This includes details such as the transaction amount, merchant, and the associated user.
    """

    id: str
    """The unique identifier of the transaction"""

    spend: UnionMember0Spend
    """
    Details specific to a spend transaction, including merchant, amount, and user
    information.
    """

    type: Literal["spend"]
    """The type of transaction"""


class UnionMember1Collateral(BaseModel):
    """
    Details of the collateral transaction, including amount, currency, and transaction details.
    """

    amount: float
    """The amount of the collateral transaction, in cents"""

    chain_id: int = FieldInfo(alias="chainId")
    """The chain ID (base-10 number) that the collateral transaction is on"""

    currency: str
    """The currency of the collateral transaction"""

    transaction_hash: str = FieldInfo(alias="transactionHash")
    """The hash of the collateral transaction"""

    wallet_address: str = FieldInfo(alias="walletAddress")
    """The wallet address the collateral was added from"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """The identifier of the company under which the collateral transaction was made"""

    memo: Optional[str] = None
    """A memo or note associated with the collateral transaction"""

    posted_at: Optional[datetime] = FieldInfo(alias="postedAt", default=None)
    """The time at which the collateral transaction was posted"""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The identifier of the user who provided the collateral"""


class UnionMember1(BaseModel):
    """
    Represents a collateral transaction, where a user provides collateral for a transaction.
    """

    id: str
    """The unique identifier of the transaction"""

    collateral: UnionMember1Collateral
    """
    Details of the collateral transaction, including amount, currency, and
    transaction details.
    """

    type: Literal["collateral"]
    """The type of transaction, in this case, a collateral transaction"""


class UnionMember2Payment(BaseModel):
    """Details of the payment transaction, including amount, currency, and status."""

    amount: int
    """The amount of the transaction, in cents"""

    currency: str
    """The currency of the transaction"""

    status: Literal["pending", "completed"]
    """The status of the transaction"""

    chain_id: Optional[int] = FieldInfo(alias="chainId", default=None)
    """The chain ID (base-10 number) that the payment transaction is on"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """The identifier of the company under which the payment transaction was made"""

    memo: Optional[str] = None
    """The memo or note associated with the transaction"""

    posted_at: Optional[str] = FieldInfo(alias="postedAt", default=None)
    """The time at which the payment transaction was posted"""

    transaction_hash: Optional[str] = FieldInfo(alias="transactionHash", default=None)
    """The hash of the payment transaction"""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The identifier of the user who made the payment"""

    wallet_address: Optional[str] = FieldInfo(alias="walletAddress", default=None)
    """The wallet address from which the payment was made"""


class UnionMember2(BaseModel):
    """
    Represents a payment transaction, where a payment is made for a particular service or product.
    """

    id: str
    """The unique identifier of the payment transaction"""

    payment: UnionMember2Payment
    """Details of the payment transaction, including amount, currency, and status."""

    type: Literal["payment"]
    """The type of transaction"""


class UnionMember3Fee(BaseModel):
    """Details of the fee transaction, including amount, description, and status."""

    amount: int
    """The amount of the fee, in cents"""

    company_id: Optional[str] = FieldInfo(alias="companyId", default=None)
    """The identifier of the company to which the fee was charged"""

    description: Optional[str] = None
    """The description of the fee"""

    posted_at: Optional[datetime] = FieldInfo(alias="postedAt", default=None)
    """The time at which the fee was posted"""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The identifier of the user to whom the fee was charged"""


class UnionMember3(BaseModel):
    """Represents a fee transaction, where a fee is charged for a service or product."""

    id: str
    """The identifier of the fee transaction"""

    fee: UnionMember3Fee
    """Details of the fee transaction, including amount, description, and status."""

    type: Literal["fee"]
    """The type of transaction, in this case, a fee transaction"""


IssuingTransaction: TypeAlias = Annotated[
    Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3], PropertyInfo(discriminator="type")
]
