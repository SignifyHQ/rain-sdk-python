# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from rain_sdk import Rain, AsyncRain
from rain_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvidence:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evidence = client.disputes.evidence.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evidence.is_closed
        assert evidence.json() == {"foo": "bar"}
        assert cast(Any, evidence.is_closed) is True
        assert isinstance(evidence, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        evidence = client.disputes.evidence.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert evidence.is_closed is True
        assert evidence.http_request.headers.get("X-Stainless-Lang") == "python"
        assert evidence.json() == {"foo": "bar"}
        assert isinstance(evidence, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.disputes.evidence.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as evidence:
            assert not evidence.is_closed
            assert evidence.http_request.headers.get("X-Stainless-Lang") == "python"

            assert evidence.json() == {"foo": "bar"}
            assert cast(Any, evidence.is_closed) is True
            assert isinstance(evidence, StreamedBinaryAPIResponse)

        assert cast(Any, evidence.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            client.disputes.evidence.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Rain) -> None:
        evidence = client.disputes.evidence.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        )
        assert evidence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Rain) -> None:
        response = client.disputes.evidence.with_raw_response.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evidence = response.parse()
        assert evidence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Rain) -> None:
        with client.disputes.evidence.with_streaming_response.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evidence = response.parse()
            assert evidence is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            client.disputes.evidence.with_raw_response.upload(
                dispute_id="",
                evidence=b"raw file contents",
                name="name",
                type="type",
            )


class TestAsyncEvidence:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        evidence = await async_client.disputes.evidence.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evidence.is_closed
        assert await evidence.json() == {"foo": "bar"}
        assert cast(Any, evidence.is_closed) is True
        assert isinstance(evidence, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        evidence = await async_client.disputes.evidence.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert evidence.is_closed is True
        assert evidence.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await evidence.json() == {"foo": "bar"}
        assert isinstance(evidence, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/disputes/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/evidence").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.disputes.evidence.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as evidence:
            assert not evidence.is_closed
            assert evidence.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await evidence.json() == {"foo": "bar"}
            assert cast(Any, evidence.is_closed) is True
            assert isinstance(evidence, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, evidence.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            await async_client.disputes.evidence.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncRain) -> None:
        evidence = await async_client.disputes.evidence.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        )
        assert evidence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncRain) -> None:
        response = await async_client.disputes.evidence.with_raw_response.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evidence = await response.parse()
        assert evidence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncRain) -> None:
        async with async_client.disputes.evidence.with_streaming_response.upload(
            dispute_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evidence=b"raw file contents",
            name="name",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evidence = await response.parse()
            assert evidence is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            await async_client.disputes.evidence.with_raw_response.upload(
                dispute_id="",
                evidence=b"raw file contents",
                name="name",
                type="type",
            )
