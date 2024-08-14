# fineract_client.PermissionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_permissions**](PermissionsApi.md#retrieve_all_permissions) | **GET** /v1/permissions | List Application Permissions
[**update_permissions_details**](PermissionsApi.md#update_permissions_details) | **PUT** /v1/permissions | Enable/Disable Permissions for Maker Checker

# **retrieve_all_permissions**
> list[GetPermissionsResponse] retrieve_all_permissions()

List Application Permissions

ARGUMENTS makerCheckerableoptional, Values are true, false. Default is false. If makerCheckerable=false or not supplied then a list of application permissions is returned. The \"selected\" attribute is always true in this case.  If makerCheckerable=true then the \"selected\" attribute shows whether the permission is enabled for Maker Check functionality.  Note: Each Apache Fineract transaction is associated with a permission.  Example Requests:  permissions   permissions?makerCheckerable=true   permissions?fields=grouping,code

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
api_instance = fineract_client.PermissionsApi(fineract_client.ApiClient(configuration))

try:
    # List Application Permissions
    api_response = api_instance.retrieve_all_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->retrieve_all_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetPermissionsResponse]**](GetPermissionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permissions_details**
> CommandProcessingResult update_permissions_details(body)

Enable/Disable Permissions for Maker Checker

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
api_instance = fineract_client.PermissionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutPermissionsRequest() # PutPermissionsRequest | 

try:
    # Enable/Disable Permissions for Maker Checker
    api_response = api_instance.update_permissions_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_permissions_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPermissionsRequest**](PutPermissionsRequest.md)|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

