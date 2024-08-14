# fineract_client.CollectionSheetApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_collection_sheet**](CollectionSheetApi.md#generate_collection_sheet) | **POST** /v1/collectionsheet | Generate Individual Collection Sheet | Save Collection Sheet

# **generate_collection_sheet**
> PostCollectionSheetResponse generate_collection_sheet(body, command=command)

Generate Individual Collection Sheet | Save Collection Sheet

Generate Individual Collection Sheet:  This Api retrieves repayment details of all individual loans under a office as on a specified meeting date.  Save Collection Sheet:  This Api allows the loan officer to perform bulk repayments of individual loans and deposit of mandatory savings on a given meeting date.

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
api_instance = fineract_client.CollectionSheetApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostCollectionSheetRequest() # PostCollectionSheetRequest | 
command = 'command_example' # str | command (optional)

try:
    # Generate Individual Collection Sheet | Save Collection Sheet
    api_response = api_instance.generate_collection_sheet(body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionSheetApi->generate_collection_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCollectionSheetRequest**](PostCollectionSheetRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostCollectionSheetResponse**](PostCollectionSheetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

