# fineract_client.FixedDepositAccountTransactionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_transaction**](FixedDepositAccountTransactionsApi.md#adjust_transaction) | **POST** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/{transactionId} | 
[**retrieve_one18**](FixedDepositAccountTransactionsApi.md#retrieve_one18) | **GET** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/{transactionId} | 
[**retrieve_template14**](FixedDepositAccountTransactionsApi.md#retrieve_template14) | **GET** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/template | 
[**transaction**](FixedDepositAccountTransactionsApi.md#transaction) | **POST** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions | 


# **adjust_transaction**
> str adjust_transaction(fixed_deposit_account_id, transaction_id, command=command, body=body)



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
    api_instance = fineract_client.FixedDepositAccountTransactionsApi(api_client)
    fixed_deposit_account_id = 56 # int | 
    transaction_id = 56 # int | 
    command = 'command_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.adjust_transaction(fixed_deposit_account_id, transaction_id, command=command, body=body)
        print("The response of FixedDepositAccountTransactionsApi->adjust_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountTransactionsApi->adjust_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 
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

# **retrieve_one18**
> str retrieve_one18(fixed_deposit_account_id, transaction_id)



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
    api_instance = fineract_client.FixedDepositAccountTransactionsApi(api_client)
    fixed_deposit_account_id = 56 # int | 
    transaction_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_one18(fixed_deposit_account_id, transaction_id)
        print("The response of FixedDepositAccountTransactionsApi->retrieve_one18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountTransactionsApi->retrieve_one18: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
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

# **retrieve_template14**
> str retrieve_template14(fixed_deposit_account_id)



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
    api_instance = fineract_client.FixedDepositAccountTransactionsApi(api_client)
    fixed_deposit_account_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_template14(fixed_deposit_account_id)
        print("The response of FixedDepositAccountTransactionsApi->retrieve_template14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountTransactionsApi->retrieve_template14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 

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

# **transaction**
> str transaction(fixed_deposit_account_id, command=command, body=body)



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
    api_instance = fineract_client.FixedDepositAccountTransactionsApi(api_client)
    fixed_deposit_account_id = 56 # int | 
    command = 'command_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.transaction(fixed_deposit_account_id, command=command, body=body)
        print("The response of FixedDepositAccountTransactionsApi->transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountTransactionsApi->transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
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

