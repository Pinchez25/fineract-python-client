# fineract_client.SelfAuthenticationApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate1**](SelfAuthenticationApi.md#authenticate1) | **POST** /v1/self/authentication | Verify authentication


# **authenticate1**
> PostSelfAuthenticationResponse authenticate1(post_authentication_request)

Verify authentication

Authenticates the credentials provided and returns the set roles and permissions allowed.  Please visit this link for more info - https://fineract.apache.org/legacy-docs/apiLive.htm#selfbasicauth

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_authentication_request import PostAuthenticationRequest
from fineract_client.models.post_self_authentication_response import PostSelfAuthenticationResponse
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
    api_instance = fineract_client.SelfAuthenticationApi(api_client)
    post_authentication_request = fineract_client.PostAuthenticationRequest() # PostAuthenticationRequest | 

    try:
        # Verify authentication
        api_response = api_instance.authenticate1(post_authentication_request)
        print("The response of SelfAuthenticationApi->authenticate1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfAuthenticationApi->authenticate1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_authentication_request** | [**PostAuthenticationRequest**](PostAuthenticationRequest.md)|  | 

### Return type

[**PostSelfAuthenticationResponse**](PostSelfAuthenticationResponse.md)

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

