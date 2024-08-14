# fineract_client.GlobalConfigurationApi

All URIs are relative to */fineract-provider/api/v1*

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
api_instance = fineract_client.GlobalConfigurationApi(fineract_client.ApiClient(configuration))
survey = false # bool | survey (optional) (default to false)

try:
    # Retrieve Global Configuration | Retrieve Global Configuration for surveys
    api_response = api_instance.retrieve_configuration(survey=survey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalConfigurationApi->retrieve_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey** | **bool**| survey | [optional] [default to false]

### Return type

[**GetGlobalConfigurationsResponse**](GetGlobalConfigurationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one3**
> GetGlobalConfigurationsResponse retrieve_one3(config_id)

Retrieve Global Configuration

Returns a global enable/disable configurations.  Example Requests:  configurations/1

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
api_instance = fineract_client.GlobalConfigurationApi(fineract_client.ApiClient(configuration))
config_id = 789 # int | configId

try:
    # Retrieve Global Configuration
    api_response = api_instance.retrieve_one3(config_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one_by_name**
> GlobalConfigurationPropertyData retrieve_one_by_name(name)

Retrieve Global Configuration

Returns a global enable/disable configuration.  Example Requests:  configurations/name/Enable-Address

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
api_instance = fineract_client.GlobalConfigurationApi(fineract_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # Retrieve Global Configuration
    api_response = api_instance.retrieve_one_by_name(name)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration1**
> PutGlobalConfigurationsResponse update_configuration1(body, config_id)

Update Global Configuration

Updates an enable/disable global configuration item.

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
api_instance = fineract_client.GlobalConfigurationApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutGlobalConfigurationsRequest() # PutGlobalConfigurationsRequest | 
config_id = 789 # int | configId

try:
    # Update Global Configuration
    api_response = api_instance.update_configuration1(body, config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalConfigurationApi->update_configuration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutGlobalConfigurationsRequest**](PutGlobalConfigurationsRequest.md)|  | 
 **config_id** | **int**| configId | 

### Return type

[**PutGlobalConfigurationsResponse**](PutGlobalConfigurationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

