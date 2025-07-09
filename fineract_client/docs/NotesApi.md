# fineract_client.NotesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_note**](NotesApi.md#add_new_note) | **POST** /v1/{resourceType}/{resourceId}/notes | Add a Resource Note
[**delete_note**](NotesApi.md#delete_note) | **DELETE** /v1/{resourceType}/{resourceId}/notes/{noteId} | Delete a Resource Note
[**retrieve_note**](NotesApi.md#retrieve_note) | **GET** /v1/{resourceType}/{resourceId}/notes/{noteId} | Retrieve a Resource Note
[**retrieve_notes_by_resource**](NotesApi.md#retrieve_notes_by_resource) | **GET** /v1/{resourceType}/{resourceId}/notes | Retrieve a Resource&#39;s description
[**update_note**](NotesApi.md#update_note) | **PUT** /v1/{resourceType}/{resourceId}/notes/{noteId} | Update a Resource Note


# **add_new_note**
> PostResourceTypeResourceIdNotesResponse add_new_note(resource_type, resource_id, post_resource_type_resource_id_notes_request)

Add a Resource Note

Adds a new note to a supported resource.

Example Requests:

clients/1/notes


groups/1/notes

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_resource_type_resource_id_notes_request import PostResourceTypeResourceIdNotesRequest
from fineract_client.models.post_resource_type_resource_id_notes_response import PostResourceTypeResourceIdNotesResponse
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
    api_instance = fineract_client.NotesApi(api_client)
    resource_type = 'resource_type_example' # str | resourceType
    resource_id = 56 # int | resourceId
    post_resource_type_resource_id_notes_request = fineract_client.PostResourceTypeResourceIdNotesRequest() # PostResourceTypeResourceIdNotesRequest | 

    try:
        # Add a Resource Note
        api_response = api_instance.add_new_note(resource_type, resource_id, post_resource_type_resource_id_notes_request)
        print("The response of NotesApi->add_new_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->add_new_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 
 **post_resource_type_resource_id_notes_request** | [**PostResourceTypeResourceIdNotesRequest**](PostResourceTypeResourceIdNotesRequest.md)|  | 

### Return type

[**PostResourceTypeResourceIdNotesResponse**](PostResourceTypeResourceIdNotesResponse.md)

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

# **delete_note**
> DeleteResourceTypeResourceIdNotesNoteIdResponse delete_note(resource_type, resource_id, note_id)

Delete a Resource Note

Deletes a Resource Note

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_resource_type_resource_id_notes_note_id_response import DeleteResourceTypeResourceIdNotesNoteIdResponse
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
    api_instance = fineract_client.NotesApi(api_client)
    resource_type = 'resource_type_example' # str | resourceType
    resource_id = 56 # int | resourceId
    note_id = 56 # int | noteId

    try:
        # Delete a Resource Note
        api_response = api_instance.delete_note(resource_type, resource_id, note_id)
        print("The response of NotesApi->delete_note:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_note**
> GetResourceTypeResourceIdNotesNoteIdResponse retrieve_note(resource_type, resource_id, note_id)

Retrieve a Resource Note

Retrieves a Resource Note

Example Requests:

clients/1/notes/76


groups/1/notes/20


clients/1/notes/76?fields=note,createdOn,createdByUsername


groups/1/notes/20?fields=note,createdOn,createdByUsername

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_resource_type_resource_id_notes_note_id_response import GetResourceTypeResourceIdNotesNoteIdResponse
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
    api_instance = fineract_client.NotesApi(api_client)
    resource_type = 'resource_type_example' # str | resourceType
    resource_id = 56 # int | resourceId
    note_id = 56 # int | noteId

    try:
        # Retrieve a Resource Note
        api_response = api_instance.retrieve_note(resource_type, resource_id, note_id)
        print("The response of NotesApi->retrieve_note:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_notes_by_resource**
> List[GetResourceTypeResourceIdNotesResponse] retrieve_notes_by_resource(resource_type, resource_id)

Retrieve a Resource's description

Retrieves a Resource's Notes

Note: Notes are returned in descending createOn order.

Example Requests:

clients/2/notes


groups/2/notes?fields=note,createdOn,createdByUsername

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_resource_type_resource_id_notes_response import GetResourceTypeResourceIdNotesResponse
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
    api_instance = fineract_client.NotesApi(api_client)
    resource_type = 'resource_type_example' # str | resourceType
    resource_id = 56 # int | resourceId

    try:
        # Retrieve a Resource's description
        api_response = api_instance.retrieve_notes_by_resource(resource_type, resource_id)
        print("The response of NotesApi->retrieve_notes_by_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->retrieve_notes_by_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 

### Return type

[**List[GetResourceTypeResourceIdNotesResponse]**](GetResourceTypeResourceIdNotesResponse.md)

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

# **update_note**
> PutResourceTypeResourceIdNotesNoteIdResponse update_note(resource_type, resource_id, note_id, put_resource_type_resource_id_notes_note_id_request)

Update a Resource Note

Updates a Resource Note

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_resource_type_resource_id_notes_note_id_request import PutResourceTypeResourceIdNotesNoteIdRequest
from fineract_client.models.put_resource_type_resource_id_notes_note_id_response import PutResourceTypeResourceIdNotesNoteIdResponse
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
    api_instance = fineract_client.NotesApi(api_client)
    resource_type = 'resource_type_example' # str | resourceType
    resource_id = 56 # int | resourceId
    note_id = 56 # int | noteId
    put_resource_type_resource_id_notes_note_id_request = fineract_client.PutResourceTypeResourceIdNotesNoteIdRequest() # PutResourceTypeResourceIdNotesNoteIdRequest | 

    try:
        # Update a Resource Note
        api_response = api_instance.update_note(resource_type, resource_id, note_id, put_resource_type_resource_id_notes_note_id_request)
        print("The response of NotesApi->update_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->update_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **resource_id** | **int**| resourceId | 
 **note_id** | **int**| noteId | 
 **put_resource_type_resource_id_notes_note_id_request** | [**PutResourceTypeResourceIdNotesNoteIdRequest**](PutResourceTypeResourceIdNotesNoteIdRequest.md)|  | 

### Return type

[**PutResourceTypeResourceIdNotesNoteIdResponse**](PutResourceTypeResourceIdNotesNoteIdResponse.md)

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

