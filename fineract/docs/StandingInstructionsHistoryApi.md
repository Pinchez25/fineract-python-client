# fineract_client.StandingInstructionsHistoryApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all20**](StandingInstructionsHistoryApi.md#retrieve_all20) | **GET** /v1/standinginstructionrunhistory | Standing Instructions Logged History


# **retrieve_all20**
> GetStandingInstructionRunHistoryResponse retrieve_all20(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type, locale=locale, date_format=date_format, from_date=from_date, to_date=to_date)

Standing Instructions Logged History

The list capability of history can support pagination and sorting 

Example Requests :

standinginstructionrunhistory

standinginstructionrunhistory?orderBy=name&sortOrder=DESC

standinginstructionrunhistory?offset=10&limit=50

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_standing_instruction_run_history_response import GetStandingInstructionRunHistoryResponse
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
    api_instance = fineract_client.StandingInstructionsHistoryApi(api_client)
    external_id = 'external_id_example' # str | externalId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    transfer_type = 56 # int | transferType (optional)
    client_name = 'client_name_example' # str | clientName (optional)
    client_id = 56 # int | clientId (optional)
    from_account_id = 56 # int | fromAccountId (optional)
    from_account_type = 56 # int | fromAccountType (optional)
    locale = 'locale_example' # str | locale (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)
    from_date = None # object | fromDate (optional)
    to_date = None # object | toDate (optional)

    try:
        # Standing Instructions Logged History
        api_response = api_instance.retrieve_all20(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type, locale=locale, date_format=date_format, from_date=from_date, to_date=to_date)
        print("The response of StandingInstructionsHistoryApi->retrieve_all20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsHistoryApi->retrieve_all20: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **transfer_type** | **int**| transferType | [optional] 
 **client_name** | **str**| clientName | [optional] 
 **client_id** | **int**| clientId | [optional] 
 **from_account_id** | **int**| fromAccountId | [optional] 
 **from_account_type** | **int**| fromAccountType | [optional] 
 **locale** | **str**| locale | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **from_date** | [**object**](.md)| fromDate | [optional] 
 **to_date** | [**object**](.md)| toDate | [optional] 

### Return type

[**GetStandingInstructionRunHistoryResponse**](GetStandingInstructionRunHistoryResponse.md)

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

