# fineract_client.ClientTransactionApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_client_transactions**](ClientTransactionApi.md#retrieve_all_client_transactions) | **GET** /v1/clients/{clientId}/transactions | List Client Transactions
[**retrieve_all_client_transactions1**](ClientTransactionApi.md#retrieve_all_client_transactions1) | **GET** /v1/clients/external-id/{clientExternalId}/transactions | List Client Transactions
[**retrieve_client_transaction**](ClientTransactionApi.md#retrieve_client_transaction) | **GET** /v1/clients/{clientId}/transactions/{transactionId} | Retrieve a Client Transaction
[**retrieve_client_transaction1**](ClientTransactionApi.md#retrieve_client_transaction1) | **GET** /v1/clients/{clientId}/transactions/external-id/{transactionExternalId} | Retrieve a Client Transaction
[**retrieve_client_transaction2**](ClientTransactionApi.md#retrieve_client_transaction2) | **GET** /v1/clients/external-id/{clientExternalId}/transactions/{transactionId} | Retrieve a Client Transaction
[**retrieve_client_transaction3**](ClientTransactionApi.md#retrieve_client_transaction3) | **GET** /v1/clients/external-id/{clientExternalId}/transactions/external-id/{transactionExternalId} | Retrieve a Client Transaction
[**undo_client_transaction**](ClientTransactionApi.md#undo_client_transaction) | **POST** /v1/clients/{clientId}/transactions/{transactionId} | Undo a Client Transaction
[**undo_client_transaction1**](ClientTransactionApi.md#undo_client_transaction1) | **POST** /v1/clients/{clientId}/transactions/external-id/{transactionExternalId} | Undo a Client Transaction
[**undo_client_transaction2**](ClientTransactionApi.md#undo_client_transaction2) | **POST** /v1/clients/external-id/{clientExternalId}/transactions/{transactionId} | Undo a Client Transaction
[**undo_client_transaction3**](ClientTransactionApi.md#undo_client_transaction3) | **POST** /v1/clients/external-id/{clientExternalId}/transactions/external-id/{transactionExternalId} | Undo a Client Transaction


# **retrieve_all_client_transactions**
> GetClientsClientIdTransactionsResponse retrieve_all_client_transactions(client_id, offset=offset, limit=limit)

List Client Transactions

The list capability of client transaction can support pagination.

Example Requests:

clients/189/transactions

clients/189/transactions?offset=10&limit=50

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_response import GetClientsClientIdTransactionsResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_id = 56 # int | clientId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List Client Transactions
        api_response = api_instance.retrieve_all_client_transactions(client_id, offset=offset, limit=limit)
        print("The response of ClientTransactionApi->retrieve_all_client_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_all_client_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**GetClientsClientIdTransactionsResponse**](GetClientsClientIdTransactionsResponse.md)

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

# **retrieve_all_client_transactions1**
> GetClientsClientIdTransactionsResponse retrieve_all_client_transactions1(client_external_id, offset=offset, limit=limit)

List Client Transactions

The list capability of client transaction can support pagination.

Example Requests:

clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions

clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?offset=10&limit=50

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_response import GetClientsClientIdTransactionsResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_external_id = 'client_external_id_example' # str | clientExternalId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List Client Transactions
        api_response = api_instance.retrieve_all_client_transactions1(client_external_id, offset=offset, limit=limit)
        print("The response of ClientTransactionApi->retrieve_all_client_transactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_all_client_transactions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_external_id** | **str**| clientExternalId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**GetClientsClientIdTransactionsResponse**](GetClientsClientIdTransactionsResponse.md)

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

# **retrieve_client_transaction**
> GetClientsClientIdTransactionsTransactionIdResponse retrieve_client_transaction(client_id, transaction_id)

Retrieve a Client Transaction

Example Requests:
clients/1/transactions/1


clients/1/transactions/1?fields=id,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_transaction_id_response import GetClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_id = 56 # int | clientId
    transaction_id = 56 # int | transactionId

    try:
        # Retrieve a Client Transaction
        api_response = api_instance.retrieve_client_transaction(client_id, transaction_id)
        print("The response of ClientTransactionApi->retrieve_client_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_client_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**GetClientsClientIdTransactionsTransactionIdResponse**](GetClientsClientIdTransactionsTransactionIdResponse.md)

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

# **retrieve_client_transaction1**
> GetClientsClientIdTransactionsTransactionIdResponse retrieve_client_transaction1(client_id, transaction_external_id)

Retrieve a Client Transaction

Example Requests:
clients/1/transactions/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854


clients/1/transactions/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?fields=id,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_transaction_id_response import GetClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_id = 56 # int | clientId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId

    try:
        # Retrieve a Client Transaction
        api_response = api_instance.retrieve_client_transaction1(client_id, transaction_external_id)
        print("The response of ClientTransactionApi->retrieve_client_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_client_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **transaction_external_id** | **str**| transactionExternalId | 

### Return type

[**GetClientsClientIdTransactionsTransactionIdResponse**](GetClientsClientIdTransactionsTransactionIdResponse.md)

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

# **retrieve_client_transaction2**
> GetClientsClientIdTransactionsTransactionIdResponse retrieve_client_transaction2(client_external_id, transaction_id)

Retrieve a Client Transaction

Example Requests:
clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/1


clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/1?fields=id,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_transaction_id_response import GetClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_external_id = 'client_external_id_example' # str | clientExternalId
    transaction_id = 56 # int | transactionId

    try:
        # Retrieve a Client Transaction
        api_response = api_instance.retrieve_client_transaction2(client_external_id, transaction_id)
        print("The response of ClientTransactionApi->retrieve_client_transaction2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_client_transaction2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_external_id** | **str**| clientExternalId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**GetClientsClientIdTransactionsTransactionIdResponse**](GetClientsClientIdTransactionsTransactionIdResponse.md)

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

# **retrieve_client_transaction3**
> GetClientsClientIdTransactionsTransactionIdResponse retrieve_client_transaction3(client_external_id, transaction_external_id)

Retrieve a Client Transaction

Example Requests:
clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854


clients/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?fields=id,officeName

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_transactions_transaction_id_response import GetClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_external_id = 'client_external_id_example' # str | clientExternalId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId

    try:
        # Retrieve a Client Transaction
        api_response = api_instance.retrieve_client_transaction3(client_external_id, transaction_external_id)
        print("The response of ClientTransactionApi->retrieve_client_transaction3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->retrieve_client_transaction3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_external_id** | **str**| clientExternalId | 
 **transaction_external_id** | **str**| transactionExternalId | 

### Return type

[**GetClientsClientIdTransactionsTransactionIdResponse**](GetClientsClientIdTransactionsTransactionIdResponse.md)

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

# **undo_client_transaction**
> PostClientsClientIdTransactionsTransactionIdResponse undo_client_transaction(client_id, transaction_id, command=command)

Undo a Client Transaction

Undoes a Client Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_transactions_transaction_id_response import PostClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_id = 56 # int | clientId
    transaction_id = 56 # int | transactionId
    command = 'command_example' # str | command (optional)

    try:
        # Undo a Client Transaction
        api_response = api_instance.undo_client_transaction(client_id, transaction_id, command=command)
        print("The response of ClientTransactionApi->undo_client_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->undo_client_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **transaction_id** | **int**| transactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdTransactionsTransactionIdResponse**](PostClientsClientIdTransactionsTransactionIdResponse.md)

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

# **undo_client_transaction1**
> PostClientsClientIdTransactionsTransactionIdResponse undo_client_transaction1(client_id, transaction_external_id, command=command)

Undo a Client Transaction

Undoes a Client Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_transactions_transaction_id_response import PostClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_id = 56 # int | clientId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId
    command = 'command_example' # str | command (optional)

    try:
        # Undo a Client Transaction
        api_response = api_instance.undo_client_transaction1(client_id, transaction_external_id, command=command)
        print("The response of ClientTransactionApi->undo_client_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->undo_client_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **transaction_external_id** | **str**| transactionExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdTransactionsTransactionIdResponse**](PostClientsClientIdTransactionsTransactionIdResponse.md)

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

# **undo_client_transaction2**
> PostClientsClientIdTransactionsTransactionIdResponse undo_client_transaction2(client_external_id, transaction_id, command=command)

Undo a Client Transaction

Undoes a Client Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_transactions_transaction_id_response import PostClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_external_id = 'client_external_id_example' # str | clientExternalId
    transaction_id = 56 # int | transactionId
    command = 'command_example' # str | command (optional)

    try:
        # Undo a Client Transaction
        api_response = api_instance.undo_client_transaction2(client_external_id, transaction_id, command=command)
        print("The response of ClientTransactionApi->undo_client_transaction2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->undo_client_transaction2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_external_id** | **str**| clientExternalId | 
 **transaction_id** | **int**| transactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdTransactionsTransactionIdResponse**](PostClientsClientIdTransactionsTransactionIdResponse.md)

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

# **undo_client_transaction3**
> PostClientsClientIdTransactionsTransactionIdResponse undo_client_transaction3(client_external_id, transaction_external_id, command=command)

Undo a Client Transaction

Undoes a Client Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_transactions_transaction_id_response import PostClientsClientIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.ClientTransactionApi(api_client)
    client_external_id = 'client_external_id_example' # str | clientExternalId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId
    command = 'command_example' # str | command (optional)

    try:
        # Undo a Client Transaction
        api_response = api_instance.undo_client_transaction3(client_external_id, transaction_external_id, command=command)
        print("The response of ClientTransactionApi->undo_client_transaction3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientTransactionApi->undo_client_transaction3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_external_id** | **str**| clientExternalId | 
 **transaction_external_id** | **str**| transactionExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdTransactionsTransactionIdResponse**](PostClientsClientIdTransactionsTransactionIdResponse.md)

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

