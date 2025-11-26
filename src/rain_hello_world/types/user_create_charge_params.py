# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateChargeParams"]


class UserCreateChargeParams(TypedDict, total=False):
    amount: Required[int]
    """The amount of the charge, in cents"""

    description: Required[str]
    """The description of the charge"""
