# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import FileTypes

__all__ = ["UboUploadDocumentParams"]


class UboUploadDocumentParams(TypedDict, total=False):
    document: Required[FileTypes]
    """The actual document file to be uploaded.

    The document must be in binary format, and the maximum allowed size is 20 MB.
    """

    email: Required[str]
    """The UBO's email address"""

    country: str
    """The country where the document was issued"""

    side: Literal["front", "back"]
    """The side of the document being uploaded"""

    type: Literal[
        "idCard",
        "passport",
        "drivers",
        "residencePermit",
        "utilityBill",
        "selfie",
        "videoSelfie",
        "profileImage",
        "idDocPhoto",
        "agreement",
        "contract",
        "driversTranslation",
        "investorDoc",
        "vehicleRegistrationCertificate",
        "incomeSource",
        "paymentMethod",
        "bankCard",
        "covidVaccinationForm",
        "other",
    ]
    """The type of the document being uploaded"""
