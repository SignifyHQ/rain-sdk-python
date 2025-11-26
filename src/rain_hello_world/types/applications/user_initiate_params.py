# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserInitiateParams"]


class UserInitiateParams(TypedDict, total=False):
    email: str
    """The user's email address"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The user's first name"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The user's last name"""

    wallet_address: Annotated[str, PropertyInfo(alias="walletAddress")]
    """The user's wallet address.

    Required if using the hosted completion flow and a Rain-managed solution. Not
    required otherwise.
    """
