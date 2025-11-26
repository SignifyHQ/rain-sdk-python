# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .applications.issuing_company import IssuingCompany

__all__ = ["CompanyListResponse"]

CompanyListResponse: TypeAlias = List[IssuingCompany]
