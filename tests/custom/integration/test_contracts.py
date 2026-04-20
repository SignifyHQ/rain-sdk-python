from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import ContractListResponse

pytestmark = [pytest.mark.integration]


class TestContractsIntegration:
    def test_list_contracts(self, sandbox_client: Rain) -> None:
        result = sandbox_client.contracts.list()
        assert_matches_type(ContractListResponse, result, path=["response"])

    async def test_list_contracts_async(self, async_sandbox_client: AsyncRain) -> None:
        result = await async_sandbox_client.contracts.list()
        assert_matches_type(ContractListResponse, result, path=["response"])
