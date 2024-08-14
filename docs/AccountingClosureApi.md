# fineract_client.AccountingClosureApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_closure**](AccountingClosureApi.md#create_gl_closure) | **POST** /v1/glclosures | Create an Accounting Closure
[**delete_gl_closure**](AccountingClosureApi.md#delete_gl_closure) | **DELETE** /v1/glclosures/{glClosureId} | Delete an accounting closure
[**retreive_closure**](AccountingClosureApi.md#retreive_closure) | **GET** /v1/glclosures/{glClosureId} | Retrieve an Accounting Closure
[**retrieve_all_closures**](AccountingClosureApi.md#retrieve_all_closures) | **GET** /v1/glclosures | List Accounting closures
[**update_gl_closure**](AccountingClosureApi.md#update_gl_closure) | **PUT** /v1/glclosures/{glClosureId} | Update an Accounting closure

# **create_gl_closure**
> PostGlClosuresResponse create_gl_closure(body)

Create an Accounting Closure

Mandatory Fields officeId,closingDate

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
api_instance = fineract_client.AccountingClosureApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostGlClosuresRequest() # PostGlClosuresRequest | 

try:
    # Create an Accounting Closure
    api_response = api_instance.create_gl_closure(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingClosureApi->create_gl_closure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGlClosuresRequest**](PostGlClosuresRequest.md)|  | 

### Return type

[**PostGlClosuresResponse**](PostGlClosuresResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gl_closure**
> DeleteGlClosuresResponse delete_gl_closure(gl_closure_id)

Delete an accounting closure

Note: Only the latest accounting closure associated with a branch may be deleted.

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
api_instance = fineract_client.AccountingClosureApi(fineract_client.ApiClient(configuration))
gl_closure_id = 789 # int | glclosureId

try:
    # Delete an accounting closure
    api_response = api_instance.delete_gl_closure(gl_closure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingClosureApi->delete_gl_closure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glclosureId | 

### Return type

[**DeleteGlClosuresResponse**](DeleteGlClosuresResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retreive_closure**
> GetGlClosureResponse retreive_closure(gl_closure_id)

Retrieve an Accounting Closure

Example Requests:  glclosures/1   /glclosures/1?fields=officeName,closingDate

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
api_instance = fineract_client.AccountingClosureApi(fineract_client.ApiClient(configuration))
gl_closure_id = 789 # int | glClosureId

try:
    # Retrieve an Accounting Closure
    api_response = api_instance.retreive_closure(gl_closure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingClosureApi->retreive_closure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glClosureId | 

### Return type

[**GetGlClosureResponse**](GetGlClosureResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_closures**
> list[GetGlClosureResponse] retrieve_all_closures(office_id=office_id)

List Accounting closures

Example Requests:  glclosures

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
api_instance = fineract_client.AccountingClosureApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)

try:
    # List Accounting closures
    api_response = api_instance.retrieve_all_closures(office_id=office_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingClosureApi->retrieve_all_closures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 

### Return type

[**list[GetGlClosureResponse]**](GetGlClosureResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gl_closure**
> PutGlClosuresResponse update_gl_closure(gl_closure_id, body=body)

Update an Accounting closure

Once an accounting closure is created, only the comments associated with it may be edited

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
api_instance = fineract_client.AccountingClosureApi(fineract_client.ApiClient(configuration))
gl_closure_id = 789 # int | glClosureId
body = fineract_client.PutGlClosuresRequest() # PutGlClosuresRequest |  (optional)

try:
    # Update an Accounting closure
    api_response = api_instance.update_gl_closure(gl_closure_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingClosureApi->update_gl_closure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_closure_id** | **int**| glClosureId | 
 **body** | [**PutGlClosuresRequest**](PutGlClosuresRequest.md)|  | [optional] 

### Return type

[**PutGlClosuresResponse**](PutGlClosuresResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

