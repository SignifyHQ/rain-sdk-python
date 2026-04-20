from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from tests.utils import assert_matches_type
from rain_sdk.types import UserListResponse

pytestmark = [pytest.mark.integration]


class TestUsersIntegration:
    def test_list_users(self, sandbox_client: Rain) -> None:
        result = sandbox_client.users.list()
        assert_matches_type(UserListResponse, result, path=["response"])

    async def test_list_users_async(self, async_sandbox_client: AsyncRain) -> None:
        result = await async_sandbox_client.users.list()
        assert_matches_type(UserListResponse, result, path=["response"])
