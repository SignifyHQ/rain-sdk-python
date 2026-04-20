from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import TransactionListResponse

pytestmark = [pytest.mark.integration]


class TestTransactionsIntegration:
    def test_list_transactions(self, sandbox_client: Rain) -> None:
        result = sandbox_client.transactions.list()
        assert_matches_type(TransactionListResponse, result, path=["response"])

    async def test_list_transactions_async(self, async_sandbox_client: AsyncRain) -> None:
        result = await async_sandbox_client.transactions.list()
        assert_matches_type(TransactionListResponse, result, path=["response"])
