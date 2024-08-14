# fineract_client.SelfUserApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update24**](SelfUserApi.md#update24) | **PUT** /v1/self/user | Update User

# **update24**
> PutSelfUserResponse update24(body)

Update User

This API can be used by Self Service user to update their own user information. Currently, \"password\" and \"repeatPassword\" are the only parameters accepted.

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
api_instance = fineract_client.SelfUserApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutSelfUserRequest() # PutSelfUserRequest | 

try:
    # Update User
    api_response = api_instance.update24(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfUserApi->update24: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSelfUserRequest**](PutSelfUserRequest.md)|  | 

### Return type

[**PutSelfUserResponse**](PutSelfUserResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

