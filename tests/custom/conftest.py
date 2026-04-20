from __future__ import annotations

import os
from typing import Iterator, AsyncIterator

import pytest

from rain_sdk import Rain, AsyncRain

SANDBOX_API_KEY = os.environ.get("RAIN_SANDBOX_API_KEY", "")


def has_sandbox_credentials() -> bool:
    return bool(SANDBOX_API_KEY)


skip_without_sandbox = pytest.mark.skipif(
    not has_sandbox_credentials(),
    reason="RAIN_SANDBOX_API_KEY not set; skipping sandbox integration test",
)


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "integration: Integration tests against the real sandbox API")


@pytest.fixture(scope="session")
def sandbox_client() -> Iterator[Rain]:
    """Sync client pointed at the dev sandbox."""
    if not has_sandbox_credentials():
        pytest.skip("RAIN_SANDBOX_API_KEY not set")

    with Rain(api_key=SANDBOX_API_KEY, environment="dev") as client:
        assert "api-dev" in str(client.base_url), "Integration tests must not run against production"
        yield client


@pytest.fixture(scope="session")
async def async_sandbox_client() -> AsyncIterator[AsyncRain]:
    """Async client pointed at the dev sandbox."""
    if not has_sandbox_credentials():
        pytest.skip("RAIN_SANDBOX_API_KEY not set")

    async with AsyncRain(api_key=SANDBOX_API_KEY, environment="dev") as client:
        assert "api-dev" in str(client.base_url), "Integration tests must not run against production"
        yield client
