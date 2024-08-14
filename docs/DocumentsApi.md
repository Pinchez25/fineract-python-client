# fineract_client.DocumentsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /v1/{entityType}/{entityId}/documents | Create a Document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /v1/{entityType}/{entityId}/documents/{documentId} | Remove a Document
[**download_file**](DocumentsApi.md#download_file) | **GET** /v1/{entityType}/{entityId}/documents/{documentId}/attachment | Retrieve Binary File associated with Document
[**get_document**](DocumentsApi.md#get_document) | **GET** /v1/{entityType}/{entityId}/documents/{documentId} | Retrieve a Document
[**retrieve_all_documents**](DocumentsApi.md#retrieve_all_documents) | **GET** /v1/{entityType}/{entityId}/documents | List documents
[**update_document**](DocumentsApi.md#update_document) | **PUT** /v1/{entityType}/{entityId}/documents/{documentId} | Update a Document

# **create_document**
> PostEntityTypeEntityIdDocumentsResponse create_document(entity_type, entity_id, date_format=date_format, description=description, locale=locale, name=name, uploaded_input_stream=uploaded_input_stream, content_length=content_length)

Create a Document

Note: A document is created using a Multi-part form upload   Body Parts  name :  Name or summary of the document  description :  Description of the document  file :  The file to be uploaded  Mandatory Fields :  file and description

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId
date_format = 'date_format_example' # str |  (optional)
description = 'description_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
name = 'name_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)
content_length = 789 # int | Content-Length (optional)

try:
    # Create a Document
    api_response = api_instance.create_document(entity_type, entity_id, date_format=date_format, description=description, locale=locale, name=name, uploaded_input_stream=uploaded_input_stream, content_length=content_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 
 **date_format** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 
 **content_length** | **int**| Content-Length | [optional] 

### Return type

[**PostEntityTypeEntityIdDocumentsResponse**](PostEntityTypeEntityIdDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> DeleteEntityTypeEntityIdDocumentsResponse delete_document(entity_type, entity_id, document_id)

Remove a Document

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId
document_id = 789 # int | documentId

try:
    # Remove a Document
    api_response = api_instance.delete_document(entity_type, entity_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 
 **document_id** | **int**| documentId | 

### Return type

[**DeleteEntityTypeEntityIdDocumentsResponse**](DeleteEntityTypeEntityIdDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file(entity_type, entity_id, document_id)

Retrieve Binary File associated with Document

Request used to download the file associated with the document  Example Requests:  clients/1/documents/1/attachment   loans/1/documents/1/attachment

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId
document_id = 789 # int | documentId

try:
    # Retrieve Binary File associated with Document
    api_instance.download_file(entity_type, entity_id, document_id)
except ApiException as e:
    print("Exception when calling DocumentsApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 
 **document_id** | **int**| documentId | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> GetEntityTypeEntityIdDocumentsResponse get_document(entity_type, entity_id, document_id)

Retrieve a Document

Example Requests:  clients/1/documents/1   loans/1/documents/1   client_identifiers/1/documents/1?fields=name,description

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId
document_id = 789 # int | documentId

try:
    # Retrieve a Document
    api_response = api_instance.get_document(entity_type, entity_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 
 **document_id** | **int**| documentId | 

### Return type

[**GetEntityTypeEntityIdDocumentsResponse**](GetEntityTypeEntityIdDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_documents**
> list[GetEntityTypeEntityIdDocumentsResponse] retrieve_all_documents(entity_type, entity_id)

List documents

Example Requests:  clients/1/documents  client_identifiers/1/documents  loans/1/documents?fields=name,description

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId

try:
    # List documents
    api_response = api_instance.retrieve_all_documents(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->retrieve_all_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 

### Return type

[**list[GetEntityTypeEntityIdDocumentsResponse]**](GetEntityTypeEntityIdDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> PutEntityTypeEntityIdDocumentsResponse update_document(entity_type, entity_id, document_id, date_format=date_format, description=description, locale=locale, name=name, uploaded_input_stream=uploaded_input_stream, content_length=content_length)

Update a Document

Note: A document is updated using a Multi-part form upload  Body Parts name Name or summary of the document description Description of the document file The file to be uploaded

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
api_instance = fineract_client.DocumentsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 789 # int | entityId
document_id = 789 # int | documentId
date_format = 'date_format_example' # str |  (optional)
description = 'description_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
name = 'name_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)
content_length = 789 # int | Content-Length (optional)

try:
    # Update a Document
    api_response = api_instance.update_document(entity_type, entity_id, document_id, date_format=date_format, description=description, locale=locale, name=name, uploaded_input_stream=uploaded_input_stream, content_length=content_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **int**| entityId | 
 **document_id** | **int**| documentId | 
 **date_format** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 
 **content_length** | **int**| Content-Length | [optional] 

### Return type

[**PutEntityTypeEntityIdDocumentsResponse**](PutEntityTypeEntityIdDocumentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

