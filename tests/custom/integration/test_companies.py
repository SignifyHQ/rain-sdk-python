from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import CompanyListResponse

pytestmark = [pytest.mark.integration]


class TestCompaniesIntegration:
    def test_list_companies(self, sandbox_client: Rain) -> None:
        result = sandbox_client.companies.list()
        assert_matches_type(CompanyListResponse, result, path=["response"])

    async def test_list_companies_async(self, async_sandbox_client: AsyncRain) -> None:
        result = await async_sandbox_client.companies.list()
        assert_matches_type(CompanyListResponse, result, path=["response"])
