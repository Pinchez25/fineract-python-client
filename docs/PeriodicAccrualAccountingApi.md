# fineract_client.PeriodicAccrualAccountingApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_periodic_accrual_accounting**](PeriodicAccrualAccountingApi.md#execute_periodic_accrual_accounting) | **POST** /v1/runaccruals | Executes Periodic Accrual Accounting

# **execute_periodic_accrual_accounting**
> execute_periodic_accrual_accounting(body)

Executes Periodic Accrual Accounting

Mandatory Fields  tillDate 

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
api_instance = fineract_client.PeriodicAccrualAccountingApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostRunaccrualsRequest() # PostRunaccrualsRequest | 

try:
    # Executes Periodic Accrual Accounting
    api_instance.execute_periodic_accrual_accounting(body)
except ApiException as e:
    print("Exception when calling PeriodicAccrualAccountingApi->execute_periodic_accrual_accounting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRunaccrualsRequest**](PostRunaccrualsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

