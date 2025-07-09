# fineract_client.TellerCashManagementApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_cash_to_cashier**](TellerCashManagementApi.md#allocate_cash_to_cashier) | **POST** /v1/tellers/{tellerId}/cashiers/{cashierId}/allocate | Allocate Cash To Cashier
[**create_cashier**](TellerCashManagementApi.md#create_cashier) | **POST** /v1/tellers/{tellerId}/cashiers | Create Cashiers
[**create_teller**](TellerCashManagementApi.md#create_teller) | **POST** /v1/tellers | Create teller
[**delete_cashier**](TellerCashManagementApi.md#delete_cashier) | **DELETE** /v1/tellers/{tellerId}/cashiers/{cashierId} | Delete Cashier
[**delete_teller**](TellerCashManagementApi.md#delete_teller) | **DELETE** /v1/tellers/{tellerId} | 
[**find_cashier_data**](TellerCashManagementApi.md#find_cashier_data) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId} | Retrieve a cashier
[**find_teller**](TellerCashManagementApi.md#find_teller) | **GET** /v1/tellers/{tellerId} | Retrieve tellers
[**find_transaction_data**](TellerCashManagementApi.md#find_transaction_data) | **GET** /v1/tellers/{tellerId}/transactions/{transactionId} | 
[**get_cashier_data1**](TellerCashManagementApi.md#get_cashier_data1) | **GET** /v1/tellers/{tellerId}/cashiers | List Cashiers
[**get_cashier_template**](TellerCashManagementApi.md#get_cashier_template) | **GET** /v1/tellers/{tellerId}/cashiers/template | Find Cashiers
[**get_cashier_txn_template**](TellerCashManagementApi.md#get_cashier_txn_template) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/transactions/template | Retrieve Cashier Transaction Template
[**get_journal_data**](TellerCashManagementApi.md#get_journal_data) | **GET** /v1/tellers/{tellerId}/journals | 
[**get_teller_data**](TellerCashManagementApi.md#get_teller_data) | **GET** /v1/tellers | List all tellers
[**get_transaction_data**](TellerCashManagementApi.md#get_transaction_data) | **GET** /v1/tellers/{tellerId}/transactions | 
[**get_transactions_for_cashier**](TellerCashManagementApi.md#get_transactions_for_cashier) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/transactions | Retrieve Cashier Transaction
[**get_transactions_wtih_summary_for_cashier**](TellerCashManagementApi.md#get_transactions_wtih_summary_for_cashier) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/summaryandtransactions | Transactions Wtih Summary For Cashier
[**settle_cash_from_cashier**](TellerCashManagementApi.md#settle_cash_from_cashier) | **POST** /v1/tellers/{tellerId}/cashiers/{cashierId}/settle | Settle Cash From Cashier
[**update_cashier**](TellerCashManagementApi.md#update_cashier) | **PUT** /v1/tellers/{tellerId}/cashiers/{cashierId} | Update Cashier
[**update_teller**](TellerCashManagementApi.md#update_teller) | **PUT** /v1/tellers/{tellerId} | Update teller


# **allocate_cash_to_cashier**
> PostTellersTellerIdCashiersCashierIdAllocateResponse allocate_cash_to_cashier(teller_id, cashier_id, post_tellers_teller_id_cashiers_cashier_id_allocate_request)

Allocate Cash To Cashier

Mandatory Fields:  Date, Amount, Currency, Notes/Comments

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_tellers_teller_id_cashiers_cashier_id_allocate_request import PostTellersTellerIdCashiersCashierIdAllocateRequest
from fineract_client.models.post_tellers_teller_id_cashiers_cashier_id_allocate_response import PostTellersTellerIdCashiersCashierIdAllocateResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId
    post_tellers_teller_id_cashiers_cashier_id_allocate_request = fineract_client.PostTellersTellerIdCashiersCashierIdAllocateRequest() # PostTellersTellerIdCashiersCashierIdAllocateRequest | 

    try:
        # Allocate Cash To Cashier
        api_response = api_instance.allocate_cash_to_cashier(teller_id, cashier_id, post_tellers_teller_id_cashiers_cashier_id_allocate_request)
        print("The response of TellerCashManagementApi->allocate_cash_to_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->allocate_cash_to_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **post_tellers_teller_id_cashiers_cashier_id_allocate_request** | [**PostTellersTellerIdCashiersCashierIdAllocateRequest**](PostTellersTellerIdCashiersCashierIdAllocateRequest.md)|  | 

### Return type

[**PostTellersTellerIdCashiersCashierIdAllocateResponse**](PostTellersTellerIdCashiersCashierIdAllocateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json, text/html
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cashier**
> PostTellersTellerIdCashiersResponse create_cashier(teller_id, post_tellers_teller_id_cashiers_request)

Create Cashiers

Mandatory Fields:  Cashier/staff, Fromm Date, To Date, Full Day or From time and To time    Optional Fields:  Description/Notes

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_tellers_teller_id_cashiers_request import PostTellersTellerIdCashiersRequest
from fineract_client.models.post_tellers_teller_id_cashiers_response import PostTellersTellerIdCashiersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    post_tellers_teller_id_cashiers_request = fineract_client.PostTellersTellerIdCashiersRequest() # PostTellersTellerIdCashiersRequest | 

    try:
        # Create Cashiers
        api_response = api_instance.create_cashier(teller_id, post_tellers_teller_id_cashiers_request)
        print("The response of TellerCashManagementApi->create_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->create_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **post_tellers_teller_id_cashiers_request** | [**PostTellersTellerIdCashiersRequest**](PostTellersTellerIdCashiersRequest.md)|  | 

### Return type

[**PostTellersTellerIdCashiersResponse**](PostTellersTellerIdCashiersResponse.md)

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

# **create_teller**
> PostTellersResponse create_teller(post_tellers_request)

Create teller

Mandatory Fields Teller name, OfficeId, Description, Start Date, Status Optional Fields End Date

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_tellers_request import PostTellersRequest
from fineract_client.models.post_tellers_response import PostTellersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    post_tellers_request = fineract_client.PostTellersRequest() # PostTellersRequest | 

    try:
        # Create teller
        api_response = api_instance.create_teller(post_tellers_request)
        print("The response of TellerCashManagementApi->create_teller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->create_teller: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_tellers_request** | [**PostTellersRequest**](PostTellersRequest.md)|  | 

### Return type

[**PostTellersResponse**](PostTellersResponse.md)

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

# **delete_cashier**
> DeleteTellersTellerIdCashiersCashierIdResponse delete_cashier(teller_id, cashier_id)

Delete Cashier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_tellers_teller_id_cashiers_cashier_id_response import DeleteTellersTellerIdCashiersCashierIdResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId

    try:
        # Delete Cashier
        api_response = api_instance.delete_cashier(teller_id, cashier_id)
        print("The response of TellerCashManagementApi->delete_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->delete_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**DeleteTellersTellerIdCashiersCashierIdResponse**](DeleteTellersTellerIdCashiersCashierIdResponse.md)

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

# **delete_teller**
> str delete_teller(teller_id)



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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId

    try:
        api_response = api_instance.delete_teller(teller_id)
        print("The response of TellerCashManagementApi->delete_teller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->delete_teller: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

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

# **find_cashier_data**
> GetTellersTellerIdCashiersCashierIdResponse find_cashier_data(teller_id, cashier_id)

Retrieve a cashier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_cashier_id_response import GetTellersTellerIdCashiersCashierIdResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId

    try:
        # Retrieve a cashier
        api_response = api_instance.find_cashier_data(teller_id, cashier_id)
        print("The response of TellerCashManagementApi->find_cashier_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->find_cashier_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**GetTellersTellerIdCashiersCashierIdResponse**](GetTellersTellerIdCashiersCashierIdResponse.md)

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

# **find_teller**
> GetTellersResponse find_teller(teller_id)

Retrieve tellers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_response import GetTellersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId

    try:
        # Retrieve tellers
        api_response = api_instance.find_teller(teller_id)
        print("The response of TellerCashManagementApi->find_teller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->find_teller: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

### Return type

[**GetTellersResponse**](GetTellersResponse.md)

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

# **find_transaction_data**
> str find_transaction_data(teller_id, transaction_id)



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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    transaction_id = 56 # int | transactionId

    try:
        api_response = api_instance.find_transaction_data(teller_id, transaction_id)
        print("The response of TellerCashManagementApi->find_transaction_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->find_transaction_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **transaction_id** | **int**| transactionId | 

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

# **get_cashier_data1**
> GetTellersTellerIdCashiersResponse get_cashier_data1(teller_id, fromdate=fromdate, todate=todate)

List Cashiers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_response import GetTellersTellerIdCashiersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    fromdate = 'fromdate_example' # str | fromdate (optional)
    todate = 'todate_example' # str | todate (optional)

    try:
        # List Cashiers
        api_response = api_instance.get_cashier_data1(teller_id, fromdate=fromdate, todate=todate)
        print("The response of TellerCashManagementApi->get_cashier_data1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_cashier_data1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **fromdate** | **str**| fromdate | [optional] 
 **todate** | **str**| todate | [optional] 

### Return type

[**GetTellersTellerIdCashiersResponse**](GetTellersTellerIdCashiersResponse.md)

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

# **get_cashier_template**
> GetTellersTellerIdCashiersTemplateResponse get_cashier_template(teller_id)

Find Cashiers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_template_response import GetTellersTellerIdCashiersTemplateResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId

    try:
        # Find Cashiers
        api_response = api_instance.get_cashier_template(teller_id)
        print("The response of TellerCashManagementApi->get_cashier_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_cashier_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

### Return type

[**GetTellersTellerIdCashiersTemplateResponse**](GetTellersTellerIdCashiersTemplateResponse.md)

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

# **get_cashier_txn_template**
> GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse get_cashier_txn_template(teller_id, cashier_id)

Retrieve Cashier Transaction Template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response import GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId

    try:
        # Retrieve Cashier Transaction Template
        api_response = api_instance.get_cashier_txn_template(teller_id, cashier_id)
        print("The response of TellerCashManagementApi->get_cashier_txn_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_cashier_txn_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse**](GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse.md)

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

# **get_journal_data**
> str get_journal_data(teller_id, cashier_id=cashier_id, date_range=date_range)



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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId (optional)
    date_range = 'date_range_example' # str | dateRange (optional)

    try:
        api_response = api_instance.get_journal_data(teller_id, cashier_id=cashier_id, date_range=date_range)
        print("The response of TellerCashManagementApi->get_journal_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_journal_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | [optional] 
 **date_range** | **str**| dateRange | [optional] 

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

# **get_teller_data**
> List[GetTellersResponse] get_teller_data(office_id=office_id)

List all tellers

Retrieves list tellers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_response import GetTellersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    office_id = 56 # int | officeId (optional)

    try:
        # List all tellers
        api_response = api_instance.get_teller_data(office_id=office_id)
        print("The response of TellerCashManagementApi->get_teller_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_teller_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 

### Return type

[**List[GetTellersResponse]**](GetTellersResponse.md)

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

# **get_transaction_data**
> str get_transaction_data(teller_id, date_range=date_range)



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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    date_range = 'date_range_example' # str | dateRange (optional)

    try:
        api_response = api_instance.get_transaction_data(teller_id, date_range=date_range)
        print("The response of TellerCashManagementApi->get_transaction_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_transaction_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **date_range** | **str**| dateRange | [optional] 

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

# **get_transactions_for_cashier**
> List[GetTellersTellerIdCashiersCashiersIdTransactionsResponse] get_transactions_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Retrieve Cashier Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_transactions_response import GetTellersTellerIdCashiersCashiersIdTransactionsResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId
    currency_code = 'currency_code_example' # str | currencyCode (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # Retrieve Cashier Transaction
        api_response = api_instance.get_transactions_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of TellerCashManagementApi->get_transactions_for_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_transactions_for_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **currency_code** | **str**| currencyCode | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**List[GetTellersTellerIdCashiersCashiersIdTransactionsResponse]**](GetTellersTellerIdCashiersCashiersIdTransactionsResponse.md)

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

# **get_transactions_wtih_summary_for_cashier**
> GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse get_transactions_wtih_summary_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Transactions Wtih Summary For Cashier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response import GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId
    currency_code = 'currency_code_example' # str | currencyCode (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # Transactions Wtih Summary For Cashier
        api_response = api_instance.get_transactions_wtih_summary_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of TellerCashManagementApi->get_transactions_wtih_summary_for_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->get_transactions_wtih_summary_for_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **currency_code** | **str**| currencyCode | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse**](GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse.md)

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

# **settle_cash_from_cashier**
> PostTellersTellerIdCashiersCashierIdSettleResponse settle_cash_from_cashier(teller_id, cashier_id, post_tellers_teller_id_cashiers_cashier_id_settle_request)

Settle Cash From Cashier

Mandatory Fields Date, Amount, Currency, Notes/Comments

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_tellers_teller_id_cashiers_cashier_id_settle_request import PostTellersTellerIdCashiersCashierIdSettleRequest
from fineract_client.models.post_tellers_teller_id_cashiers_cashier_id_settle_response import PostTellersTellerIdCashiersCashierIdSettleResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId
    post_tellers_teller_id_cashiers_cashier_id_settle_request = fineract_client.PostTellersTellerIdCashiersCashierIdSettleRequest() # PostTellersTellerIdCashiersCashierIdSettleRequest | 

    try:
        # Settle Cash From Cashier
        api_response = api_instance.settle_cash_from_cashier(teller_id, cashier_id, post_tellers_teller_id_cashiers_cashier_id_settle_request)
        print("The response of TellerCashManagementApi->settle_cash_from_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->settle_cash_from_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **post_tellers_teller_id_cashiers_cashier_id_settle_request** | [**PostTellersTellerIdCashiersCashierIdSettleRequest**](PostTellersTellerIdCashiersCashierIdSettleRequest.md)|  | 

### Return type

[**PostTellersTellerIdCashiersCashierIdSettleResponse**](PostTellersTellerIdCashiersCashierIdSettleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json, text/html
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cashier**
> PutTellersTellerIdCashiersCashierIdResponse update_cashier(teller_id, cashier_id, put_tellers_teller_id_cashiers_cashier_id_request)

Update Cashier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_tellers_teller_id_cashiers_cashier_id_request import PutTellersTellerIdCashiersCashierIdRequest
from fineract_client.models.put_tellers_teller_id_cashiers_cashier_id_response import PutTellersTellerIdCashiersCashierIdResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    cashier_id = 56 # int | cashierId
    put_tellers_teller_id_cashiers_cashier_id_request = fineract_client.PutTellersTellerIdCashiersCashierIdRequest() # PutTellersTellerIdCashiersCashierIdRequest | 

    try:
        # Update Cashier
        api_response = api_instance.update_cashier(teller_id, cashier_id, put_tellers_teller_id_cashiers_cashier_id_request)
        print("The response of TellerCashManagementApi->update_cashier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->update_cashier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **put_tellers_teller_id_cashiers_cashier_id_request** | [**PutTellersTellerIdCashiersCashierIdRequest**](PutTellersTellerIdCashiersCashierIdRequest.md)|  | 

### Return type

[**PutTellersTellerIdCashiersCashierIdResponse**](PutTellersTellerIdCashiersCashierIdResponse.md)

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

# **update_teller**
> PutTellersResponse update_teller(teller_id, put_tellers_request)

Update teller

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_tellers_request import PutTellersRequest
from fineract_client.models.put_tellers_response import PutTellersResponse
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
    api_instance = fineract_client.TellerCashManagementApi(api_client)
    teller_id = 56 # int | tellerId
    put_tellers_request = fineract_client.PutTellersRequest() # PutTellersRequest | 

    try:
        # Update teller
        api_response = api_instance.update_teller(teller_id, put_tellers_request)
        print("The response of TellerCashManagementApi->update_teller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TellerCashManagementApi->update_teller: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **put_tellers_request** | [**PutTellersRequest**](PutTellersRequest.md)|  | 

### Return type

[**PutTellersResponse**](PutTellersResponse.md)

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

