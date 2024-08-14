# fineract_client.NotesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_note**](NotesApi.md#add_new_note) | **POST** /v1/{resourceType}/{resourceId}/notes | Add a Resource Note
[**delete_note**](NotesApi.md#delete_note) | **DELETE** /v1/{resourceType}/{resourceId}/notes/{noteId} | Delete a Resource Note
[**retrieve_note**](NotesApi.md#retrieve_note) | **GET** /v1/{resourceType}/{resourceId}/notes/{noteId} | Retrieve a Resource Note
[**retrieve_notes_by_resource**](NotesApi.md#retrieve_notes_by_resource) | **GET** /v1/{resourceType}/{resourceId}/notes | Retrieve a Resource&#x27;s description
[**update_note**](NotesApi.md#update_note) | **PUT** /v1/{resourceType}/{resourceId}/notes/{noteId} | Update a Resource Note

# **add_new_note**
> PostResourceTypeResourceIdNotesResponse add_new_note(body, resource_type, resource_id)

Add a Resource Note

Adds a new note to a supported resource.  Example Requests:  clients/1/notes   groups/1/notes

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
api_instance = fineract_client.NotesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostResourceTypeResourceIdNotesRequest() # PostResourceTypeResourceIdNotesRequest | 
resource_type = 'resource_type_example' # str | resourceType
resource_id = 789 # int | resourceId

try:
    # Add a Resource Note
    api_response = api_instance.add_new_note(body, resource_type, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->add_new_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostResourceTypeResourceIdNotesRequest**](PostResourceTypeResourceIdNotesRequest.md)|  | 
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 

### Return type

[**PostResourceTypeResourceIdNotesResponse**](PostResourceTypeResourceIdNotesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> DeleteResourceTypeResourceIdNotesNoteIdResponse delete_note(resource_type, resource_id, note_id)

Delete a Resource Note

Deletes a Resource Note

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
api_instance = fineract_client.NotesApi(fineract_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | resourceType
resource_id = 789 # int | resourceId
note_id = 789 # int | noteId

try:
    # Delete a Resource Note
    api_response = api_instance.delete_note(resource_type, resource_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 
 **note_id** | **int**| noteId | 

### Return type

[**DeleteResourceTypeResourceIdNotesNoteIdResponse**](DeleteResourceTypeResourceIdNotesNoteIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_note**
> GetResourceTypeResourceIdNotesNoteIdResponse retrieve_note(resource_type, resource_id, note_id)

Retrieve a Resource Note

Retrieves a Resource Note  Example Requests:  clients/1/notes/76   groups/1/notes/20   clients/1/notes/76?fields=note,createdOn,createdByUsername   groups/1/notes/20?fields=note,createdOn,createdByUsername

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
api_instance = fineract_client.NotesApi(fineract_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | resourceType
resource_id = 789 # int | resourceId
note_id = 789 # int | noteId

try:
    # Retrieve a Resource Note
    api_response = api_instance.retrieve_note(resource_type, resource_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->retrieve_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 
 **note_id** | **int**| noteId | 

### Return type

[**GetResourceTypeResourceIdNotesNoteIdResponse**](GetResourceTypeResourceIdNotesNoteIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_notes_by_resource**
> list[GetResourceTypeResourceIdNotesResponse] retrieve_notes_by_resource(resource_type, resource_id)

Retrieve a Resource's description

Retrieves a Resource's Notes  Note: Notes are returned in descending createOn order.  Example Requests:  clients/2/notes   groups/2/notes?fields=note,createdOn,createdByUsername

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
api_instance = fineract_client.NotesApi(fineract_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | resourceType
resource_id = 789 # int | resourceId

try:
    # Retrieve a Resource's description
    api_response = api_instance.retrieve_notes_by_resource(resource_type, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->retrieve_notes_by_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 

### Return type

[**list[GetResourceTypeResourceIdNotesResponse]**](GetResourceTypeResourceIdNotesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note**
> PutResourceTypeResourceIdNotesNoteIdResponse update_note(body, resource_type, resource_id, note_id)

Update a Resource Note

Updates a Resource Note

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
api_instance = fineract_client.NotesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutResourceTypeResourceIdNotesNoteIdRequest() # PutResourceTypeResourceIdNotesNoteIdRequest | 
resource_type = 'resource_type_example' # str | resourceType
resource_id = 789 # int | resourceId
note_id = 789 # int | noteId

try:
    # Update a Resource Note
    api_response = api_instance.update_note(body, resource_type, resource_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutResourceTypeResourceIdNotesNoteIdRequest**](PutResourceTypeResourceIdNotesNoteIdRequest.md)|  | 
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 
 **note_id** | **int**| noteId | 

### Return type

[**PutResourceTypeResourceIdNotesNoteIdResponse**](PutResourceTypeResourceIdNotesNoteIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

