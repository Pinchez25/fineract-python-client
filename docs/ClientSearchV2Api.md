# fineract_client.ClientSearchV2Api

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_by_text**](ClientSearchV2Api.md#search_by_text) | **POST** /v2/clients/search | Search Clients by text

# **search_by_text**
> PageClientSearchData search_by_text(body=body)

Search Clients by text

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
api_instance = fineract_client.ClientSearchV2Api(fineract_client.ApiClient(configuration))
body = fineract_client.PagedRequestClientTextSearch() # PagedRequestClientTextSearch |  (optional)

try:
    # Search Clients by text
    api_response = api_instance.search_by_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientSearchV2Api->search_by_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PagedRequestClientTextSearch**](PagedRequestClientTextSearch.md)|  | [optional] 

### Return type

[**PageClientSearchData**](PageClientSearchData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

