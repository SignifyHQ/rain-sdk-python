# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .applications.issuing_user import IssuingUser

__all__ = ["UserListResponse"]

UserListResponse: TypeAlias = List[IssuingUser]
