# fineract_client.ExternalEventConfigurationApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_external_event_configuration**](ExternalEventConfigurationApi.md#retrieve_external_event_configuration) | **GET** /v1/externalevents/configuration | List all external event configurations
[**update_external_event_configurations_details**](ExternalEventConfigurationApi.md#update_external_event_configurations_details) | **PUT** /v1/externalevents/configuration | Enable/Disable external events posting


# **retrieve_external_event_configuration**
> GetExternalEventConfigurationsResponse retrieve_external_event_configuration()

List all external event configurations

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_external_event_configurations_response import GetExternalEventConfigurationsResponse
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
    api_instance = fineract_client.ExternalEventConfigurationApi(api_client)

    try:
        # List all external event configurations
        api_response = api_instance.retrieve_external_event_configuration()
        print("The response of ExternalEventConfigurationApi->retrieve_external_event_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEventConfigurationApi->retrieve_external_event_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetExternalEventConfigurationsResponse**](GetExternalEventConfigurationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all external event configurations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_event_configurations_details**
> CommandProcessingResult update_external_event_configurations_details(put_external_event_configurations_request)

Enable/Disable external events posting

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.command_processing_result import CommandProcessingResult
from fineract_client.models.put_external_event_configurations_request import PutExternalEventConfigurationsRequest
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
    api_instance = fineract_client.ExternalEventConfigurationApi(api_client)
    put_external_event_configurations_request = fineract_client.PutExternalEventConfigurationsRequest() # PutExternalEventConfigurationsRequest | 

    try:
        # Enable/Disable external events posting
        api_response = api_instance.update_external_event_configurations_details(put_external_event_configurations_request)
        print("The response of ExternalEventConfigurationApi->update_external_event_configurations_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEventConfigurationApi->update_external_event_configurations_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_external_event_configurations_request** | [**PutExternalEventConfigurationsRequest**](PutExternalEventConfigurationsRequest.md)|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

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

