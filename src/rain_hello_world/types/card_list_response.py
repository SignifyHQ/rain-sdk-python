# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .issuing_card import IssuingCard

__all__ = ["CardListResponse"]

CardListResponse: TypeAlias = List[IssuingCard]
