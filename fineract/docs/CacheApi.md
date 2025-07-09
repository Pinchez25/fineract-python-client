# fineract_client.CacheApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all4**](CacheApi.md#retrieve_all4) | **GET** /v1/caches | Retrieve Cache Types
[**switch_cache**](CacheApi.md#switch_cache) | **PUT** /v1/caches | Switch Cache


# **retrieve_all4**
> List[GetCachesResponse] retrieve_all4()

Retrieve Cache Types

Returns the list of caches.

Example Requests:

caches

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_caches_response import GetCachesResponse
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
    api_instance = fineract_client.CacheApi(api_client)

    try:
        # Retrieve Cache Types
        api_response = api_instance.retrieve_all4()
        print("The response of CacheApi->retrieve_all4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->retrieve_all4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetCachesResponse]**](GetCachesResponse.md)

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

# **switch_cache**
> PutCachesResponse switch_cache(put_caches_request)

Switch Cache

Switches the cache to chosen one.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_caches_request import PutCachesRequest
from fineract_client.models.put_caches_response import PutCachesResponse
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
    api_instance = fineract_client.CacheApi(api_client)
    put_caches_request = fineract_client.PutCachesRequest() # PutCachesRequest | 

    try:
        # Switch Cache
        api_response = api_instance.switch_cache(put_caches_request)
        print("The response of CacheApi->switch_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->switch_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_caches_request** | [**PutCachesRequest**](PutCachesRequest.md)|  | 

### Return type

[**PutCachesResponse**](PutCachesResponse.md)

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

