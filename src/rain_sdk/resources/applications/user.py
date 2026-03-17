# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union, Mapping, cast
from datetime import date
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.applications import (
    user_create_params,
    user_update_params,
    user_reapply_params,
    user_initiate_params,
    user_upload_document_params,
)
from ...types.applications.issuing_user import IssuingUser
from ...types.applications.physical_address_param import PhysicalAddressParam
from ...types.applications.user_retrieve_response import UserRetrieveResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        sumsub_share_token: str,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          annual_salary: The user's annual salary

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          occupation: The user's occupation

          sumsub_share_token: The Sumsub share token used for user verification

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        persona_share_token: str,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          annual_salary: The user's annual salary

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          occupation: The user's occupation

          persona_share_token: The Persona inquiry ID

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_purpose: str,
        address: PhysicalAddressParam,
        annual_salary: str,
        birth_date: Union[str, date],
        country_of_issue: str,
        email: str,
        expected_monthly_volume: str,
        first_name: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        last_name: str,
        national_id: str,
        occupation: str,
        id: str | Omit = omit,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          address: The person's address

          annual_salary: The user's annual salary

          birth_date: The person's birth date

          country_of_issue: The 2-digit country code of the person's national ID issuer

          email: The user's email address

          expected_monthly_volume: The estimated monthly spending amount for the user

          first_name: The person's first name

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The person's last name

          national_id: The person's national ID number. For the US, this is a 9-digit SSN

          occupation: The user's occupation

          id: The person's unique identifier

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          phone_country_code: The country code for the phone number

          phone_number: The phone number of the person

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_purpose",
            "annual_salary",
            "expected_monthly_volume",
            "ip_address",
            "is_terms_of_service_accepted",
            "occupation",
            "sumsub_share_token",
        ],
        [
            "account_purpose",
            "annual_salary",
            "expected_monthly_volume",
            "ip_address",
            "is_terms_of_service_accepted",
            "occupation",
            "persona_share_token",
        ],
        [
            "account_purpose",
            "address",
            "annual_salary",
            "birth_date",
            "country_of_issue",
            "email",
            "expected_monthly_volume",
            "first_name",
            "ip_address",
            "is_terms_of_service_accepted",
            "last_name",
            "national_id",
            "occupation",
        ],
    )
    def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        sumsub_share_token: str | Omit = omit,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        persona_share_token: str | Omit = omit,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        id: str | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        return self._post(
            "/applications/user",
            body=maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "annual_salary": annual_salary,
                    "expected_monthly_volume": expected_monthly_volume,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "occupation": occupation,
                    "sumsub_share_token": sumsub_share_token,
                    "chain_id": chain_id,
                    "contract_address": contract_address,
                    "has_existing_documents": has_existing_documents,
                    "solana_address": solana_address,
                    "source_key": source_key,
                    "wallet_address": wallet_address,
                    "persona_share_token": persona_share_token,
                    "address": address,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "national_id": national_id,
                    "id": id,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """Retrieves the current status and details of a user's consumer application.

        This
        includes the user's application progress and related information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/applications/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def update(
        self,
        user_id: str,
        *,
        account_purpose: str | Omit = omit,
        address: PhysicalAddressParam | Omit = omit,
        annual_salary: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        expected_monthly_volume: str | Omit = omit,
        first_name: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        ip_address: str | Omit = omit,
        is_terms_of_service_accepted: Literal[True] | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        occupation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        Updates the application information for a user, including personal details such
        as name, birth date, occupation, national ID, and account purpose.

        Args:
          account_purpose: The purpose of the user's account

          address: The user's address

          annual_salary: The user's annual salary

          birth_date: The user's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          expected_monthly_volume: The estimated monthly spending amount for the user

          first_name: The user's first name

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          ip_address: The user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          national_id: The user's national ID number. For the US, this is a 9-digit SSN.

          occupation: The user's occupation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/applications/user/{user_id}",
            body=maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "address": address,
                    "annual_salary": annual_salary,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "expected_monthly_volume": expected_monthly_volume,
                    "first_name": first_name,
                    "has_existing_documents": has_existing_documents,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "national_id": national_id,
                    "occupation": occupation,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def initiate(
        self,
        *,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an initial application for creating a consumer account.

        This request
        gathers basic personal details of the user, including their first and last name,
        email address, and optional wallet address if using a Rain-managed solution or
        hosted completion flow.

        Args:
          email: The user's email address

          first_name: The user's first name

          last_name: The user's last name

          wallet_address: The user's wallet address. Required if using the hosted completion flow and a
              Rain-managed solution. Not required otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/applications/user/initiate",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "wallet_address": wallet_address,
                },
                user_initiate_params.UserInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    @typing_extensions.deprecated("deprecated")
    def reapply(
        self,
        user_id: str,
        *,
        account_purpose: str,
        address: PhysicalAddressParam,
        annual_salary: str,
        birth_date: Union[str, date],
        country_of_issue: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        national_id: str,
        occupation: str,
        has_existing_documents: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        Allows a user to reapply or respond to a request for additional information
        regarding their consumer application. This is used when the initial application
        needs updating or more information is required.

        Args:
          account_purpose: The purpose of the user's account

          address: The user's address

          annual_salary: The user's annual salary

          birth_date: The user's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: The user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          national_id: The user's national ID number. For the US, this is a 9-digit SSN

          occupation: The user's occupation

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/applications/user/{user_id}/reapply",
            body=maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "address": address,
                    "annual_salary": annual_salary,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "expected_monthly_volume": expected_monthly_volume,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "national_id": national_id,
                    "occupation": occupation,
                    "has_existing_documents": has_existing_documents,
                },
                user_reapply_params.UserReapplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    def upload_document(
        self,
        user_id: str,
        *,
        document: FileTypes,
        country: str | Omit = omit,
        name: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
        type: Literal[
            "idCard",
            "passport",
            "drivers",
            "residencePermit",
            "utilityBill",
            "selfie",
            "videoSelfie",
            "profileImage",
            "idDocPhoto",
            "agreement",
            "contract",
            "driversTranslation",
            "investorDoc",
            "vehicleRegistrationCertificate",
            "incomeSource",
            "paymentMethod",
            "bankCard",
            "covidVaccinationForm",
            "other",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Uploads a document for a user to support their consumer application.

        This is
        used to provide additional verification documents such as IDs, utility bills,
        and other required legal documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          name: The name or title of the document being uploaded

          side: The side of the document being uploaded

          type: The type of the document being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "name": name,
                "side": side,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            f"/applications/user/{user_id}/document",
            body=maybe_transform(body, user_upload_document_params.UserUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SignifyHQ/rain-sdk-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        sumsub_share_token: str,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          annual_salary: The user's annual salary

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          occupation: The user's occupation

          sumsub_share_token: The Sumsub share token used for user verification

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        persona_share_token: str,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          annual_salary: The user's annual salary

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          occupation: The user's occupation

          persona_share_token: The Persona inquiry ID

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_purpose: str,
        address: PhysicalAddressParam,
        annual_salary: str,
        birth_date: Union[str, date],
        country_of_issue: str,
        email: str,
        expected_monthly_volume: str,
        first_name: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        last_name: str,
        national_id: str,
        occupation: str,
        id: str | Omit = omit,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an application to create a consumer account for a user.

        The application
        can be submitted using a Sumsub share token, Persona share token, or directly
        via API. The user must provide details about their wallet, occupation, salary,
        and other account-related information.

        Args:
          account_purpose: The purpose of the user's account

          address: The person's address

          annual_salary: The user's annual salary

          birth_date: The person's birth date

          country_of_issue: The 2-digit country code of the person's national ID issuer

          email: The user's email address

          expected_monthly_volume: The estimated monthly spending amount for the user

          first_name: The person's first name

          ip_address: This user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The person's last name

          national_id: The person's national ID number. For the US, this is a 9-digit SSN

          occupation: The user's occupation

          id: The person's unique identifier

          chain_id: The chain ID of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          contract_address: The address of the user's external collateral contract, if applicable. Not
              required when using Rain's collateral contracts.

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          phone_country_code: The country code for the phone number

          phone_number: The phone number of the person

          solana_address: The user's Solana address. Either walletAddress or solanaAddress is required if
              using a Rain-managed solution, but optional otherwise.

          source_key: A unique identifier for the source of this user.

          wallet_address: The user's Ethereum Virtual Machine (EVM) address. Either walletAddress or
              solanaAddress is required if using a Rain-managed solution, but optional
              otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_purpose",
            "annual_salary",
            "expected_monthly_volume",
            "ip_address",
            "is_terms_of_service_accepted",
            "occupation",
            "sumsub_share_token",
        ],
        [
            "account_purpose",
            "annual_salary",
            "expected_monthly_volume",
            "ip_address",
            "is_terms_of_service_accepted",
            "occupation",
            "persona_share_token",
        ],
        [
            "account_purpose",
            "address",
            "annual_salary",
            "birth_date",
            "country_of_issue",
            "email",
            "expected_monthly_volume",
            "first_name",
            "ip_address",
            "is_terms_of_service_accepted",
            "last_name",
            "national_id",
            "occupation",
        ],
    )
    async def create(
        self,
        *,
        account_purpose: str,
        annual_salary: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        occupation: str,
        sumsub_share_token: str | Omit = omit,
        chain_id: str | Omit = omit,
        contract_address: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        solana_address: str | Omit = omit,
        source_key: str | Omit = omit,
        wallet_address: str | Omit = omit,
        persona_share_token: str | Omit = omit,
        address: PhysicalAddressParam | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        id: str | Omit = omit,
        phone_country_code: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        return await self._post(
            "/applications/user",
            body=await async_maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "annual_salary": annual_salary,
                    "expected_monthly_volume": expected_monthly_volume,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "occupation": occupation,
                    "sumsub_share_token": sumsub_share_token,
                    "chain_id": chain_id,
                    "contract_address": contract_address,
                    "has_existing_documents": has_existing_documents,
                    "solana_address": solana_address,
                    "source_key": source_key,
                    "wallet_address": wallet_address,
                    "persona_share_token": persona_share_token,
                    "address": address,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "national_id": national_id,
                    "id": id,
                    "phone_country_code": phone_country_code,
                    "phone_number": phone_number,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """Retrieves the current status and details of a user's consumer application.

        This
        includes the user's application progress and related information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/applications/user/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def update(
        self,
        user_id: str,
        *,
        account_purpose: str | Omit = omit,
        address: PhysicalAddressParam | Omit = omit,
        annual_salary: str | Omit = omit,
        birth_date: Union[str, date] | Omit = omit,
        country_of_issue: str | Omit = omit,
        expected_monthly_volume: str | Omit = omit,
        first_name: str | Omit = omit,
        has_existing_documents: bool | Omit = omit,
        ip_address: str | Omit = omit,
        is_terms_of_service_accepted: Literal[True] | Omit = omit,
        last_name: str | Omit = omit,
        national_id: str | Omit = omit,
        occupation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        Updates the application information for a user, including personal details such
        as name, birth date, occupation, national ID, and account purpose.

        Args:
          account_purpose: The purpose of the user's account

          address: The user's address

          annual_salary: The user's annual salary

          birth_date: The user's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          expected_monthly_volume: The estimated monthly spending amount for the user

          first_name: The user's first name

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          ip_address: The user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          last_name: The user's last name

          national_id: The user's national ID number. For the US, this is a 9-digit SSN.

          occupation: The user's occupation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/applications/user/{user_id}",
            body=await async_maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "address": address,
                    "annual_salary": annual_salary,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "expected_monthly_volume": expected_monthly_volume,
                    "first_name": first_name,
                    "has_existing_documents": has_existing_documents,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "last_name": last_name,
                    "national_id": national_id,
                    "occupation": occupation,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def initiate(
        self,
        *,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        wallet_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """Submits an initial application for creating a consumer account.

        This request
        gathers basic personal details of the user, including their first and last name,
        email address, and optional wallet address if using a Rain-managed solution or
        hosted completion flow.

        Args:
          email: The user's email address

          first_name: The user's first name

          last_name: The user's last name

          wallet_address: The user's wallet address. Required if using the hosted completion flow and a
              Rain-managed solution. Not required otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/applications/user/initiate",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "wallet_address": wallet_address,
                },
                user_initiate_params.UserInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    @typing_extensions.deprecated("deprecated")
    async def reapply(
        self,
        user_id: str,
        *,
        account_purpose: str,
        address: PhysicalAddressParam,
        annual_salary: str,
        birth_date: Union[str, date],
        country_of_issue: str,
        expected_monthly_volume: str,
        ip_address: str,
        is_terms_of_service_accepted: Literal[True],
        national_id: str,
        occupation: str,
        has_existing_documents: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IssuingUser:
        """
        Allows a user to reapply or respond to a request for additional information
        regarding their consumer application. This is used when the initial application
        needs updating or more information is required.

        Args:
          account_purpose: The purpose of the user's account

          address: The user's address

          annual_salary: The user's annual salary

          birth_date: The user's birth date

          country_of_issue: The 2-digit country code of the user's national ID issuer

          expected_monthly_volume: The estimated monthly spending amount for the user

          ip_address: The user's IP address

          is_terms_of_service_accepted: Indicates whether the user has accepted the terms of service

          national_id: The user's national ID number. For the US, this is a 9-digit SSN

          occupation: The user's occupation

          has_existing_documents: Indicates whether the user will use existing documents for additional
              verification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/applications/user/{user_id}/reapply",
            body=await async_maybe_transform(
                {
                    "account_purpose": account_purpose,
                    "address": address,
                    "annual_salary": annual_salary,
                    "birth_date": birth_date,
                    "country_of_issue": country_of_issue,
                    "expected_monthly_volume": expected_monthly_volume,
                    "ip_address": ip_address,
                    "is_terms_of_service_accepted": is_terms_of_service_accepted,
                    "national_id": national_id,
                    "occupation": occupation,
                    "has_existing_documents": has_existing_documents,
                },
                user_reapply_params.UserReapplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuingUser,
        )

    async def upload_document(
        self,
        user_id: str,
        *,
        document: FileTypes,
        country: str | Omit = omit,
        name: str | Omit = omit,
        side: Literal["front", "back"] | Omit = omit,
        type: Literal[
            "idCard",
            "passport",
            "drivers",
            "residencePermit",
            "utilityBill",
            "selfie",
            "videoSelfie",
            "profileImage",
            "idDocPhoto",
            "agreement",
            "contract",
            "driversTranslation",
            "investorDoc",
            "vehicleRegistrationCertificate",
            "incomeSource",
            "paymentMethod",
            "bankCard",
            "covidVaccinationForm",
            "other",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Uploads a document for a user to support their consumer application.

        This is
        used to provide additional verification documents such as IDs, utility bills,
        and other required legal documents.

        Args:
          document: The actual document file to be uploaded. The document must be in binary format,
              and the maximum allowed size is 20 MB.

          country: The country where the document was issued

          name: The name or title of the document being uploaded

          side: The side of the document being uploaded

          type: The type of the document being uploaded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "document": document,
                "country": country,
                "name": name,
                "side": side,
                "type": type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["document"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            f"/applications/user/{user_id}/document",
            body=await async_maybe_transform(body, user_upload_document_params.UserUploadDocumentParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_raw_response_wrapper(
            user.create,
        )
        self.retrieve = to_raw_response_wrapper(
            user.retrieve,
        )
        self.update = to_raw_response_wrapper(
            user.update,
        )
        self.initiate = to_raw_response_wrapper(
            user.initiate,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                user.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = to_raw_response_wrapper(
            user.upload_document,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_raw_response_wrapper(
            user.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            user.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            user.update,
        )
        self.initiate = async_to_raw_response_wrapper(
            user.initiate,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                user.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = async_to_raw_response_wrapper(
            user.upload_document,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.create = to_streamed_response_wrapper(
            user.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            user.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            user.update,
        )
        self.initiate = to_streamed_response_wrapper(
            user.initiate,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                user.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = to_streamed_response_wrapper(
            user.upload_document,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.create = async_to_streamed_response_wrapper(
            user.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            user.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            user.update,
        )
        self.initiate = async_to_streamed_response_wrapper(
            user.initiate,
        )
        self.reapply = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                user.reapply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upload_document = async_to_streamed_response_wrapper(
            user.upload_document,
        )
