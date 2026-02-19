# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import BalanceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rain) -> None:
        balance = client.balances.retrieve()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rain) -> None:
        response = client.balances.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rain) -> None:
        with client.balances.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRain) -> None:
        balance = await async_client.balances.retrieve()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRain) -> None:
        response = await async_client.balances.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRain) -> None:
        async with async_client.balances.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True
