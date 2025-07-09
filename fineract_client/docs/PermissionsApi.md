# fineract_client.PermissionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_permissions**](PermissionsApi.md#retrieve_all_permissions) | **GET** /v1/permissions | List Application Permissions
[**update_permissions_details**](PermissionsApi.md#update_permissions_details) | **PUT** /v1/permissions | Enable/Disable Permissions for Maker Checker


# **retrieve_all_permissions**
> List[GetPermissionsResponse] retrieve_all_permissions()

List Application Permissions

ARGUMENTS
makerCheckerableoptional, Values are true, false. Default is false.
If makerCheckerable=false or not supplied then a list of application permissions is returned. The "selected" attribute is always true in this case.

If makerCheckerable=true then the "selected" attribute shows whether the permission is enabled for Maker Check functionality.

Note: Each Apache Fineract transaction is associated with a permission.

Example Requests:

permissions


permissions?makerCheckerable=true


permissions?fields=grouping,code

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_permissions_response import GetPermissionsResponse
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
    api_instance = fineract_client.PermissionsApi(api_client)

    try:
        # List Application Permissions
        api_response = api_instance.retrieve_all_permissions()
        print("The response of PermissionsApi->retrieve_all_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->retrieve_all_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPermissionsResponse]**](GetPermissionsResponse.md)

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

# **update_permissions_details**
> CommandProcessingResult update_permissions_details(put_permissions_request)

Enable/Disable Permissions for Maker Checker

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.command_processing_result import CommandProcessingResult
from fineract_client.models.put_permissions_request import PutPermissionsRequest
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
    api_instance = fineract_client.PermissionsApi(api_client)
    put_permissions_request = fineract_client.PutPermissionsRequest() # PutPermissionsRequest | 

    try:
        # Enable/Disable Permissions for Maker Checker
        api_response = api_instance.update_permissions_details(put_permissions_request)
        print("The response of PermissionsApi->update_permissions_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->update_permissions_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_permissions_request** | [**PutPermissionsRequest**](PutPermissionsRequest.md)|  | 

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

