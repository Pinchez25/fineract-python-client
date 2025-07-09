# fineract_client.CodeValuesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code_value**](CodeValuesApi.md#create_code_value) | **POST** /v1/codes/{codeId}/codevalues | Create a Code description
[**delete_code_value**](CodeValuesApi.md#delete_code_value) | **DELETE** /v1/codes/{codeId}/codevalues/{codeValueId} | Delete a Code description
[**retrieve_all_code_values**](CodeValuesApi.md#retrieve_all_code_values) | **GET** /v1/codes/{codeId}/codevalues | List Code Values
[**retrieve_code_value**](CodeValuesApi.md#retrieve_code_value) | **GET** /v1/codes/{codeId}/codevalues/{codeValueId} | Retrieve a Code description
[**update_code_value**](CodeValuesApi.md#update_code_value) | **PUT** /v1/codes/{codeId}/codevalues/{codeValueId} | Update a Code description


# **create_code_value**
> PostCodeValueDataResponse create_code_value(code_id, post_code_values_data_request)

Create a Code description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_code_value_data_response import PostCodeValueDataResponse
from fineract_client.models.post_code_values_data_request import PostCodeValuesDataRequest
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
    api_instance = fineract_client.CodeValuesApi(api_client)
    code_id = 56 # int | codeId
    post_code_values_data_request = fineract_client.PostCodeValuesDataRequest() # PostCodeValuesDataRequest | 

    try:
        # Create a Code description
        api_response = api_instance.create_code_value(code_id, post_code_values_data_request)
        print("The response of CodeValuesApi->create_code_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeValuesApi->create_code_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 
 **post_code_values_data_request** | [**PostCodeValuesDataRequest**](PostCodeValuesDataRequest.md)|  | 

### Return type

[**PostCodeValueDataResponse**](PostCodeValueDataResponse.md)

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

# **delete_code_value**
> DeleteCodeValueDataResponse delete_code_value(code_id, code_value_id)

Delete a Code description

Deletes a code description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_code_value_data_response import DeleteCodeValueDataResponse
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
    api_instance = fineract_client.CodeValuesApi(api_client)
    code_id = 56 # int | codeId
    code_value_id = 56 # int | codeValueId

    try:
        # Delete a Code description
        api_response = api_instance.delete_code_value(code_id, code_value_id)
        print("The response of CodeValuesApi->delete_code_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeValuesApi->delete_code_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 
 **code_value_id** | **int**| codeValueId | 

### Return type

[**DeleteCodeValueDataResponse**](DeleteCodeValueDataResponse.md)

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

# **retrieve_all_code_values**
> List[GetCodeValuesDataResponse] retrieve_all_code_values(code_id)

List Code Values

Returns the list of Code Values for a given Code

Example Requests:

codes/1/codevalues

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_code_values_data_response import GetCodeValuesDataResponse
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
    api_instance = fineract_client.CodeValuesApi(api_client)
    code_id = 56 # int | codeId

    try:
        # List Code Values
        api_response = api_instance.retrieve_all_code_values(code_id)
        print("The response of CodeValuesApi->retrieve_all_code_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeValuesApi->retrieve_all_code_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 

### Return type

[**List[GetCodeValuesDataResponse]**](GetCodeValuesDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A List of code values for a given code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_code_value**
> GetCodeValuesDataResponse retrieve_code_value(code_value_id, code_id)

Retrieve a Code description

Returns the details of a Code Value

Example Requests:

codes/1/codevalues/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_code_values_data_response import GetCodeValuesDataResponse
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
    api_instance = fineract_client.CodeValuesApi(api_client)
    code_value_id = 56 # int | codeValueId
    code_id = 56 # int | codeId

    try:
        # Retrieve a Code description
        api_response = api_instance.retrieve_code_value(code_value_id, code_id)
        print("The response of CodeValuesApi->retrieve_code_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeValuesApi->retrieve_code_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_value_id** | **int**| codeValueId | 
 **code_id** | **int**| codeId | 

### Return type

[**GetCodeValuesDataResponse**](GetCodeValuesDataResponse.md)

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

# **update_code_value**
> PutCodeValueDataResponse update_code_value(code_id, code_value_id, put_code_values_data_request)

Update a Code description

Updates the details of a code description.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_code_value_data_response import PutCodeValueDataResponse
from fineract_client.models.put_code_values_data_request import PutCodeValuesDataRequest
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
    api_instance = fineract_client.CodeValuesApi(api_client)
    code_id = 56 # int | codeId
    code_value_id = 56 # int | codeValueId
    put_code_values_data_request = fineract_client.PutCodeValuesDataRequest() # PutCodeValuesDataRequest | 

    try:
        # Update a Code description
        api_response = api_instance.update_code_value(code_id, code_value_id, put_code_values_data_request)
        print("The response of CodeValuesApi->update_code_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeValuesApi->update_code_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 
 **code_value_id** | **int**| codeValueId | 
 **put_code_values_data_request** | [**PutCodeValuesDataRequest**](PutCodeValuesDataRequest.md)|  | 

### Return type

[**PutCodeValueDataResponse**](PutCodeValueDataResponse.md)

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

