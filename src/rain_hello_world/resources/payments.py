# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import payment_initiate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_initiate_response import PaymentInitiateResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    def initiate(
        self,
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
    ) -> PaymentInitiateResponse:
        """This endpoint initiates a payment for an authorized user tenant.

        The request
        includes the amount to be transferred and the wallet address to send the payment
        from.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                payment_initiate_params.PaymentInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentInitiateResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def initiate(
        self,
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
    ) -> PaymentInitiateResponse:
        """This endpoint initiates a payment for an authorized user tenant.

        The request
        includes the amount to be transferred and the wallet address to send the payment
        from.

        Args:
          amount: The amount of the payment, in cents

          wallet_address: The wallet address the payment is being sent from

          chain_id: The chain ID (base-10 number) that the payment transaction is on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "wallet_address": wallet_address,
                    "chain_id": chain_id,
                },
                payment_initiate_params.PaymentInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentInitiateResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.initiate = to_raw_response_wrapper(
            payments.initiate,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.initiate = async_to_raw_response_wrapper(
            payments.initiate,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.initiate = to_streamed_response_wrapper(
            payments.initiate,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.initiate = async_to_streamed_response_wrapper(
            payments.initiate,
        )
