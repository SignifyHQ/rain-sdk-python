# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    IssuingCardStatus,
    user_list_params,
    user_create_params,
    user_update_params,
    user_create_card_params,
    user_create_charge_params,
    user_initiate_payment_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.issuing_card import IssuingCard
from ...types.user_list_response import UserListResponse
from ...types.issuing_card_status import IssuingCardStatus
from ...types.issuing_card_limit_param import IssuingCardLimitParam
from ...types.applications.issuing_user import IssuingUser
from ...types.issuing_charge_create_response import IssuingChargeCreateResponse
from ...types.user_initiate_payment_response import UserInitiatePaymentResponse
from ...types.user_retrieve_balances_response import UserRetrieveBalancesResponse
from ...types.user_retrieve_contracts_response import UserRetrieveContractsResponse
from ...types.applications.physical_address_param import PhysicalAddressParam

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def signatures(self) -> SignaturesResource:
        return SignaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        first_name: str,
        last_name: str,
        address: PhysicalAddressParam | Omit = omit,
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
        """
        This endpoint allows the creation of a new authorized user with the necessary
        personal details, including contact and wallet information.

        Args:
          email: The user's email address

          first_name: The user's first name

          last_name: The user's last name

          address: The user's address

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          wallet_address: The user's wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "address": address,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                    "wallet_address": wallet_address,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """This endpoint retrieves a specific user by their unique ID.

        The user details,
        including contact and wallet information, are returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def update(
        self,
        user_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_terms_of_service_accepted: bool | Omit = omit,
        last_name: str | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        This endpoint allows the update of a specific user's information, such as their
        name, email, and contact details.

        Args:
          address: The user's address

          email: The user's email address

          first_name: The user's first name

          is_active: Indicates whether the user is active

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/users/{user_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "email": email,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """This endpoint retrieves all users associated with a specific company.

        The
        response will return a list of users, including their personal and contact
        details.

        Args:
          company_id: For corporate cards, the identifier of the company to get users for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint deletes a user by their unique ID.

        Once deleted, the user will no
        longer have access to the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_card(
        self,
        user_id: str,
        *,
        type: Literal["physical", "virtual"],
        billing: PhysicalAddressParam | Omit = omit,
        configuration: user_create_card_params.Configuration | Omit = omit,
        limit: IssuingCardLimitParam | Omit = omit,
        shipping: user_create_card_params.Shipping | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """This endpoint allows the creation of a card for a specific user.

        The card can
        either be physical or virtual and can include various configuration options such
        as the display name and limit.

        Args:
          billing: The address that will serve as the billing address for the card. Defaults to the
              shipping address or team address if not explicitly provided.

          configuration: Configuration details for the card, including display name, product ID, and
              virtual card art

          limit: The initial credit limit for the card, expressed in cents

          shipping: The address to ship the card, if it is a physical card

          status: The initial status of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/users/{user_id}/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "billing": billing,
                    "configuration": configuration,
                    "limit": limit,
                    "shipping": shipping,
                    "status": status,
                },
                user_create_card_params.UserCreateCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    def create_charge(
        self,
        user_id: str,
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
        """This endpoint allows creating a custom fee charge for a specific user.

        The fee
        can be defined in the request body along with its details.

        Args:
          amount: The amount of the charge, in cents

          description: The description of the charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/users/{user_id}/charges",
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                user_create_charge_params.UserCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingChargeCreateResponse,
        )

    def initiate_payment(
        self,
        user_id: str,
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
    ) -> UserInitiatePaymentResponse:
        """This endpoint allows initiating a payment for a specific user.

        The payment is
        made from the user's wallet address to the specified recipient address.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/users/{user_id}/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                user_initiate_payment_params.UserInitiatePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInitiatePaymentResponse,
        )

    def retrieve_balances(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBalancesResponse:
        """This endpoint retrieves the credit balances for a specific user.

        It provides
        information about the user's credit limit, pending charges, posted charges,
        balance due, and spending power.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/users/{user_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveBalancesResponse,
        )

    def retrieve_contracts(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveContractsResponse:
        """This endpoint retrieves smart contract information for a specific user.

        It
        returns a list of contracts associated with the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/users/{user_id}/contracts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveContractsResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def signatures(self) -> AsyncSignaturesResource:
        return AsyncSignaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        first_name: str,
        last_name: str,
        address: PhysicalAddressParam | Omit = omit,
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
        """
        This endpoint allows the creation of a new authorized user with the necessary
        personal details, including contact and wallet information.

        Args:
          email: The user's email address

          first_name: The user's first name

          last_name: The user's last name

          address: The user's address

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          wallet_address: The user's wallet address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "address": address,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                    "wallet_address": wallet_address,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """This endpoint retrieves a specific user by their unique ID.

        The user details,
        including contact and wallet information, are returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def update(
        self,
        user_id: str,
        *,
        address: PhysicalAddressParam | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        is_active: bool | Omit = omit,
        is_terms_of_service_accepted: bool | Omit = omit,
        last_name: str | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        This endpoint allows the update of a specific user's information, such as their
        name, email, and contact details.

        Args:
          address: The user's address

          email: The user's email address

          first_name: The user's first name

          is_active: Indicates whether the user is active

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          phone_country_code: The user's phone country code

          phone_number: The user's phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "email": email,
                    "first_name": first_name,
                    "is_active": is_active,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """This endpoint retrieves all users associated with a specific company.

        The
        response will return a list of users, including their personal and contact
        details.

        Args:
          company_id: For corporate cards, the identifier of the company to get users for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_id": company_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint deletes a user by their unique ID.

        Once deleted, the user will no
        longer have access to the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_card(
        self,
        user_id: str,
        *,
        type: Literal["physical", "virtual"],
        billing: PhysicalAddressParam | Omit = omit,
        configuration: user_create_card_params.Configuration | Omit = omit,
        limit: IssuingCardLimitParam | Omit = omit,
        shipping: user_create_card_params.Shipping | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """This endpoint allows the creation of a card for a specific user.

        The card can
        either be physical or virtual and can include various configuration options such
        as the display name and limit.

        Args:
          billing: The address that will serve as the billing address for the card. Defaults to the
              shipping address or team address if not explicitly provided.

          configuration: Configuration details for the card, including display name, product ID, and
              virtual card art

          limit: The initial credit limit for the card, expressed in cents

          shipping: The address to ship the card, if it is a physical card

          status: The initial status of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/users/{user_id}/cards",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "billing": billing,
                    "configuration": configuration,
                    "limit": limit,
                    "shipping": shipping,
                    "status": status,
                },
                user_create_card_params.UserCreateCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    async def create_charge(
        self,
        user_id: str,
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
        """This endpoint allows creating a custom fee charge for a specific user.

        The fee
        can be defined in the request body along with its details.

        Args:
          amount: The amount of the charge, in cents

          description: The description of the charge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/users/{user_id}/charges",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                },
                user_create_charge_params.UserCreateChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingChargeCreateResponse,
        )

    async def initiate_payment(
        self,
        user_id: str,
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
    ) -> UserInitiatePaymentResponse:
        """This endpoint allows initiating a payment for a specific user.

        The payment is
        made from the user's wallet address to the specified recipient address.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/users/{user_id}/payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                user_initiate_payment_params.UserInitiatePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserInitiatePaymentResponse,
        )

    async def retrieve_balances(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBalancesResponse:
        """This endpoint retrieves the credit balances for a specific user.

        It provides
        information about the user's credit limit, pending charges, posted charges,
        balance due, and spending power.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/users/{user_id}/balances",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveBalancesResponse,
        )

    async def retrieve_contracts(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveContractsResponse:
        """This endpoint retrieves smart contract information for a specific user.

        It
        returns a list of contracts associated with the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/users/{user_id}/contracts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveContractsResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.create_card = to_raw_response_wrapper(
            users.create_card,
        )
        self.create_charge = to_raw_response_wrapper(
            users.create_charge,
        )
        self.initiate_payment = to_raw_response_wrapper(
            users.initiate_payment,
        )
        self.retrieve_balances = to_raw_response_wrapper(
            users.retrieve_balances,
        )
        self.retrieve_contracts = to_raw_response_wrapper(
            users.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> SignaturesResourceWithRawResponse:
        return SignaturesResourceWithRawResponse(self._users.signatures)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.create_card = async_to_raw_response_wrapper(
            users.create_card,
        )
        self.create_charge = async_to_raw_response_wrapper(
            users.create_charge,
        )
        self.initiate_payment = async_to_raw_response_wrapper(
            users.initiate_payment,
        )
        self.retrieve_balances = async_to_raw_response_wrapper(
            users.retrieve_balances,
        )
        self.retrieve_contracts = async_to_raw_response_wrapper(
            users.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> AsyncSignaturesResourceWithRawResponse:
        return AsyncSignaturesResourceWithRawResponse(self._users.signatures)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.create_card = to_streamed_response_wrapper(
            users.create_card,
        )
        self.create_charge = to_streamed_response_wrapper(
            users.create_charge,
        )
        self.initiate_payment = to_streamed_response_wrapper(
            users.initiate_payment,
        )
        self.retrieve_balances = to_streamed_response_wrapper(
            users.retrieve_balances,
        )
        self.retrieve_contracts = to_streamed_response_wrapper(
            users.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> SignaturesResourceWithStreamingResponse:
        return SignaturesResourceWithStreamingResponse(self._users.signatures)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.create_card = async_to_streamed_response_wrapper(
            users.create_card,
        )
        self.create_charge = async_to_streamed_response_wrapper(
            users.create_charge,
        )
        self.initiate_payment = async_to_streamed_response_wrapper(
            users.initiate_payment,
        )
        self.retrieve_balances = async_to_streamed_response_wrapper(
            users.retrieve_balances,
        )
        self.retrieve_contracts = async_to_streamed_response_wrapper(
            users.retrieve_contracts,
        )

    @cached_property
    def signatures(self) -> AsyncSignaturesResourceWithStreamingResponse:
        return AsyncSignaturesResourceWithStreamingResponse(self._users.signatures)
