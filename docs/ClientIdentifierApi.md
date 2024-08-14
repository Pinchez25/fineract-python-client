# fineract_client.ClientIdentifierApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_identifier**](ClientIdentifierApi.md#create_client_identifier) | **POST** /v1/clients/{clientId}/identifiers | Create an Identifier for a Client
[**delete_client_identifier**](ClientIdentifierApi.md#delete_client_identifier) | **DELETE** /v1/clients/{clientId}/identifiers/{identifierId} | Delete a Client Identifier
[**new_client_identifier_details**](ClientIdentifierApi.md#new_client_identifier_details) | **GET** /v1/clients/{clientId}/identifiers/template | Retrieve Client Identifier Details Template
[**retrieve_all_client_identifiers**](ClientIdentifierApi.md#retrieve_all_client_identifiers) | **GET** /v1/clients/{clientId}/identifiers | List all Identifiers for a Client
[**retrieve_client_identifiers**](ClientIdentifierApi.md#retrieve_client_identifiers) | **GET** /v1/clients/{clientId}/identifiers/{identifierId} | Retrieve a Client Identifier
[**update_client_identifer**](ClientIdentifierApi.md#update_client_identifer) | **PUT** /v1/clients/{clientId}/identifiers/{identifierId} | Update a Client Identifier

# **create_client_identifier**
> PostClientsClientIdIdentifiersResponse create_client_identifier(body, client_id)

Create an Identifier for a Client

Mandatory Fields documentKey, documentTypeId 

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostClientsClientIdIdentifiersRequest() # PostClientsClientIdIdentifiersRequest | 
client_id = 789 # int | clientId

try:
    # Create an Identifier for a Client
    api_response = api_instance.create_client_identifier(body, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientIdentifierApi->create_client_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostClientsClientIdIdentifiersRequest**](PostClientsClientIdIdentifiersRequest.md)|  | 
 **client_id** | **int**| clientId | 

### Return type

[**PostClientsClientIdIdentifiersResponse**](PostClientsClientIdIdentifiersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_identifier**
> DeleteClientsClientIdIdentifiersIdentifierIdResponse delete_client_identifier(client_id, identifier_id)

Delete a Client Identifier

Deletes a Client Identifier

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
identifier_id = 789 # int | identifierId

try:
    # Delete a Client Identifier
    api_response = api_instance.delete_client_identifier(client_id, identifier_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_client_identifier_details**
> GetClientsClientIdIdentifiersTemplateResponse new_client_identifier_details(client_id)

Retrieve Client Identifier Details Template

This is a convenience resource useful for building maintenance user interface screens for client applications. The template data returned consists of any or all of:   Field Defaults  Allowed description Lists   Example Request: clients/1/identifiers/template

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId

try:
    # Retrieve Client Identifier Details Template
    api_response = api_instance.new_client_identifier_details(client_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_client_identifiers**
> list[GetClientsClientIdIdentifiersResponse] retrieve_all_client_identifiers(client_id)

List all Identifiers for a Client

Example Requests: clients/1/identifiers   clients/1/identifiers?fields=documentKey,documentType,description

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId

try:
    # List all Identifiers for a Client
    api_response = api_instance.retrieve_all_client_identifiers(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientIdentifierApi->retrieve_all_client_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**list[GetClientsClientIdIdentifiersResponse]**](GetClientsClientIdIdentifiersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_client_identifiers**
> GetClientsClientIdIdentifiersResponse retrieve_client_identifiers(client_id, identifier_id)

Retrieve a Client Identifier

Example Requests: clients/1/identifier/2   clients/1/identifier/2?template=true  clients/1/identifiers/2?fields=documentKey,documentType,description

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
identifier_id = 789 # int | identifierId

try:
    # Retrieve a Client Identifier
    api_response = api_instance.retrieve_client_identifiers(client_id, identifier_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_identifer**
> PutClientsClientIdIdentifiersIdentifierIdResponse update_client_identifer(body, client_id, identifier_id)

Update a Client Identifier

Updates a Client Identifier

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
api_instance = fineract_client.ClientIdentifierApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutClientsClientIdIdentifiersIdentifierIdRequest() # PutClientsClientIdIdentifiersIdentifierIdRequest | 
client_id = 789 # int | clientId
identifier_id = 789 # int | identifierId

try:
    # Update a Client Identifier
    api_response = api_instance.update_client_identifer(body, client_id, identifier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientIdentifierApi->update_client_identifer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutClientsClientIdIdentifiersIdentifierIdRequest**](PutClientsClientIdIdentifiersIdentifierIdRequest.md)|  | 
 **client_id** | **int**| clientId | 
 **identifier_id** | **int**| identifierId | 

### Return type

[**PutClientsClientIdIdentifiersIdentifierIdResponse**](PutClientsClientIdIdentifiersIdentifierIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

