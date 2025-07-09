# fineract_client.ClientIdentifierApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_identifier**](ClientIdentifierApi.md#create_client_identifier) | **POST** /v1/clients/{clientId}/identifiers | Create an Identifier for a Client
[**delete_client_identifier**](ClientIdentifierApi.md#delete_client_identifier) | **DELETE** /v1/clients/{clientId}/identifiers/{identifierId} | Delete a Client Identifier
[**new_client_identifier_details**](ClientIdentifierApi.md#new_client_identifier_details) | **GET** /v1/clients/{clientId}/identifiers/template | Retrieve Client Identifier Details Template
[**retrieve_all_client_identifiers**](ClientIdentifierApi.md#retrieve_all_client_identifiers) | **GET** /v1/clients/{clientId}/identifiers | List all Identifiers for a Client
[**retrieve_client_identifiers**](ClientIdentifierApi.md#retrieve_client_identifiers) | **GET** /v1/clients/{clientId}/identifiers/{identifierId} | Retrieve a Client Identifier
[**update_client_identifer**](ClientIdentifierApi.md#update_client_identifer) | **PUT** /v1/clients/{clientId}/identifiers/{identifierId} | Update a Client Identifier


# **create_client_identifier**
> PostClientsClientIdIdentifiersResponse create_client_identifier(client_id, post_clients_client_id_identifiers_request)

Create an Identifier for a Client

Mandatory Fields
documentKey, documentTypeId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_identifiers_request import PostClientsClientIdIdentifiersRequest
from fineract_client.models.post_clients_client_id_identifiers_response import PostClientsClientIdIdentifiersResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId
    post_clients_client_id_identifiers_request = fineract_client.PostClientsClientIdIdentifiersRequest() # PostClientsClientIdIdentifiersRequest | 

    try:
        # Create an Identifier for a Client
        api_response = api_instance.create_client_identifier(client_id, post_clients_client_id_identifiers_request)
        print("The response of ClientIdentifierApi->create_client_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->create_client_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **post_clients_client_id_identifiers_request** | [**PostClientsClientIdIdentifiersRequest**](PostClientsClientIdIdentifiersRequest.md)|  | 

### Return type

[**PostClientsClientIdIdentifiersResponse**](PostClientsClientIdIdentifiersResponse.md)

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

# **delete_client_identifier**
> DeleteClientsClientIdIdentifiersIdentifierIdResponse delete_client_identifier(client_id, identifier_id)

Delete a Client Identifier

Deletes a Client Identifier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_clients_client_id_identifiers_identifier_id_response import DeleteClientsClientIdIdentifiersIdentifierIdResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId
    identifier_id = 56 # int | identifierId

    try:
        # Delete a Client Identifier
        api_response = api_instance.delete_client_identifier(client_id, identifier_id)
        print("The response of ClientIdentifierApi->delete_client_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->delete_client_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **identifier_id** | **int**| identifierId | 

### Return type

[**DeleteClientsClientIdIdentifiersIdentifierIdResponse**](DeleteClientsClientIdIdentifiersIdentifierIdResponse.md)

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

# **new_client_identifier_details**
> GetClientsClientIdIdentifiersTemplateResponse new_client_identifier_details(client_id)

Retrieve Client Identifier Details Template

This is a convenience resource useful for building maintenance user interface screens for client applications. The template data returned consists of any or all of:

 Field Defaults
 Allowed description Lists


Example Request:
clients/1/identifiers/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_identifiers_template_response import GetClientsClientIdIdentifiersTemplateResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId

    try:
        # Retrieve Client Identifier Details Template
        api_response = api_instance.new_client_identifier_details(client_id)
        print("The response of ClientIdentifierApi->new_client_identifier_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->new_client_identifier_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**GetClientsClientIdIdentifiersTemplateResponse**](GetClientsClientIdIdentifiersTemplateResponse.md)

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

# **retrieve_all_client_identifiers**
> List[GetClientsClientIdIdentifiersResponse] retrieve_all_client_identifiers(client_id)

List all Identifiers for a Client

Example Requests:
clients/1/identifiers


clients/1/identifiers?fields=documentKey,documentType,description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_identifiers_response import GetClientsClientIdIdentifiersResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId

    try:
        # List all Identifiers for a Client
        api_response = api_instance.retrieve_all_client_identifiers(client_id)
        print("The response of ClientIdentifierApi->retrieve_all_client_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->retrieve_all_client_identifiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**List[GetClientsClientIdIdentifiersResponse]**](GetClientsClientIdIdentifiersResponse.md)

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

# **retrieve_client_identifiers**
> GetClientsClientIdIdentifiersResponse retrieve_client_identifiers(client_id, identifier_id)

Retrieve a Client Identifier

Example Requests:
clients/1/identifier/2


clients/1/identifier/2?template=true

clients/1/identifiers/2?fields=documentKey,documentType,description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_identifiers_response import GetClientsClientIdIdentifiersResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId
    identifier_id = 56 # int | identifierId

    try:
        # Retrieve a Client Identifier
        api_response = api_instance.retrieve_client_identifiers(client_id, identifier_id)
        print("The response of ClientIdentifierApi->retrieve_client_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->retrieve_client_identifiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **identifier_id** | **int**| identifierId | 

### Return type

[**GetClientsClientIdIdentifiersResponse**](GetClientsClientIdIdentifiersResponse.md)

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

# **update_client_identifer**
> PutClientsClientIdIdentifiersIdentifierIdResponse update_client_identifer(client_id, identifier_id, put_clients_client_id_identifiers_identifier_id_request)

Update a Client Identifier

Updates a Client Identifier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_clients_client_id_identifiers_identifier_id_request import PutClientsClientIdIdentifiersIdentifierIdRequest
from fineract_client.models.put_clients_client_id_identifiers_identifier_id_response import PutClientsClientIdIdentifiersIdentifierIdResponse
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
    api_instance = fineract_client.ClientIdentifierApi(api_client)
    client_id = 56 # int | clientId
    identifier_id = 56 # int | identifierId
    put_clients_client_id_identifiers_identifier_id_request = fineract_client.PutClientsClientIdIdentifiersIdentifierIdRequest() # PutClientsClientIdIdentifiersIdentifierIdRequest | 

    try:
        # Update a Client Identifier
        api_response = api_instance.update_client_identifer(client_id, identifier_id, put_clients_client_id_identifiers_identifier_id_request)
        print("The response of ClientIdentifierApi->update_client_identifer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientIdentifierApi->update_client_identifer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **identifier_id** | **int**| identifierId | 
 **put_clients_client_id_identifiers_identifier_id_request** | [**PutClientsClientIdIdentifiersIdentifierIdRequest**](PutClientsClientIdIdentifiersIdentifierIdRequest.md)|  | 

### Return type

[**PutClientsClientIdIdentifiersIdentifierIdResponse**](PutClientsClientIdIdentifiersIdentifierIdResponse.md)

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

