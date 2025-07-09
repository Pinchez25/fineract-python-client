# fineract_client.ClientsAddressApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_address**](ClientsAddressApi.md#add_client_address) | **POST** /v1/client/{clientid}/addresses | Create an address for a Client
[**get_addresses1**](ClientsAddressApi.md#get_addresses1) | **GET** /v1/client/{clientid}/addresses | List all addresses for a Client
[**get_addresses_template**](ClientsAddressApi.md#get_addresses_template) | **GET** /v1/client/addresses/template | 
[**update_client_address**](ClientsAddressApi.md#update_client_address) | **PUT** /v1/client/{clientid}/addresses | Update an address for a Client


# **add_client_address**
> PostClientClientIdAddressesResponse add_client_address(clientid, post_client_client_id_addresses_request, type=type)

Create an address for a Client

Mandatory Fields :  type and clientId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_client_client_id_addresses_request import PostClientClientIdAddressesRequest
from fineract_client.models.post_client_client_id_addresses_response import PostClientClientIdAddressesResponse
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
    api_instance = fineract_client.ClientsAddressApi(api_client)
    clientid = 56 # int | clientId
    post_client_client_id_addresses_request = fineract_client.PostClientClientIdAddressesRequest() # PostClientClientIdAddressesRequest | 
    type = 56 # int | type (optional)

    try:
        # Create an address for a Client
        api_response = api_instance.add_client_address(clientid, post_client_client_id_addresses_request, type=type)
        print("The response of ClientsAddressApi->add_client_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsAddressApi->add_client_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| clientId | 
 **post_client_client_id_addresses_request** | [**PostClientClientIdAddressesRequest**](PostClientClientIdAddressesRequest.md)|  | 
 **type** | **int**| type | [optional] 

### Return type

[**PostClientClientIdAddressesResponse**](PostClientClientIdAddressesResponse.md)

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

# **get_addresses1**
> List[GetClientClientIdAddressesResponse] get_addresses1(clientid, status=status, type=type)

List all addresses for a Client

Example Requests:  client/1/addresses   clients/1/addresses?status=false,true&&type=1,2,3

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_client_client_id_addresses_response import GetClientClientIdAddressesResponse
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
    api_instance = fineract_client.ClientsAddressApi(api_client)
    clientid = 56 # int | clientId
    status = 'status_example' # str | status (optional)
    type = 56 # int | type (optional)

    try:
        # List all addresses for a Client
        api_response = api_instance.get_addresses1(clientid, status=status, type=type)
        print("The response of ClientsAddressApi->get_addresses1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsAddressApi->get_addresses1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| clientId | 
 **status** | **str**| status | [optional] 
 **type** | **int**| type | [optional] 

### Return type

[**List[GetClientClientIdAddressesResponse]**](GetClientClientIdAddressesResponse.md)

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

# **get_addresses_template**
> str get_addresses_template()



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
    api_instance = fineract_client.ClientsAddressApi(api_client)

    try:
        api_response = api_instance.get_addresses_template()
        print("The response of ClientsAddressApi->get_addresses_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsAddressApi->get_addresses_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **update_client_address**
> PutClientClientIdAddressesResponse update_client_address(clientid, put_client_client_id_addresses_request)

Update an address for a Client

All the address fields can be updated by using update client address API  Mandatory Fields type and addressId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_client_client_id_addresses_request import PutClientClientIdAddressesRequest
from fineract_client.models.put_client_client_id_addresses_response import PutClientClientIdAddressesResponse
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
    api_instance = fineract_client.ClientsAddressApi(api_client)
    clientid = 56 # int | clientId
    put_client_client_id_addresses_request = fineract_client.PutClientClientIdAddressesRequest() # PutClientClientIdAddressesRequest | 

    try:
        # Update an address for a Client
        api_response = api_instance.update_client_address(clientid, put_client_client_id_addresses_request)
        print("The response of ClientsAddressApi->update_client_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsAddressApi->update_client_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| clientId | 
 **put_client_client_id_addresses_request** | [**PutClientClientIdAddressesRequest**](PutClientClientIdAddressesRequest.md)|  | 

### Return type

[**PutClientClientIdAddressesResponse**](PutClientClientIdAddressesResponse.md)

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

