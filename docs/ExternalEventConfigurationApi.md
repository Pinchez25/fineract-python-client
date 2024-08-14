# fineract_client.ExternalEventConfigurationApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_external_event_configuration**](ExternalEventConfigurationApi.md#retrieve_external_event_configuration) | **GET** /v1/externalevents/configuration | List all external event configurations
[**update_external_event_configurations_details**](ExternalEventConfigurationApi.md#update_external_event_configurations_details) | **PUT** /v1/externalevents/configuration | Enable/Disable external events posting

# **retrieve_external_event_configuration**
> GetExternalEventConfigurationsResponse retrieve_external_event_configuration()

List all external event configurations

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
api_instance = fineract_client.ExternalEventConfigurationApi(fineract_client.ApiClient(configuration))

try:
    # List all external event configurations
    api_response = api_instance.retrieve_external_event_configuration()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_event_configurations_details**
> CommandProcessingResult update_external_event_configurations_details(body)

Enable/Disable external events posting

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
api_instance = fineract_client.ExternalEventConfigurationApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutExternalEventConfigurationsRequest() # PutExternalEventConfigurationsRequest | 

try:
    # Enable/Disable external events posting
    api_response = api_instance.update_external_event_configurations_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalEventConfigurationApi->update_external_event_configurations_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutExternalEventConfigurationsRequest**](PutExternalEventConfigurationsRequest.md)|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

