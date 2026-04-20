from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import BalanceRetrieveResponse

pytestmark = [pytest.mark.integration]


class TestBalancesIntegration:
    def test_retrieve_balances(self, sandbox_client: Rain) -> None:
        result = sandbox_client.balances.retrieve()
        assert_matches_type(BalanceRetrieveResponse, result, path=["response"])

    async def test_retrieve_balances_async(self, async_sandbox_client: AsyncRain) -> None:
        result = await async_sandbox_client.balances.retrieve()
        assert_matches_type(BalanceRetrieveResponse, result, path=["response"])
