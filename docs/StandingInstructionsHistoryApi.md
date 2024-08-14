# fineract_client.StandingInstructionsHistoryApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all20**](StandingInstructionsHistoryApi.md#retrieve_all20) | **GET** /v1/standinginstructionrunhistory | Standing Instructions Logged History

# **retrieve_all20**
> GetStandingInstructionRunHistoryResponse retrieve_all20(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type, locale=locale, date_format=date_format, from_date=from_date, to_date=to_date)

Standing Instructions Logged History

The list capability of history can support pagination and sorting   Example Requests :  standinginstructionrunhistory  standinginstructionrunhistory?orderBy=name&sortOrder=DESC  standinginstructionrunhistory?offset=10&limit=50

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
api_instance = fineract_client.StandingInstructionsHistoryApi(fineract_client.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
transfer_type = 56 # int | transferType (optional)
client_name = 'client_name_example' # str | clientName (optional)
client_id = 789 # int | clientId (optional)
from_account_id = 789 # int | fromAccountId (optional)
from_account_type = 56 # int | fromAccountType (optional)
locale = 'locale_example' # str | locale (optional)
date_format = 'date_format_example' # str | dateFormat (optional)
from_date = fineract_client.DateParam() # DateParam | fromDate (optional)
to_date = fineract_client.DateParam() # DateParam | toDate (optional)

try:
    # Standing Instructions Logged History
    api_response = api_instance.retrieve_all20(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type, locale=locale, date_format=date_format, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
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
 **from_date** | [**DateParam**](.md)| fromDate | [optional] 
 **to_date** | [**DateParam**](.md)| toDate | [optional] 

### Return type

[**GetStandingInstructionRunHistoryResponse**](GetStandingInstructionRunHistoryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

