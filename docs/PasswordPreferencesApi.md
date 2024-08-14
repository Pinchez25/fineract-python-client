# fineract_client.PasswordPreferencesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve1**](PasswordPreferencesApi.md#retrieve1) | **GET** /v1/passwordpreferences | 
[**template21**](PasswordPreferencesApi.md#template21) | **GET** /v1/passwordpreferences/template | List Application Password validation policies
[**update25**](PasswordPreferencesApi.md#update25) | **PUT** /v1/passwordpreferences | Update password preferences

# **retrieve1**
> GetPasswordPreferencesTemplateResponse retrieve1()



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
api_instance = fineract_client.PasswordPreferencesApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordPreferencesApi->retrieve1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPasswordPreferencesTemplateResponse**](GetPasswordPreferencesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template21**
> list[GetPasswordPreferencesTemplateResponse] template21()

List Application Password validation policies

ARGUMENTS Example Requests:  passwordpreferences

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
api_instance = fineract_client.PasswordPreferencesApi(fineract_client.ApiClient(configuration))

try:
    # List Application Password validation policies
    api_response = api_instance.template21()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordPreferencesApi->template21: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetPasswordPreferencesTemplateResponse]**](GetPasswordPreferencesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update25**
> update25(body)

Update password preferences

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
api_instance = fineract_client.PasswordPreferencesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutPasswordPreferencesTemplateRequest() # PutPasswordPreferencesTemplateRequest | 

try:
    # Update password preferences
    api_instance.update25(body)
except ApiException as e:
    print("Exception when calling PasswordPreferencesApi->update25: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPasswordPreferencesTemplateRequest**](PutPasswordPreferencesTemplateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

