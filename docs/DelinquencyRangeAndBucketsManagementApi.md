# fineract_client.DelinquencyRangeAndBucketsManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_delinquency_bucket**](DelinquencyRangeAndBucketsManagementApi.md#create_delinquency_bucket) | **POST** /v1/delinquency/buckets | Create Delinquency Bucket
[**create_delinquency_range**](DelinquencyRangeAndBucketsManagementApi.md#create_delinquency_range) | **POST** /v1/delinquency/ranges | Create Delinquency Range
[**delete_delinquency_bucket**](DelinquencyRangeAndBucketsManagementApi.md#delete_delinquency_bucket) | **DELETE** /v1/delinquency/buckets/{delinquencyBucketId} | Delete Delinquency Bucket based on the Id
[**delete_delinquency_range**](DelinquencyRangeAndBucketsManagementApi.md#delete_delinquency_range) | **DELETE** /v1/delinquency/ranges/{delinquencyRangeId} | Update Delinquency Range based on the Id
[**get_delinquency_bucket**](DelinquencyRangeAndBucketsManagementApi.md#get_delinquency_bucket) | **GET** /v1/delinquency/buckets/{delinquencyBucketId} | Retrieve a specific Delinquency Bucket based on the Id
[**get_delinquency_buckets**](DelinquencyRangeAndBucketsManagementApi.md#get_delinquency_buckets) | **GET** /v1/delinquency/buckets | List all Delinquency Buckets
[**get_delinquency_range**](DelinquencyRangeAndBucketsManagementApi.md#get_delinquency_range) | **GET** /v1/delinquency/ranges/{delinquencyRangeId} | Retrieve a specific Delinquency Range based on the Id
[**get_delinquency_ranges**](DelinquencyRangeAndBucketsManagementApi.md#get_delinquency_ranges) | **GET** /v1/delinquency/ranges | List all Delinquency Ranges
[**update_delinquency_bucket**](DelinquencyRangeAndBucketsManagementApi.md#update_delinquency_bucket) | **PUT** /v1/delinquency/buckets/{delinquencyBucketId} | Update Delinquency Bucket based on the Id
[**update_delinquency_range**](DelinquencyRangeAndBucketsManagementApi.md#update_delinquency_range) | **PUT** /v1/delinquency/ranges/{delinquencyRangeId} | Update Delinquency Range based on the Id

# **create_delinquency_bucket**
> PostDelinquencyBucketResponse create_delinquency_bucket(body)

Create Delinquency Bucket

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 

try:
    # Create Delinquency Bucket
    api_response = api_instance.create_delinquency_bucket(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->create_delinquency_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 

### Return type

[**PostDelinquencyBucketResponse**](PostDelinquencyBucketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_delinquency_range**
> PostDelinquencyRangeResponse create_delinquency_range(body)

Create Delinquency Range

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 

try:
    # Create Delinquency Range
    api_response = api_instance.create_delinquency_range(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->create_delinquency_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 

### Return type

[**PostDelinquencyRangeResponse**](PostDelinquencyRangeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delinquency_bucket**
> DeleteDelinquencyBucketResponse delete_delinquency_bucket(body, delinquency_bucket_id)

Delete Delinquency Bucket based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 
delinquency_bucket_id = 789 # int | delinquencyBucketId

try:
    # Delete Delinquency Bucket based on the Id
    api_response = api_instance.delete_delinquency_bucket(body, delinquency_bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->delete_delinquency_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 
 **delinquency_bucket_id** | **int**| delinquencyBucketId | 

### Return type

[**DeleteDelinquencyBucketResponse**](DeleteDelinquencyBucketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delinquency_range**
> DeleteDelinquencyRangeResponse delete_delinquency_range(body, delinquency_range_id)

Update Delinquency Range based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 
delinquency_range_id = 789 # int | delinquencyRangeId

try:
    # Update Delinquency Range based on the Id
    api_response = api_instance.delete_delinquency_range(body, delinquency_range_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->delete_delinquency_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 
 **delinquency_range_id** | **int**| delinquencyRangeId | 

### Return type

[**DeleteDelinquencyRangeResponse**](DeleteDelinquencyRangeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_bucket**
> GetDelinquencyBucketsResponse get_delinquency_bucket(delinquency_bucket_id)

Retrieve a specific Delinquency Bucket based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
delinquency_bucket_id = 789 # int | delinquencyBucketId

try:
    # Retrieve a specific Delinquency Bucket based on the Id
    api_response = api_instance.get_delinquency_bucket(delinquency_bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_bucket_id** | **int**| delinquencyBucketId | 

### Return type

[**GetDelinquencyBucketsResponse**](GetDelinquencyBucketsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_buckets**
> list[GetDelinquencyBucketsResponse] get_delinquency_buckets()

List all Delinquency Buckets

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))

try:
    # List all Delinquency Buckets
    api_response = api_instance.get_delinquency_buckets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_buckets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetDelinquencyBucketsResponse]**](GetDelinquencyBucketsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_range**
> GetDelinquencyRangesResponse get_delinquency_range(delinquency_range_id)

Retrieve a specific Delinquency Range based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
delinquency_range_id = 789 # int | delinquencyRangeId

try:
    # Retrieve a specific Delinquency Range based on the Id
    api_response = api_instance.get_delinquency_range(delinquency_range_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_range_id** | **int**| delinquencyRangeId | 

### Return type

[**GetDelinquencyRangesResponse**](GetDelinquencyRangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_ranges**
> list[GetDelinquencyRangesResponse] get_delinquency_ranges()

List all Delinquency Ranges

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))

try:
    # List all Delinquency Ranges
    api_response = api_instance.get_delinquency_ranges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_ranges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetDelinquencyRangesResponse]**](GetDelinquencyRangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delinquency_bucket**
> PutDelinquencyBucketResponse update_delinquency_bucket(body, delinquency_bucket_id)

Update Delinquency Bucket based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 
delinquency_bucket_id = 789 # int | delinquencyBucketId

try:
    # Update Delinquency Bucket based on the Id
    api_response = api_instance.update_delinquency_bucket(body, delinquency_bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->update_delinquency_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 
 **delinquency_bucket_id** | **int**| delinquencyBucketId | 

### Return type

[**PutDelinquencyBucketResponse**](PutDelinquencyBucketResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delinquency_range**
> PutDelinquencyRangeResponse update_delinquency_range(body, delinquency_range_id)

Update Delinquency Range based on the Id

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
api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 
delinquency_range_id = 789 # int | delinquencyRangeId

try:
    # Update Delinquency Range based on the Id
    api_response = api_instance.update_delinquency_range(body, delinquency_range_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelinquencyRangeAndBucketsManagementApi->update_delinquency_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 
 **delinquency_range_id** | **int**| delinquencyRangeId | 

### Return type

[**PutDelinquencyRangeResponse**](PutDelinquencyRangeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

