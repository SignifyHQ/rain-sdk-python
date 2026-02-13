# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaymentInitiateResponse"]


class PaymentInitiateResponse(BaseModel):
    address: str
    """The address to send the payment to"""
