# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "IssuingApplication",
    "ApplicationCompletionLink",
    "ApplicationCompletionLinkParams",
    "ApplicationExternalVerificationLink",
    "ApplicationExternalVerificationLinkParams",
]


class ApplicationCompletionLinkParams(BaseModel):
    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The user's unique identifier"""


class ApplicationCompletionLink(BaseModel):
    """The link to the application completion page"""

    url: str
    """The URL for the completion page"""

    params: Optional[ApplicationCompletionLinkParams] = None


class ApplicationExternalVerificationLinkParams(BaseModel):
    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """The user's unique identifier"""


class ApplicationExternalVerificationLink(BaseModel):
    """The link to the external verification page for the application"""

    url: str
    """The URL for the external verification page"""

    params: Optional[ApplicationExternalVerificationLinkParams] = None


class IssuingApplication(BaseModel):
    """The details of an issuing application."""

    application_status: Literal[
        "approved", "pending", "needsInformation", "needsVerification", "manualReview", "denied", "locked", "canceled"
    ] = FieldInfo(alias="applicationStatus")
    """Represents the possible statuses of an application."""

    application_completion_link: Optional[ApplicationCompletionLink] = FieldInfo(
        alias="applicationCompletionLink", default=None
    )
    """The link to the application completion page"""

    application_external_verification_link: Optional[ApplicationExternalVerificationLink] = FieldInfo(
        alias="applicationExternalVerificationLink", default=None
    )
    """The link to the external verification page for the application"""

    application_reason: Optional[str] = FieldInfo(alias="applicationReason", default=None)
    """The reason behind the current application status"""
