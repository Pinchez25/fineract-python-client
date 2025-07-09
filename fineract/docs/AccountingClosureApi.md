# fineract_client.AccountingClosureApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_closure**](AccountingClosureApi.md#create_gl_closure) | **POST** /v1/glclosures | Create an Accounting Closure
[**delete_gl_closure**](AccountingClosureApi.md#delete_gl_closure) | **DELETE** /v1/glclosures/{glClosureId} | Delete an accounting closure
[**retreive_closure**](AccountingClosureApi.md#retreive_closure) | **GET** /v1/glclosures/{glClosureId} | Retrieve an Accounting Closure
[**retrieve_all_closures**](AccountingClosureApi.md#retrieve_all_closures) | **GET** /v1/glclosures | List Accounting closures
[**update_gl_closure**](AccountingClosureApi.md#update_gl_closure) | **PUT** /v1/glclosures/{glClosureId} | Update an Accounting closure


# **create_gl_closure**
> PostGlClosuresResponse create_gl_closure(post_gl_closures_request)

Create an Accounting Closure

Mandatory Fields officeId,closingDate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_gl_closures_request import PostGlClosuresRequest
from fineract_client.models.post_gl_closures_response import PostGlClosuresResponse
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
    api_instance = fineract_client.AccountingClosureApi(api_client)
    post_gl_closures_request = fineract_client.PostGlClosuresRequest() # PostGlClosuresRequest | 

    try:
        # Create an Accounting Closure
        api_response = api_instance.create_gl_closure(post_gl_closures_request)
        print("The response of AccountingClosureApi->create_gl_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingClosureApi->create_gl_closure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_gl_closures_request** | [**PostGlClosuresRequest**](PostGlClosuresRequest.md)|  | 

### Return type

[**PostGlClosuresResponse**](PostGlClosuresResponse.md)

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

# **delete_gl_closure**
> DeleteGlClosuresResponse delete_gl_closure(gl_closure_id)

Delete an accounting closure

Note: Only the latest accounting closure associated with a branch may be deleted.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_gl_closures_response import DeleteGlClosuresResponse
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
    api_instance = fineract_client.AccountingClosureApi(api_client)
    gl_closure_id = 56 # int | glclosureId

    try:
        # Delete an accounting closure
        api_response = api_instance.delete_gl_closure(gl_closure_id)
        print("The response of AccountingClosureApi->delete_gl_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingClosureApi->delete_gl_closure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glclosureId | 

### Return type

[**DeleteGlClosuresResponse**](DeleteGlClosuresResponse.md)

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

# **retreive_closure**
> GetGlClosureResponse retreive_closure(gl_closure_id)

Retrieve an Accounting Closure

Example Requests:  glclosures/1   /glclosures/1?fields=officeName,closingDate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_gl_closure_response import GetGlClosureResponse
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
    api_instance = fineract_client.AccountingClosureApi(api_client)
    gl_closure_id = 56 # int | glClosureId

    try:
        # Retrieve an Accounting Closure
        api_response = api_instance.retreive_closure(gl_closure_id)
        print("The response of AccountingClosureApi->retreive_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingClosureApi->retreive_closure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glClosureId | 

### Return type

[**GetGlClosureResponse**](GetGlClosureResponse.md)

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

# **retrieve_all_closures**
> List[GetGlClosureResponse] retrieve_all_closures(office_id=office_id)

List Accounting closures

Example Requests:  glclosures

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_gl_closure_response import GetGlClosureResponse
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
    api_instance = fineract_client.AccountingClosureApi(api_client)
    office_id = 56 # int |  (optional)

    try:
        # List Accounting closures
        api_response = api_instance.retrieve_all_closures(office_id=office_id)
        print("The response of AccountingClosureApi->retrieve_all_closures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingClosureApi->retrieve_all_closures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 

### Return type

[**List[GetGlClosureResponse]**](GetGlClosureResponse.md)

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

# **update_gl_closure**
> PutGlClosuresResponse update_gl_closure(gl_closure_id, put_gl_closures_request=put_gl_closures_request)

Update an Accounting closure

Once an accounting closure is created, only the comments associated with it may be edited

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_gl_closures_request import PutGlClosuresRequest
from fineract_client.models.put_gl_closures_response import PutGlClosuresResponse
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
    api_instance = fineract_client.AccountingClosureApi(api_client)
    gl_closure_id = 56 # int | glClosureId
    put_gl_closures_request = fineract_client.PutGlClosuresRequest() # PutGlClosuresRequest |  (optional)

    try:
        # Update an Accounting closure
        api_response = api_instance.update_gl_closure(gl_closure_id, put_gl_closures_request=put_gl_closures_request)
        print("The response of AccountingClosureApi->update_gl_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingClosureApi->update_gl_closure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glClosureId | 
 **put_gl_closures_request** | [**PutGlClosuresRequest**](PutGlClosuresRequest.md)|  | [optional] 

### Return type

[**PutGlClosuresResponse**](PutGlClosuresResponse.md)

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

