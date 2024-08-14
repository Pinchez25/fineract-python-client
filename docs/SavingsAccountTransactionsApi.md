# fineract_client.SavingsAccountTransactionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_transaction1**](SavingsAccountTransactionsApi.md#adjust_transaction1) | **POST** /v1/savingsaccounts/{savingsId}/transactions/{transactionId} | Undo/Reverse/Modify/Release Amount transaction API
[**advanced_query1**](SavingsAccountTransactionsApi.md#advanced_query1) | **POST** /v1/savingsaccounts/{savingsId}/transactions/query | Advanced search Savings Account Transactions
[**retrieve_one24**](SavingsAccountTransactionsApi.md#retrieve_one24) | **GET** /v1/savingsaccounts/{savingsId}/transactions/{transactionId} | 
[**retrieve_template19**](SavingsAccountTransactionsApi.md#retrieve_template19) | **GET** /v1/savingsaccounts/{savingsId}/transactions/template | 
[**search_transactions**](SavingsAccountTransactionsApi.md#search_transactions) | **GET** /v1/savingsaccounts/{savingsId}/transactions/search | Search Savings Account Transactions
[**transaction2**](SavingsAccountTransactionsApi.md#transaction2) | **POST** /v1/savingsaccounts/{savingsId}/transactions | 

# **adjust_transaction1**
> list[PostSavingsAccountBulkReversalTransactionsRequest] adjust_transaction1(body, savings_id, transaction_id, command=command)

Undo/Reverse/Modify/Release Amount transaction API

Undo/Reverse/Modify/Release Amount transaction API  Example Requests:   savingsaccounts/{savingsId}/transactions/{transactionId}?command=reverse  Accepted command = undo, reverse, modify, releaseAmount

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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSavingsAccountBulkReversalTransactionsRequest() # PostSavingsAccountBulkReversalTransactionsRequest | 
savings_id = 789 # int | 
transaction_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    # Undo/Reverse/Modify/Release Amount transaction API
    api_response = api_instance.adjust_transaction1(body, savings_id, transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->adjust_transaction1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSavingsAccountBulkReversalTransactionsRequest**](PostSavingsAccountBulkReversalTransactionsRequest.md)|  | 
 **savings_id** | **int**|  | 
 **transaction_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**list[PostSavingsAccountBulkReversalTransactionsRequest]**](PostSavingsAccountBulkReversalTransactionsRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_query1**
> str advanced_query1(savings_id, body=body)

Advanced search Savings Account Transactions

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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
savings_id = 789 # int | savingsId
body = fineract_client.PagedLocalRequestAdvancedQueryRequest() # PagedLocalRequestAdvancedQueryRequest |  (optional)

try:
    # Advanced search Savings Account Transactions
    api_response = api_instance.advanced_query1(savings_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->advanced_query1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**| savingsId | 
 **body** | [**PagedLocalRequestAdvancedQueryRequest**](PagedLocalRequestAdvancedQueryRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one24**
> str retrieve_one24(savings_id, transaction_id)



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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
savings_id = 789 # int | 
transaction_id = 789 # int | 

try:
    api_response = api_instance.retrieve_one24(savings_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->retrieve_one24: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template19**
> str retrieve_template19(savings_id)



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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
savings_id = 789 # int | 

try:
    api_response = api_instance.retrieve_template19(savings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->retrieve_template19: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> SavingsAccountTransactionsSearchResponse search_transactions(savings_id, from_date=from_date, to_date=to_date, from_submitted_date=from_submitted_date, to_submitted_date=to_submitted_date, from_amount=from_amount, to_amount=to_amount, types=types, credit=credit, debit=debit, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format)

Search Savings Account Transactions

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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
savings_id = 789 # int | savings account id
from_date = 'from_date_example' # str | minimum value date (inclusive) (optional)
to_date = 'to_date_example' # str | maximum value date (inclusive) (optional)
from_submitted_date = 'from_submitted_date_example' # str | minimum booking date (inclusive) (optional)
to_submitted_date = 'to_submitted_date_example' # str | maximum booking date (inclusive) (optional)
from_amount = 1.2 # float | minimum transaction amount (inclusive) (optional)
to_amount = 1.2 # float | maximum transaction amount (inclusive) (optional)
types = 'types_example' # str | transaction types (optional)
credit = true # bool | credit (optional)
debit = true # bool | debit (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | sort properties (optional)
sort_order = 'sort_order_example' # str | sort direction (optional)
locale = 'locale_example' # str | locale (optional)
date_format = 'date_format_example' # str | date format (optional)

try:
    # Search Savings Account Transactions
    api_response = api_instance.search_transactions(savings_id, from_date=from_date, to_date=to_date, from_submitted_date=from_submitted_date, to_submitted_date=to_submitted_date, from_amount=from_amount, to_amount=to_amount, types=types, credit=credit, debit=debit, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->search_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**| savings account id | 
 **from_date** | **str**| minimum value date (inclusive) | [optional] 
 **to_date** | **str**| maximum value date (inclusive) | [optional] 
 **from_submitted_date** | **str**| minimum booking date (inclusive) | [optional] 
 **to_submitted_date** | **str**| maximum booking date (inclusive) | [optional] 
 **from_amount** | **float**| minimum transaction amount (inclusive) | [optional] 
 **to_amount** | **float**| maximum transaction amount (inclusive) | [optional] 
 **types** | **str**| transaction types | [optional] 
 **credit** | **bool**| credit | [optional] 
 **debit** | **bool**| debit | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| sort properties | [optional] 
 **sort_order** | **str**| sort direction | [optional] 
 **locale** | **str**| locale | [optional] 
 **date_format** | **str**| date format | [optional] 

### Return type

[**SavingsAccountTransactionsSearchResponse**](SavingsAccountTransactionsSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction2**
> PostSavingsAccountTransactionsResponse transaction2(body, savings_id, command=command)



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
api_instance = fineract_client.SavingsAccountTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSavingsAccountTransactionsRequest() # PostSavingsAccountTransactionsRequest | 
savings_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.transaction2(body, savings_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsAccountTransactionsApi->transaction2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSavingsAccountTransactionsRequest**](PostSavingsAccountTransactionsRequest.md)|  | 
 **savings_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**PostSavingsAccountTransactionsResponse**](PostSavingsAccountTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

