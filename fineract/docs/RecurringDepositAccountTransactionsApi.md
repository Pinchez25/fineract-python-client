# fineract_client.RecurringDepositAccountTransactionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_transaction_commands**](RecurringDepositAccountTransactionsApi.md#handle_transaction_commands) | **POST** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/{transactionId} | Adjust Transaction | Undo transaction
[**retrieve_one21**](RecurringDepositAccountTransactionsApi.md#retrieve_one21) | **GET** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/{transactionId} | Retrieve Recurring Deposit Account Transaction
[**retrieve_template16**](RecurringDepositAccountTransactionsApi.md#retrieve_template16) | **GET** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/template | Retrieve Recurring Deposit Account Transaction Template
[**transaction1**](RecurringDepositAccountTransactionsApi.md#transaction1) | **POST** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions | Deposit Transaction | Withdrawal Transaction


# **handle_transaction_commands**
> PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse handle_transaction_commands(recurring_deposit_account_id, transaction_id, post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request, command=command)

Adjust Transaction | Undo transaction

Adjust Transaction:

This command modifies the given transaction.

Undo transaction:

This command reverses the given transaction.

Showing request/response for 'Adjust Transaction'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.RecurringDepositAccountTransactionsApi(api_client)
    recurring_deposit_account_id = 56 # int | recurringDepositAccountId
    transaction_id = 56 # int | transactionId
    post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request = fineract_client.PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest() # PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Adjust Transaction | Undo transaction
        api_response = api_instance.handle_transaction_commands(recurring_deposit_account_id, transaction_id, post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request, command=command)
        print("The response of RecurringDepositAccountTransactionsApi->handle_transaction_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringDepositAccountTransactionsApi->handle_transaction_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **transaction_id** | **int**| transactionId | 
 **post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request** | [**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one21**
> GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse retrieve_one21(recurring_deposit_account_id, transaction_id)

Retrieve Recurring Deposit Account Transaction

Retrieves Recurring Deposit Account Transaction

Example Requests:

recurringdepositaccounts/1/transactions/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response import GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.RecurringDepositAccountTransactionsApi(api_client)
    recurring_deposit_account_id = 56 # int | recurringDepositAccountId
    transaction_id = 56 # int | transactionId

    try:
        # Retrieve Recurring Deposit Account Transaction
        api_response = api_instance.retrieve_one21(recurring_deposit_account_id, transaction_id)
        print("The response of RecurringDepositAccountTransactionsApi->retrieve_one21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringDepositAccountTransactionsApi->retrieve_one21: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse**](GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template16**
> GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse retrieve_template16(recurring_deposit_account_id, command=command)

Retrieve Recurring Deposit Account Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists
Example Requests:

recurringdepositaccounts/1/transactions/template?command=deposit

recurringdepositaccounts/1/transactions/template?command=withdrawal

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response import GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.RecurringDepositAccountTransactionsApi(api_client)
    recurring_deposit_account_id = 56 # int | recurringDepositAccountId
    command = 'command_example' # str | command (optional)

    try:
        # Retrieve Recurring Deposit Account Transaction Template
        api_response = api_instance.retrieve_template16(recurring_deposit_account_id, command=command)
        print("The response of RecurringDepositAccountTransactionsApi->retrieve_template16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringDepositAccountTransactionsApi->retrieve_template16: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **command** | **str**| command | [optional] 

### Return type

[**GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse**](GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction1**
> PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse transaction1(recurring_deposit_account_id, post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request, command=command)

Deposit Transaction | Withdrawal Transaction

Deposit Transaction:

Used for a deposit transaction

Withdrawal Transaction:

Used for a Withdrawal Transaction

Showing request/response for Deposit Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.RecurringDepositAccountTransactionsApi(api_client)
    recurring_deposit_account_id = 56 # int | recurringDepositAccountId
    post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request = fineract_client.PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest() # PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Deposit Transaction | Withdrawal Transaction
        api_response = api_instance.transaction1(recurring_deposit_account_id, post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request, command=command)
        print("The response of RecurringDepositAccountTransactionsApi->transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringDepositAccountTransactionsApi->transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request** | [**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

