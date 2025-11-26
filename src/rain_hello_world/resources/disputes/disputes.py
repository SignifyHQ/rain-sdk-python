# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import dispute_list_params, dispute_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .evidence import (
    EvidenceResource,
    AsyncEvidenceResource,
    EvidenceResourceWithRawResponse,
    AsyncEvidenceResourceWithRawResponse,
    EvidenceResourceWithStreamingResponse,
    AsyncEvidenceResourceWithStreamingResponse,
)
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
from ...types.dispute_list_response import DisputeListResponse

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
    @cached_property
    def evidence(self) -> EvidenceResource:
        return EvidenceResource(self._client)

    @cached_property
    def with_raw_response(self) -> DisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return DisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return DisputesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingDispute:
        """
        Retrieve details of a specific dispute using its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        return self._get(
            f"/disputes/{dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingDispute,
        )

    def update(
        self,
        dispute_id: str,
        *,
        status: Literal["canceled"] | Omit = omit,
        text_evidence: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update the status or evidence of a dispute, typically to mark it as canceled or
        add new evidence.

        Args:
          status: The new status of the dispute. Can only be set to 'canceled'.

          text_evidence: The textual evidence to add to the dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/disputes/{dispute_id}",
            body=maybe_transform(
                {
                    "status": status,
                    "text_evidence": text_evidence,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        transaction_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeListResponse:
        """
        Retrieve all disputes, optionally filtered by company, user, or transaction ID.

        Args:
          company_id: For corporate cards, the identifier of the company to get disputes for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          transaction_id: The ID of the transaction to get disputes for

          user_id: The ID of the user to get disputes for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/disputes",
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
                        "transaction_id": transaction_id,
                        "user_id": user_id,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            cast_to=DisputeListResponse,
        )


class AsyncDisputesResource(AsyncAPIResource):
    @cached_property
    def evidence(self) -> AsyncEvidenceResource:
        return AsyncEvidenceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/rain-hello-world-python#with_streaming_response
        """
        return AsyncDisputesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingDispute:
        """
        Retrieve details of a specific dispute using its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        return await self._get(
            f"/disputes/{dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingDispute,
        )

    async def update(
        self,
        dispute_id: str,
        *,
        status: Literal["canceled"] | Omit = omit,
        text_evidence: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update the status or evidence of a dispute, typically to mark it as canceled or
        add new evidence.

        Args:
          status: The new status of the dispute. Can only be set to 'canceled'.

          text_evidence: The textual evidence to add to the dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/disputes/{dispute_id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "text_evidence": text_evidence,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        company_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        transaction_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeListResponse:
        """
        Retrieve all disputes, optionally filtered by company, user, or transaction ID.

        Args:
          company_id: For corporate cards, the identifier of the company to get disputes for

          cursor: The ID of the resource after which to start fetching

          limit: The number of resources to fetch

          transaction_id: The ID of the transaction to get disputes for

          user_id: The ID of the user to get disputes for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/disputes",
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
                        "transaction_id": transaction_id,
                        "user_id": user_id,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            cast_to=DisputeListResponse,
        )


class DisputesResourceWithRawResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            disputes.update,
        )
        self.list = to_raw_response_wrapper(
            disputes.list,
        )

    @cached_property
    def evidence(self) -> EvidenceResourceWithRawResponse:
        return EvidenceResourceWithRawResponse(self._disputes.evidence)


class AsyncDisputesResourceWithRawResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            disputes.update,
        )
        self.list = async_to_raw_response_wrapper(
            disputes.list,
        )

    @cached_property
    def evidence(self) -> AsyncEvidenceResourceWithRawResponse:
        return AsyncEvidenceResourceWithRawResponse(self._disputes.evidence)


class DisputesResourceWithStreamingResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )

    @cached_property
    def evidence(self) -> EvidenceResourceWithStreamingResponse:
        return EvidenceResourceWithStreamingResponse(self._disputes.evidence)


class AsyncDisputesResourceWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )

    @cached_property
    def evidence(self) -> AsyncEvidenceResourceWithStreamingResponse:
        return AsyncEvidenceResourceWithStreamingResponse(self._disputes.evidence)
