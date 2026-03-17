# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cards import pin_update_params
from ..._base_client import make_request_options
from ...types.cards.pin_retrieve_response import PinRetrieveResponse

__all__ = ["PinResource", "AsyncPinResource"]


class PinResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return PinResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> PinRetrieveResponse:
        """
        Retrieve the encrypted PIN for a specific card

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
            f"/cards/{card_id}/pin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinRetrieveResponse,
        )

    def update(
        self,
        card_id: str,
        *,
        encrypted_pin: pin_update_params.EncryptedPin,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates the PIN of a specific card by setting the encrypted PIN

        Args:
          encrypted_pin: The encrypted pin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"SessionId": session_id})
        return self._put(
            f"/cards/{card_id}/pin",
            body=maybe_transform({"encrypted_pin": encrypted_pin}, pin_update_params.PinUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPinResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncPinResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> PinRetrieveResponse:
        """
        Retrieve the encrypted PIN for a specific card

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
            f"/cards/{card_id}/pin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PinRetrieveResponse,
        )

    async def update(
        self,
        card_id: str,
        *,
        encrypted_pin: pin_update_params.EncryptedPin,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates the PIN of a specific card by setting the encrypted PIN

        Args:
          encrypted_pin: The encrypted pin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"SessionId": session_id})
        return await self._put(
            f"/cards/{card_id}/pin",
            body=await async_maybe_transform({"encrypted_pin": encrypted_pin}, pin_update_params.PinUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PinResourceWithRawResponse:
    def __init__(self, pin: PinResource) -> None:
        self._pin = pin

        self.retrieve = to_raw_response_wrapper(
            pin.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pin.update,
        )


class AsyncPinResourceWithRawResponse:
    def __init__(self, pin: AsyncPinResource) -> None:
        self._pin = pin

        self.retrieve = async_to_raw_response_wrapper(
            pin.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pin.update,
        )


class PinResourceWithStreamingResponse:
    def __init__(self, pin: PinResource) -> None:
        self._pin = pin

        self.retrieve = to_streamed_response_wrapper(
            pin.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pin.update,
        )


class AsyncPinResourceWithStreamingResponse:
    def __init__(self, pin: AsyncPinResource) -> None:
        self._pin = pin

        self.retrieve = async_to_streamed_response_wrapper(
            pin.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pin.update,
        )
