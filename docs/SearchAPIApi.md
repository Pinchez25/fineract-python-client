# fineract_client.SearchAPIApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_search**](SearchAPIApi.md#advanced_search) | **POST** /v1/search/advance | Adhoc query search
[**retrieve_ad_hoc_search_query_template**](SearchAPIApi.md#retrieve_ad_hoc_search_query_template) | **GET** /v1/search/template | Retrive Adhoc Search query template
[**search_data**](SearchAPIApi.md#search_data) | **GET** /v1/search | Search Resources

# **advanced_search**
> list[PostAdhocQuerySearchResponse] advanced_search(body)

Adhoc query search

AdHocQuery search has more search options, it is a POST request, it uses request body to send search parameters   Mandatory fields:entities  Optional fields:loanStatus, loanProducts, offices, loanDateOption, loanFromDate, loanToDate,  includeOutStandingAmountPercentage, outStandingAmountPercentageCondition,  minOutStandingAmountPercentage and maxOutStandingAmountPercentage OR outStandingAmountPercentage,  includeOutstandingAmount, outstandingAmountCondition,  minOutstandingAmount and maxOutstandingAmount OR outstandingAmount

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
api_instance = fineract_client.SearchAPIApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostAdhocQuerySearchRequest() # PostAdhocQuerySearchRequest | 

try:
    # Adhoc query search
    api_response = api_instance.advanced_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAPIApi->advanced_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAdhocQuerySearchRequest**](PostAdhocQuerySearchRequest.md)|  | 

### Return type

[**list[PostAdhocQuerySearchResponse]**](PostAdhocQuerySearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_ad_hoc_search_query_template**
> GetSearchResponse retrieve_ad_hoc_search_query_template()

Retrive Adhoc Search query template

Mandatory Fields  search?query=000000001 

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
api_instance = fineract_client.SearchAPIApi(fineract_client.ApiClient(configuration))

try:
    # Retrive Adhoc Search query template
    api_response = api_instance.retrieve_ad_hoc_search_query_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAPIApi->retrieve_ad_hoc_search_query_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSearchResponse**](GetSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_data**
> list[GetSearchResponse] search_data(query=query, resource=resource, exact_match=exact_match)

Search Resources

Example Requests:  search?query=000000001   search?query=Petra&resource=clients,groups   search?query=Petra&resource=clients,groups&exactMatch=true

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
api_instance = fineract_client.SearchAPIApi(fineract_client.ApiClient(configuration))
query = 'query_example' # str | query (optional)
resource = 'resource_example' # str | resource (optional)
exact_match = false # bool | exactMatch (optional) (default to false)

try:
    # Search Resources
    api_response = api_instance.search_data(query=query, resource=resource, exact_match=exact_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchAPIApi->search_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | [optional] 
 **resource** | **str**| resource | [optional] 
 **exact_match** | **bool**| exactMatch | [optional] [default to false]

### Return type

[**list[GetSearchResponse]**](GetSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

