# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...types import (
    company_list_params,
    company_charge_params,
    company_update_params,
    company_create_user_params,
    company_initiate_payment_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .signatures import (
    SignaturesResource,
    AsyncSignaturesResource,
    SignaturesResourceWithRawResponse,
    AsyncSignaturesResourceWithRawResponse,
    SignaturesResourceWithStreamingResponse,
    AsyncSignaturesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.company_list_response import CompanyListResponse
from ...types.applications.issuing_user import IssuingUser
from ...types.applications.issuing_company import IssuingCompany
from ...types.issuing_charge_create_response import IssuingChargeCreateResponse
from ...types.company_initiate_payment_response import CompanyInitiatePaymentResponse
from ...types.company_retrieve_balances_response import CompanyRetrieveBalancesResponse
from ...types.applications.physical_address_param import PhysicalAddressParam
from ...types.company_retrieve_contracts_response import CompanyRetrieveContractsResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def signatures(self) -> SignaturesResource:
        return SignaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

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
    ) -> IssuingCompany:
        """
        Retrieve detailed information about a specific company using its unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/companies/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    def update(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Update the details of an existing company such as its name and address

        Args:
          address: The company's physical address

          name: The company's name on the Rain platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._patch(
            f"/companies/{company_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "name": name,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyListResponse:
        """
        Retrieves a list of all companies registered in the system

        Args:
          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyListResponse,
        )

    def charge(
        self,
        company_id: str,
        *,
        amount: int,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingChargeCreateResponse:
        """
        Initiate a custom fee charge for a company.

        Args:
          amount: The amount of the charge, in cents

          description: The description of the charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._post(
            f"/companies/{company_id}/charges",
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                company_charge_params.CompanyChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingChargeCreateResponse,
        )

    def create_user(
        self,
        company_id: str,
        *,
        email: str,
        first_name: str,
        is_terms_of_service_accepted: bool,
        last_name: str,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Creates a new user within a specific company.

        The user must provide details such
        as their name, birthdate, and contact information.

        Args:
          email: The user's email address

          first_name: The user's first name

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          address: The user's address

          birth_date: The user's birth date

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          wallet_address: The user's wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._post(
            f"/companies/{company_id}/users",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "address": address,
                    "birth_date": birth_date,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                    "wallet_address": wallet_address,
                },
                company_create_user_params.CompanyCreateUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def initiate_payment(
        self,
        company_id: str,
        *,
        amount: int,
        wallet_address: str,
        chain_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyInitiatePaymentResponse:
        """
        Initiate a payment for a specific company by providing the payment amount and
        wallet address.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._post(
            f"/companies/{company_id}/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                company_initiate_payment_params.CompanyInitiatePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyInitiatePaymentResponse,
        )

    def retrieve_balances(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveBalancesResponse:
        """
        Retrieve the current credit balances of a company, including credit limits,
        pending charges, and the amount due.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/companies/{company_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveBalancesResponse,
        )

    def retrieve_contracts(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveContractsResponse:
        """
        Retrieve the smart contract details associated with a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/companies/{company_id}/contracts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveContractsResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def signatures(self) -> AsyncSignaturesResource:
        return AsyncSignaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

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
    ) -> IssuingCompany:
        """
        Retrieve detailed information about a specific company using its unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/companies/{company_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    async def update(
        self,
        company_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCompany:
        """
        Update the details of an existing company such as its name and address

        Args:
          address: The company's physical address

          name: The company's name on the Rain platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._patch(
            f"/companies/{company_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "name": name,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCompany,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyListResponse:
        """
        Retrieves a list of all companies registered in the system

        Args:
          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyListResponse,
        )

    async def charge(
        self,
        company_id: str,
        *,
        amount: int,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingChargeCreateResponse:
        """
        Initiate a custom fee charge for a company.

        Args:
          amount: The amount of the charge, in cents

          description: The description of the charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._post(
            f"/companies/{company_id}/charges",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                company_charge_params.CompanyChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingChargeCreateResponse,
        )

    async def create_user(
        self,
        company_id: str,
        *,
        email: str,
        first_name: str,
        is_terms_of_service_accepted: bool,
        last_name: str,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Creates a new user within a specific company.

        The user must provide details such
        as their name, birthdate, and contact information.

        Args:
          email: The user's email address

          first_name: The user's first name

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          address: The user's address

          birth_date: The user's birth date

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          wallet_address: The user's wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._post(
            f"/companies/{company_id}/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "address": address,
                    "birth_date": birth_date,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                    "wallet_address": wallet_address,
                },
                company_create_user_params.CompanyCreateUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def initiate_payment(
        self,
        company_id: str,
        *,
        amount: int,
        wallet_address: str,
        chain_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyInitiatePaymentResponse:
        """
        Initiate a payment for a specific company by providing the payment amount and
        wallet address.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._post(
            f"/companies/{company_id}/payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                company_initiate_payment_params.CompanyInitiatePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyInitiatePaymentResponse,
        )

    async def retrieve_balances(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveBalancesResponse:
        """
        Retrieve the current credit balances of a company, including credit limits,
        pending charges, and the amount due.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/companies/{company_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveBalancesResponse,
        )

    async def retrieve_contracts(
        self,
        company_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveContractsResponse:
        """
        Retrieve the smart contract details associated with a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/companies/{company_id}/contracts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveContractsResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.charge = to_raw_response_wrapper(
            companies.charge,
        )
        self.create_user = to_raw_response_wrapper(
            companies.create_user,
        )
        self.initiate_payment = to_raw_response_wrapper(
            companies.initiate_payment,
        )
        self.retrieve_balances = to_raw_response_wrapper(
            companies.retrieve_balances,
        )
        self.retrieve_contracts = to_raw_response_wrapper(
            companies.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> SignaturesResourceWithRawResponse:
        return SignaturesResourceWithRawResponse(self._companies.signatures)


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.charge = async_to_raw_response_wrapper(
            companies.charge,
        )
        self.create_user = async_to_raw_response_wrapper(
            companies.create_user,
        )
        self.initiate_payment = async_to_raw_response_wrapper(
            companies.initiate_payment,
        )
        self.retrieve_balances = async_to_raw_response_wrapper(
            companies.retrieve_balances,
        )
        self.retrieve_contracts = async_to_raw_response_wrapper(
            companies.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> AsyncSignaturesResourceWithRawResponse:
        return AsyncSignaturesResourceWithRawResponse(self._companies.signatures)


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.charge = to_streamed_response_wrapper(
            companies.charge,
        )
        self.create_user = to_streamed_response_wrapper(
            companies.create_user,
        )
        self.initiate_payment = to_streamed_response_wrapper(
            companies.initiate_payment,
        )
        self.retrieve_balances = to_streamed_response_wrapper(
            companies.retrieve_balances,
        )
        self.retrieve_contracts = to_streamed_response_wrapper(
            companies.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> SignaturesResourceWithStreamingResponse:
        return SignaturesResourceWithStreamingResponse(self._companies.signatures)


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.charge = async_to_streamed_response_wrapper(
            companies.charge,
        )
        self.create_user = async_to_streamed_response_wrapper(
            companies.create_user,
        )
        self.initiate_payment = async_to_streamed_response_wrapper(
            companies.initiate_payment,
        )
        self.retrieve_balances = async_to_streamed_response_wrapper(
            companies.retrieve_balances,
        )
        self.retrieve_contracts = async_to_streamed_response_wrapper(
            companies.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> AsyncSignaturesResourceWithStreamingResponse:
        return AsyncSignaturesResourceWithStreamingResponse(self._companies.signatures)
