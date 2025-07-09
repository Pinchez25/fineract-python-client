# fineract_client.UserGeneratedDocumentsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

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
> PostTemplatesResponse create_template(post_templates_request)

Add a UGD

Adds a new UGD.  Mandatory Fields name    Example Requests:  templates/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_templates_request import PostTemplatesRequest
from fineract_client.models.post_templates_response import PostTemplatesResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    post_templates_request = fineract_client.PostTemplatesRequest() # PostTemplatesRequest | 

    try:
        # Add a UGD
        api_response = api_instance.create_template(post_templates_request)
        print("The response of UserGeneratedDocumentsApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGeneratedDocumentsApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_templates_request** | [**PostTemplatesRequest**](PostTemplatesRequest.md)|  | 

### Return type

[**PostTemplatesResponse**](PostTemplatesResponse.md)

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

# **delete_template**
> DeleteTemplatesTemplateIdResponse delete_template(template_id)

Delete a UGD

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_templates_template_id_response import DeleteTemplatesTemplateIdResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    template_id = 56 # int | templateId

    try:
        # Delete a UGD
        api_response = api_instance.delete_template(template_id)
        print("The response of UserGeneratedDocumentsApi->delete_template:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_by_template**
> str get_template_by_template(template_id)



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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    template_id = 56 # int | 

    try:
        api_response = api_instance.get_template_by_template(template_id)
        print("The response of UserGeneratedDocumentsApi->get_template_by_template:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_template**
> str merge_template(template_id, body=body)



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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    template_id = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.merge_template(template_id, body=body)
        print("The response of UserGeneratedDocumentsApi->merge_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGeneratedDocumentsApi->merge_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all40**
> GetTemplatesResponse retrieve_all40(type_id=type_id, entity_id=entity_id)

Retrieve all UGDs

Example Requests:  templates  It is also possible to get specific UGDs by entity and type:  templates?type=0&entity=0 [Entity: Id]      client: 0, loan: 1  [Type: Id]    Document: 0, E-Mail (not yet): 1,  SMS: 2

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_templates_response import GetTemplatesResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    type_id = -1 # int | typeId (optional) (default to -1)
    entity_id = -1 # int | entityId (optional) (default to -1)

    try:
        # Retrieve all UGDs
        api_response = api_instance.retrieve_all40(type_id=type_id, entity_id=entity_id)
        print("The response of UserGeneratedDocumentsApi->retrieve_all40:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one30**
> GetTemplatesTemplateIdResponse retrieve_one30(template_id)

Retrieve a UGD

Example Requests:  templates/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_templates_template_id_response import GetTemplatesTemplateIdResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    template_id = 56 # int | templateId

    try:
        # Retrieve a UGD
        api_response = api_instance.retrieve_one30(template_id)
        print("The response of UserGeneratedDocumentsApi->retrieve_one30:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_template**
> PutTemplatesTemplateIdResponse save_template(template_id, put_templates_template_id_request)

Update a UGD

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_templates_template_id_request import PutTemplatesTemplateIdRequest
from fineract_client.models.put_templates_template_id_response import PutTemplatesTemplateIdResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)
    template_id = 56 # int | templateId
    put_templates_template_id_request = fineract_client.PutTemplatesTemplateIdRequest() # PutTemplatesTemplateIdRequest | 

    try:
        # Update a UGD
        api_response = api_instance.save_template(template_id, put_templates_template_id_request)
        print("The response of UserGeneratedDocumentsApi->save_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGeneratedDocumentsApi->save_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| templateId | 
 **put_templates_template_id_request** | [**PutTemplatesTemplateIdRequest**](PutTemplatesTemplateIdRequest.md)|  | 

### Return type

[**PutTemplatesTemplateIdResponse**](PutTemplatesTemplateIdResponse.md)

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

# **template20**
> GetTemplatesTemplateResponse template20()

Retrieve UGD Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for UGDs. The UGD data returned consists of any or all of:  ARGUMENTS name String entity String type String text String optional mappers Mapper optional Example Request:  templates/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_templates_template_response import GetTemplatesTemplateResponse
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
    api_instance = fineract_client.UserGeneratedDocumentsApi(api_client)

    try:
        # Retrieve UGD Details Template
        api_response = api_instance.template20()
        print("The response of UserGeneratedDocumentsApi->template20:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

