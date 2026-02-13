# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import PaymentInitiateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate(self, client: Rain) -> None:
        payment = client.payments.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params(self, client: Rain) -> None:
        payment = client.payments.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: Rain) -> None:
        response = client.payments.with_raw_response.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: Rain) -> None:
        with client.payments.with_streaming_response.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncRain) -> None:
        payment = await async_client.payments.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params(self, async_client: AsyncRain) -> None:
        payment = await async_client.payments.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncRain) -> None:
        response = await async_client.payments.with_raw_response.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncRain) -> None:
        async with async_client.payments.with_streaming_response.initiate(
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentInitiateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
