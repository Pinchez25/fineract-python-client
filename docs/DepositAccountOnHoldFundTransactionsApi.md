# fineract_client.DepositAccountOnHoldFundTransactionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all28**](DepositAccountOnHoldFundTransactionsApi.md#retrieve_all28) | **GET** /v1/savingsaccounts/{savingsId}/onholdtransactions | 

# **retrieve_all28**
> str retrieve_all28(savings_id, guarantor_funding_id=guarantor_funding_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)



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
api_instance = fineract_client.DepositAccountOnHoldFundTransactionsApi(fineract_client.ApiClient(configuration))
savings_id = 789 # int | 
guarantor_funding_id = 789 # int |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_all28(savings_id, guarantor_funding_id=guarantor_funding_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositAccountOnHoldFundTransactionsApi->retrieve_all28: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_id** | **int**|  | 
 **guarantor_funding_id** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

