# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, RainHelloWorldError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        keys,
        cards,
        users,
        balances,
        disputes,
        payments,
        companies,
        contracts,
        signatures,
        applications,
        transactions,
    )
    from .resources.keys import KeysResource, AsyncKeysResource
    from .resources.balances import BalancesResource, AsyncBalancesResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.contracts import ContractsResource, AsyncContractsResource
    from .resources.signatures import SignaturesResource, AsyncSignaturesResource
    from .resources.cards.cards import CardsResource, AsyncCardsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.disputes.disputes import DisputesResource, AsyncDisputesResource
    from .resources.companies.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.applications.applications import ApplicationsResource, AsyncApplicationsResource
    from .resources.transactions.transactions import TransactionsResource, AsyncTransactionsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "RainHelloWorld",
    "AsyncRainHelloWorld",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "dev": "https://api-dev.raincards.xyz/v1/issuing",
    "production": "https://api.raincards.xyz/v1/issuing",
}


class RainHelloWorld(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["dev", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous RainHelloWorld client instance.

        This automatically infers the `api_key` argument from the `RAIN_HELLO_WORLD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RAIN_HELLO_WORLD_API_KEY")
        if api_key is None:
            raise RainHelloWorldError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RAIN_HELLO_WORLD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("RAIN_HELLO_WORLD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `RAIN_HELLO_WORLD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "dev"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def applications(self) -> ApplicationsResource:
        from .resources.applications import ApplicationsResource

        return ApplicationsResource(self)

    @cached_property
    def balances(self) -> BalancesResource:
        from .resources.balances import BalancesResource

        return BalancesResource(self)

    @cached_property
    def cards(self) -> CardsResource:
        from .resources.cards import CardsResource

        return CardsResource(self)

    @cached_property
    def companies(self) -> CompaniesResource:
        from .resources.companies import CompaniesResource

        return CompaniesResource(self)

    @cached_property
    def contracts(self) -> ContractsResource:
        from .resources.contracts import ContractsResource

        return ContractsResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        from .resources.disputes import DisputesResource

        return DisputesResource(self)

    @cached_property
    def keys(self) -> KeysResource:
        from .resources.keys import KeysResource

        return KeysResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def signatures(self) -> SignaturesResource:
        from .resources.signatures import SignaturesResource

        return SignaturesResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> RainHelloWorldWithRawResponse:
        return RainHelloWorldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RainHelloWorldWithStreamedResponse:
        return RainHelloWorldWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRainHelloWorld(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["dev", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRainHelloWorld client instance.

        This automatically infers the `api_key` argument from the `RAIN_HELLO_WORLD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RAIN_HELLO_WORLD_API_KEY")
        if api_key is None:
            raise RainHelloWorldError(
                "The api_key client option must be set either by passing api_key to the client or by setting the RAIN_HELLO_WORLD_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("RAIN_HELLO_WORLD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `RAIN_HELLO_WORLD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "dev"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        from .resources.applications import AsyncApplicationsResource

        return AsyncApplicationsResource(self)

    @cached_property
    def balances(self) -> AsyncBalancesResource:
        from .resources.balances import AsyncBalancesResource

        return AsyncBalancesResource(self)

    @cached_property
    def cards(self) -> AsyncCardsResource:
        from .resources.cards import AsyncCardsResource

        return AsyncCardsResource(self)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        from .resources.companies import AsyncCompaniesResource

        return AsyncCompaniesResource(self)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        from .resources.contracts import AsyncContractsResource

        return AsyncContractsResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        from .resources.disputes import AsyncDisputesResource

        return AsyncDisputesResource(self)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        from .resources.keys import AsyncKeysResource

        return AsyncKeysResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def signatures(self) -> AsyncSignaturesResource:
        from .resources.signatures import AsyncSignaturesResource

        return AsyncSignaturesResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRainHelloWorldWithRawResponse:
        return AsyncRainHelloWorldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRainHelloWorldWithStreamedResponse:
        return AsyncRainHelloWorldWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RainHelloWorldWithRawResponse:
    _client: RainHelloWorld

    def __init__(self, client: RainHelloWorld) -> None:
        self._client = client

    @cached_property
    def applications(self) -> applications.ApplicationsResourceWithRawResponse:
        from .resources.applications import ApplicationsResourceWithRawResponse

        return ApplicationsResourceWithRawResponse(self._client.applications)

    @cached_property
    def balances(self) -> balances.BalancesResourceWithRawResponse:
        from .resources.balances import BalancesResourceWithRawResponse

        return BalancesResourceWithRawResponse(self._client.balances)

    @cached_property
    def cards(self) -> cards.CardsResourceWithRawResponse:
        from .resources.cards import CardsResourceWithRawResponse

        return CardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def contracts(self) -> contracts.ContractsResourceWithRawResponse:
        from .resources.contracts import ContractsResourceWithRawResponse

        return ContractsResourceWithRawResponse(self._client.contracts)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        from .resources.disputes import DisputesResourceWithRawResponse

        return DisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def keys(self) -> keys.KeysResourceWithRawResponse:
        from .resources.keys import KeysResourceWithRawResponse

        return KeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def signatures(self) -> signatures.SignaturesResourceWithRawResponse:
        from .resources.signatures import SignaturesResourceWithRawResponse

        return SignaturesResourceWithRawResponse(self._client.signatures)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithRawResponse:
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncRainHelloWorldWithRawResponse:
    _client: AsyncRainHelloWorld

    def __init__(self, client: AsyncRainHelloWorld) -> None:
        self._client = client

    @cached_property
    def applications(self) -> applications.AsyncApplicationsResourceWithRawResponse:
        from .resources.applications import AsyncApplicationsResourceWithRawResponse

        return AsyncApplicationsResourceWithRawResponse(self._client.applications)

    @cached_property
    def balances(self) -> balances.AsyncBalancesResourceWithRawResponse:
        from .resources.balances import AsyncBalancesResourceWithRawResponse

        return AsyncBalancesResourceWithRawResponse(self._client.balances)

    @cached_property
    def cards(self) -> cards.AsyncCardsResourceWithRawResponse:
        from .resources.cards import AsyncCardsResourceWithRawResponse

        return AsyncCardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def contracts(self) -> contracts.AsyncContractsResourceWithRawResponse:
        from .resources.contracts import AsyncContractsResourceWithRawResponse

        return AsyncContractsResourceWithRawResponse(self._client.contracts)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        from .resources.disputes import AsyncDisputesResourceWithRawResponse

        return AsyncDisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithRawResponse:
        from .resources.keys import AsyncKeysResourceWithRawResponse

        return AsyncKeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def signatures(self) -> signatures.AsyncSignaturesResourceWithRawResponse:
        from .resources.signatures import AsyncSignaturesResourceWithRawResponse

        return AsyncSignaturesResourceWithRawResponse(self._client.signatures)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithRawResponse:
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class RainHelloWorldWithStreamedResponse:
    _client: RainHelloWorld

    def __init__(self, client: RainHelloWorld) -> None:
        self._client = client

    @cached_property
    def applications(self) -> applications.ApplicationsResourceWithStreamingResponse:
        from .resources.applications import ApplicationsResourceWithStreamingResponse

        return ApplicationsResourceWithStreamingResponse(self._client.applications)

    @cached_property
    def balances(self) -> balances.BalancesResourceWithStreamingResponse:
        from .resources.balances import BalancesResourceWithStreamingResponse

        return BalancesResourceWithStreamingResponse(self._client.balances)

    @cached_property
    def cards(self) -> cards.CardsResourceWithStreamingResponse:
        from .resources.cards import CardsResourceWithStreamingResponse

        return CardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def contracts(self) -> contracts.ContractsResourceWithStreamingResponse:
        from .resources.contracts import ContractsResourceWithStreamingResponse

        return ContractsResourceWithStreamingResponse(self._client.contracts)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        from .resources.disputes import DisputesResourceWithStreamingResponse

        return DisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def keys(self) -> keys.KeysResourceWithStreamingResponse:
        from .resources.keys import KeysResourceWithStreamingResponse

        return KeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def signatures(self) -> signatures.SignaturesResourceWithStreamingResponse:
        from .resources.signatures import SignaturesResourceWithStreamingResponse

        return SignaturesResourceWithStreamingResponse(self._client.signatures)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithStreamingResponse:
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncRainHelloWorldWithStreamedResponse:
    _client: AsyncRainHelloWorld

    def __init__(self, client: AsyncRainHelloWorld) -> None:
        self._client = client

    @cached_property
    def applications(self) -> applications.AsyncApplicationsResourceWithStreamingResponse:
        from .resources.applications import AsyncApplicationsResourceWithStreamingResponse

        return AsyncApplicationsResourceWithStreamingResponse(self._client.applications)

    @cached_property
    def balances(self) -> balances.AsyncBalancesResourceWithStreamingResponse:
        from .resources.balances import AsyncBalancesResourceWithStreamingResponse

        return AsyncBalancesResourceWithStreamingResponse(self._client.balances)

    @cached_property
    def cards(self) -> cards.AsyncCardsResourceWithStreamingResponse:
        from .resources.cards import AsyncCardsResourceWithStreamingResponse

        return AsyncCardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def contracts(self) -> contracts.AsyncContractsResourceWithStreamingResponse:
        from .resources.contracts import AsyncContractsResourceWithStreamingResponse

        return AsyncContractsResourceWithStreamingResponse(self._client.contracts)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        from .resources.disputes import AsyncDisputesResourceWithStreamingResponse

        return AsyncDisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithStreamingResponse:
        from .resources.keys import AsyncKeysResourceWithStreamingResponse

        return AsyncKeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def signatures(self) -> signatures.AsyncSignaturesResourceWithStreamingResponse:
        from .resources.signatures import AsyncSignaturesResourceWithStreamingResponse

        return AsyncSignaturesResourceWithStreamingResponse(self._client.signatures)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithStreamingResponse:
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = RainHelloWorld

AsyncClient = AsyncRainHelloWorld
