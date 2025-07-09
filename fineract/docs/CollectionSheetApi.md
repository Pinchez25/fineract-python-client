# fineract_client.CollectionSheetApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_collection_sheet**](CollectionSheetApi.md#generate_collection_sheet) | **POST** /v1/collectionsheet | Generate Individual Collection Sheet | Save Collection Sheet


# **generate_collection_sheet**
> PostCollectionSheetResponse generate_collection_sheet(post_collection_sheet_request, command=command)

Generate Individual Collection Sheet | Save Collection Sheet

Generate Individual Collection Sheet:

This Api retrieves repayment details of all individual loans under a office as on a specified meeting date.

Save Collection Sheet:

This Api allows the loan officer to perform bulk repayments of individual loans and deposit of mandatory savings on a given meeting date.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_collection_sheet_request import PostCollectionSheetRequest
from fineract_client.models.post_collection_sheet_response import PostCollectionSheetResponse
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
    api_instance = fineract_client.CollectionSheetApi(api_client)
    post_collection_sheet_request = fineract_client.PostCollectionSheetRequest() # PostCollectionSheetRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Generate Individual Collection Sheet | Save Collection Sheet
        api_response = api_instance.generate_collection_sheet(post_collection_sheet_request, command=command)
        print("The response of CollectionSheetApi->generate_collection_sheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionSheetApi->generate_collection_sheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_collection_sheet_request** | [**PostCollectionSheetRequest**](PostCollectionSheetRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostCollectionSheetResponse**](PostCollectionSheetResponse.md)

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

