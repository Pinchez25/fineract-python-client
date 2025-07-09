# fineract_client.SPMAPILookUpTableApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lookup_table**](SPMAPILookUpTableApi.md#create_lookup_table) | **POST** /v1/surveys/{surveyId}/lookuptables | Create a Lookup Table entry
[**fetch_lookup_tables**](SPMAPILookUpTableApi.md#fetch_lookup_tables) | **GET** /v1/surveys/{surveyId}/lookuptables | List all Lookup Table entries
[**find_lookup_table**](SPMAPILookUpTableApi.md#find_lookup_table) | **GET** /v1/surveys/{surveyId}/lookuptables/{key} | Retrieve a Lookup Table entry


# **create_lookup_table**
> create_lookup_table(survey_id, lookup_table_data=lookup_table_data)

Create a Lookup Table entry

Add a new entry to a survey.  Mandatory Fields key, score, validFrom, validTo

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.lookup_table_data import LookupTableData
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
    api_instance = fineract_client.SPMAPILookUpTableApi(api_client)
    survey_id = 56 # int | Enter surveyId
    lookup_table_data = fineract_client.LookupTableData() # LookupTableData |  (optional)

    try:
        # Create a Lookup Table entry
        api_instance.create_lookup_table(survey_id, lookup_table_data=lookup_table_data)
    except Exception as e:
        print("Exception when calling SPMAPILookUpTableApi->create_lookup_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 
 **lookup_table_data** | [**LookupTableData**](LookupTableData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_lookup_tables**
> List[LookupTableData] fetch_lookup_tables(survey_id)

List all Lookup Table entries

List all Lookup Table entries for a survey.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.lookup_table_data import LookupTableData
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
    api_instance = fineract_client.SPMAPILookUpTableApi(api_client)
    survey_id = 56 # int | Enter surveyId

    try:
        # List all Lookup Table entries
        api_response = api_instance.fetch_lookup_tables(survey_id)
        print("The response of SPMAPILookUpTableApi->fetch_lookup_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SPMAPILookUpTableApi->fetch_lookup_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 

### Return type

[**List[LookupTableData]**](LookupTableData.md)

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

# **find_lookup_table**
> LookupTableData find_lookup_table(survey_id, key)

Retrieve a Lookup Table entry

Retrieve a Lookup Table entry for a survey.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.lookup_table_data import LookupTableData
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
    api_instance = fineract_client.SPMAPILookUpTableApi(api_client)
    survey_id = 56 # int | Enter surveyId
    key = 'key_example' # str | Enter key

    try:
        # Retrieve a Lookup Table entry
        api_response = api_instance.find_lookup_table(survey_id, key)
        print("The response of SPMAPILookUpTableApi->find_lookup_table:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

