# fineract_client.CodesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code**](CodesApi.md#create_code) | **POST** /v1/codes | Create a Code
[**delete_code**](CodesApi.md#delete_code) | **DELETE** /v1/codes/{codeId} | Delete a Code
[**retrieve_code**](CodesApi.md#retrieve_code) | **GET** /v1/codes/{codeId} | Retrieve a Code
[**retrieve_codes**](CodesApi.md#retrieve_codes) | **GET** /v1/codes | Retrieve Codes
[**update_code**](CodesApi.md#update_code) | **PUT** /v1/codes/{codeId} | Update a Code

# **create_code**
> PostCodesResponse create_code(body)

Create a Code

Creates a code. Codes created through api are always 'user defined' and so system defined is marked as false.

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
api_instance = fineract_client.CodesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostCodesRequest() # PostCodesRequest | 

try:
    # Create a Code
    api_response = api_instance.create_code(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodesApi->create_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCodesRequest**](PostCodesRequest.md)|  | 

### Return type

[**PostCodesResponse**](PostCodesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_code**
> DeleteCodesResponse delete_code(code_id)

Delete a Code

Deletes a code if it is not system defined.

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
api_instance = fineract_client.CodesApi(fineract_client.ApiClient(configuration))
code_id = 789 # int | codeId

try:
    # Delete a Code
    api_response = api_instance.delete_code(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodesApi->delete_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 

### Return type

[**DeleteCodesResponse**](DeleteCodesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_code**
> GetCodesResponse retrieve_code(code_id)

Retrieve a Code

Returns the details of a Code.  Example Requests:  codes/1

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
api_instance = fineract_client.CodesApi(fineract_client.ApiClient(configuration))
code_id = 789 # int | codeId

try:
    # Retrieve a Code
    api_response = api_instance.retrieve_code(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodesApi->retrieve_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 

### Return type

[**GetCodesResponse**](GetCodesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_codes**
> list[GetCodesResponse] retrieve_codes()

Retrieve Codes

Returns the list of codes.  Example Requests:  codes

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
api_instance = fineract_client.CodesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Codes
    api_response = api_instance.retrieve_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodesApi->retrieve_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetCodesResponse]**](GetCodesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_code**
> PutCodesResponse update_code(body, code_id)

Update a Code

Updates the details of a code if it is not system defined.

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
api_instance = fineract_client.CodesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutCodesRequest() # PutCodesRequest | 
code_id = 789 # int | codeId

try:
    # Update a Code
    api_response = api_instance.update_code(body, code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodesApi->update_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCodesRequest**](PutCodesRequest.md)|  | 
 **code_id** | **int**| codeId | 

### Return type

[**PutCodesResponse**](PutCodesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

