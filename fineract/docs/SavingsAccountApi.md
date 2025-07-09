# fineract_client.SavingsAccountApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete19**](SavingsAccountApi.md#delete19) | **DELETE** /v1/savingsaccounts/{accountId} | Delete a savings application
[**delete20**](SavingsAccountApi.md#delete20) | **DELETE** /v1/savingsaccounts/external-id/{externalId} | Delete a savings application
[**get_savings_template**](SavingsAccountApi.md#get_savings_template) | **GET** /v1/savingsaccounts/downloadtemplate | 
[**get_savings_transaction_template**](SavingsAccountApi.md#get_savings_transaction_template) | **GET** /v1/savingsaccounts/transactions/downloadtemplate | 
[**handle_commands6**](SavingsAccountApi.md#handle_commands6) | **POST** /v1/savingsaccounts/{accountId} | Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions
[**handle_commands7**](SavingsAccountApi.md#handle_commands7) | **POST** /v1/savingsaccounts/external-id/{externalId} | Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions
[**handle_gsim_commands**](SavingsAccountApi.md#handle_gsim_commands) | **POST** /v1/savingsaccounts/gsimcommands/{parentAccountId} | 
[**post_savings_template**](SavingsAccountApi.md#post_savings_template) | **POST** /v1/savingsaccounts/uploadtemplate | 
[**post_savings_transaction_template**](SavingsAccountApi.md#post_savings_transaction_template) | **POST** /v1/savingsaccounts/transactions/uploadtemplate | 
[**retrieve_all33**](SavingsAccountApi.md#retrieve_all33) | **GET** /v1/savingsaccounts | List savings applications/accounts
[**retrieve_one25**](SavingsAccountApi.md#retrieve_one25) | **GET** /v1/savingsaccounts/{accountId} | Retrieve a savings application/account
[**retrieve_one26**](SavingsAccountApi.md#retrieve_one26) | **GET** /v1/savingsaccounts/external-id/{externalId} | Retrieve a savings application/account by external id
[**submit_application2**](SavingsAccountApi.md#submit_application2) | **POST** /v1/savingsaccounts | Submit new savings application
[**submit_gsim_application**](SavingsAccountApi.md#submit_gsim_application) | **POST** /v1/savingsaccounts/gsim | 
[**template14**](SavingsAccountApi.md#template14) | **GET** /v1/savingsaccounts/template | Retrieve Savings Account Template
[**update20**](SavingsAccountApi.md#update20) | **PUT** /v1/savingsaccounts/{accountId} | Modify a savings application | Modify savings account withhold tax applicability
[**update21**](SavingsAccountApi.md#update21) | **PUT** /v1/savingsaccounts/external-id/{externalId} | Modify a savings application | Modify savings account withhold tax applicability
[**update_gsim**](SavingsAccountApi.md#update_gsim) | **PUT** /v1/savingsaccounts/gsim/{parentAccountId} | 


# **delete19**
> DeleteSavingsAccountsAccountIdResponse delete19(account_id)

Delete a savings application

At present we support hard delete of savings application so long as its in 'Submitted and pending approval' state. One the application is moves past this state, it is not possible to do a 'hard' delete of the application or the account. An API endpoint will be added to close/de-activate the savings account.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_savings_accounts_account_id_response import DeleteSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    account_id = 56 # int | accountId

    try:
        # Delete a savings application
        api_response = api_instance.delete19(account_id)
        print("The response of SavingsAccountApi->delete19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->delete19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 

### Return type

[**DeleteSavingsAccountsAccountIdResponse**](DeleteSavingsAccountsAccountIdResponse.md)

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

# **delete20**
> DeleteSavingsAccountsAccountIdResponse delete20(external_id)

Delete a savings application

At present we support hard delete of savings application so long as its in 'Submitted and pending approval' state. One the application is moves past this state, it is not possible to do a 'hard' delete of the application or the account. An API endpoint will be added to close/de-activate the savings account.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_savings_accounts_account_id_response import DeleteSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    external_id = 'external_id_example' # str | externalId

    try:
        # Delete a savings application
        api_response = api_instance.delete20(external_id)
        print("The response of SavingsAccountApi->delete20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->delete20: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**DeleteSavingsAccountsAccountIdResponse**](DeleteSavingsAccountsAccountIdResponse.md)

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

# **get_savings_template**
> get_savings_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    office_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_savings_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->get_savings_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **staff_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_savings_transaction_template**
> get_savings_transaction_template(office_id=office_id, date_format=date_format)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    office_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_savings_transaction_template(office_id=office_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->get_savings_transaction_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands6**
> PostSavingsAccountsAccountIdResponse handle_commands6(account_id, post_savings_accounts_account_id_request, command=command)

Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions

Approve savings application:  Approves savings application so long as its in 'Submitted and pending approval' state.  Undo approval savings application:  Will move 'approved' savings application back to 'Submitted and pending approval' state.  Assign Savings Officer:  Allows you to assign Savings Officer for existing Savings Account.  Unassign Savings Officer:  Allows you to unassign the Savings Officer.  Reject savings application:  Rejects savings application so long as its in 'Submitted and pending approval' state.  Withdraw savings application:  Used when an applicant withdraws from the savings application. It must be in 'Submitted and pending approval' state.  Activate a savings account:  Results in an approved savings application being converted into an 'active' savings account.  Close a savings account:  Results in an Activated savings application being converted into an 'closed' savings account.  closedOnDate is closure date of savings account  withdrawBalance is a boolean description, true value of this field performs a withdrawal transaction with account's running balance.  Mandatory Fields: dateFormat,locale,closedOnDate  Optional Fields: note, withdrawBalance, paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber  Calculate Interest on Savings Account:  Calculates interest earned on a savings account based on todays date. It does not attempt to post or credit the interest on the account. That is responsibility of the Post Interest API that will likely be called by overnight process.  Post Interest on Savings Account:  Calculates and Posts interest earned on a savings account based on today's date and whether an interest posting or crediting event is due.  Block Savings Account:  Blocks Savings account from all types of credit and debit transactions  Unblock Savings Account:  Unblock a blocked account. On unblocking account, user can perform debit and credit transactions  Block Savings Account Credit transactions:  Savings account will be blocked from all types of credit transactions.  Unblock Savings Account Credit transactions:  It unblocks the Saving account's credit operations. Now all types of credits can be transacted to Savings account  Block Savings Account Debit transactions:  All types of debit operations from Savings account wil be blocked  Unblock Savings Account debit transactions:  It unblocks the Saving account's debit operations. Now all types of debits can be transacted from Savings account  Showing request/response for 'Unassign Savings Officer'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_accounts_account_id_request import PostSavingsAccountsAccountIdRequest
from fineract_client.models.post_savings_accounts_account_id_response import PostSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    account_id = 56 # int | accountId
    post_savings_accounts_account_id_request = fineract_client.PostSavingsAccountsAccountIdRequest() # PostSavingsAccountsAccountIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions
        api_response = api_instance.handle_commands6(account_id, post_savings_accounts_account_id_request, command=command)
        print("The response of SavingsAccountApi->handle_commands6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->handle_commands6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **post_savings_accounts_account_id_request** | [**PostSavingsAccountsAccountIdRequest**](PostSavingsAccountsAccountIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSavingsAccountsAccountIdResponse**](PostSavingsAccountsAccountIdResponse.md)

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

# **handle_commands7**
> PostSavingsAccountsAccountIdResponse handle_commands7(external_id, post_savings_accounts_account_id_request, command=command)

Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions

Approve savings application:  Approves savings application so long as its in 'Submitted and pending approval' state.  Undo approval savings application:  Will move 'approved' savings application back to 'Submitted and pending approval' state.  Assign Savings Officer:  Allows you to assign Savings Officer for existing Savings Account.  Unassign Savings Officer:  Allows you to unassign the Savings Officer.  Reject savings application:  Rejects savings application so long as its in 'Submitted and pending approval' state.  Withdraw savings application:  Used when an applicant withdraws from the savings application. It must be in 'Submitted and pending approval' state.  Activate a savings account:  Results in an approved savings application being converted into an 'active' savings account.  Close a savings account:  Results in an Activated savings application being converted into an 'closed' savings account.  closedOnDate is closure date of savings account  withdrawBalance is a boolean description, true value of this field performs a withdrawal transaction with account's running balance.  Mandatory Fields: dateFormat,locale,closedOnDate  Optional Fields: note, withdrawBalance, paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber  Calculate Interest on Savings Account:  Calculates interest earned on a savings account based on todays date. It does not attempt to post or credit the interest on the account. That is responsibility of the Post Interest API that will likely be called by overnight process.  Post Interest on Savings Account:  Calculates and Posts interest earned on a savings account based on today's date and whether an interest posting or crediting event is due.  Block Savings Account:  Blocks Savings account from all types of credit and debit transactions  Unblock Savings Account:  Unblock a blocked account. On unblocking account, user can perform debit and credit transactions  Block Savings Account Credit transactions:  Savings account will be blocked from all types of credit transactions.  Unblock Savings Account Credit transactions:  It unblocks the Saving account's credit operations. Now all types of credits can be transacted to Savings account  Block Savings Account Debit transactions:  All types of debit operations from Savings account wil be blocked  Unblock Savings Account debit transactions:  It unblocks the Saving account's debit operations. Now all types of debits can be transacted from Savings account  Showing request/response for 'Unassign Savings Officer'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_accounts_account_id_request import PostSavingsAccountsAccountIdRequest
from fineract_client.models.post_savings_accounts_account_id_response import PostSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    external_id = 'external_id_example' # str | externalId
    post_savings_accounts_account_id_request = fineract_client.PostSavingsAccountsAccountIdRequest() # PostSavingsAccountsAccountIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Approve savings application | Undo approval savings application | Assign Savings Officer | Unassign Savings Officer | Reject savings application | Withdraw savings application | Activate a savings account | Close a savings account | Calculate Interest on Savings Account | Post Interest on Savings Account | Block Savings Account | Unblock Savings Account | Block Savings Account Credit transactions | Unblock Savings Account Credit transactions | Block Savings Account Debit transactions | Unblock Savings Account debit transactions
        api_response = api_instance.handle_commands7(external_id, post_savings_accounts_account_id_request, command=command)
        print("The response of SavingsAccountApi->handle_commands7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->handle_commands7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **post_savings_accounts_account_id_request** | [**PostSavingsAccountsAccountIdRequest**](PostSavingsAccountsAccountIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSavingsAccountsAccountIdResponse**](PostSavingsAccountsAccountIdResponse.md)

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

# **handle_gsim_commands**
> str handle_gsim_commands(parent_account_id, command=command, body=body)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    parent_account_id = 56 # int | 
    command = 'command_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.handle_gsim_commands(parent_account_id, command=command, body=body)
        print("The response of SavingsAccountApi->handle_gsim_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->handle_gsim_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_account_id** | **int**|  | 
 **command** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_savings_template**
> str post_savings_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_savings_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of SavingsAccountApi->post_savings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->post_savings_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_savings_transaction_template**
> str post_savings_transaction_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_savings_transaction_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of SavingsAccountApi->post_savings_transaction_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->post_savings_transaction_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all33**
> GetSavingsAccountsResponse retrieve_all33(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List savings applications/accounts

Lists savings applications/accounts  Example Requests:  savingsaccounts   savingsaccounts?fields=name

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_response import GetSavingsAccountsResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    external_id = 'external_id_example' # str | externalId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # List savings applications/accounts
        api_response = api_instance.retrieve_all33(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of SavingsAccountApi->retrieve_all33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->retrieve_all33: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetSavingsAccountsResponse**](GetSavingsAccountsResponse.md)

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

# **retrieve_one25**
> GetSavingsAccountsAccountIdResponse retrieve_one25(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)

Retrieve a savings application/account

Retrieves a savings application/account  Example Requests :  savingsaccounts/1   savingsaccounts/1?associations=all

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_account_id_response import GetSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    account_id = 56 # int | accountId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')

    try:
        # Retrieve a savings application/account
        api_response = api_instance.retrieve_one25(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)
        print("The response of SavingsAccountApi->retrieve_one25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->retrieve_one25: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]

### Return type

[**GetSavingsAccountsAccountIdResponse**](GetSavingsAccountsAccountIdResponse.md)

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

# **retrieve_one26**
> GetSavingsAccountsAccountIdResponse retrieve_one26(external_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)

Retrieve a savings application/account by external id

Retrieves a savings application/account by external id  Example Requests :  savingsaccounts/external-id/ExternalId1   savingsaccounts/external-id/ExternalId1?associations=all

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_account_id_response import GetSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    external_id = 'external_id_example' # str | externalId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')

    try:
        # Retrieve a savings application/account by external id
        api_response = api_instance.retrieve_one26(external_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)
        print("The response of SavingsAccountApi->retrieve_one26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->retrieve_one26: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]

### Return type

[**GetSavingsAccountsAccountIdResponse**](GetSavingsAccountsAccountIdResponse.md)

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

# **submit_application2**
> PostSavingsAccountsResponse submit_application2(post_savings_accounts_request)

Submit new savings application

Submits new savings application  Mandatory Fields: clientId or groupId, productId, submittedOnDate  Optional Fields: accountNo, externalId, fieldOfficerId  Inherited from Product (if not provided): nominalAnnualInterestRate, interestCompoundingPeriodType, interestCalculationType, interestCalculationDaysInYearType, minRequiredOpeningBalance, lockinPeriodFrequency, lockinPeriodFrequencyType, withdrawalFeeForTransfers, allowOverdraft, overdraftLimit, withHoldTax  Additional Mandatory Field if Entity-Datatable Check is enabled for the entity of type Savings: datatables

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_accounts_request import PostSavingsAccountsRequest
from fineract_client.models.post_savings_accounts_response import PostSavingsAccountsResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    post_savings_accounts_request = fineract_client.PostSavingsAccountsRequest() # PostSavingsAccountsRequest | 

    try:
        # Submit new savings application
        api_response = api_instance.submit_application2(post_savings_accounts_request)
        print("The response of SavingsAccountApi->submit_application2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->submit_application2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_savings_accounts_request** | [**PostSavingsAccountsRequest**](PostSavingsAccountsRequest.md)|  | 

### Return type

[**PostSavingsAccountsResponse**](PostSavingsAccountsResponse.md)

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

# **submit_gsim_application**
> str submit_gsim_application(body=body)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.submit_gsim_application(body=body)
        print("The response of SavingsAccountApi->submit_gsim_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->submit_gsim_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template14**
> GetSavingsAccountsTemplateResponse template14(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve Savings Account Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  savingsaccounts/template?clientId=1   savingsaccounts/template?clientId=1&productId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_template_response import GetSavingsAccountsTemplateResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    client_id = 56 # int | clientId (optional)
    group_id = 56 # int | groupId (optional)
    product_id = 56 # int | productId (optional)
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve Savings Account Template
        api_response = api_instance.template14(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of SavingsAccountApi->template14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->template14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **product_id** | **int**| productId | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetSavingsAccountsTemplateResponse**](GetSavingsAccountsTemplateResponse.md)

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

# **update20**
> PutSavingsAccountsAccountIdResponse update20(account_id, put_savings_accounts_account_id_request, command=command)

Modify a savings application | Modify savings account withhold tax applicability

Modify a savings application:  Savings application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method. Specific api endpoints will be created to allow change of interest detail such as rate, compounding period, posting period etc  Modify savings account withhold tax applicability:  Savings application's withhold tax can be modified when in 'Active' state. Once the application is activated, can modify the account withhold tax to post tax or vice-versaShowing request/response for 'Modify a savings application'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_savings_accounts_account_id_request import PutSavingsAccountsAccountIdRequest
from fineract_client.models.put_savings_accounts_account_id_response import PutSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    account_id = 56 # int | accountId
    put_savings_accounts_account_id_request = fineract_client.PutSavingsAccountsAccountIdRequest() # PutSavingsAccountsAccountIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Modify a savings application | Modify savings account withhold tax applicability
        api_response = api_instance.update20(account_id, put_savings_accounts_account_id_request, command=command)
        print("The response of SavingsAccountApi->update20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->update20: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **put_savings_accounts_account_id_request** | [**PutSavingsAccountsAccountIdRequest**](PutSavingsAccountsAccountIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PutSavingsAccountsAccountIdResponse**](PutSavingsAccountsAccountIdResponse.md)

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

# **update21**
> PutSavingsAccountsAccountIdResponse update21(external_id, put_savings_accounts_account_id_request, command=command)

Modify a savings application | Modify savings account withhold tax applicability

Modify a savings application:  Savings application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method. Specific api endpoints will be created to allow change of interest detail such as rate, compounding period, posting period etc  Modify savings account withhold tax applicability:  Savings application's withhold tax can be modified when in 'Active' state. Once the application is activated, can modify the account withhold tax to post tax or vice-versaShowing request/response for 'Modify a savings application'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_savings_accounts_account_id_request import PutSavingsAccountsAccountIdRequest
from fineract_client.models.put_savings_accounts_account_id_response import PutSavingsAccountsAccountIdResponse
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    external_id = 'external_id_example' # str | externalId
    put_savings_accounts_account_id_request = fineract_client.PutSavingsAccountsAccountIdRequest() # PutSavingsAccountsAccountIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Modify a savings application | Modify savings account withhold tax applicability
        api_response = api_instance.update21(external_id, put_savings_accounts_account_id_request, command=command)
        print("The response of SavingsAccountApi->update21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->update21: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 
 **put_savings_accounts_account_id_request** | [**PutSavingsAccountsAccountIdRequest**](PutSavingsAccountsAccountIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PutSavingsAccountsAccountIdResponse**](PutSavingsAccountsAccountIdResponse.md)

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

# **update_gsim**
> str update_gsim(parent_account_id, body=body)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SavingsAccountApi(api_client)
    parent_account_id = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.update_gsim(parent_account_id, body=body)
        print("The response of SavingsAccountApi->update_gsim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountApi->update_gsim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_account_id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

