# fineract_client.SelfClientApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_client_image2**](SelfClientApi.md#add_new_client_image2) | **POST** /v1/self/clients/{clientId}/images | 
[**delete_client_image1**](SelfClientApi.md#delete_client_image1) | **DELETE** /v1/self/clients/{clientId}/images | 
[**retrieve_all36**](SelfClientApi.md#retrieve_all36) | **GET** /v1/self/clients | List Clients associated to the user
[**retrieve_all_client_charges1**](SelfClientApi.md#retrieve_all_client_charges1) | **GET** /v1/self/clients/{clientId}/charges | List Client Charges
[**retrieve_all_client_transactions2**](SelfClientApi.md#retrieve_all_client_transactions2) | **GET** /v1/self/clients/{clientId}/transactions | List Client Transactions
[**retrieve_associated_accounts2**](SelfClientApi.md#retrieve_associated_accounts2) | **GET** /v1/self/clients/{clientId}/accounts | Retrieve client accounts overview
[**retrieve_client_charge1**](SelfClientApi.md#retrieve_client_charge1) | **GET** /v1/self/clients/{clientId}/charges/{chargeId} | Retrieve a Client Charge
[**retrieve_client_transaction4**](SelfClientApi.md#retrieve_client_transaction4) | **GET** /v1/self/clients/{clientId}/transactions/{transactionId} | Retrieve a Client Transaction
[**retrieve_image1**](SelfClientApi.md#retrieve_image1) | **GET** /v1/self/clients/{clientId}/images | Retrieve Client Image
[**retrieve_obligee_details2**](SelfClientApi.md#retrieve_obligee_details2) | **GET** /v1/self/clients/{clientId}/obligeedetails | 
[**retrieve_one28**](SelfClientApi.md#retrieve_one28) | **GET** /v1/self/clients/{clientId} | Retrieve a Client


# **add_new_client_image2**
> str add_new_client_image2(client_id, content_length=content_length, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | 
    content_length = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.add_new_client_image2(client_id, content_length=content_length, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of SelfClientApi->add_new_client_image2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->add_new_client_image2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **content_length** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_image1**
> str delete_client_image1(client_id)



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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | 

    try:
        api_response = api_instance.delete_client_image1(client_id)
        print("The response of SelfClientApi->delete_client_image1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->delete_client_image1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

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

# **retrieve_all36**
> GetSelfClientsResponse retrieve_all36(display_name=display_name, first_name=first_name, last_name=last_name, offset=offset, status=status, limit=limit, order_by=order_by, sort_order=sort_order)

List Clients associated to the user

The list capability of clients can support pagination and sorting.  Example Requests:  self/clients  self/clients?fields=displayName,officeName  self/clients?offset=10&limit=50  self/clients?orderBy=displayName&sortOrder=DESC

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_response import GetSelfClientsResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    display_name = 'display_name_example' # str | displayName (optional)
    first_name = 'first_name_example' # str | firstName (optional)
    last_name = 'last_name_example' # str | lastName (optional)
    offset = 56 # int | offset (optional)
    status = 'status_example' # str | status (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # List Clients associated to the user
        api_response = api_instance.retrieve_all36(display_name=display_name, first_name=first_name, last_name=last_name, offset=offset, status=status, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of SelfClientApi->retrieve_all36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_all36: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| displayName | [optional] 
 **first_name** | **str**| firstName | [optional] 
 **last_name** | **str**| lastName | [optional] 
 **offset** | **int**| offset | [optional] 
 **status** | **str**| status | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetSelfClientsResponse**](GetSelfClientsResponse.md)

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

# **retrieve_all_client_charges1**
> GetSelfClientsClientIdChargesResponse retrieve_all_client_charges1(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)

List Client Charges

The list capability of client charges supports pagination.  Example Requests:  self/clients/1/charges  self/clients/1/charges?offset=0&limit=5

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_charges_response import GetSelfClientsClientIdChargesResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')
    pending_payment = True # bool | pendingPayment (optional)
    limit = 56 # int | limit (optional)
    offset = 56 # int | offset (optional)

    try:
        # List Client Charges
        api_response = api_instance.retrieve_all_client_charges1(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)
        print("The response of SelfClientApi->retrieve_all_client_charges1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_all_client_charges1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]
 **pending_payment** | **bool**| pendingPayment | [optional] 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**GetSelfClientsClientIdChargesResponse**](GetSelfClientsClientIdChargesResponse.md)

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

# **retrieve_all_client_transactions2**
> GetSelfClientsClientIdTransactionsResponse retrieve_all_client_transactions2(client_id, offset=offset, limit=limit)

List Client Transactions

The list capability of client transaction can support pagination.  Example Requests:  self/clients/189/transactions  self/clients/189/transactions?offset=10&limit=50

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_transactions_response import GetSelfClientsClientIdTransactionsResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List Client Transactions
        api_response = api_instance.retrieve_all_client_transactions2(client_id, offset=offset, limit=limit)
        print("The response of SelfClientApi->retrieve_all_client_transactions2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_all_client_transactions2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**GetSelfClientsClientIdTransactionsResponse**](GetSelfClientsClientIdTransactionsResponse.md)

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

# **retrieve_associated_accounts2**
> GetSelfClientsClientIdAccountsResponse retrieve_associated_accounts2(client_id)

Retrieve client accounts overview

An example of how a loan portfolio summary can be provided. This is requested in a specific use case of the community application. It is quite reasonable to add resources like this to simplify User Interface development.  Example Requests:  self/clients/1/accounts   self/clients/1/accounts?fields=loanAccounts,savingsAccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_accounts_response import GetSelfClientsClientIdAccountsResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId

    try:
        # Retrieve client accounts overview
        api_response = api_instance.retrieve_associated_accounts2(client_id)
        print("The response of SelfClientApi->retrieve_associated_accounts2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_associated_accounts2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**GetSelfClientsClientIdAccountsResponse**](GetSelfClientsClientIdAccountsResponse.md)

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

# **retrieve_client_charge1**
> GetSelfClientsClientIdChargesChargeIdResponse retrieve_client_charge1(client_id, charge_id)

Retrieve a Client Charge

Retrieves a Client Charge  Example Requests:  self/clients/1/charges/1   self/clients/1/charges/1?fields=name,id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_charges_charge_id_response import GetSelfClientsClientIdChargesChargeIdResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId
    charge_id = 56 # int | chargeId

    try:
        # Retrieve a Client Charge
        api_response = api_instance.retrieve_client_charge1(client_id, charge_id)
        print("The response of SelfClientApi->retrieve_client_charge1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_client_charge1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_id** | **int**| chargeId | 

### Return type

[**GetSelfClientsClientIdChargesChargeIdResponse**](GetSelfClientsClientIdChargesChargeIdResponse.md)

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

# **retrieve_client_transaction4**
> GetSelfClientsClientIdTransactionsTransactionIdResponse retrieve_client_transaction4(client_id, transaction_id)

Retrieve a Client Transaction

Retrieves a Client TransactionExample Requests:  self/clients/1/transactions/1   self/clients/1/transactions/1?fields=id,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_transactions_transaction_id_response import GetSelfClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId
    transaction_id = 56 # int | transactionId

    try:
        # Retrieve a Client Transaction
        api_response = api_instance.retrieve_client_transaction4(client_id, transaction_id)
        print("The response of SelfClientApi->retrieve_client_transaction4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_client_transaction4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**GetSelfClientsClientIdTransactionsTransactionIdResponse**](GetSelfClientsClientIdTransactionsTransactionIdResponse.md)

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

# **retrieve_image1**
> retrieve_image1(client_id, max_width=max_width, max_height=max_height, output=output)

Retrieve Client Image

Optional arguments are identical to those of Get Image associated with an Entity (Binary file)  Example Requests:  self/clients/1/images

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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId
    max_width = maxWidth # int |  (optional)
    max_height = maxHeight # int |  (optional)
    output = 'output' # str |  (optional)

    try:
        # Retrieve Client Image
        api_instance.retrieve_image1(client_id, max_width=max_width, max_height=max_height, output=output)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_image1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **max_width** | **int**|  | [optional] 
 **max_height** | **int**|  | [optional] 
 **output** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_obligee_details2**
> str retrieve_obligee_details2(client_id)



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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_obligee_details2(client_id)
        print("The response of SelfClientApi->retrieve_obligee_details2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_obligee_details2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

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

# **retrieve_one28**
> GetSelfClientsClientIdResponse retrieve_one28(client_id)

Retrieve a Client

Retrieves a Client  Example Requests:  self/clients/1  self/clients/1?fields=id,displayName,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_clients_client_id_response import GetSelfClientsClientIdResponse
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
    api_instance = fineract_client.SelfClientApi(api_client)
    client_id = 56 # int | clientId

    try:
        # Retrieve a Client
        api_response = api_instance.retrieve_one28(client_id)
        print("The response of SelfClientApi->retrieve_one28:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfClientApi->retrieve_one28: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**GetSelfClientsClientIdResponse**](GetSelfClientsClientIdResponse.md)

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

