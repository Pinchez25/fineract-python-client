# fineract_client.UserGeneratedDocumentsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](UserGeneratedDocumentsApi.md#create_template) | **POST** /v1/templates | Add a UGD
[**delete_template**](UserGeneratedDocumentsApi.md#delete_template) | **DELETE** /v1/templates/{templateId} | Delete a UGD
[**get_template_by_template**](UserGeneratedDocumentsApi.md#get_template_by_template) | **GET** /v1/templates/{templateId}/template | 
[**merge_template**](UserGeneratedDocumentsApi.md#merge_template) | **POST** /v1/templates/{templateId} | 
[**retrieve_all40**](UserGeneratedDocumentsApi.md#retrieve_all40) | **GET** /v1/templates | Retrieve all UGDs
[**retrieve_one30**](UserGeneratedDocumentsApi.md#retrieve_one30) | **GET** /v1/templates/{templateId} | Retrieve a UGD
[**save_template**](UserGeneratedDocumentsApi.md#save_template) | **PUT** /v1/templates/{templateId} | Update a UGD
[**template20**](UserGeneratedDocumentsApi.md#template20) | **GET** /v1/templates/template | Retrieve UGD Details Template

# **create_template**
> PostTemplatesResponse create_template(body)

Add a UGD

Adds a new UGD.  Mandatory Fields name    Example Requests:  templates/1

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTemplatesRequest() # PostTemplatesRequest | 

try:
    # Add a UGD
    api_response = api_instance.create_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTemplatesRequest**](PostTemplatesRequest.md)|  | 

### Return type

[**PostTemplatesResponse**](PostTemplatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> DeleteTemplatesTemplateIdResponse delete_template(template_id)

Delete a UGD

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
template_id = 789 # int | templateId

try:
    # Delete a UGD
    api_response = api_instance.delete_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| templateId | 

### Return type

[**DeleteTemplatesTemplateIdResponse**](DeleteTemplatesTemplateIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_by_template**
> str get_template_by_template(template_id)



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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
template_id = 789 # int | 

try:
    api_response = api_instance.get_template_by_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->get_template_by_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_template**
> str merge_template(template_id, body=body)



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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
template_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.merge_template(template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->merge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all40**
> GetTemplatesResponse retrieve_all40(type_id=type_id, entity_id=entity_id)

Retrieve all UGDs

Example Requests:  templates  It is also possible to get specific UGDs by entity and type:  templates?type=0&entity=0 [Entity: Id]      client: 0, loan: 1  [Type: Id]    Document: 0, E-Mail (not yet): 1,  SMS: 2

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
type_id = -1 # int | typeId (optional) (default to -1)
entity_id = -1 # int | entityId (optional) (default to -1)

try:
    # Retrieve all UGDs
    api_response = api_instance.retrieve_all40(type_id=type_id, entity_id=entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->retrieve_all40: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **int**| typeId | [optional] [default to -1]
 **entity_id** | **int**| entityId | [optional] [default to -1]

### Return type

[**GetTemplatesResponse**](GetTemplatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one30**
> GetTemplatesTemplateIdResponse retrieve_one30(template_id)

Retrieve a UGD

Example Requests:  templates/1

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
template_id = 789 # int | templateId

try:
    # Retrieve a UGD
    api_response = api_instance.retrieve_one30(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->retrieve_one30: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| templateId | 

### Return type

[**GetTemplatesTemplateIdResponse**](GetTemplatesTemplateIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_template**
> PutTemplatesTemplateIdResponse save_template(body, template_id)

Update a UGD

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutTemplatesTemplateIdRequest() # PutTemplatesTemplateIdRequest | 
template_id = 789 # int | templateId

try:
    # Update a UGD
    api_response = api_instance.save_template(body, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->save_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutTemplatesTemplateIdRequest**](PutTemplatesTemplateIdRequest.md)|  | 
 **template_id** | **int**| templateId | 

### Return type

[**PutTemplatesTemplateIdResponse**](PutTemplatesTemplateIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template20**
> GetTemplatesTemplateResponse template20()

Retrieve UGD Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for UGDs. The UGD data returned consists of any or all of:  ARGUMENTS name String entity String type String text String optional mappers Mapper optional Example Request:  templates/template

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
api_instance = fineract_client.UserGeneratedDocumentsApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve UGD Details Template
    api_response = api_instance.template20()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGeneratedDocumentsApi->template20: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTemplatesTemplateResponse**](GetTemplatesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

