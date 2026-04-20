from __future__ import annotations

import pytest

from rain_sdk import Rain, AsyncRain
from rain_sdk._exceptions import AuthenticationError

pytestmark = [pytest.mark.integration]


class TestConnectivity:
    def test_sandbox_auth(self, sandbox_client: Rain) -> None:
        """Verify that the sandbox API key is valid and the API is reachable."""
        try:
            sandbox_client.balances.retrieve()
        except AuthenticationError:
            pytest.fail("Sandbox API key is invalid or expired — check RAIN_SANDBOX_API_KEY")

    async def test_async_sandbox_auth(self, async_sandbox_client: AsyncRain) -> None:
        """Verify that the async sandbox client can authenticate."""
        try:
            await async_sandbox_client.balances.retrieve()
        except AuthenticationError:
            pytest.fail("Sandbox API key is invalid or expired — check RAIN_SANDBOX_API_KEY")
