# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Mapping, Iterable, cast
from typing_extensions import Literal

import httpx

from .ubo.ubo import (
    UboResource,
    AsyncUboResource,
    UboResourceWithRawResponse,
    AsyncUboResourceWithRawResponse,
    UboResourceWithStreamingResponse,
    AsyncUboResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.applications import (
    company_create_params,
    company_update_params,
    company_reapply_params,
    company_upload_document_params,
)
from ....types.applications.issuing_company import IssuingCompany
from ....types.applications.physical_address_param import PhysicalAddressParam
from ....types.applications.company_retrieve_response import CompanyRetrieveResponse
from ....types.applications.issuing_application_person_param import IssuingApplicationPersonParam

__all__ = ["CompanyResource", "AsyncCompanyResource"]


class CompanyResource(SyncAPIResource):
    @cached_property
    def ubo(self) -> UboResource:
        return UboResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return CompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return CompanyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: PhysicalAddressParam,
        entity: company_create_params.Entity,
        initial_user: company_create_params.InitialUser,
        name: str,
        representatives: Iterable[IssuingApplicationPersonParam],
        ultimate_beneficial_owners: Iterable[IssuingApplicationPersonParam],
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        source_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """Submits an application to create a corporate account.

        The application requires
        details about the company, its legal entity, representatives, and beneficial
        owners. The initial user must provide a wallet address.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          initial_user: The initial user of the company. This user must have a wallet address, and their
              wallet address will be associated as an owner on the company's Rain smart
              contract.

          name: The name of the company requesting to create an account

          representatives: The company's representatives

          ultimate_beneficial_owners: The company's ultimate beneficial owners (UBOs)

          chain_id: The chain ID of the external collateral contract, if used. Not required when
              using Rain's collateral contracts.

          contract_address: The address of the external collateral contract, if used. Not required when
              using Rain's collateral contracts.

          source_key: A unique identifier for the origin of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/applications/company",
            body=maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "initial_user": initial_user,
                    "name": name,
                    "representatives": representatives,
                    "ultimate_beneficial_owners": ultimate_beneficial_owners,
                    "chain_id": chain_id,
                    "contract_address": contract_address,
                    "source_key": source_key,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    def retrieve(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        Retrieves the current status and details of a company's corporate application,
        including the company's ultimate beneficial owners and application progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/applications/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def update(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        entity: company_update_params.Entity | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """Updates the information for an existing corporate account application.

        The
        company's details, including name, address, and legal entity information, can be
        modified through this endpoint.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          name: The name of the company for the corporate application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._patch(
            f"/applications/company/{company_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "name": name,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    @typing_extensions.deprecated("deprecated")
    def reapply(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam,
        entity: company_reapply_params.Entity,
        initial_user: company_reapply_params.InitialUser,
        name: str,
        representatives: Iterable[IssuingApplicationPersonParam],
        ultimate_beneficial_owners: Iterable[IssuingApplicationPersonParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Allows a company to reapply or respond to a request for information after
        submitting their corporate application. This endpoint is typically used when
        additional information or corrections are needed.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          initial_user: The initial user of the company who will be the owner on the Rain smart
              contract. This user must provide various personal details.

          name: The name of the company reapplying for the corporate application

          representatives: The company's representatives

          ultimate_beneficial_owners: The company's ultimate beneficial owners (UBOs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._put(
            f"/applications/company/{company_id}/reapply",
            body=maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "initial_user": initial_user,
                    "name": name,
                    "representatives": representatives,
                    "ultimate_beneficial_owners": ultimate_beneficial_owners,
                },
                company_reapply_params.CompanyReapplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    def upload_document(
        self,
        company_id: str,
        *,
        document: FileTypes,
        country: str | Omit = omit,
        name: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
        type: Literal[
            "directorsRegistry",
            "stateRegistry",
            "incumbencyCert",
            "proofOfAddress",
            "trustAgreement",
            "informationStatement",
            "incorporationCert",
            "incorporationArticles",
            "shareholderRegistry",
            "goodStandingCert",
            "powerOfAttorney",
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
        """Uploads a document that supports a company's corporate application.

        This is
        typically used to provide additional documentation, such as proof of address,
        incorporation certificates, or other required legal documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          name: The name of the document being uploaded

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
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "name": name,
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
            f"/applications/company/{company_id}/document",
            body=maybe_transform(body, company_upload_document_params.CompanyUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCompanyResource(AsyncAPIResource):
    @cached_property
    def ubo(self) -> AsyncUboResource:
        return AsyncUboResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return AsyncCompanyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: PhysicalAddressParam,
        entity: company_create_params.Entity,
        initial_user: company_create_params.InitialUser,
        name: str,
        representatives: Iterable[IssuingApplicationPersonParam],
        ultimate_beneficial_owners: Iterable[IssuingApplicationPersonParam],
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        source_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """Submits an application to create a corporate account.

        The application requires
        details about the company, its legal entity, representatives, and beneficial
        owners. The initial user must provide a wallet address.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          initial_user: The initial user of the company. This user must have a wallet address, and their
              wallet address will be associated as an owner on the company's Rain smart
              contract.

          name: The name of the company requesting to create an account

          representatives: The company's representatives

          ultimate_beneficial_owners: The company's ultimate beneficial owners (UBOs)

          chain_id: The chain ID of the external collateral contract, if used. Not required when
              using Rain's collateral contracts.

          contract_address: The address of the external collateral contract, if used. Not required when
              using Rain's collateral contracts.

          source_key: A unique identifier for the origin of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/applications/company",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "initial_user": initial_user,
                    "name": name,
                    "representatives": representatives,
                    "ultimate_beneficial_owners": ultimate_beneficial_owners,
                    "chain_id": chain_id,
                    "contract_address": contract_address,
                    "source_key": source_key,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    async def retrieve(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        Retrieves the current status and details of a company's corporate application,
        including the company's ultimate beneficial owners and application progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/applications/company/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveResponse,
        )

    async def update(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        entity: company_update_params.Entity | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """Updates the information for an existing corporate account application.

        The
        company's details, including name, address, and legal entity information, can be
        modified through this endpoint.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          name: The name of the company for the corporate application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._patch(
            f"/applications/company/{company_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "name": name,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    @typing_extensions.deprecated("deprecated")
    async def reapply(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam,
        entity: company_reapply_params.Entity,
        initial_user: company_reapply_params.InitialUser,
        name: str,
        representatives: Iterable[IssuingApplicationPersonParam],
        ultimate_beneficial_owners: Iterable[IssuingApplicationPersonParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Allows a company to reapply or respond to a request for information after
        submitting their corporate application. This endpoint is typically used when
        additional information or corrections are needed.

        Args:
          address: The company's physical address

          entity: The company's legal entity details.

          initial_user: The initial user of the company who will be the owner on the Rain smart
              contract. This user must provide various personal details.

          name: The name of the company reapplying for the corporate application

          representatives: The company's representatives

          ultimate_beneficial_owners: The company's ultimate beneficial owners (UBOs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._put(
            f"/applications/company/{company_id}/reapply",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "entity": entity,
                    "initial_user": initial_user,
                    "name": name,
                    "representatives": representatives,
                    "ultimate_beneficial_owners": ultimate_beneficial_owners,
                },
                company_reapply_params.CompanyReapplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    async def upload_document(
        self,
        company_id: str,
        *,
        document: FileTypes,
        country: str | Omit = omit,
        name: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
        type: Literal[
            "directorsRegistry",
            "stateRegistry",
            "incumbencyCert",
            "proofOfAddress",
            "trustAgreement",
            "informationStatement",
            "incorporationCert",
            "incorporationArticles",
            "shareholderRegistry",
            "goodStandingCert",
            "powerOfAttorney",
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
        """Uploads a document that supports a company's corporate application.

        This is
        typically used to provide additional documentation, such as proof of address,
        incorporation certificates, or other required legal documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          name: The name of the document being uploaded

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
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "name": name,
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
            f"/applications/company/{company_id}/document",
            body=await async_maybe_transform(body, company_upload_document_params.CompanyUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CompanyResourceWithRawResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.create = to_raw_response_wrapper(
            company.create,
        )
        self.retrieve = to_raw_response_wrapper(
            company.retrieve,
        )
        self.update = to_raw_response_wrapper(
            company.update,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                company.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = to_raw_response_wrapper(
            company.upload_document,
        )

    @cached_property
    def ubo(self) -> UboResourceWithRawResponse:
        return UboResourceWithRawResponse(self._company.ubo)


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.create = async_to_raw_response_wrapper(
            company.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            company.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            company.update,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                company.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = async_to_raw_response_wrapper(
            company.upload_document,
        )

    @cached_property
    def ubo(self) -> AsyncUboResourceWithRawResponse:
        return AsyncUboResourceWithRawResponse(self._company.ubo)


class CompanyResourceWithStreamingResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.create = to_streamed_response_wrapper(
            company.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            company.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            company.update,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                company.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = to_streamed_response_wrapper(
            company.upload_document,
        )

    @cached_property
    def ubo(self) -> UboResourceWithStreamingResponse:
        return UboResourceWithStreamingResponse(self._company.ubo)


class AsyncCompanyResourceWithStreamingResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.create = async_to_streamed_response_wrapper(
            company.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            company.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            company.update,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                company.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = async_to_streamed_response_wrapper(
            company.upload_document,
        )

    @cached_property
    def ubo(self) -> AsyncUboResourceWithStreamingResponse:
        return AsyncUboResourceWithStreamingResponse(self._company.ubo)
