# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .issuing_dispute import IssuingDispute

__all__ = ["DisputeListResponse"]

DisputeListResponse: TypeAlias = List[IssuingDispute]
