# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import (
    IssuingCard,
    UserListResponse,
    IssuingChargeCreateResponse,
    UserInitiatePaymentResponse,
    UserRetrieveBalancesResponse,
    UserRetrieveContractsResponse,
)
from rain_sdk.types.applications import IssuingUser

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Rain) -> None:
        user = client.users.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Rain) -> None:
        user = client.users.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            phone_country_code="1",
            phone_number="5555555555",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Rain) -> None:
        response = client.users.with_raw_response.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Rain) -> None:
        with client.users.with_streaming_response.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rain) -> None:
        user = client.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rain) -> None:
        response = client.users.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rain) -> None:
        with client.users.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Rain) -> None:
        user = client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Rain) -> None:
        user = client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            email="email",
            first_name="firstName",
            is_active=True,
            is_terms_of_service_accepted=True,
            last_name="lastName",
            phone_country_code="1",
            phone_number="5555555555",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Rain) -> None:
        response = client.users.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Rain) -> None:
        with client.users.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Rain) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Rain) -> None:
        user = client.users.list(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Rain) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Rain) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Rain) -> None:
        user = client.users.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Rain) -> None:
        response = client.users.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Rain) -> None:
        with client.users.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_card(self, client: Rain) -> None:
        user = client.users.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        )
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_card_with_all_params(self, client: Rain) -> None:
        user = client.users.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
            billing={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            configuration={
                "display_name": "displayName",
                "product_id": "productId",
                "product_ref": "productRef",
                "virtual_card_art": "virtualCardArt",
            },
            limit={
                "amount": 0,
                "frequency": "per24HourPeriod",
            },
            shipping={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
                "phone_number": "phoneNumber",
                "method": "standard",
            },
            status="notActivated",
        )
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_card(self, client: Rain) -> None:
        response = client.users.with_raw_response.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_card(self, client: Rain) -> None:
        with client.users.with_streaming_response.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingCard, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_card(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.create_card(
                user_id="",
                type="physical",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_charge(self, client: Rain) -> None:
        user = client.users.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )
        assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_charge(self, client: Rain) -> None:
        response = client.users.with_raw_response.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_charge(self, client: Rain) -> None:
        with client.users.with_streaming_response.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_charge(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.create_charge(
                user_id="",
                amount=1,
                description="description",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_payment(self, client: Rain) -> None:
        user = client.users.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_payment_with_all_params(self, client: Rain) -> None:
        user = client.users.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_payment(self, client: Rain) -> None:
        response = client.users.with_raw_response.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_payment(self, client: Rain) -> None:
        with client.users.with_streaming_response.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_payment(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.initiate_payment(
                user_id="",
                amount=0,
                wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balances(self, client: Rain) -> None:
        user = client.users.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balances(self, client: Rain) -> None:
        response = client.users.with_raw_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balances(self, client: Rain) -> None:
        with client.users.with_streaming_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_balances(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_contracts(self, client: Rain) -> None:
        user = client.users.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_contracts(self, client: Rain) -> None:
        response = client.users.with_raw_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_contracts(self, client: Rain) -> None:
        with client.users.with_streaming_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_contracts(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve_contracts(
                "",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRain) -> None:
        user = await async_client.users.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.users.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            phone_country_code="1",
            phone_number="5555555555",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.create(
            email="email",
            first_name="firstName",
            last_name="lastName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRain) -> None:
        user = await async_client.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRain) -> None:
        user = await async_client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            email="email",
            first_name="firstName",
            is_active=True,
            is_terms_of_service_accepted=True,
            last_name="lastName",
            phone_country_code="1",
            phone_number="5555555555",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRain) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.users.list(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRain) -> None:
        user = await async_client.users.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_card(self, async_client: AsyncRain) -> None:
        user = await async_client.users.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        )
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_card_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.users.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
            billing={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            configuration={
                "display_name": "displayName",
                "product_id": "productId",
                "product_ref": "productRef",
                "virtual_card_art": "virtualCardArt",
            },
            limit={
                "amount": 0,
                "frequency": "per24HourPeriod",
            },
            shipping={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
                "phone_number": "phoneNumber",
                "method": "standard",
            },
            status="notActivated",
        )
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_card(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingCard, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_card(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.create_card(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="physical",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingCard, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_card(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.create_card(
                user_id="",
                type="physical",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_charge(self, async_client: AsyncRain) -> None:
        user = await async_client.users.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )
        assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_charge(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_charge(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.create_charge(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingChargeCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_charge(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.create_charge(
                user_id="",
                amount=1,
                description="description",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_payment(self, async_client: AsyncRain) -> None:
        user = await async_client.users.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_payment_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.users.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_payment(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_payment(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.initiate_payment(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserInitiatePaymentResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_payment(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.initiate_payment(
                user_id="",
                amount=0,
                wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balances(self, async_client: AsyncRain) -> None:
        user = await async_client.users.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balances(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balances(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveBalancesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balances(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_contracts(self, async_client: AsyncRain) -> None:
        user = await async_client.users.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_contracts(self, async_client: AsyncRain) -> None:
        response = await async_client.users.with_raw_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_contracts(self, async_client: AsyncRain) -> None:
        async with async_client.users.with_streaming_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveContractsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_contracts(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve_contracts(
                "",
            )
