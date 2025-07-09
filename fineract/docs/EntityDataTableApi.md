# fineract_client.EntityDataTableApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_datatable_check**](EntityDataTableApi.md#create_entity_datatable_check) | **POST** /v1/entityDatatableChecks | Create Entity-Datatable Checks
[**delete_datatable1**](EntityDataTableApi.md#delete_datatable1) | **DELETE** /v1/entityDatatableChecks/{entityDatatableCheckId} | Delete Entity-Datatable Checks
[**get_template**](EntityDataTableApi.md#get_template) | **GET** /v1/entityDatatableChecks/template | Retrieve Entity-Datatable Checks Template
[**retrieve_all6**](EntityDataTableApi.md#retrieve_all6) | **GET** /v1/entityDatatableChecks | List Entity-Datatable Checks


# **create_entity_datatable_check**
> PostEntityDatatableChecksTemplateResponse create_entity_datatable_check(post_entity_datatable_checks_template_request)

Create Entity-Datatable Checks

Mandatory Fields : 
entity, status, datatableName

Non-Mandatory Fields : 
productId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_entity_datatable_checks_template_request import PostEntityDatatableChecksTemplateRequest
from fineract_client.models.post_entity_datatable_checks_template_response import PostEntityDatatableChecksTemplateResponse
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
    api_instance = fineract_client.EntityDataTableApi(api_client)
    post_entity_datatable_checks_template_request = fineract_client.PostEntityDatatableChecksTemplateRequest() # PostEntityDatatableChecksTemplateRequest | 

    try:
        # Create Entity-Datatable Checks
        api_response = api_instance.create_entity_datatable_check(post_entity_datatable_checks_template_request)
        print("The response of EntityDataTableApi->create_entity_datatable_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityDataTableApi->create_entity_datatable_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_entity_datatable_checks_template_request** | [**PostEntityDatatableChecksTemplateRequest**](PostEntityDatatableChecksTemplateRequest.md)|  | 

### Return type

[**PostEntityDatatableChecksTemplateResponse**](PostEntityDatatableChecksTemplateResponse.md)

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

# **delete_datatable1**
> DeleteEntityDatatableChecksTemplateResponse delete_datatable1(entity_datatable_check_id, body=body)

Delete Entity-Datatable Checks

Deletes an existing Entity-Datatable Check

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_entity_datatable_checks_template_response import DeleteEntityDatatableChecksTemplateResponse
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
    api_instance = fineract_client.EntityDataTableApi(api_client)
    entity_datatable_check_id = 56 # int | entityDatatableCheckId
    body = 'body_example' # str |  (optional)

    try:
        # Delete Entity-Datatable Checks
        api_response = api_instance.delete_datatable1(entity_datatable_check_id, body=body)
        print("The response of EntityDataTableApi->delete_datatable1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityDataTableApi->delete_datatable1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_datatable_check_id** | **int**| entityDatatableCheckId | 
 **body** | **str**|  | [optional] 

### Return type

[**DeleteEntityDatatableChecksTemplateResponse**](DeleteEntityDatatableChecksTemplateResponse.md)

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

# **get_template**
> GetEntityDatatableChecksTemplateResponse get_template()

Retrieve Entity-Datatable Checks Template

This is a convenience resource useful for building maintenance user interface screens for Entity-Datatable Checks applications. The template data returned consists of:

Allowed description Lists
Example Request:

entityDatatableChecks/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_entity_datatable_checks_template_response import GetEntityDatatableChecksTemplateResponse
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
    api_instance = fineract_client.EntityDataTableApi(api_client)

    try:
        # Retrieve Entity-Datatable Checks Template
        api_response = api_instance.get_template()
        print("The response of EntityDataTableApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityDataTableApi->get_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetEntityDatatableChecksTemplateResponse**](GetEntityDatatableChecksTemplateResponse.md)

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

# **retrieve_all6**
> List[GetEntityDatatableChecksResponse] retrieve_all6(status=status, entity=entity, product_id=product_id, offset=offset, limit=limit)

List Entity-Datatable Checks

The list capability of Entity-Datatable Checks can support pagination.

OPTIONAL ARGUMENTS
offset Integer optional, defaults to 0 Indicates the result from which pagination startslimit Integer optional, defaults to 200 Restricts the size of results returned. To override the default and return all entries you must explicitly pass a non-positive integer value for limit e.g. limit=0, or limit=-1
Example Request:

entityDatatableChecks?offset=0&limit=15

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_entity_datatable_checks_response import GetEntityDatatableChecksResponse
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
    api_instance = fineract_client.EntityDataTableApi(api_client)
    status = 56 # int | status (optional)
    entity = 'entity_example' # str | entity (optional)
    product_id = 56 # int | productId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List Entity-Datatable Checks
        api_response = api_instance.retrieve_all6(status=status, entity=entity, product_id=product_id, offset=offset, limit=limit)
        print("The response of EntityDataTableApi->retrieve_all6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityDataTableApi->retrieve_all6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| status | [optional] 
 **entity** | **str**| entity | [optional] 
 **product_id** | **int**| productId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**List[GetEntityDatatableChecksResponse]**](GetEntityDatatableChecksResponse.md)

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

