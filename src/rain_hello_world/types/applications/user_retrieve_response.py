# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .issuing_application import IssuingApplication

__all__ = ["UserRetrieveResponse"]


class UserRetrieveResponse(IssuingApplication):
    id: str
    """The identifier of the user's application"""
