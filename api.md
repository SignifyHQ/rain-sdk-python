# Applications

## Company

Types:

```python
from rain_sdk.types.applications import (
    IssuingApplication,
    IssuingApplicationPerson,
    IssuingCompany,
    PhysicalAddress,
    CompanyRetrieveResponse,
)
```

Methods:

- <code title="post /applications/company">client.applications.company.<a href="./src/rain_sdk/resources/applications/company/company.py">create</a>(\*\*<a href="src/rain_sdk/types/applications/company_create_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="get /applications/company/{companyId}">client.applications.company.<a href="./src/rain_sdk/resources/applications/company/company.py">retrieve</a>(company_id) -> <a href="./src/rain_sdk/types/applications/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="patch /applications/company/{companyId}">client.applications.company.<a href="./src/rain_sdk/resources/applications/company/company.py">update</a>(company_id, \*\*<a href="src/rain_sdk/types/applications/company_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="put /applications/company/{companyId}/reapply">client.applications.company.<a href="./src/rain_sdk/resources/applications/company/company.py">reapply</a>(company_id, \*\*<a href="src/rain_sdk/types/applications/company_reapply_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="put /applications/company/{companyId}/document">client.applications.company.<a href="./src/rain_sdk/resources/applications/company/company.py">upload_document</a>(company_id, \*\*<a href="src/rain_sdk/types/applications/company_upload_document_params.py">params</a>) -> None</code>

### Ubo

Methods:

- <code title="patch /applications/company/{companyId}/ubo/{uboId}">client.applications.company.ubo.<a href="./src/rain_sdk/resources/applications/company/ubo/ubo.py">update</a>(ubo_id, \*, company_id, \*\*<a href="src/rain_sdk/types/applications/company/ubo_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="put /applications/company/{companyId}/ubo/document">client.applications.company.ubo.<a href="./src/rain_sdk/resources/applications/company/ubo/ubo.py">upload_document</a>(company_id, \*\*<a href="src/rain_sdk/types/applications/company/ubo_upload_document_params.py">params</a>) -> None</code>

#### Document

Methods:

- <code title="put /applications/company/{companyId}/ubo/{uboId}/document">client.applications.company.ubo.document.<a href="./src/rain_sdk/resources/applications/company/ubo/document.py">upload</a>(ubo_id, \*, company_id, \*\*<a href="src/rain_sdk/types/applications/company/ubo/document_upload_params.py">params</a>) -> None</code>

## User

Types:

```python
from rain_sdk.types.applications import IssuingUser, UserRetrieveResponse
```

Methods:

- <code title="post /applications/user">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">create</a>(\*\*<a href="src/rain_sdk/types/applications/user_create_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="get /applications/user/{userId}">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">retrieve</a>(user_id) -> <a href="./src/rain_sdk/types/applications/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /applications/user/{userId}">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">update</a>(user_id, \*\*<a href="src/rain_sdk/types/applications/user_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="post /applications/user/initiate">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">initiate</a>(\*\*<a href="src/rain_sdk/types/applications/user_initiate_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="put /applications/user/{userId}/reapply">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">reapply</a>(user_id, \*\*<a href="src/rain_sdk/types/applications/user_reapply_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="put /applications/user/{userId}/document">client.applications.user.<a href="./src/rain_sdk/resources/applications/user.py">upload_document</a>(user_id, \*\*<a href="src/rain_sdk/types/applications/user_upload_document_params.py">params</a>) -> None</code>

# Balances

Types:

```python
from rain_sdk.types import BalanceRetrieveResponse
```

Methods:

- <code title="get /balances">client.balances.<a href="./src/rain_sdk/resources/balances.py">retrieve</a>() -> <a href="./src/rain_sdk/types/balance_retrieve_response.py">BalanceRetrieveResponse</a></code>

# Cards

Types:

```python
from rain_sdk.types import (
    IssuingCard,
    IssuingCardLimit,
    IssuingCardStatus,
    CardListResponse,
    CardRetrieveSecretsResponse,
)
```

Methods:

- <code title="get /cards/{cardId}">client.cards.<a href="./src/rain_sdk/resources/cards/cards.py">retrieve</a>(card_id) -> <a href="./src/rain_sdk/types/issuing_card.py">IssuingCard</a></code>
- <code title="patch /cards/{cardId}">client.cards.<a href="./src/rain_sdk/resources/cards/cards.py">update</a>(card_id, \*\*<a href="src/rain_sdk/types/card_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/issuing_card.py">IssuingCard</a></code>
- <code title="get /cards">client.cards.<a href="./src/rain_sdk/resources/cards/cards.py">list</a>(\*\*<a href="src/rain_sdk/types/card_list_params.py">params</a>) -> <a href="./src/rain_sdk/types/card_list_response.py">CardListResponse</a></code>
- <code title="get /cards/{cardId}/secrets">client.cards.<a href="./src/rain_sdk/resources/cards/cards.py">retrieve_secrets</a>(card_id) -> <a href="./src/rain_sdk/types/card_retrieve_secrets_response.py">CardRetrieveSecretsResponse</a></code>

## Pin

Types:

```python
from rain_sdk.types.cards import PinRetrieveResponse
```

Methods:

- <code title="get /cards/{cardId}/pin">client.cards.pin.<a href="./src/rain_sdk/resources/cards/pin.py">retrieve</a>(card_id) -> <a href="./src/rain_sdk/types/cards/pin_retrieve_response.py">PinRetrieveResponse</a></code>
- <code title="put /cards/{cardId}/pin">client.cards.pin.<a href="./src/rain_sdk/resources/cards/pin.py">update</a>(card_id, \*\*<a href="src/rain_sdk/types/cards/pin_update_params.py">params</a>) -> None</code>

# Companies

Types:

```python
from rain_sdk.types import (
    IssuingChargeCreateBody,
    IssuingChargeCreateResponse,
    IssuingContract,
    CompanyListResponse,
    CompanyInitiatePaymentResponse,
    CompanyRetrieveBalancesResponse,
    CompanyRetrieveContractsResponse,
)
```

Methods:

- <code title="get /companies/{companyId}">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">retrieve</a>(company_id) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="patch /companies/{companyId}">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">update</a>(company_id, \*\*<a href="src/rain_sdk/types/company_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_company.py">IssuingCompany</a></code>
- <code title="get /companies">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">list</a>(\*\*<a href="src/rain_sdk/types/company_list_params.py">params</a>) -> <a href="./src/rain_sdk/types/company_list_response.py">CompanyListResponse</a></code>
- <code title="post /companies/{companyId}/charges">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">charge</a>(company_id, \*\*<a href="src/rain_sdk/types/company_charge_params.py">params</a>) -> <a href="./src/rain_sdk/types/issuing_charge_create_response.py">IssuingChargeCreateResponse</a></code>
- <code title="post /companies/{companyId}/users">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">create_user</a>(company_id, \*\*<a href="src/rain_sdk/types/company_create_user_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="post /companies/{companyId}/payments">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">initiate_payment</a>(company_id, \*\*<a href="src/rain_sdk/types/company_initiate_payment_params.py">params</a>) -> <a href="./src/rain_sdk/types/company_initiate_payment_response.py">CompanyInitiatePaymentResponse</a></code>
- <code title="get /companies/{companyId}/balances">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">retrieve_balances</a>(company_id) -> <a href="./src/rain_sdk/types/company_retrieve_balances_response.py">CompanyRetrieveBalancesResponse</a></code>
- <code title="get /companies/{companyId}/contracts">client.companies.<a href="./src/rain_sdk/resources/companies/companies.py">retrieve_contracts</a>(company_id) -> <a href="./src/rain_sdk/types/company_retrieve_contracts_response.py">CompanyRetrieveContractsResponse</a></code>

## Signatures

Types:

```python
from rain_sdk.types.companies import IssuingSignature
```

Methods:

- <code title="get /companies/{companyId}/signatures/payments">client.companies.signatures.<a href="./src/rain_sdk/resources/companies/signatures.py">retrieve_payment_signature</a>(company_id, \*\*<a href="src/rain_sdk/types/companies/signature_retrieve_payment_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>
- <code title="get /companies/{companyId}/signatures/withdrawals">client.companies.signatures.<a href="./src/rain_sdk/resources/companies/signatures.py">retrieve_withdrawal_signature</a>(company_id, \*\*<a href="src/rain_sdk/types/companies/signature_retrieve_withdrawal_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>

# Contracts

Types:

```python
from rain_sdk.types import ContractListResponse
```

Methods:

- <code title="get /contracts">client.contracts.<a href="./src/rain_sdk/resources/contracts.py">list</a>() -> <a href="./src/rain_sdk/types/contract_list_response.py">ContractListResponse</a></code>

# Disputes

Types:

```python
from rain_sdk.types import IssuingDispute, DisputeListResponse
```

Methods:

- <code title="get /disputes/{disputeId}">client.disputes.<a href="./src/rain_sdk/resources/disputes/disputes.py">retrieve</a>(dispute_id) -> <a href="./src/rain_sdk/types/issuing_dispute.py">IssuingDispute</a></code>
- <code title="patch /disputes/{disputeId}">client.disputes.<a href="./src/rain_sdk/resources/disputes/disputes.py">update</a>(dispute_id, \*\*<a href="src/rain_sdk/types/dispute_update_params.py">params</a>) -> None</code>
- <code title="get /disputes">client.disputes.<a href="./src/rain_sdk/resources/disputes/disputes.py">list</a>(\*\*<a href="src/rain_sdk/types/dispute_list_params.py">params</a>) -> <a href="./src/rain_sdk/types/dispute_list_response.py">DisputeListResponse</a></code>

## Evidence

Methods:

- <code title="get /disputes/{disputeId}/evidence">client.disputes.evidence.<a href="./src/rain_sdk/resources/disputes/evidence.py">list</a>(dispute_id) -> BinaryAPIResponse</code>
- <code title="put /disputes/{disputeId}/evidence">client.disputes.evidence.<a href="./src/rain_sdk/resources/disputes/evidence.py">upload</a>(dispute_id, \*\*<a href="src/rain_sdk/types/disputes/evidence_upload_params.py">params</a>) -> None</code>

# Keys

Types:

```python
from rain_sdk.types import KeyCreateResponse
```

Methods:

- <code title="post /keys">client.keys.<a href="./src/rain_sdk/resources/keys.py">create</a>(\*\*<a href="src/rain_sdk/types/key_create_params.py">params</a>) -> <a href="./src/rain_sdk/types/key_create_response.py">KeyCreateResponse</a></code>
- <code title="delete /keys/{keyId}">client.keys.<a href="./src/rain_sdk/resources/keys.py">delete</a>(key_id) -> None</code>

# Payments

Types:

```python
from rain_sdk.types import PaymentInitiateResponse
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/rain_sdk/resources/payments.py">initiate</a>(\*\*<a href="src/rain_sdk/types/payment_initiate_params.py">params</a>) -> <a href="./src/rain_sdk/types/payment_initiate_response.py">PaymentInitiateResponse</a></code>

# Signatures

Methods:

- <code title="get /signatures/payments">client.signatures.<a href="./src/rain_sdk/resources/signatures.py">retrieve_payment_signature</a>(\*\*<a href="src/rain_sdk/types/signature_retrieve_payment_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>
- <code title="get /signatures/withdrawals">client.signatures.<a href="./src/rain_sdk/resources/signatures.py">retrieve_withdrawal_signature</a>(\*\*<a href="src/rain_sdk/types/signature_retrieve_withdrawal_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>

# Transactions

Types:

```python
from rain_sdk.types import IssuingTransaction, TransactionListResponse
```

Methods:

- <code title="get /transactions/{transactionId}">client.transactions.<a href="./src/rain_sdk/resources/transactions/transactions.py">retrieve</a>(transaction_id) -> <a href="./src/rain_sdk/types/issuing_transaction.py">IssuingTransaction</a></code>
- <code title="patch /transactions/{transactionId}">client.transactions.<a href="./src/rain_sdk/resources/transactions/transactions.py">update</a>(transaction_id, \*\*<a href="src/rain_sdk/types/transaction_update_params.py">params</a>) -> None</code>
- <code title="get /transactions">client.transactions.<a href="./src/rain_sdk/resources/transactions/transactions.py">list</a>(\*\*<a href="src/rain_sdk/types/transaction_list_params.py">params</a>) -> <a href="./src/rain_sdk/types/transaction_list_response.py">TransactionListResponse</a></code>
- <code title="post /transactions/{transactionId}/disputes">client.transactions.<a href="./src/rain_sdk/resources/transactions/transactions.py">create_dispute</a>(transaction_id, \*\*<a href="src/rain_sdk/types/transaction_create_dispute_params.py">params</a>) -> <a href="./src/rain_sdk/types/issuing_dispute.py">IssuingDispute</a></code>

## Receipt

Methods:

- <code title="get /transactions/{transactionId}/receipt">client.transactions.receipt.<a href="./src/rain_sdk/resources/transactions/receipt.py">retrieve</a>(transaction_id) -> BinaryAPIResponse</code>
- <code title="put /transactions/{transactionId}/receipt">client.transactions.receipt.<a href="./src/rain_sdk/resources/transactions/receipt.py">upload</a>(transaction_id, \*\*<a href="src/rain_sdk/types/transactions/receipt_upload_params.py">params</a>) -> None</code>

# Users

Types:

```python
from rain_sdk.types import (
    UserListResponse,
    UserInitiatePaymentResponse,
    UserRetrieveBalancesResponse,
    UserRetrieveContractsResponse,
)
```

Methods:

- <code title="post /users">client.users.<a href="./src/rain_sdk/resources/users/users.py">create</a>(\*\*<a href="src/rain_sdk/types/user_create_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="get /users/{userId}">client.users.<a href="./src/rain_sdk/resources/users/users.py">retrieve</a>(user_id) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="patch /users/{userId}">client.users.<a href="./src/rain_sdk/resources/users/users.py">update</a>(user_id, \*\*<a href="src/rain_sdk/types/user_update_params.py">params</a>) -> <a href="./src/rain_sdk/types/applications/issuing_user.py">IssuingUser</a></code>
- <code title="get /users">client.users.<a href="./src/rain_sdk/resources/users/users.py">list</a>(\*\*<a href="src/rain_sdk/types/user_list_params.py">params</a>) -> <a href="./src/rain_sdk/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{userId}">client.users.<a href="./src/rain_sdk/resources/users/users.py">delete</a>(user_id) -> None</code>
- <code title="post /users/{userId}/cards">client.users.<a href="./src/rain_sdk/resources/users/users.py">create_card</a>(user_id, \*\*<a href="src/rain_sdk/types/user_create_card_params.py">params</a>) -> <a href="./src/rain_sdk/types/issuing_card.py">IssuingCard</a></code>
- <code title="post /users/{userId}/charges">client.users.<a href="./src/rain_sdk/resources/users/users.py">create_charge</a>(user_id, \*\*<a href="src/rain_sdk/types/user_create_charge_params.py">params</a>) -> <a href="./src/rain_sdk/types/issuing_charge_create_response.py">IssuingChargeCreateResponse</a></code>
- <code title="post /users/{userId}/payments">client.users.<a href="./src/rain_sdk/resources/users/users.py">initiate_payment</a>(user_id, \*\*<a href="src/rain_sdk/types/user_initiate_payment_params.py">params</a>) -> <a href="./src/rain_sdk/types/user_initiate_payment_response.py">UserInitiatePaymentResponse</a></code>
- <code title="get /users/{userId}/balances">client.users.<a href="./src/rain_sdk/resources/users/users.py">retrieve_balances</a>(user_id) -> <a href="./src/rain_sdk/types/user_retrieve_balances_response.py">UserRetrieveBalancesResponse</a></code>
- <code title="get /users/{userId}/contracts">client.users.<a href="./src/rain_sdk/resources/users/users.py">retrieve_contracts</a>(user_id) -> <a href="./src/rain_sdk/types/user_retrieve_contracts_response.py">UserRetrieveContractsResponse</a></code>

## Signatures

Methods:

- <code title="get /users/{userId}/signatures/payments">client.users.signatures.<a href="./src/rain_sdk/resources/users/signatures.py">retrieve_payment_signature</a>(user_id, \*\*<a href="src/rain_sdk/types/users/signature_retrieve_payment_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>
- <code title="get /users/{userId}/signatures/withdrawals">client.users.signatures.<a href="./src/rain_sdk/resources/users/signatures.py">retrieve_withdrawal_signature</a>(user_id, \*\*<a href="src/rain_sdk/types/users/signature_retrieve_withdrawal_signature_params.py">params</a>) -> <a href="./src/rain_sdk/types/companies/issuing_signature.py">IssuingSignature</a></code>
