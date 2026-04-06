# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.companies import (
    signature_retrieve_payment_signature_params,
    signature_retrieve_withdrawal_signature_params,
)
from ...types.companies.issuing_signature import IssuingSignature

__all__ = ["SignaturesResource", "AsyncSignaturesResource"]


class SignaturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SignaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SignaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SignaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return SignaturesResourceWithStreamingResponse(self)

    def retrieve_payment_signature(
        self,
        company_id: str,
        *,
        token: str,
        admin_address: str,
        amount: str,
        chain_id: int | Omit = omit,
        is_amount_native: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingSignature:
        """
        Retrieve the payment signature for a company, which is required for completing
        payment transactions.

        Args:
          token: The address of the token that the payment should be made in (as a hex string for
              EVM or base58 string for Solana)

          admin_address: The address of the admin making the payment, as a hex string for EVM or base58
              string for Solana

          amount: The amount of tokens that are being paid

          chain_id: The chain ID (base-10 number) that the smart contract is deployed on

          is_amount_native: Indicates whether the amount is in the asset's native units. If false, the
              amount is expressed in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return cast(
            IssuingSignature,
            self._get(
                path_template("/companies/{company_id}/signatures/payments", company_id=company_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "token": token,
                            "admin_address": admin_address,
                            "amount": amount,
                            "chain_id": chain_id,
                            "is_amount_native": is_amount_native,
                        },
                        signature_retrieve_payment_signature_params.SignatureRetrievePaymentSignatureParams,
                    ),
                ),
                cast_to=cast(Any, IssuingSignature),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_withdrawal_signature(
        self,
        company_id: str,
        *,
        token: str,
        admin_address: str,
        amount: str,
        recipient_address: str,
        chain_id: int | Omit = omit,
        is_amount_native: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingSignature:
        """
        Retrieve the withdrawal signature for a company, which is required for
        processing withdrawal requests.

        Args:
          token: The address of the token that the withdrawal should be made in, as a hex string
              for EVM or base58 string for Solana

          admin_address: The address of the admin making the payment, as a hex string for EVM or base58
              string for Solana

          amount: The amount of tokens being withdrawn

          recipient_address: The address the withdrawal should be sent to, as a hex string for EVM or base58
              string for Solana

          chain_id: The chain ID (base-10 number) that the smart contract is deployed on

          is_amount_native: Indicates whether the amount is in the asset's native units. If false, the
              amount is expressed in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return cast(
            IssuingSignature,
            self._get(
                path_template("/companies/{company_id}/signatures/withdrawals", company_id=company_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "token": token,
                            "admin_address": admin_address,
                            "amount": amount,
                            "recipient_address": recipient_address,
                            "chain_id": chain_id,
                            "is_amount_native": is_amount_native,
                        },
                        signature_retrieve_withdrawal_signature_params.SignatureRetrieveWithdrawalSignatureParams,
                    ),
                ),
                cast_to=cast(Any, IssuingSignature),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSignaturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSignaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSignaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSignaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncSignaturesResourceWithStreamingResponse(self)

    async def retrieve_payment_signature(
        self,
        company_id: str,
        *,
        token: str,
        admin_address: str,
        amount: str,
        chain_id: int | Omit = omit,
        is_amount_native: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingSignature:
        """
        Retrieve the payment signature for a company, which is required for completing
        payment transactions.

        Args:
          token: The address of the token that the payment should be made in (as a hex string for
              EVM or base58 string for Solana)

          admin_address: The address of the admin making the payment, as a hex string for EVM or base58
              string for Solana

          amount: The amount of tokens that are being paid

          chain_id: The chain ID (base-10 number) that the smart contract is deployed on

          is_amount_native: Indicates whether the amount is in the asset's native units. If false, the
              amount is expressed in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return cast(
            IssuingSignature,
            await self._get(
                path_template("/companies/{company_id}/signatures/payments", company_id=company_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "token": token,
                            "admin_address": admin_address,
                            "amount": amount,
                            "chain_id": chain_id,
                            "is_amount_native": is_amount_native,
                        },
                        signature_retrieve_payment_signature_params.SignatureRetrievePaymentSignatureParams,
                    ),
                ),
                cast_to=cast(Any, IssuingSignature),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_withdrawal_signature(
        self,
        company_id: str,
        *,
        token: str,
        admin_address: str,
        amount: str,
        recipient_address: str,
        chain_id: int | Omit = omit,
        is_amount_native: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingSignature:
        """
        Retrieve the withdrawal signature for a company, which is required for
        processing withdrawal requests.

        Args:
          token: The address of the token that the withdrawal should be made in, as a hex string
              for EVM or base58 string for Solana

          admin_address: The address of the admin making the payment, as a hex string for EVM or base58
              string for Solana

          amount: The amount of tokens being withdrawn

          recipient_address: The address the withdrawal should be sent to, as a hex string for EVM or base58
              string for Solana

          chain_id: The chain ID (base-10 number) that the smart contract is deployed on

          is_amount_native: Indicates whether the amount is in the asset's native units. If false, the
              amount is expressed in cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return cast(
            IssuingSignature,
            await self._get(
                path_template("/companies/{company_id}/signatures/withdrawals", company_id=company_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "token": token,
                            "admin_address": admin_address,
                            "amount": amount,
                            "recipient_address": recipient_address,
                            "chain_id": chain_id,
                            "is_amount_native": is_amount_native,
                        },
                        signature_retrieve_withdrawal_signature_params.SignatureRetrieveWithdrawalSignatureParams,
                    ),
                ),
                cast_to=cast(Any, IssuingSignature),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SignaturesResourceWithRawResponse:
    def __init__(self, signatures: SignaturesResource) -> None:
        self._signatures = signatures

        self.retrieve_payment_signature = to_raw_response_wrapper(
            signatures.retrieve_payment_signature,
        )
        self.retrieve_withdrawal_signature = to_raw_response_wrapper(
            signatures.retrieve_withdrawal_signature,
        )


class AsyncSignaturesResourceWithRawResponse:
    def __init__(self, signatures: AsyncSignaturesResource) -> None:
        self._signatures = signatures

        self.retrieve_payment_signature = async_to_raw_response_wrapper(
            signatures.retrieve_payment_signature,
        )
        self.retrieve_withdrawal_signature = async_to_raw_response_wrapper(
            signatures.retrieve_withdrawal_signature,
        )


class SignaturesResourceWithStreamingResponse:
    def __init__(self, signatures: SignaturesResource) -> None:
        self._signatures = signatures

        self.retrieve_payment_signature = to_streamed_response_wrapper(
            signatures.retrieve_payment_signature,
        )
        self.retrieve_withdrawal_signature = to_streamed_response_wrapper(
            signatures.retrieve_withdrawal_signature,
        )


class AsyncSignaturesResourceWithStreamingResponse:
    def __init__(self, signatures: AsyncSignaturesResource) -> None:
        self._signatures = signatures

        self.retrieve_payment_signature = async_to_streamed_response_wrapper(
            signatures.retrieve_payment_signature,
        )
        self.retrieve_withdrawal_signature = async_to_streamed_response_wrapper(
            signatures.retrieve_withdrawal_signature,
        )
