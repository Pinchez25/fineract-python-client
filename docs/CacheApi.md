# fineract_client.CacheApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all4**](CacheApi.md#retrieve_all4) | **GET** /v1/caches | Retrieve Cache Types
[**switch_cache**](CacheApi.md#switch_cache) | **PUT** /v1/caches | Switch Cache

# **retrieve_all4**
> list[GetCachesResponse] retrieve_all4()

Retrieve Cache Types

Returns the list of caches.  Example Requests:  caches

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
api_instance = fineract_client.CacheApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Cache Types
    api_response = api_instance.retrieve_all4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->retrieve_all4: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetCachesResponse]**](GetCachesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_cache**
> PutCachesResponse switch_cache(body)

Switch Cache

Switches the cache to chosen one.

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
api_instance = fineract_client.CacheApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutCachesRequest() # PutCachesRequest | 

try:
    # Switch Cache
    api_response = api_instance.switch_cache(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheApi->switch_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCachesRequest**](PutCachesRequest.md)|  | 

### Return type

[**PutCachesResponse**](PutCachesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

