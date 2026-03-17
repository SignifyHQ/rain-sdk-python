# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, FileTypes, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
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
from ...types.disputes import evidence_upload_params

__all__ = ["EvidenceResource", "AsyncEvidenceResource"]


class EvidenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvidenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvidenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvidenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return EvidenceResourceWithStreamingResponse(self)

    def list(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve the file evidence associated with a dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/disputes/{dispute_id}/evidence",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        dispute_id: str,
        *,
        evidence: FileTypes,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upload a file that will serve as evidence for a dispute.

        Args:
          evidence: The evidence to upload

          name: The name of the evidence

          type: The type of evidence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "evidence": evidence,
                "name": name,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["evidence"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            f"/disputes/{dispute_id}/evidence",
            body=maybe_transform(body, evidence_upload_params.EvidenceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvidenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvidenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvidenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvidenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncEvidenceResourceWithStreamingResponse(self)

    async def list(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve the file evidence associated with a dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/disputes/{dispute_id}/evidence",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        dispute_id: str,
        *,
        evidence: FileTypes,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upload a file that will serve as evidence for a dispute.

        Args:
          evidence: The evidence to upload

          name: The name of the evidence

          type: The type of evidence

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "evidence": evidence,
                "name": name,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["evidence"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            f"/disputes/{dispute_id}/evidence",
            body=await async_maybe_transform(body, evidence_upload_params.EvidenceUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvidenceResourceWithRawResponse:
    def __init__(self, evidence: EvidenceResource) -> None:
        self._evidence = evidence

        self.list = to_custom_raw_response_wrapper(
            evidence.list,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            evidence.upload,
        )


class AsyncEvidenceResourceWithRawResponse:
    def __init__(self, evidence: AsyncEvidenceResource) -> None:
        self._evidence = evidence

        self.list = async_to_custom_raw_response_wrapper(
            evidence.list,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            evidence.upload,
        )


class EvidenceResourceWithStreamingResponse:
    def __init__(self, evidence: EvidenceResource) -> None:
        self._evidence = evidence

        self.list = to_custom_streamed_response_wrapper(
            evidence.list,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            evidence.upload,
        )


class AsyncEvidenceResourceWithStreamingResponse:
    def __init__(self, evidence: AsyncEvidenceResource) -> None:
        self._evidence = evidence

        self.list = async_to_custom_streamed_response_wrapper(
            evidence.list,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            evidence.upload,
        )
