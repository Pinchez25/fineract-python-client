# fineract_client.ExternalServicesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_one2**](ExternalServicesApi.md#retrieve_one2) | **GET** /v1/externalservice/{servicename} | Retrieve External Services Configuration
[**update_external_service_properties**](ExternalServicesApi.md#update_external_service_properties) | **PUT** /v1/externalservice/{servicename} | Update External Service


# **retrieve_one2**
> ExternalServicesPropertiesData retrieve_one2(servicename)

Retrieve External Services Configuration

Returns a external Service configurations based on the Service Name.

Service Names supported are S3 and SMTP.

Example Requests:

externalservice/SMTP

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.external_services_properties_data import ExternalServicesPropertiesData
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
    api_instance = fineract_client.ExternalServicesApi(api_client)
    servicename = 'servicename_example' # str | servicename

    try:
        # Retrieve External Services Configuration
        api_response = api_instance.retrieve_one2(servicename)
        print("The response of ExternalServicesApi->retrieve_one2:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_service_properties**
> update_external_service_properties(servicename, put_external_service_request)

Update External Service

Updates the external Service Configuration for a Service Name.

Example: 

externalservice/S3

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_external_service_request import PutExternalServiceRequest
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
    api_instance = fineract_client.ExternalServicesApi(api_client)
    servicename = 'servicename_example' # str | servicename
    put_external_service_request = fineract_client.PutExternalServiceRequest() # PutExternalServiceRequest | 

    try:
        # Update External Service
        api_instance.update_external_service_properties(servicename, put_external_service_request)
    except Exception as e:
        print("Exception when calling ExternalServicesApi->update_external_service_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servicename** | **str**| servicename | 
 **put_external_service_request** | [**PutExternalServiceRequest**](PutExternalServiceRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

