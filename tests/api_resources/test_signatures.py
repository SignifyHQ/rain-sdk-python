# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types.companies import IssuingSignature

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSignatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_payment_signature(self, client: Rain) -> None:
        signature = client.signatures.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_payment_signature_with_all_params(self, client: Rain) -> None:
        signature = client.signatures.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            chain_id=0,
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_payment_signature(self, client: Rain) -> None:
        response = client.signatures.with_raw_response.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signature = response.parse()
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_payment_signature(self, client: Rain) -> None:
        with client.signatures.with_streaming_response.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signature = response.parse()
            assert_matches_type(IssuingSignature, signature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_withdrawal_signature(self, client: Rain) -> None:
        signature = client.signatures.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_withdrawal_signature_with_all_params(self, client: Rain) -> None:
        signature = client.signatures.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
            chain_id=0,
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_withdrawal_signature(self, client: Rain) -> None:
        response = client.signatures.with_raw_response.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signature = response.parse()
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_withdrawal_signature(self, client: Rain) -> None:
        with client.signatures.with_streaming_response.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signature = response.parse()
            assert_matches_type(IssuingSignature, signature, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSignatures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_payment_signature(self, async_client: AsyncRain) -> None:
        signature = await async_client.signatures.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_payment_signature_with_all_params(self, async_client: AsyncRain) -> None:
        signature = await async_client.signatures.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            chain_id=0,
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_payment_signature(self, async_client: AsyncRain) -> None:
        response = await async_client.signatures.with_raw_response.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signature = await response.parse()
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_payment_signature(self, async_client: AsyncRain) -> None:
        async with async_client.signatures.with_streaming_response.retrieve_payment_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signature = await response.parse()
            assert_matches_type(IssuingSignature, signature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_withdrawal_signature(self, async_client: AsyncRain) -> None:
        signature = await async_client.signatures.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_withdrawal_signature_with_all_params(self, async_client: AsyncRain) -> None:
        signature = await async_client.signatures.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
            chain_id=0,
        )
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_withdrawal_signature(self, async_client: AsyncRain) -> None:
        response = await async_client.signatures.with_raw_response.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signature = await response.parse()
        assert_matches_type(IssuingSignature, signature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_withdrawal_signature(self, async_client: AsyncRain) -> None:
        async with async_client.signatures.with_streaming_response.retrieve_withdrawal_signature(
            token="token",
            admin_address="adminAddress",
            amount="amount",
            recipient_address="recipientAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signature = await response.parse()
            assert_matches_type(IssuingSignature, signature, path=["response"])

        assert cast(Any, response.is_closed) is True
