# fineract_client.ExternalServicesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_one2**](ExternalServicesApi.md#retrieve_one2) | **GET** /v1/externalservice/{servicename} | Retrieve External Services Configuration
[**update_external_service_properties**](ExternalServicesApi.md#update_external_service_properties) | **PUT** /v1/externalservice/{servicename} | Update External Service

# **retrieve_one2**
> ExternalServicesPropertiesData retrieve_one2(servicename)

Retrieve External Services Configuration

Returns a external Service configurations based on the Service Name.  Service Names supported are S3 and SMTP.  Example Requests:  externalservice/SMTP

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
api_instance = fineract_client.ExternalServicesApi(fineract_client.ApiClient(configuration))
servicename = 'servicename_example' # str | servicename

try:
    # Retrieve External Services Configuration
    api_response = api_instance.retrieve_one2(servicename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalServicesApi->retrieve_one2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servicename** | **str**| servicename | 

### Return type

[**ExternalServicesPropertiesData**](ExternalServicesPropertiesData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_service_properties**
> update_external_service_properties(body, servicename)

Update External Service

Updates the external Service Configuration for a Service Name.  Example:   externalservice/S3

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
api_instance = fineract_client.ExternalServicesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutExternalServiceRequest() # PutExternalServiceRequest | 
servicename = 'servicename_example' # str | servicename

try:
    # Update External Service
    api_instance.update_external_service_properties(body, servicename)
except ApiException as e:
    print("Exception when calling ExternalServicesApi->update_external_service_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutExternalServiceRequest**](PutExternalServiceRequest.md)|  | 
 **servicename** | **str**| servicename | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

