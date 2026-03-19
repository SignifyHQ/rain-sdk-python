# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, FileTypes, not_given
from ..._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.transactions import receipt_upload_params

__all__ = ["ReceiptResource", "AsyncReceiptResource"]


class ReceiptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReceiptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReceiptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReceiptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return ReceiptResourceWithStreamingResponse(self)

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
    ) -> BinaryAPIResponse:
        """This endpoint retrieves the receipt for a specific transaction.

        The receipt is
        returned as a binary file, typically in PDF or similar format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/transactions/{transaction_id}/receipt", transaction_id=transaction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        transaction_id: str,
        *,
        receipt: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint allows you to upload a receipt for a specific transaction.

        The
        receipt is provided as a binary file, typically in PDF format.

        Args:
          receipt: The receipt file to upload, typically in PDF or other binary formats

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"receipt": receipt})
        files = extract_files(cast(Mapping[str, object], body), paths=[["receipt"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            path_template("/transactions/{transaction_id}/receipt", transaction_id=transaction_id),
            body=maybe_transform(body, receipt_upload_params.ReceiptUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReceiptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReceiptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReceiptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReceiptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncReceiptResourceWithStreamingResponse(self)

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
    ) -> AsyncBinaryAPIResponse:
        """This endpoint retrieves the receipt for a specific transaction.

        The receipt is
        returned as a binary file, typically in PDF or similar format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/transactions/{transaction_id}/receipt", transaction_id=transaction_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        transaction_id: str,
        *,
        receipt: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint allows you to upload a receipt for a specific transaction.

        The
        receipt is provided as a binary file, typically in PDF format.

        Args:
          receipt: The receipt file to upload, typically in PDF or other binary formats

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_id:
            raise ValueError(f"Expected a non-empty value for `transaction_id` but received {transaction_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"receipt": receipt})
        files = extract_files(cast(Mapping[str, object], body), paths=[["receipt"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            path_template("/transactions/{transaction_id}/receipt", transaction_id=transaction_id),
            body=await async_maybe_transform(body, receipt_upload_params.ReceiptUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReceiptResourceWithRawResponse:
    def __init__(self, receipt: ReceiptResource) -> None:
        self._receipt = receipt

        self.retrieve = to_custom_raw_response_wrapper(
            receipt.retrieve,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            receipt.upload,
        )


class AsyncReceiptResourceWithRawResponse:
    def __init__(self, receipt: AsyncReceiptResource) -> None:
        self._receipt = receipt

        self.retrieve = async_to_custom_raw_response_wrapper(
            receipt.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            receipt.upload,
        )


class ReceiptResourceWithStreamingResponse:
    def __init__(self, receipt: ReceiptResource) -> None:
        self._receipt = receipt

        self.retrieve = to_custom_streamed_response_wrapper(
            receipt.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            receipt.upload,
        )


class AsyncReceiptResourceWithStreamingResponse:
    def __init__(self, receipt: AsyncReceiptResource) -> None:
        self._receipt = receipt

        self.retrieve = async_to_custom_streamed_response_wrapper(
            receipt.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            receipt.upload,
        )
