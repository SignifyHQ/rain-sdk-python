# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .issuing_transaction import IssuingTransaction

__all__ = ["TransactionListResponse"]

TransactionListResponse: TypeAlias = List[IssuingTransaction]
