# fineract_client.ClientsAddressApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_address**](ClientsAddressApi.md#add_client_address) | **POST** /v1/client/{clientid}/addresses | Create an address for a Client
[**get_addresses1**](ClientsAddressApi.md#get_addresses1) | **GET** /v1/client/{clientid}/addresses | List all addresses for a Client
[**get_addresses_template**](ClientsAddressApi.md#get_addresses_template) | **GET** /v1/client/addresses/template | 
[**update_client_address**](ClientsAddressApi.md#update_client_address) | **PUT** /v1/client/{clientid}/addresses | Update an address for a Client

# **add_client_address**
> PostClientClientIdAddressesResponse add_client_address(body, clientid, type=type)

Create an address for a Client

Mandatory Fields :  type and clientId

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
api_instance = fineract_client.ClientsAddressApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostClientClientIdAddressesRequest() # PostClientClientIdAddressesRequest | 
clientid = 789 # int | clientId
type = 789 # int | type (optional)

try:
    # Create an address for a Client
    api_response = api_instance.add_client_address(body, clientid, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsAddressApi->add_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostClientClientIdAddressesRequest**](PostClientClientIdAddressesRequest.md)|  | 
 **clientid** | **int**| clientId | 
 **type** | **int**| type | [optional] 

### Return type

[**PostClientClientIdAddressesResponse**](PostClientClientIdAddressesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresses1**
> list[GetClientClientIdAddressesResponse] get_addresses1(clientid, status=status, type=type)

List all addresses for a Client

Example Requests:  client/1/addresses   clients/1/addresses?status=false,true&&type=1,2,3

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
api_instance = fineract_client.ClientsAddressApi(fineract_client.ApiClient(configuration))
clientid = 789 # int | clientId
status = 'status_example' # str | status (optional)
type = 789 # int | type (optional)

try:
    # List all addresses for a Client
    api_response = api_instance.get_addresses1(clientid, status=status, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsAddressApi->get_addresses1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **int**| clientId | 
 **status** | **str**| status | [optional] 
 **type** | **int**| type | [optional] 

### Return type

[**list[GetClientClientIdAddressesResponse]**](GetClientClientIdAddressesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresses_template**
> str get_addresses_template()



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
api_instance = fineract_client.ClientsAddressApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.get_addresses_template()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_address**
> PutClientClientIdAddressesResponse update_client_address(body, clientid)

Update an address for a Client

All the address fields can be updated by using update client address API  Mandatory Fields type and addressId

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
api_instance = fineract_client.ClientsAddressApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutClientClientIdAddressesRequest() # PutClientClientIdAddressesRequest | 
clientid = 789 # int | clientId

try:
    # Update an address for a Client
    api_response = api_instance.update_client_address(body, clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsAddressApi->update_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutClientClientIdAddressesRequest**](PutClientClientIdAddressesRequest.md)|  | 
 **clientid** | **int**| clientId | 

### Return type

[**PutClientClientIdAddressesResponse**](PutClientClientIdAddressesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

