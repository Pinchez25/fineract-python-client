# fineract_client.CashierJournalsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_journal_data1**](CashierJournalsApi.md#get_journal_data1) | **GET** /v1/cashiersjournal | 

# **get_journal_data1**
> str get_journal_data1(office_id=office_id, teller_id=teller_id, cashier_id=cashier_id, date_range=date_range)



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
api_instance = fineract_client.CashierJournalsApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
teller_id = 789 # int |  (optional)
cashier_id = 789 # int |  (optional)
date_range = 'date_range_example' # str |  (optional)

try:
    api_response = api_instance.get_journal_data1(office_id=office_id, teller_id=teller_id, cashier_id=cashier_id, date_range=date_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CashierJournalsApi->get_journal_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **teller_id** | **int**|  | [optional] 
 **cashier_id** | **int**|  | [optional] 
 **date_range** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

