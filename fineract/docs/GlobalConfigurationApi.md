# fineract_client.GlobalConfigurationApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_configuration**](GlobalConfigurationApi.md#retrieve_configuration) | **GET** /v1/configurations | Retrieve Global Configuration | Retrieve Global Configuration for surveys
[**retrieve_one3**](GlobalConfigurationApi.md#retrieve_one3) | **GET** /v1/configurations/{configId} | Retrieve Global Configuration
[**retrieve_one_by_name**](GlobalConfigurationApi.md#retrieve_one_by_name) | **GET** /v1/configurations/name/{name} | Retrieve Global Configuration
[**update_configuration1**](GlobalConfigurationApi.md#update_configuration1) | **PUT** /v1/configurations/{configId} | Update Global Configuration


# **retrieve_configuration**
> GetGlobalConfigurationsResponse retrieve_configuration(survey=survey)

Retrieve Global Configuration | Retrieve Global Configuration for surveys

Returns the list global enable/disable configurations.  Example Requests:  configurations   Returns the list global enable/disable survey configurations.  Example Requests:  configurations/survey

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_global_configurations_response import GetGlobalConfigurationsResponse
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
    api_instance = fineract_client.GlobalConfigurationApi(api_client)
    survey = False # bool | survey (optional) (default to False)

    try:
        # Retrieve Global Configuration | Retrieve Global Configuration for surveys
        api_response = api_instance.retrieve_configuration(survey=survey)
        print("The response of GlobalConfigurationApi->retrieve_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalConfigurationApi->retrieve_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey** | **bool**| survey | [optional] [default to False]

### Return type

[**GetGlobalConfigurationsResponse**](GetGlobalConfigurationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of example \\n response \\nsurveys response   \\ngiven below |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one3**
> GetGlobalConfigurationsResponse retrieve_one3(config_id)

Retrieve Global Configuration

Returns a global enable/disable configurations.  Example Requests:  configurations/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_global_configurations_response import GetGlobalConfigurationsResponse
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
    api_instance = fineract_client.GlobalConfigurationApi(api_client)
    config_id = 56 # int | configId

    try:
        # Retrieve Global Configuration
        api_response = api_instance.retrieve_one3(config_id)
        print("The response of GlobalConfigurationApi->retrieve_one3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalConfigurationApi->retrieve_one3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| configId | 

### Return type

[**GetGlobalConfigurationsResponse**](GetGlobalConfigurationsResponse.md)

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

# **retrieve_one_by_name**
> GlobalConfigurationPropertyData retrieve_one_by_name(name)

Retrieve Global Configuration

Returns a global enable/disable configuration.  Example Requests:  configurations/name/Enable-Address

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.global_configuration_property_data import GlobalConfigurationPropertyData
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
    api_instance = fineract_client.GlobalConfigurationApi(api_client)
    name = 'name_example' # str | name

    try:
        # Retrieve Global Configuration
        api_response = api_instance.retrieve_one_by_name(name)
        print("The response of GlobalConfigurationApi->retrieve_one_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalConfigurationApi->retrieve_one_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**GlobalConfigurationPropertyData**](GlobalConfigurationPropertyData.md)

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

# **update_configuration1**
> PutGlobalConfigurationsResponse update_configuration1(config_id, put_global_configurations_request)

Update Global Configuration

Updates an enable/disable global configuration item.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_global_configurations_request import PutGlobalConfigurationsRequest
from fineract_client.models.put_global_configurations_response import PutGlobalConfigurationsResponse
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
    api_instance = fineract_client.GlobalConfigurationApi(api_client)
    config_id = 56 # int | configId
    put_global_configurations_request = fineract_client.PutGlobalConfigurationsRequest() # PutGlobalConfigurationsRequest | 

    try:
        # Update Global Configuration
        api_response = api_instance.update_configuration1(config_id, put_global_configurations_request)
        print("The response of GlobalConfigurationApi->update_configuration1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalConfigurationApi->update_configuration1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| configId | 
 **put_global_configurations_request** | [**PutGlobalConfigurationsRequest**](PutGlobalConfigurationsRequest.md)|  | 

### Return type

[**PutGlobalConfigurationsResponse**](PutGlobalConfigurationsResponse.md)

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

