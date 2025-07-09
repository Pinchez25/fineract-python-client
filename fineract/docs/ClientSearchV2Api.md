# fineract_client.ClientSearchV2Api

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_by_text**](ClientSearchV2Api.md#search_by_text) | **POST** /v2/clients/search | Search Clients by text


# **search_by_text**
> PageClientSearchData search_by_text(paged_request_client_text_search=paged_request_client_text_search)

Search Clients by text

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.page_client_search_data import PageClientSearchData
from fineract_client.models.paged_request_client_text_search import PagedRequestClientTextSearch
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
    api_instance = fineract_client.ClientSearchV2Api(api_client)
    paged_request_client_text_search = fineract_client.PagedRequestClientTextSearch() # PagedRequestClientTextSearch |  (optional)

    try:
        # Search Clients by text
        api_response = api_instance.search_by_text(paged_request_client_text_search=paged_request_client_text_search)
        print("The response of ClientSearchV2Api->search_by_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientSearchV2Api->search_by_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paged_request_client_text_search** | [**PagedRequestClientTextSearch**](PagedRequestClientTextSearch.md)|  | [optional] 

### Return type

[**PageClientSearchData**](PageClientSearchData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

