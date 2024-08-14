# fineract_client.LoanAccountLockApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_locked_accounts**](LoanAccountLockApi.md#retrieve_locked_accounts) | **GET** /v1/loans/locked | List locked loan accounts

# **retrieve_locked_accounts**
> GetLoanAccountLockResponse retrieve_locked_accounts(page=page, limit=limit)

List locked loan accounts

Returns the locked loan IDs

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
api_instance = fineract_client.LoanAccountLockApi(fineract_client.ApiClient(configuration))
page = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # List locked loan accounts
    api_response = api_instance.retrieve_locked_accounts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanAccountLockApi->retrieve_locked_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**GetLoanAccountLockResponse**](GetLoanAccountLockResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

