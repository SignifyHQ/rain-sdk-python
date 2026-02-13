# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import transaction_list_params, transaction_update_params, transaction_create_dispute_params
from .receipt import (
    ReceiptResource,
    AsyncReceiptResource,
    ReceiptResourceWithRawResponse,
    AsyncReceiptResourceWithRawResponse,
    ReceiptResourceWithStreamingResponse,
    AsyncReceiptResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.issuing_dispute import IssuingDispute
from ...types.issuing_transaction import IssuingTransaction
from ...types.transaction_list_response import TransactionListResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def receipt(self) -> ReceiptResource:
        return ReceiptResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingTransaction:
        """This endpoint retrieves a transaction by its unique ID.

        The transaction
        information returned includes details such as the transaction type, amount, and
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return cast(
            IssuingTransaction,
            self._get(
                f"/transactions/{transaction_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, IssuingTransaction
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        transaction_id: str,
        *,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint allows updating a specific transaction by its ID.

        You can modify
        the transaction's memo or other editable fields.

        Args:
          memo: A memo or note to attach to the transaction, providing additional information or
              context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/transactions/{transaction_id}",
            body=maybe_transform({"memo": memo}, transaction_update_params.TransactionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        authorized_after: Union[str, datetime] | Omit = omit,
        authorized_before: Union[str, datetime] | Omit = omit,
        card_id: str | Omit = omit,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        transaction_hash: str | Omit = omit,
        type: List[Literal["spend", "collateral", "payment", "fee"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListResponse:
        """
        This endpoint retrieves all transactions associated with corporate cards, users,
        or specific cards.

        Args:
          authorized_after: Filter transactions authorized after a specific date

          authorized_before: Filter transactions authorized before a specific date

          card_id: The ID of the card to get transactions for

          company_id: For corporate cards, the identifier of the company to get transactions for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          posted_after: Filter transactions posted after a specific date

          posted_before: Filter transactions posted before a specific date

          transaction_hash: The hash of the transaction to retrieve

          type: The type of transactions to retrieve

          user_id: The ID of the user to get transactions for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "authorized_after": authorized_after,
                        "authorized_before": authorized_before,
                        "card_id": card_id,
                        "company_id": company_id,
                        "cursor": cursor,
                        "limit": limit,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "transaction_hash": transaction_hash,
                        "type": type,
                        "user_id": user_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )

    def create_dispute(
        self,
        transaction_id: str,
        *,
        text_evidence: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingDispute:
        """This endpoint allows the creation of a dispute for a specific transaction.

        The
        dispute can include textual evidence to support the claim.

        Args:
          text_evidence: The textual evidence that supports the dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return self._post(
            f"/transactions/{transaction_id}/disputes",
            body=maybe_transform(
                {"text_evidence": text_evidence}, transaction_create_dispute_params.TransactionCreateDisputeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingDispute,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def receipt(self) -> AsyncReceiptResource:
        return AsyncReceiptResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingTransaction:
        """This endpoint retrieves a transaction by its unique ID.

        The transaction
        information returned includes details such as the transaction type, amount, and
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return cast(
            IssuingTransaction,
            await self._get(
                f"/transactions/{transaction_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, IssuingTransaction
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        transaction_id: str,
        *,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint allows updating a specific transaction by its ID.

        You can modify
        the transaction's memo or other editable fields.

        Args:
          memo: A memo or note to attach to the transaction, providing additional information or
              context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/transactions/{transaction_id}",
            body=await async_maybe_transform({"memo": memo}, transaction_update_params.TransactionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        authorized_after: Union[str, datetime] | Omit = omit,
        authorized_before: Union[str, datetime] | Omit = omit,
        card_id: str | Omit = omit,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        transaction_hash: str | Omit = omit,
        type: List[Literal["spend", "collateral", "payment", "fee"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListResponse:
        """
        This endpoint retrieves all transactions associated with corporate cards, users,
        or specific cards.

        Args:
          authorized_after: Filter transactions authorized after a specific date

          authorized_before: Filter transactions authorized before a specific date

          card_id: The ID of the card to get transactions for

          company_id: For corporate cards, the identifier of the company to get transactions for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          posted_after: Filter transactions posted after a specific date

          posted_before: Filter transactions posted before a specific date

          transaction_hash: The hash of the transaction to retrieve

          type: The type of transactions to retrieve

          user_id: The ID of the user to get transactions for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "authorized_after": authorized_after,
                        "authorized_before": authorized_before,
                        "card_id": card_id,
                        "company_id": company_id,
                        "cursor": cursor,
                        "limit": limit,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "transaction_hash": transaction_hash,
                        "type": type,
                        "user_id": user_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )

    async def create_dispute(
        self,
        transaction_id: str,
        *,
        text_evidence: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingDispute:
        """This endpoint allows the creation of a dispute for a specific transaction.

        The
        dispute can include textual evidence to support the claim.

        Args:
          text_evidence: The textual evidence that supports the dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        return await self._post(
            f"/transactions/{transaction_id}/disputes",
            body=await async_maybe_transform(
                {"text_evidence": text_evidence}, transaction_create_dispute_params.TransactionCreateDisputeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingDispute,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            transactions.update,
        )
        self.list = to_raw_response_wrapper(
            transactions.list,
        )
        self.create_dispute = to_raw_response_wrapper(
            transactions.create_dispute,
        )

    @cached_property
    def receipt(self) -> ReceiptResourceWithRawResponse:
        return ReceiptResourceWithRawResponse(self._transactions.receipt)


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            transactions.update,
        )
        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )
        self.create_dispute = async_to_raw_response_wrapper(
            transactions.create_dispute,
        )

    @cached_property
    def receipt(self) -> AsyncReceiptResourceWithRawResponse:
        return AsyncReceiptResourceWithRawResponse(self._transactions.receipt)


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.create_dispute = to_streamed_response_wrapper(
            transactions.create_dispute,
        )

    @cached_property
    def receipt(self) -> ReceiptResourceWithStreamingResponse:
        return ReceiptResourceWithStreamingResponse(self._transactions.receipt)


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.create_dispute = async_to_streamed_response_wrapper(
            transactions.create_dispute,
        )

    @cached_property
    def receipt(self) -> AsyncReceiptResourceWithStreamingResponse:
        return AsyncReceiptResourceWithStreamingResponse(self._transactions.receipt)
