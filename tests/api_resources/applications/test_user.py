# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk._utils import parse_date
from rain_sdk.types.applications import (
    IssuingUser,
    UserRetrieveResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Rain) -> None:
        user = client.applications.user.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            phone_country_code="1",
            phone_number="5555555555",
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Rain) -> None:
        user = client.applications.user.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.applications.user.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Rain) -> None:
        user = client.applications.user.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Rain) -> None:
        user = client.applications.user.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="countryOfIssue",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            has_existing_documents=True,
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.update(
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
            client.applications.user.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate(self, client: Rain) -> None:
        user = client.applications.user.initiate()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params(self, client: Rain) -> None:
        user = client.applications.user.initiate(
            email="email",
            first_name="firstName",
            last_name="lastName",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.initiate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.initiate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reapply(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            user = client.applications.user.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            )

        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reapply_with_all_params(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            user = client.applications.user.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
                has_existing_documents=True,
            )

        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reapply(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.applications.user.with_raw_response.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reapply(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            with client.applications.user.with_streaming_response.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                user = response.parse()
                assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reapply(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
                client.applications.user.with_raw_response.reapply(
                    user_id="",
                    account_purpose="accountPurpose",
                    address={
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    annual_salary="annualSalary",
                    birth_date=parse_date("2000-01-01"),
                    country_of_issue="countryOfIssue",
                    expected_monthly_volume="expectedMonthlyVolume",
                    ip_address="ipAddress",
                    is_terms_of_service_accepted=True,
                    national_id="nationalId",
                    occupation="occupation",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_document(self, client: Rain) -> None:
        user = client.applications.user.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_document_with_all_params(self, client: Rain) -> None:
        user = client.applications.user.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            name="name",
            side="front",
            type="idCard",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_document(self, client: Rain) -> None:
        response = client.applications.user.with_raw_response.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_document(self, client: Rain) -> None:
        with client.applications.user.with_streaming_response.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_document(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.applications.user.with_raw_response.upload_document(
                user_id="",
                document=b"raw file contents",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            sumsub_share_token="sumsubShareToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            annual_salary="annualSalary",
            expected_monthly_volume="expectedMonthlyVolume",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            occupation="occupation",
            persona_share_token="personaShareToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            has_existing_documents=True,
            phone_country_code="1",
            phone_number="5555555555",
            solana_address="WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
            source_key="x",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.create(
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="xx",
            email="email",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.applications.user.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_purpose="accountPurpose",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            annual_salary="annualSalary",
            birth_date=parse_date("2000-01-01"),
            country_of_issue="countryOfIssue",
            expected_monthly_volume="expectedMonthlyVolume",
            first_name="firstName",
            has_existing_documents=True,
            ip_address="ipAddress",
            is_terms_of_service_accepted=True,
            last_name="lastName",
            national_id="nationalId",
            occupation="occupation",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.update(
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
            await async_client.applications.user.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.initiate()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.initiate(
            email="email",
            first_name="firstName",
            last_name="lastName",
            wallet_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
        )
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.initiate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.initiate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reapply(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            user = await async_client.applications.user.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            )

        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reapply_with_all_params(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            user = await async_client.applications.user.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
                has_existing_documents=True,
            )

        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reapply(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.applications.user.with_raw_response.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(IssuingUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reapply(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.applications.user.with_streaming_response.reapply(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_purpose="accountPurpose",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                annual_salary="annualSalary",
                birth_date=parse_date("2000-01-01"),
                country_of_issue="countryOfIssue",
                expected_monthly_volume="expectedMonthlyVolume",
                ip_address="ipAddress",
                is_terms_of_service_accepted=True,
                national_id="nationalId",
                occupation="occupation",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                user = await response.parse()
                assert_matches_type(IssuingUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reapply(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
                await async_client.applications.user.with_raw_response.reapply(
                    user_id="",
                    account_purpose="accountPurpose",
                    address={
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    annual_salary="annualSalary",
                    birth_date=parse_date("2000-01-01"),
                    country_of_issue="countryOfIssue",
                    expected_monthly_volume="expectedMonthlyVolume",
                    ip_address="ipAddress",
                    is_terms_of_service_accepted=True,
                    national_id="nationalId",
                    occupation="occupation",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_document(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_document_with_all_params(self, async_client: AsyncRain) -> None:
        user = await async_client.applications.user.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            name="name",
            side="front",
            type="idCard",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_document(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.user.with_raw_response.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_document(self, async_client: AsyncRain) -> None:
        async with async_client.applications.user.with_streaming_response.upload_document(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_document(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.applications.user.with_raw_response.upload_document(
                user_id="",
                document=b"raw file contents",
            )
