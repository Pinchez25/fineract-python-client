# fineract_client.SelfUserDetailsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_authenticated_user_data1**](SelfUserDetailsApi.md#fetch_authenticated_user_data1) | **GET** /v1/self/userdetails | Fetch authenticated user details

# **fetch_authenticated_user_data1**
> GetSelfUserDetailsResponse fetch_authenticated_user_data1()

Fetch authenticated user details

Checks the Authentication and returns the set roles and permissions allowed  For more info visit this link - https://fineract.apache.org/legacy-docs/apiLive.htm#selfoauth

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
api_instance = fineract_client.SelfUserDetailsApi(fineract_client.ApiClient(configuration))

try:
    # Fetch authenticated user details
    api_response = api_instance.fetch_authenticated_user_data1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfUserDetailsApi->fetch_authenticated_user_data1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSelfUserDetailsResponse**](GetSelfUserDetailsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

