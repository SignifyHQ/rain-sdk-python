# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rain_sdk import Rain, AsyncRain

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Rain) -> None:
        document = client.applications.company.ubo.document.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Rain) -> None:
        document = client.applications.company.ubo.document.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            side="front",
            type="idCard",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Rain) -> None:
        response = client.applications.company.ubo.document.with_raw_response.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Rain) -> None:
        with client.applications.company.ubo.document.with_streaming_response.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Rain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.applications.company.ubo.document.with_raw_response.upload(
                ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                company_id="",
                document=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ubo_id` but received ''"):
            client.applications.company.ubo.document.with_raw_response.upload(
                ubo_id="",
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"raw file contents",
            )


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncRain) -> None:
        document = await async_client.applications.company.ubo.document.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncRain) -> None:
        document = await async_client.applications.company.ubo.document.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            side="front",
            type="idCard",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncRain) -> None:
        response = await async_client.applications.company.ubo.document.with_raw_response.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncRain) -> None:
        async with async_client.applications.company.ubo.document.with_streaming_response.upload(
            ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncRain) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.applications.company.ubo.document.with_raw_response.upload(
                ubo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                company_id="",
                document=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ubo_id` but received ''"):
            await async_client.applications.company.ubo.document.with_raw_response.upload(
                ubo_id="",
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document=b"raw file contents",
            )
