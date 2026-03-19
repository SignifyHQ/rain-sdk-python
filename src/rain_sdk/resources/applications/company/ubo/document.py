# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ....._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.applications.company.ubo import document_upload_params

__all__ = ["DocumentResource", "AsyncDocumentResource"]


class DocumentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return DocumentResourceWithStreamingResponse(self)

    def upload(
        self,
        ubo_id: str,
        *,
        company_id: str,
        document: FileTypes,
        country: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Uploads a document for a company's Ultimate Beneficial Owner (UBO) to support
        the company's corporate application. This endpoint allows for the submission of
        various legal and identification documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          side: The side of the document being uploaded

          type: The type of the document being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        if not ubo_id:
            raise ValueError(f"Expected a non-empty value for `ubo_id` but received {ubo_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "side": side,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            path_template(
                "/applications/company/{company_id}/ubo/{ubo_id}/document", company_id=company_id, ubo_id=ubo_id
            ),
            body=maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDocumentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncDocumentResourceWithStreamingResponse(self)

    async def upload(
        self,
        ubo_id: str,
        *,
        company_id: str,
        document: FileTypes,
        country: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
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
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Uploads a document for a company's Ultimate Beneficial Owner (UBO) to support
        the company's corporate application. This endpoint allows for the submission of
        various legal and identification documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          side: The side of the document being uploaded

          type: The type of the document being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        if not ubo_id:
            raise ValueError(f"Expected a non-empty value for `ubo_id` but received {ubo_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "side": side,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            path_template(
                "/applications/company/{company_id}/ubo/{ubo_id}/document", company_id=company_id, ubo_id=ubo_id
            ),
            body=await async_maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DocumentResourceWithRawResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.upload = to_raw_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithRawResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.upload = async_to_raw_response_wrapper(
            document.upload,
        )


class DocumentResourceWithStreamingResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.upload = to_streamed_response_wrapper(
            document.upload,
        )


class AsyncDocumentResourceWithStreamingResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.upload = async_to_streamed_response_wrapper(
            document.upload,
        )
