# fineract_client.CodeValuesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code_value**](CodeValuesApi.md#create_code_value) | **POST** /v1/codes/{codeId}/codevalues | Create a Code description
[**delete_code_value**](CodeValuesApi.md#delete_code_value) | **DELETE** /v1/codes/{codeId}/codevalues/{codeValueId} | Delete a Code description
[**retrieve_all_code_values**](CodeValuesApi.md#retrieve_all_code_values) | **GET** /v1/codes/{codeId}/codevalues | List Code Values
[**retrieve_code_value**](CodeValuesApi.md#retrieve_code_value) | **GET** /v1/codes/{codeId}/codevalues/{codeValueId} | Retrieve a Code description
[**update_code_value**](CodeValuesApi.md#update_code_value) | **PUT** /v1/codes/{codeId}/codevalues/{codeValueId} | Update a Code description

# **create_code_value**
> PostCodeValueDataResponse create_code_value(body, code_id)

Create a Code description

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
api_instance = fineract_client.CodeValuesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostCodeValuesDataRequest() # PostCodeValuesDataRequest | 
code_id = 789 # int | codeId

try:
    # Create a Code description
    api_response = api_instance.create_code_value(body, code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeValuesApi->create_code_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCodeValuesDataRequest**](PostCodeValuesDataRequest.md)|  | 
 **code_id** | **int**| codeId | 

### Return type

[**PostCodeValueDataResponse**](PostCodeValueDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_code_value**
> DeleteCodeValueDataResponse delete_code_value(code_id, code_value_id)

Delete a Code description

Deletes a code description

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
api_instance = fineract_client.CodeValuesApi(fineract_client.ApiClient(configuration))
code_id = 789 # int | codeId
code_value_id = 789 # int | codeValueId

try:
    # Delete a Code description
    api_response = api_instance.delete_code_value(code_id, code_value_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeValuesApi->delete_code_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 
 **code_value_id** | **int**| codeValueId | 

### Return type

[**DeleteCodeValueDataResponse**](DeleteCodeValueDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_code_values**
> list[GetCodeValuesDataResponse] retrieve_all_code_values(code_id)

List Code Values

Returns the list of Code Values for a given Code  Example Requests:  codes/1/codevalues

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
api_instance = fineract_client.CodeValuesApi(fineract_client.ApiClient(configuration))
code_id = 789 # int | codeId

try:
    # List Code Values
    api_response = api_instance.retrieve_all_code_values(code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeValuesApi->retrieve_all_code_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_id** | **int**| codeId | 

### Return type

[**list[GetCodeValuesDataResponse]**](GetCodeValuesDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_code_value**
> GetCodeValuesDataResponse retrieve_code_value(code_value_id, code_id)

Retrieve a Code description

Returns the details of a Code Value  Example Requests:  codes/1/codevalues/1

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
api_instance = fineract_client.CodeValuesApi(fineract_client.ApiClient(configuration))
code_value_id = 789 # int | codeValueId
code_id = 789 # int | codeId

try:
    # Retrieve a Code description
    api_response = api_instance.retrieve_code_value(code_value_id, code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeValuesApi->retrieve_code_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_value_id** | **int**| codeValueId | 
 **code_id** | **int**| codeId | 

### Return type

[**GetCodeValuesDataResponse**](GetCodeValuesDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_code_value**
> PutCodeValueDataResponse update_code_value(body, code_id, code_value_id)

Update a Code description

Updates the details of a code description.

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
api_instance = fineract_client.CodeValuesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutCodeValuesDataRequest() # PutCodeValuesDataRequest | 
code_id = 789 # int | codeId
code_value_id = 789 # int | codeValueId

try:
    # Update a Code description
    api_response = api_instance.update_code_value(body, code_id, code_value_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodeValuesApi->update_code_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCodeValuesDataRequest**](PutCodeValuesDataRequest.md)|  | 
 **code_id** | **int**| codeId | 
 **code_value_id** | **int**| codeValueId | 

### Return type

[**PutCodeValueDataResponse**](PutCodeValueDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

