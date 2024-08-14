# fineract_client.RecurringDepositAccountTransactionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_transaction_commands**](RecurringDepositAccountTransactionsApi.md#handle_transaction_commands) | **POST** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/{transactionId} | Adjust Transaction | Undo transaction
[**retrieve_one21**](RecurringDepositAccountTransactionsApi.md#retrieve_one21) | **GET** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/{transactionId} | Retrieve Recurring Deposit Account Transaction
[**retrieve_template16**](RecurringDepositAccountTransactionsApi.md#retrieve_template16) | **GET** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions/template | Retrieve Recurring Deposit Account Transaction Template
[**transaction1**](RecurringDepositAccountTransactionsApi.md#transaction1) | **POST** /v1/recurringdepositaccounts/{recurringDepositAccountId}/transactions | Deposit Transaction | Withdrawal Transaction

# **handle_transaction_commands**
> PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse handle_transaction_commands(body, recurring_deposit_account_id, transaction_id, command=command)

Adjust Transaction | Undo transaction

Adjust Transaction:  This command modifies the given transaction.  Undo transaction:  This command reverses the given transaction.  Showing request/response for 'Adjust Transaction'

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.RecurringDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest() # PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest | 
recurring_deposit_account_id = 789 # int | recurringDepositAccountId
transaction_id = 789 # int | transactionId
command = 'command_example' # str | command (optional)

try:
    # Adjust Transaction | Undo transaction
    api_response = api_instance.handle_transaction_commands(body, recurring_deposit_account_id, transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountTransactionsApi->handle_transaction_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.md)|  | 
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **transaction_id** | **int**| transactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one21**
> GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse retrieve_one21(recurring_deposit_account_id, transaction_id)

Retrieve Recurring Deposit Account Transaction

Retrieves Recurring Deposit Account Transaction  Example Requests:  recurringdepositaccounts/1/transactions/1

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.RecurringDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
recurring_deposit_account_id = 789 # int | recurringDepositAccountId
transaction_id = 789 # int | transactionId

try:
    # Retrieve Recurring Deposit Account Transaction
    api_response = api_instance.retrieve_one21(recurring_deposit_account_id, transaction_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template16**
> GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse retrieve_template16(recurring_deposit_account_id, command=command)

Retrieve Recurring Deposit Account Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Requests:  recurringdepositaccounts/1/transactions/template?command=deposit  recurringdepositaccounts/1/transactions/template?command=withdrawal

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.RecurringDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
recurring_deposit_account_id = 789 # int | recurringDepositAccountId
command = 'command_example' # str | command (optional)

try:
    # Retrieve Recurring Deposit Account Transaction Template
    api_response = api_instance.retrieve_template16(recurring_deposit_account_id, command=command)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction1**
> PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse transaction1(body, recurring_deposit_account_id, command=command)

Deposit Transaction | Withdrawal Transaction

Deposit Transaction:  Used for a deposit transaction  Withdrawal Transaction:  Used for a Withdrawal Transaction  Showing request/response for Deposit Transaction

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.RecurringDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest() # PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest | 
recurring_deposit_account_id = 789 # int | recurringDepositAccountId
command = 'command_example' # str | command (optional)

try:
    # Deposit Transaction | Withdrawal Transaction
    api_response = api_instance.transaction1(body, recurring_deposit_account_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountTransactionsApi->transaction1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.md)|  | 
 **recurring_deposit_account_id** | **int**| recurringDepositAccountId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse**](PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

