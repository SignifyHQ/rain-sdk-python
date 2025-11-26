# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from rain_hello_world import RainHelloWorld, AsyncRainHelloWorld
from rain_hello_world._utils import parse_date
from rain_hello_world.types.applications import (
    IssuingCompany,
    CompanyRetrieveResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompany:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: RainHelloWorld) -> None:
        company = client.applications.company.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: RainHelloWorld) -> None:
        company = client.applications.company.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
                "description": "description",
                "expected_spend": "expectedSpend",
                "type": "type",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "phone_country_code": "1",
                "phone_number": "5555555555",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
                "role": "role",
                "solana_address": "WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
                "wallet_address": "0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "phone_country_code": "1",
                    "phone_number": "5555555555",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "phone_country_code": "1",
                    "phone_number": "5555555555",
                }
            ],
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            source_key="x",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: RainHelloWorld) -> None:
        response = client.applications.company.with_raw_response.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: RainHelloWorld) -> None:
        with client.applications.company.with_streaming_response.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: RainHelloWorld) -> None:
        company = client.applications.company.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: RainHelloWorld) -> None:
        response = client.applications.company.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: RainHelloWorld) -> None:
        with client.applications.company.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: RainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.applications.company.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: RainHelloWorld) -> None:
        company = client.applications.company.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: RainHelloWorld) -> None:
        company = client.applications.company.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            entity={
                "description": "description",
                "expected_spend": "expectedSpend",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "type": "type",
                "website": "website",
            },
            name="name",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: RainHelloWorld) -> None:
        response = client.applications.company.with_raw_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: RainHelloWorld) -> None:
        with client.applications.company.with_streaming_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: RainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.applications.company.with_raw_response.update(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reapply(self, client: RainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            company = client.applications.company.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            )

        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reapply_with_all_params(self, client: RainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            company = client.applications.company.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                entity={
                    "website": "website",
                    "description": "description",
                    "expected_spend": "expectedSpend",
                    "type": "type",
                },
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                    "role": "role",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                            "line2": "line2",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "phone_country_code": "1",
                        "phone_number": "5555555555",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                            "line2": "line2",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "phone_country_code": "1",
                        "phone_number": "5555555555",
                    }
                ],
            )

        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reapply(self, client: RainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.applications.company.with_raw_response.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reapply(self, client: RainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            with client.applications.company.with_streaming_response.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                company = response.parse()
                assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reapply(self, client: RainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
                client.applications.company.with_raw_response.reapply(
                    company_id="",
                    address={
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    entity={"website": "website"},
                    initial_user={
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "countryOfIssue",
                        "ip_address": "ipAddress",
                        "is_terms_of_service_accepted": True,
                        "national_id": "nationalId",
                    },
                    name="name",
                    representatives=[
                        {
                            "address": {
                                "city": "city",
                                "country": "country",
                                "country_code": "xx",
                                "line1": "line1",
                                "postal_code": "postalCode",
                                "region": "region",
                            },
                            "birth_date": parse_date("2000-01-01"),
                            "country_of_issue": "xx",
                            "email": "email",
                            "first_name": "firstName",
                            "last_name": "lastName",
                            "national_id": "nationalId",
                        }
                    ],
                    ultimate_beneficial_owners=[
                        {
                            "address": {
                                "city": "city",
                                "country": "country",
                                "country_code": "xx",
                                "line1": "line1",
                                "postal_code": "postalCode",
                                "region": "region",
                            },
                            "birth_date": parse_date("2000-01-01"),
                            "country_of_issue": "xx",
                            "email": "email",
                            "first_name": "firstName",
                            "last_name": "lastName",
                            "national_id": "nationalId",
                        }
                    ],
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_document(self, client: RainHelloWorld) -> None:
        company = client.applications.company.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_document_with_all_params(self, client: RainHelloWorld) -> None:
        company = client.applications.company.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            name="name",
            side="front",
            type="directorsRegistry",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_document(self, client: RainHelloWorld) -> None:
        response = client.applications.company.with_raw_response.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_document(self, client: RainHelloWorld) -> None:
        with client.applications.company.with_streaming_response.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert company is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_document(self, client: RainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            client.applications.company.with_raw_response.upload_document(
                company_id="",
                document=b"raw file contents",
            )


class TestAsyncCompany:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
                "description": "description",
                "expected_spend": "expectedSpend",
                "type": "type",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "phone_country_code": "1",
                "phone_number": "5555555555",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
                "role": "role",
                "solana_address": "WRktL2iKFTHZg6qNBPzV1b1WLYwfnZ5JSHo2UV8L1R",
                "wallet_address": "0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "phone_country_code": "1",
                    "phone_number": "5555555555",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "phone_country_code": "1",
                    "phone_number": "5555555555",
                }
            ],
            chain_id="chainId",
            contract_address="0xE1CB97d8EBbDbaAae6d9B1ca0D1cFaADcCcbdaDa",
            source_key="x",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRainHelloWorld) -> None:
        response = await async_client.applications.company.with_raw_response.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRainHelloWorld) -> None:
        async with async_client.applications.company.with_streaming_response.create(
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
            },
            entity={
                "name": "name",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "website": "website",
            },
            initial_user={
                "address": {
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                "birth_date": parse_date("2000-01-01"),
                "country_of_issue": "xx",
                "email": "email",
                "first_name": "firstName",
                "last_name": "lastName",
                "national_id": "nationalId",
                "ip_address": "ipAddress",
                "is_terms_of_service_accepted": True,
            },
            name="name",
            representatives=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
            ultimate_beneficial_owners=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "xx",
                    "email": "email",
                    "first_name": "firstName",
                    "last_name": "lastName",
                    "national_id": "nationalId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRainHelloWorld) -> None:
        response = await async_client.applications.company.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRainHelloWorld) -> None:
        async with async_client.applications.company.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.applications.company.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "city",
                "country": "country",
                "country_code": "xx",
                "line1": "line1",
                "postal_code": "postalCode",
                "region": "region",
                "line2": "line2",
            },
            entity={
                "description": "description",
                "expected_spend": "expectedSpend",
                "registration_number": "registrationNumber",
                "tax_id": "taxId",
                "type": "type",
                "website": "website",
            },
            name="name",
        )
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRainHelloWorld) -> None:
        response = await async_client.applications.company.with_raw_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRainHelloWorld) -> None:
        async with async_client.applications.company.with_streaming_response.update(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.applications.company.with_raw_response.update(
                company_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reapply(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            company = await async_client.applications.company.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            )

        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reapply_with_all_params(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            company = await async_client.applications.company.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                    "line2": "line2",
                },
                entity={
                    "website": "website",
                    "description": "description",
                    "expected_spend": "expectedSpend",
                    "type": "type",
                },
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                        "line2": "line2",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                    "role": "role",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                            "line2": "line2",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "phone_country_code": "1",
                        "phone_number": "5555555555",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                            "line2": "line2",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "phone_country_code": "1",
                        "phone_number": "5555555555",
                    }
                ],
            )

        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reapply(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.applications.company.with_raw_response.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(IssuingCompany, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reapply(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.applications.company.with_streaming_response.reapply(
                company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                address={
                    "city": "city",
                    "country": "country",
                    "country_code": "xx",
                    "line1": "line1",
                    "postal_code": "postalCode",
                    "region": "region",
                },
                entity={"website": "website"},
                initial_user={
                    "address": {
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    "birth_date": parse_date("2000-01-01"),
                    "country_of_issue": "countryOfIssue",
                    "ip_address": "ipAddress",
                    "is_terms_of_service_accepted": True,
                    "national_id": "nationalId",
                },
                name="name",
                representatives=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
                ultimate_beneficial_owners=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "xx",
                        "email": "email",
                        "first_name": "firstName",
                        "last_name": "lastName",
                        "national_id": "nationalId",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                company = await response.parse()
                assert_matches_type(IssuingCompany, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reapply(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
                await async_client.applications.company.with_raw_response.reapply(
                    company_id="",
                    address={
                        "city": "city",
                        "country": "country",
                        "country_code": "xx",
                        "line1": "line1",
                        "postal_code": "postalCode",
                        "region": "region",
                    },
                    entity={"website": "website"},
                    initial_user={
                        "address": {
                            "city": "city",
                            "country": "country",
                            "country_code": "xx",
                            "line1": "line1",
                            "postal_code": "postalCode",
                            "region": "region",
                        },
                        "birth_date": parse_date("2000-01-01"),
                        "country_of_issue": "countryOfIssue",
                        "ip_address": "ipAddress",
                        "is_terms_of_service_accepted": True,
                        "national_id": "nationalId",
                    },
                    name="name",
                    representatives=[
                        {
                            "address": {
                                "city": "city",
                                "country": "country",
                                "country_code": "xx",
                                "line1": "line1",
                                "postal_code": "postalCode",
                                "region": "region",
                            },
                            "birth_date": parse_date("2000-01-01"),
                            "country_of_issue": "xx",
                            "email": "email",
                            "first_name": "firstName",
                            "last_name": "lastName",
                            "national_id": "nationalId",
                        }
                    ],
                    ultimate_beneficial_owners=[
                        {
                            "address": {
                                "city": "city",
                                "country": "country",
                                "country_code": "xx",
                                "line1": "line1",
                                "postal_code": "postalCode",
                                "region": "region",
                            },
                            "birth_date": parse_date("2000-01-01"),
                            "country_of_issue": "xx",
                            "email": "email",
                            "first_name": "firstName",
                            "last_name": "lastName",
                            "national_id": "nationalId",
                        }
                    ],
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_document(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_document_with_all_params(self, async_client: AsyncRainHelloWorld) -> None:
        company = await async_client.applications.company.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
            country="xxx",
            name="name",
            side="front",
            type="directorsRegistry",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_document(self, async_client: AsyncRainHelloWorld) -> None:
        response = await async_client.applications.company.with_raw_response.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_document(self, async_client: AsyncRainHelloWorld) -> None:
        async with async_client.applications.company.with_streaming_response.upload_document(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert company is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_document(self, async_client: AsyncRainHelloWorld) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `company_id` but received ''"):
            await async_client.applications.company.with_raw_response.upload_document(
                company_id="",
                document=b"raw file contents",
            )
