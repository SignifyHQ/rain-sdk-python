# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types.cards import PinRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rain) -> None:
        pin = client.cards.pin.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        )
        assert_matches_type(PinRetrieveResponse, pin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rain) -> None:
        response = client.cards.pin.with_raw_response.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pin = response.parse()
        assert_matches_type(PinRetrieveResponse, pin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rain) -> None:
        with client.cards.pin.with_streaming_response.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pin = response.parse()
            assert_matches_type(PinRetrieveResponse, pin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.pin.with_raw_response.retrieve(
                card_id="",
                session_id="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Rain) -> None:
        pin = client.cards.pin.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        )
        assert pin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Rain) -> None:
        response = client.cards.pin.with_raw_response.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pin = response.parse()
        assert pin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Rain) -> None:
        with client.cards.pin.with_streaming_response.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pin = response.parse()
            assert pin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.pin.with_raw_response.update(
                card_id="",
                encrypted_pin={
                    "data": "data",
                    "iv": "iv",
                },
                session_id="x",
            )


class TestAsyncPin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRain) -> None:
        pin = await async_client.cards.pin.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        )
        assert_matches_type(PinRetrieveResponse, pin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRain) -> None:
        response = await async_client.cards.pin.with_raw_response.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pin = await response.parse()
        assert_matches_type(PinRetrieveResponse, pin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRain) -> None:
        async with async_client.cards.pin.with_streaming_response.retrieve(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pin = await response.parse()
            assert_matches_type(PinRetrieveResponse, pin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.pin.with_raw_response.retrieve(
                card_id="",
                session_id="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRain) -> None:
        pin = await async_client.cards.pin.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        )
        assert pin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRain) -> None:
        response = await async_client.cards.pin.with_raw_response.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pin = await response.parse()
        assert pin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRain) -> None:
        async with async_client.cards.pin.with_streaming_response.update(
            card_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            encrypted_pin={
                "data": "data",
                "iv": "iv",
            },
            session_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pin = await response.parse()
            assert pin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.pin.with_raw_response.update(
                card_id="",
                encrypted_pin={
                    "data": "data",
                    "iv": "iv",
                },
                session_id="x",
            )
