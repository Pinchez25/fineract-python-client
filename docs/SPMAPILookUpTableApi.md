# fineract_client.SPMAPILookUpTableApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lookup_table**](SPMAPILookUpTableApi.md#create_lookup_table) | **POST** /v1/surveys/{surveyId}/lookuptables | Create a Lookup Table entry
[**fetch_lookup_tables**](SPMAPILookUpTableApi.md#fetch_lookup_tables) | **GET** /v1/surveys/{surveyId}/lookuptables | List all Lookup Table entries
[**find_lookup_table**](SPMAPILookUpTableApi.md#find_lookup_table) | **GET** /v1/surveys/{surveyId}/lookuptables/{key} | Retrieve a Lookup Table entry

# **create_lookup_table**
> create_lookup_table(survey_id, body=body)

Create a Lookup Table entry

Add a new entry to a survey.  Mandatory Fields key, score, validFrom, validTo

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
api_instance = fineract_client.SPMAPILookUpTableApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId
body = fineract_client.LookupTableData() # LookupTableData |  (optional)

try:
    # Create a Lookup Table entry
    api_instance.create_lookup_table(survey_id, body=body)
except ApiException as e:
    print("Exception when calling SPMAPILookUpTableApi->create_lookup_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 
 **body** | [**LookupTableData**](LookupTableData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_lookup_tables**
> list[LookupTableData] fetch_lookup_tables(survey_id)

List all Lookup Table entries

List all Lookup Table entries for a survey.

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
api_instance = fineract_client.SPMAPILookUpTableApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId

try:
    # List all Lookup Table entries
    api_response = api_instance.fetch_lookup_tables(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SPMAPILookUpTableApi->fetch_lookup_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 

### Return type

[**list[LookupTableData]**](LookupTableData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_lookup_table**
> LookupTableData find_lookup_table(survey_id, key)

Retrieve a Lookup Table entry

Retrieve a Lookup Table entry for a survey.

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
api_instance = fineract_client.SPMAPILookUpTableApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId
key = 'key_example' # str | Enter key

try:
    # Retrieve a Lookup Table entry
    api_response = api_instance.find_lookup_table(survey_id, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SPMAPILookUpTableApi->find_lookup_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 
 **key** | **str**| Enter key | 

### Return type

[**LookupTableData**](LookupTableData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

