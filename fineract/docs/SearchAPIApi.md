# fineract_client.SearchAPIApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_search**](SearchAPIApi.md#advanced_search) | **POST** /v1/search/advance | Adhoc query search
[**retrieve_ad_hoc_search_query_template**](SearchAPIApi.md#retrieve_ad_hoc_search_query_template) | **GET** /v1/search/template | Retrive Adhoc Search query template
[**search_data**](SearchAPIApi.md#search_data) | **GET** /v1/search | Search Resources


# **advanced_search**
> List[PostAdhocQuerySearchResponse] advanced_search(post_adhoc_query_search_request)

Adhoc query search

AdHocQuery search has more search options, it is a POST request, it uses request body to send search parameters   Mandatory fields:entities  Optional fields:loanStatus, loanProducts, offices, loanDateOption, loanFromDate, loanToDate,  includeOutStandingAmountPercentage, outStandingAmountPercentageCondition,  minOutStandingAmountPercentage and maxOutStandingAmountPercentage OR outStandingAmountPercentage,  includeOutstandingAmount, outstandingAmountCondition,  minOutstandingAmount and maxOutstandingAmount OR outstandingAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_adhoc_query_search_request import PostAdhocQuerySearchRequest
from fineract_client.models.post_adhoc_query_search_response import PostAdhocQuerySearchResponse
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
    api_instance = fineract_client.SearchAPIApi(api_client)
    post_adhoc_query_search_request = fineract_client.PostAdhocQuerySearchRequest() # PostAdhocQuerySearchRequest | 

    try:
        # Adhoc query search
        api_response = api_instance.advanced_search(post_adhoc_query_search_request)
        print("The response of SearchAPIApi->advanced_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAPIApi->advanced_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_adhoc_query_search_request** | [**PostAdhocQuerySearchRequest**](PostAdhocQuerySearchRequest.md)|  | 

### Return type

[**List[PostAdhocQuerySearchResponse]**](PostAdhocQuerySearchResponse.md)

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

# **retrieve_ad_hoc_search_query_template**
> GetSearchResponse retrieve_ad_hoc_search_query_template()

Retrive Adhoc Search query template

Mandatory Fields  search?query=000000001 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_search_response import GetSearchResponse
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
    api_instance = fineract_client.SearchAPIApi(api_client)

    try:
        # Retrive Adhoc Search query template
        api_response = api_instance.retrieve_ad_hoc_search_query_template()
        print("The response of SearchAPIApi->retrieve_ad_hoc_search_query_template:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_data**
> List[GetSearchResponse] search_data(query=query, resource=resource, exact_match=exact_match)

Search Resources

Example Requests:  search?query=000000001   search?query=Petra&resource=clients,groups   search?query=Petra&resource=clients,groups&exactMatch=true

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_search_response import GetSearchResponse
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
    api_instance = fineract_client.SearchAPIApi(api_client)
    query = 'query_example' # str | query (optional)
    resource = 'resource_example' # str | resource (optional)
    exact_match = False # bool | exactMatch (optional) (default to False)

    try:
        # Search Resources
        api_response = api_instance.search_data(query=query, resource=resource, exact_match=exact_match)
        print("The response of SearchAPIApi->search_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAPIApi->search_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | [optional] 
 **resource** | **str**| resource | [optional] 
 **exact_match** | **bool**| exactMatch | [optional] [default to False]

### Return type

[**List[GetSearchResponse]**](GetSearchResponse.md)

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

