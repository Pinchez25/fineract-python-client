# fineract_client.SelfUserDetailsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_authenticated_user_data1**](SelfUserDetailsApi.md#fetch_authenticated_user_data1) | **GET** /v1/self/userdetails | Fetch authenticated user details


# **fetch_authenticated_user_data1**
> GetSelfUserDetailsResponse fetch_authenticated_user_data1()

Fetch authenticated user details

Checks the Authentication and returns the set roles and permissions allowed  For more info visit this link - https://fineract.apache.org/legacy-docs/apiLive.htm#selfoauth

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_user_details_response import GetSelfUserDetailsResponse
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
    api_instance = fineract_client.SelfUserDetailsApi(api_client)

    try:
        # Fetch authenticated user details
        api_response = api_instance.fetch_authenticated_user_data1()
        print("The response of SelfUserDetailsApi->fetch_authenticated_user_data1:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

