# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pin import (
    PinResource,
    AsyncPinResource,
    PinResourceWithRawResponse,
    AsyncPinResourceWithRawResponse,
    PinResourceWithStreamingResponse,
    AsyncPinResourceWithStreamingResponse,
)
from ...types import IssuingCardStatus, card_list_params, card_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.issuing_card import IssuingCard
from ...types.card_list_response import CardListResponse
from ...types.issuing_card_status import IssuingCardStatus
from ...types.issuing_card_limit_param import IssuingCardLimitParam
from ...types.card_retrieve_secrets_response import CardRetrieveSecretsResponse
from ...types.applications.physical_address_param import PhysicalAddressParam

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def pin(self) -> PinResource:
        return PinResource(self._client)

    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """
        Retrieve detailed information for a specific card by its unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    def update(
        self,
        card_id: str,
        *,
        billing: PhysicalAddressParam | Omit = omit,
        configuration: card_update_params.Configuration | Omit = omit,
        limit: IssuingCardLimitParam | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """
        Update details for an existing card, such as status, limit, billing address, and
        configuration.

        Args:
          billing: The billing address associated with the card.

          configuration: Configuration for the card, such as virtual card art

          limit: The limit associated with the card

          status: The current status of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            f"/cards/{card_id}",
            body=maybe_transform(
                {
                    "billing": billing,
                    "configuration": configuration,
                    "limit": limit,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """Retrieves all cards associated with a user or company.

        You can filter by user or
        company ID and card status.

        Args:
          company_id: For corporate cards, the identifier of the company to get cards for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          status: Filter cards by status

          user_id: The identifier of the user to get cards for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cards",
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
                        "status": status,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )

    def retrieve_secrets(
        self,
        card_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveSecretsResponse:
        """
        Retrieve the encrypted data for a specific card, including the encrypted PAN and
        CVC

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"SessionId": session_id, **(extra_headers or {})}
        return self._get(
            f"/cards/{card_id}/secrets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardRetrieveSecretsResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def pin(self) -> AsyncPinResource:
        return AsyncPinResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        card_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """
        Retrieve detailed information for a specific card by its unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/cards/{card_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    async def update(
        self,
        card_id: str,
        *,
        billing: PhysicalAddressParam | Omit = omit,
        configuration: card_update_params.Configuration | Omit = omit,
        limit: IssuingCardLimitParam | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingCard:
        """
        Update details for an existing card, such as status, limit, billing address, and
        configuration.

        Args:
          billing: The billing address associated with the card.

          configuration: Configuration for the card, such as virtual card art

          limit: The limit associated with the card

          status: The current status of the card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            f"/cards/{card_id}",
            body=await async_maybe_transform(
                {
                    "billing": billing,
                    "configuration": configuration,
                    "limit": limit,
                    "status": status,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingCard,
        )

    async def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: IssuingCardStatus | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """Retrieves all cards associated with a user or company.

        You can filter by user or
        company ID and card status.

        Args:
          company_id: For corporate cards, the identifier of the company to get cards for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          status: Filter cards by status

          user_id: The identifier of the user to get cards for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cards",
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
                        "status": status,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )

    async def retrieve_secrets(
        self,
        card_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveSecretsResponse:
        """
        Retrieve the encrypted data for a specific card, including the encrypted PAN and
        CVC

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"SessionId": session_id, **(extra_headers or {})}
        return await self._get(
            f"/cards/{card_id}/secrets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardRetrieveSecretsResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )
        self.retrieve_secrets = to_raw_response_wrapper(
            cards.retrieve_secrets,
        )

    @cached_property
    def pin(self) -> PinResourceWithRawResponse:
        return PinResourceWithRawResponse(self._cards.pin)


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )
        self.retrieve_secrets = async_to_raw_response_wrapper(
            cards.retrieve_secrets,
        )

    @cached_property
    def pin(self) -> AsyncPinResourceWithRawResponse:
        return AsyncPinResourceWithRawResponse(self._cards.pin)


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )
        self.retrieve_secrets = to_streamed_response_wrapper(
            cards.retrieve_secrets,
        )

    @cached_property
    def pin(self) -> PinResourceWithStreamingResponse:
        return PinResourceWithStreamingResponse(self._cards.pin)


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
        self.retrieve_secrets = async_to_streamed_response_wrapper(
            cards.retrieve_secrets,
        )

    @cached_property
    def pin(self) -> AsyncPinResourceWithStreamingResponse:
        return AsyncPinResourceWithStreamingResponse(self._cards.pin)
