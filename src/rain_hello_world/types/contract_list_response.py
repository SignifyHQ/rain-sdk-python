# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .issuing_contract import IssuingContract

__all__ = ["ContractListResponse"]

ContractListResponse: TypeAlias = List[IssuingContract]
