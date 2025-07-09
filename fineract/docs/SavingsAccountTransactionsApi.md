# fineract_client.SavingsAccountTransactionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_transaction1**](SavingsAccountTransactionsApi.md#adjust_transaction1) | **POST** /v1/savingsaccounts/{savingsId}/transactions/{transactionId} | Undo/Reverse/Modify/Release Amount transaction API
[**advanced_query1**](SavingsAccountTransactionsApi.md#advanced_query1) | **POST** /v1/savingsaccounts/{savingsId}/transactions/query | Advanced search Savings Account Transactions
[**retrieve_one24**](SavingsAccountTransactionsApi.md#retrieve_one24) | **GET** /v1/savingsaccounts/{savingsId}/transactions/{transactionId} | 
[**retrieve_template19**](SavingsAccountTransactionsApi.md#retrieve_template19) | **GET** /v1/savingsaccounts/{savingsId}/transactions/template | 
[**search_transactions**](SavingsAccountTransactionsApi.md#search_transactions) | **GET** /v1/savingsaccounts/{savingsId}/transactions/search | Search Savings Account Transactions
[**transaction2**](SavingsAccountTransactionsApi.md#transaction2) | **POST** /v1/savingsaccounts/{savingsId}/transactions | 


# **adjust_transaction1**
> List[PostSavingsAccountBulkReversalTransactionsRequest] adjust_transaction1(savings_id, transaction_id, post_savings_account_bulk_reversal_transactions_request, command=command)

Undo/Reverse/Modify/Release Amount transaction API

Undo/Reverse/Modify/Release Amount transaction API

Example Requests:


savingsaccounts/{savingsId}/transactions/{transactionId}?command=reverse

Accepted command = undo, reverse, modify, releaseAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_account_bulk_reversal_transactions_request import PostSavingsAccountBulkReversalTransactionsRequest
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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | 
    transaction_id = 56 # int | 
    post_savings_account_bulk_reversal_transactions_request = fineract_client.PostSavingsAccountBulkReversalTransactionsRequest() # PostSavingsAccountBulkReversalTransactionsRequest | 
    command = 'command_example' # str |  (optional)

    try:
        # Undo/Reverse/Modify/Release Amount transaction API
        api_response = api_instance.adjust_transaction1(savings_id, transaction_id, post_savings_account_bulk_reversal_transactions_request, command=command)
        print("The response of SavingsAccountTransactionsApi->adjust_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountTransactionsApi->adjust_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**|  | 
 **transaction_id** | **int**|  | 
 **post_savings_account_bulk_reversal_transactions_request** | [**PostSavingsAccountBulkReversalTransactionsRequest**](PostSavingsAccountBulkReversalTransactionsRequest.md)|  | 
 **command** | **str**|  | [optional] 

### Return type

[**List[PostSavingsAccountBulkReversalTransactionsRequest]**](PostSavingsAccountBulkReversalTransactionsRequest.md)

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

# **advanced_query1**
> str advanced_query1(savings_id, paged_local_request_advanced_query_request=paged_local_request_advanced_query_request)

Advanced search Savings Account Transactions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.paged_local_request_advanced_query_request import PagedLocalRequestAdvancedQueryRequest
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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | savingsId
    paged_local_request_advanced_query_request = fineract_client.PagedLocalRequestAdvancedQueryRequest() # PagedLocalRequestAdvancedQueryRequest |  (optional)

    try:
        # Advanced search Savings Account Transactions
        api_response = api_instance.advanced_query1(savings_id, paged_local_request_advanced_query_request=paged_local_request_advanced_query_request)
        print("The response of SavingsAccountTransactionsApi->advanced_query1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountTransactionsApi->advanced_query1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**| savingsId | 
 **paged_local_request_advanced_query_request** | [**PagedLocalRequestAdvancedQueryRequest**](PagedLocalRequestAdvancedQueryRequest.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one24**
> str retrieve_one24(savings_id, transaction_id)

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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_one24(savings_id, transaction_id)
        print("The response of SavingsAccountTransactionsApi->retrieve_one24:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template19**
> str retrieve_template19(savings_id)

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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_template19(savings_id)
        print("The response of SavingsAccountTransactionsApi->retrieve_template19:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> SavingsAccountTransactionsSearchResponse search_transactions(savings_id, from_date=from_date, to_date=to_date, from_submitted_date=from_submitted_date, to_submitted_date=to_submitted_date, from_amount=from_amount, to_amount=to_amount, types=types, credit=credit, debit=debit, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format)

Search Savings Account Transactions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.savings_account_transactions_search_response import SavingsAccountTransactionsSearchResponse
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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | savings account id
    from_date = '2023-08-08' # str | minimum value date (inclusive) (optional)
    to_date = '2023-08-15' # str | maximum value date (inclusive) (optional)
    from_submitted_date = '2023-08-08' # str | minimum booking date (inclusive) (optional)
    to_submitted_date = '2023-08-15' # str | maximum booking date (inclusive) (optional)
    from_amount = 1000 # float | minimum transaction amount (inclusive) (optional)
    to_amount = 50000000 # float | maximum transaction amount (inclusive) (optional)
    types = '1,2,4,20,21' # str | transaction types (optional)
    credit = True # bool | credit (optional)
    debit = True # bool | debit (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'createdDate,transactionDate,id' # str | sort properties (optional)
    sort_order = 'sort_order_example' # str | sort direction (optional)
    locale = 'locale_example' # str | locale (optional)
    date_format = 'yyyy-MM-dd' # str | date format (optional)

    try:
        # Search Savings Account Transactions
        api_response = api_instance.search_transactions(savings_id, from_date=from_date, to_date=to_date, from_submitted_date=from_submitted_date, to_submitted_date=to_submitted_date, from_amount=from_amount, to_amount=to_amount, types=types, credit=credit, debit=debit, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format)
        print("The response of SavingsAccountTransactionsApi->search_transactions:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction2**
> PostSavingsAccountTransactionsResponse transaction2(savings_id, post_savings_account_transactions_request, command=command, idempotency_key=idempotency_key)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_account_transactions_request import PostSavingsAccountTransactionsRequest
from fineract_client.models.post_savings_account_transactions_response import PostSavingsAccountTransactionsResponse
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
    api_instance = fineract_client.SavingsAccountTransactionsApi(api_client)
    savings_id = 56 # int | 
    post_savings_account_transactions_request = fineract_client.PostSavingsAccountTransactionsRequest() # PostSavingsAccountTransactionsRequest | 
    command = 'command_example' # str |  (optional)
    idempotency_key = 'idempotency_key_example' # str | Optional idempotency key to prevent duplicate submissions (optional)

    try:
        api_response = api_instance.transaction2(savings_id, post_savings_account_transactions_request, command=command, idempotency_key=idempotency_key)
        print("The response of SavingsAccountTransactionsApi->transaction2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsAccountTransactionsApi->transaction2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**|  | 
 **post_savings_account_transactions_request** | [**PostSavingsAccountTransactionsRequest**](PostSavingsAccountTransactionsRequest.md)|  | 
 **command** | **str**|  | [optional] 
 **idempotency_key** | **str**| Optional idempotency key to prevent duplicate submissions | [optional] 

### Return type

[**PostSavingsAccountTransactionsResponse**](PostSavingsAccountTransactionsResponse.md)

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

