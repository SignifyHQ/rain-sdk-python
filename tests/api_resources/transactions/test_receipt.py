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


class TestReceipt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        receipt = client.transactions.receipt.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert receipt.is_closed
        assert receipt.json() == {"foo": "bar"}
        assert cast(Any, receipt.is_closed) is True
        assert isinstance(receipt, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        receipt = client.transactions.receipt.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert receipt.is_closed is True
        assert receipt.http_request.headers.get("X-Stainless-Lang") == "python"
        assert receipt.json() == {"foo": "bar"}
        assert isinstance(receipt, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Rain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.transactions.receipt.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as receipt:
            assert not receipt.is_closed
            assert receipt.http_request.headers.get("X-Stainless-Lang") == "python"

            assert receipt.json() == {"foo": "bar"}
            assert cast(Any, receipt.is_closed) is True
            assert isinstance(receipt, StreamedBinaryAPIResponse)

        assert cast(Any, receipt.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.receipt.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Rain) -> None:
        receipt = client.transactions.receipt.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        )
        assert receipt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Rain) -> None:
        response = client.transactions.receipt.with_raw_response.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receipt = response.parse()
        assert receipt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Rain) -> None:
        with client.transactions.receipt.with_streaming_response.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receipt = response.parse()
            assert receipt is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.receipt.with_raw_response.upload(
                transaction_id="",
                receipt=b"raw file contents",
            )


class TestAsyncReceipt:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        receipt = await async_client.transactions.receipt.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert receipt.is_closed
        assert await receipt.json() == {"foo": "bar"}
        assert cast(Any, receipt.is_closed) is True
        assert isinstance(receipt, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        receipt = await async_client.transactions.receipt.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert receipt.is_closed is True
        assert receipt.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await receipt.json() == {"foo": "bar"}
        assert isinstance(receipt, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncRain, respx_mock: MockRouter) -> None:
        respx_mock.get("/transactions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/receipt").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.transactions.receipt.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as receipt:
            assert not receipt.is_closed
            assert receipt.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await receipt.json() == {"foo": "bar"}
            assert cast(Any, receipt.is_closed) is True
            assert isinstance(receipt, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, receipt.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.receipt.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncRain) -> None:
        receipt = await async_client.transactions.receipt.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        )
        assert receipt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncRain) -> None:
        response = await async_client.transactions.receipt.with_raw_response.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        receipt = await response.parse()
        assert receipt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncRain) -> None:
        async with async_client.transactions.receipt.with_streaming_response.upload(
            transaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            receipt = await response.parse()
            assert receipt is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.receipt.with_raw_response.upload(
                transaction_id="",
                receipt=b"raw file contents",
            )
