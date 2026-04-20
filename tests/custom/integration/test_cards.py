from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import CardListResponse

pytestmark = [pytest.mark.integration]


class TestCardsIntegration:
    def test_list_cards(self, sandbox_client: Rain) -> None:
        """GET /cards — retrieves all cards."""
        result = sandbox_client.cards.list()
        assert_matches_type(CardListResponse, result, path=["response"])

    async def test_list_cards_async(self, async_sandbox_client: AsyncRain) -> None:
        """GET /cards — retrieves all cards (async)."""
        result = await async_sandbox_client.cards.list()
        assert_matches_type(CardListResponse, result, path=["response"])
