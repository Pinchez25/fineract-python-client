# fineract_client.DelinquencyRangeAndBucketsManagementApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

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
> PostDelinquencyBucketResponse create_delinquency_bucket(post_delinquency_bucket_request)

Create Delinquency Bucket

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_delinquency_bucket_request import PostDelinquencyBucketRequest
from fineract_client.models.post_delinquency_bucket_response import PostDelinquencyBucketResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    post_delinquency_bucket_request = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 

    try:
        # Create Delinquency Bucket
        api_response = api_instance.create_delinquency_bucket(post_delinquency_bucket_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->create_delinquency_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->create_delinquency_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_delinquency_bucket_request** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 

### Return type

[**PostDelinquencyBucketResponse**](PostDelinquencyBucketResponse.md)

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

# **create_delinquency_range**
> PostDelinquencyRangeResponse create_delinquency_range(post_delinquency_range_request)

Create Delinquency Range

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_delinquency_range_request import PostDelinquencyRangeRequest
from fineract_client.models.post_delinquency_range_response import PostDelinquencyRangeResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    post_delinquency_range_request = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 

    try:
        # Create Delinquency Range
        api_response = api_instance.create_delinquency_range(post_delinquency_range_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->create_delinquency_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->create_delinquency_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_delinquency_range_request** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 

### Return type

[**PostDelinquencyRangeResponse**](PostDelinquencyRangeResponse.md)

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

# **delete_delinquency_bucket**
> DeleteDelinquencyBucketResponse delete_delinquency_bucket(delinquency_bucket_id, post_delinquency_bucket_request)

Delete Delinquency Bucket based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_delinquency_bucket_response import DeleteDelinquencyBucketResponse
from fineract_client.models.post_delinquency_bucket_request import PostDelinquencyBucketRequest
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_bucket_id = 56 # int | delinquencyBucketId
    post_delinquency_bucket_request = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 

    try:
        # Delete Delinquency Bucket based on the Id
        api_response = api_instance.delete_delinquency_bucket(delinquency_bucket_id, post_delinquency_bucket_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->delete_delinquency_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->delete_delinquency_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_bucket_id** | **int**| delinquencyBucketId | 
 **post_delinquency_bucket_request** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 

### Return type

[**DeleteDelinquencyBucketResponse**](DeleteDelinquencyBucketResponse.md)

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

# **delete_delinquency_range**
> DeleteDelinquencyRangeResponse delete_delinquency_range(delinquency_range_id, post_delinquency_range_request)

Update Delinquency Range based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_delinquency_range_response import DeleteDelinquencyRangeResponse
from fineract_client.models.post_delinquency_range_request import PostDelinquencyRangeRequest
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_range_id = 56 # int | delinquencyRangeId
    post_delinquency_range_request = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 

    try:
        # Update Delinquency Range based on the Id
        api_response = api_instance.delete_delinquency_range(delinquency_range_id, post_delinquency_range_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->delete_delinquency_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->delete_delinquency_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_range_id** | **int**| delinquencyRangeId | 
 **post_delinquency_range_request** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 

### Return type

[**DeleteDelinquencyRangeResponse**](DeleteDelinquencyRangeResponse.md)

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

# **get_delinquency_bucket**
> GetDelinquencyBucketsResponse get_delinquency_bucket(delinquency_bucket_id)

Retrieve a specific Delinquency Bucket based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_delinquency_buckets_response import GetDelinquencyBucketsResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_bucket_id = 56 # int | delinquencyBucketId

    try:
        # Retrieve a specific Delinquency Bucket based on the Id
        api_response = api_instance.get_delinquency_bucket(delinquency_bucket_id)
        print("The response of DelinquencyRangeAndBucketsManagementApi->get_delinquency_bucket:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_buckets**
> List[GetDelinquencyBucketsResponse] get_delinquency_buckets()

List all Delinquency Buckets

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_delinquency_buckets_response import GetDelinquencyBucketsResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)

    try:
        # List all Delinquency Buckets
        api_response = api_instance.get_delinquency_buckets()
        print("The response of DelinquencyRangeAndBucketsManagementApi->get_delinquency_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_buckets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetDelinquencyBucketsResponse]**](GetDelinquencyBucketsResponse.md)

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

# **get_delinquency_range**
> GetDelinquencyRangesResponse get_delinquency_range(delinquency_range_id)

Retrieve a specific Delinquency Range based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_delinquency_ranges_response import GetDelinquencyRangesResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_range_id = 56 # int | delinquencyRangeId

    try:
        # Retrieve a specific Delinquency Range based on the Id
        api_response = api_instance.get_delinquency_range(delinquency_range_id)
        print("The response of DelinquencyRangeAndBucketsManagementApi->get_delinquency_range:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_ranges**
> List[GetDelinquencyRangesResponse] get_delinquency_ranges()

List all Delinquency Ranges

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_delinquency_ranges_response import GetDelinquencyRangesResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)

    try:
        # List all Delinquency Ranges
        api_response = api_instance.get_delinquency_ranges()
        print("The response of DelinquencyRangeAndBucketsManagementApi->get_delinquency_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->get_delinquency_ranges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetDelinquencyRangesResponse]**](GetDelinquencyRangesResponse.md)

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

# **update_delinquency_bucket**
> PutDelinquencyBucketResponse update_delinquency_bucket(delinquency_bucket_id, post_delinquency_bucket_request)

Update Delinquency Bucket based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_delinquency_bucket_request import PostDelinquencyBucketRequest
from fineract_client.models.put_delinquency_bucket_response import PutDelinquencyBucketResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_bucket_id = 56 # int | delinquencyBucketId
    post_delinquency_bucket_request = fineract_client.PostDelinquencyBucketRequest() # PostDelinquencyBucketRequest | 

    try:
        # Update Delinquency Bucket based on the Id
        api_response = api_instance.update_delinquency_bucket(delinquency_bucket_id, post_delinquency_bucket_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->update_delinquency_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->update_delinquency_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_bucket_id** | **int**| delinquencyBucketId | 
 **post_delinquency_bucket_request** | [**PostDelinquencyBucketRequest**](PostDelinquencyBucketRequest.md)|  | 

### Return type

[**PutDelinquencyBucketResponse**](PutDelinquencyBucketResponse.md)

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

# **update_delinquency_range**
> PutDelinquencyRangeResponse update_delinquency_range(delinquency_range_id, post_delinquency_range_request)

Update Delinquency Range based on the Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_delinquency_range_request import PostDelinquencyRangeRequest
from fineract_client.models.put_delinquency_range_response import PutDelinquencyRangeResponse
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
    api_instance = fineract_client.DelinquencyRangeAndBucketsManagementApi(api_client)
    delinquency_range_id = 56 # int | delinquencyRangeId
    post_delinquency_range_request = fineract_client.PostDelinquencyRangeRequest() # PostDelinquencyRangeRequest | 

    try:
        # Update Delinquency Range based on the Id
        api_response = api_instance.update_delinquency_range(delinquency_range_id, post_delinquency_range_request)
        print("The response of DelinquencyRangeAndBucketsManagementApi->update_delinquency_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DelinquencyRangeAndBucketsManagementApi->update_delinquency_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delinquency_range_id** | **int**| delinquencyRangeId | 
 **post_delinquency_range_request** | [**PostDelinquencyRangeRequest**](PostDelinquencyRangeRequest.md)|  | 

### Return type

[**PutDelinquencyRangeResponse**](PutDelinquencyRangeResponse.md)

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

