# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import (
    CompanyListResponse,
    IssuingChargeCreateResponse,
    CompanyInitiatePaymentResponse,
    CompanyRetrieveBalancesResponse,
    CompanyRetrieveContractsResponse,
)
from rain_sdk._utils import parse_date
from rain_sdk.types.applications import IssuingUser, IssuingCompany

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rain) -> None:
        company = client.companies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rain) -> None:
        response = client.companies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rain) -> None:
        with client.companies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Rain) -> None:
        company = client.companies.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Rain) -> None:
        company = client.companies.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            name="name",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Rain) -> None:
        response = client.companies.with_raw_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Rain) -> None:
        with client.companies.with_streaming_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.update(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Rain) -> None:
        company = client.companies.list()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Rain) -> None:
        company = client.companies.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Rain) -> None:
        response = client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Rain) -> None:
        with client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_charge(self, client: Rain) -> None:
        company = client.companies.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )
        assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_charge(self, client: Rain) -> None:
        response = client.companies.with_raw_response.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_charge(self, client: Rain) -> None:
        with client.companies.with_streaming_response.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_charge(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.charge(
                company_id="",
                amount=1,
                description="description",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_user(self, client: Rain) -> None:
        company = client.companies.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        )
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_user_with_all_params(self, client: Rain) -> None:
        company = client.companies.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
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
            birth_date=parse_date("2019-12-27"),
            phone_country_code="phoneCountryCode",
            phone_number="phoneNumber",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_user(self, client: Rain) -> None:
        response = client.companies.with_raw_response.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_user(self, client: Rain) -> None:
        with client.companies.with_streaming_response.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingUser, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_user(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.create_user(
                company_id="",
                email="email",
                first_name="firstName",
                is_terms_of_service_accepted=True,
                last_name="lastName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_payment(self, client: Rain) -> None:
        company = client.companies.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_payment_with_all_params(self, client: Rain) -> None:
        company = client.companies.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_payment(self, client: Rain) -> None:
        response = client.companies.with_raw_response.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_payment(self, client: Rain) -> None:
        with client.companies.with_streaming_response.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_payment(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.initiate_payment(
                company_id="",
                amount=0,
                wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balances(self, client: Rain) -> None:
        company = client.companies.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balances(self, client: Rain) -> None:
        response = client.companies.with_raw_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balances(self, client: Rain) -> None:
        with client.companies.with_streaming_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_balances(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_contracts(self, client: Rain) -> None:
        company = client.companies.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_contracts(self, client: Rain) -> None:
        response = client.companies.with_raw_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_contracts(self, client: Rain) -> None:
        with client.companies.with_streaming_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_contracts(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.companies.with_raw_response.retrieve_contracts(
                "",
            )


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            name="name",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.update(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.list()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_charge(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )
        assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_charge(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_charge(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.charge(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingChargeCreateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_charge(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.charge(
                company_id="",
                amount=1,
                description="description",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_user(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        )
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_user_with_all_params(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
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
            birth_date=parse_date("2019-12-27"),
            phone_country_code="phoneCountryCode",
            phone_number="phoneNumber",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_user(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingUser, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_user(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.create_user(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="email",
            first_name="firstName",
            is_terms_of_service_accepted=True,
            last_name="lastName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingUser, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_user(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.create_user(
                company_id="",
                email="email",
                first_name="firstName",
                is_terms_of_service_accepted=True,
                last_name="lastName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_payment(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_payment_with_all_params(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            chain_id=0,
        )
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_payment(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_payment(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.initiate_payment(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyInitiatePaymentResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_payment(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.initiate_payment(
                company_id="",
                amount=0,
                wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balances(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balances(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balances(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.retrieve_balances(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveBalancesResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balances(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_contracts(self, async_client: AsyncRain) -> None:
        company = await async_client.companies.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_contracts(self, async_client: AsyncRain) -> None:
        response = await async_client.companies.with_raw_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_contracts(self, async_client: AsyncRain) -> None:
        async with async_client.companies.with_streaming_response.retrieve_contracts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveContractsResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_contracts(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.companies.with_raw_response.retrieve_contracts(
                "",
            )
