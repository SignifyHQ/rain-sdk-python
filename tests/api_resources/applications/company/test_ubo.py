# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk._utils import parse_date
from rain_sdk.types.applications import IssuingCompany

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUbo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Rain) -> None:
        ubo = client.applications.company.ubo.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Rain) -> None:
        ubo = client.applications.company.ubo.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            birth_date=parse_date("2000-01-01"),
            country_of_issue="countryOfIssue",
            email="dev@stainless.com",
            first_name="firstName",
            last_name="lastName",
            national_id="nationalId",
        )
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Rain) -> None:
        response = client.applications.company.ubo.with_raw_response.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ubo = response.parse()
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Rain) -> None:
        with client.applications.company.ubo.with_streaming_response.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ubo = response.parse()
            assert_matches_type(IssuingCompany, ubo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.applications.company.ubo.with_raw_response.update(
                ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                company_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ubo_id` but received ''"):
            client.applications.company.ubo.with_raw_response.update(
                ubo_id="",
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_document(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            ubo = client.applications.company.ubo.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            )

        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_document_with_all_params(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            ubo = client.applications.company.ubo.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
                country="xxx",
                side="front",
                type="idCard",
            )

        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_document(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.applications.company.ubo.with_raw_response.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ubo = response.parse()
        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_document(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            with client.applications.company.ubo.with_streaming_response.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                ubo = response.parse()
                assert ubo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload_document(self, client: Rain) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
                client.applications.company.ubo.with_raw_response.upload_document(
                    company_id="",
                    document=b"Example data",
                    email="email",
                )


class TestAsyncUbo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRain) -> None:
        ubo = await async_client.applications.company.ubo.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRain) -> None:
        ubo = await async_client.applications.company.ubo.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            birth_date=parse_date("2000-01-01"),
            country_of_issue="countryOfIssue",
            email="dev@stainless.com",
            first_name="firstName",
            last_name="lastName",
            national_id="nationalId",
        )
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.company.ubo.with_raw_response.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ubo = await response.parse()
        assert_matches_type(IssuingCompany, ubo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRain) -> None:
        async with async_client.applications.company.ubo.with_streaming_response.update(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ubo = await response.parse()
            assert_matches_type(IssuingCompany, ubo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.applications.company.ubo.with_raw_response.update(
                ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                company_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ubo_id` but received ''"):
            await async_client.applications.company.ubo.with_raw_response.update(
                ubo_id="",
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_document(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            ubo = await async_client.applications.company.ubo.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            )

        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_document_with_all_params(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            ubo = await async_client.applications.company.ubo.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
                country="xxx",
                side="front",
                type="idCard",
            )

        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_document(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.applications.company.ubo.with_raw_response.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ubo = await response.parse()
        assert ubo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_document(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.applications.company.ubo.with_streaming_response.upload_document(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"Example data",
                email="email",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                ubo = await response.parse()
                assert ubo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload_document(self, async_client: AsyncRain) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
                await async_client.applications.company.ubo.with_raw_response.upload_document(
                    company_id="",
                    document=b"Example data",
                    email="email",
                )
