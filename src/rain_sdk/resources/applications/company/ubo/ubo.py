# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union, Mapping, cast
from datetime import date
from typing_extensions import Literal

import httpx

from .document import (
    DocumentResource,
    AsyncDocumentResource,
    DocumentResourceWithRawResponse,
    AsyncDocumentResourceWithRawResponse,
    DocumentResourceWithStreamingResponse,
    AsyncDocumentResourceWithStreamingResponse,
)
from ....._files import deepcopy_with_paths
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ....._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.applications.company import ubo_update_params, ubo_upload_document_params
from .....types.applications.issuing_company import IssuingCompany
from .....types.applications.physical_address_param import PhysicalAddressParam

__all__ = ["UboResource", "AsyncUboResource"]


class UboResource(SyncAPIResource):
    @cached_property
    def document(self) -> DocumentResource:
        return DocumentResource(self._client)

    @cached_property
    def with_raw_response(self) -> UboResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UboResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UboResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return UboResourceWithStreamingResponse(self)

    def update(
        self,
        ubo_id: str,
        *,
        company_id: str,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Updates the application information for a company's Ultimate Beneficial Owner
        (UBO). This allows modification of the UBO's personal details such as name,
        birth date, national ID, and address.

        Args:
          address: The UBO's address

          birth_date: The UBO's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          email: The UBO's email address

          first_name: The UBO's first name

          last_name: The UBO's last name

          national_id: The UBO's national ID number. For the US, this is a 9-digit SSN

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        if not ubo_id:
            raise ValueError(f"Expected a non-empty value for `ubo_id` but received {ubo_id!r}")
        return self._patch(
            path_template("/applications/company/{company_id}/ubo/{ubo_id}", company_id=company_id, ubo_id=ubo_id),
            body=maybe_transform(
                {
                    "address": address,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "national_id": national_id,
                },
                ubo_update_params.UboUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    @typing_extensions.deprecated("deprecated")
    def upload_document(
        self,
        company_id: str,
        *,
        document: FileTypes,
        email: str,
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
        This deprecated endpoint allows the upload of a document for a UBO to support a
        company's corporate application. It is recommended to use the newer endpoint for
        document uploads.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          email: The UBO's email address

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "document": document,
                "email": email,
                "country": country,
                "side": side,
                "type": type,
            },
            [["document"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            path_template("/applications/company/{company_id}/ubo/document", company_id=company_id),
            body=maybe_transform(body, ubo_upload_document_params.UboUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUboResource(AsyncAPIResource):
    @cached_property
    def document(self) -> AsyncDocumentResource:
        return AsyncDocumentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUboResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUboResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUboResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncUboResourceWithStreamingResponse(self)

    async def update(
        self,
        ubo_id: str,
        *,
        company_id: str,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Updates the application information for a company's Ultimate Beneficial Owner
        (UBO). This allows modification of the UBO's personal details such as name,
        birth date, national ID, and address.

        Args:
          address: The UBO's address

          birth_date: The UBO's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          email: The UBO's email address

          first_name: The UBO's first name

          last_name: The UBO's last name

          national_id: The UBO's national ID number. For the US, this is a 9-digit SSN

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        if not ubo_id:
            raise ValueError(f"Expected a non-empty value for `ubo_id` but received {ubo_id!r}")
        return await self._patch(
            path_template("/applications/company/{company_id}/ubo/{ubo_id}", company_id=company_id, ubo_id=ubo_id),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "national_id": national_id,
                },
                ubo_update_params.UboUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    @typing_extensions.deprecated("deprecated")
    async def upload_document(
        self,
        company_id: str,
        *,
        document: FileTypes,
        email: str,
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
        This deprecated endpoint allows the upload of a document for a UBO to support a
        company's corporate application. It is recommended to use the newer endpoint for
        document uploads.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          email: The UBO's email address

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "document": document,
                "email": email,
                "country": country,
                "side": side,
                "type": type,
            },
            [["document"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            path_template("/applications/company/{company_id}/ubo/document", company_id=company_id),
            body=await async_maybe_transform(body, ubo_upload_document_params.UboUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UboResourceWithRawResponse:
    def __init__(self, ubo: UboResource) -> None:
        self._ubo = ubo

        self.update = to_raw_response_wrapper(
            ubo.update,
        )
        self.upload_document = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                ubo.upload_document,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def document(self) -> DocumentResourceWithRawResponse:
        return DocumentResourceWithRawResponse(self._ubo.document)


class AsyncUboResourceWithRawResponse:
    def __init__(self, ubo: AsyncUboResource) -> None:
        self._ubo = ubo

        self.update = async_to_raw_response_wrapper(
            ubo.update,
        )
        self.upload_document = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                ubo.upload_document,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def document(self) -> AsyncDocumentResourceWithRawResponse:
        return AsyncDocumentResourceWithRawResponse(self._ubo.document)


class UboResourceWithStreamingResponse:
    def __init__(self, ubo: UboResource) -> None:
        self._ubo = ubo

        self.update = to_streamed_response_wrapper(
            ubo.update,
        )
        self.upload_document = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                ubo.upload_document,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def document(self) -> DocumentResourceWithStreamingResponse:
        return DocumentResourceWithStreamingResponse(self._ubo.document)


class AsyncUboResourceWithStreamingResponse:
    def __init__(self, ubo: AsyncUboResource) -> None:
        self._ubo = ubo

        self.update = async_to_streamed_response_wrapper(
            ubo.update,
        )
        self.upload_document = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                ubo.upload_document,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def document(self) -> AsyncDocumentResourceWithStreamingResponse:
        return AsyncDocumentResourceWithStreamingResponse(self._ubo.document)
