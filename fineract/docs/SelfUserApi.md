# fineract_client.SelfUserApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update24**](SelfUserApi.md#update24) | **PUT** /v1/self/user | Update User


# **update24**
> PutSelfUserResponse update24(put_self_user_request)

Update User

This API can be used by Self Service user to update their own user information. Currently, \"password\" and \"repeatPassword\" are the only parameters accepted.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_self_user_request import PutSelfUserRequest
from fineract_client.models.put_self_user_response import PutSelfUserResponse
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
    api_instance = fineract_client.SelfUserApi(api_client)
    put_self_user_request = fineract_client.PutSelfUserRequest() # PutSelfUserRequest | 

    try:
        # Update User
        api_response = api_instance.update24(put_self_user_request)
        print("The response of SelfUserApi->update24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfUserApi->update24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_self_user_request** | [**PutSelfUserRequest**](PutSelfUserRequest.md)|  | 

### Return type

[**PutSelfUserResponse**](PutSelfUserResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

