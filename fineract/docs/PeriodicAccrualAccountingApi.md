# fineract_client.PeriodicAccrualAccountingApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_periodic_accrual_accounting**](PeriodicAccrualAccountingApi.md#execute_periodic_accrual_accounting) | **POST** /v1/runaccruals | Executes Periodic Accrual Accounting


# **execute_periodic_accrual_accounting**
> execute_periodic_accrual_accounting(post_runaccruals_request)

Executes Periodic Accrual Accounting

Mandatory Fields  tillDate 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_runaccruals_request import PostRunaccrualsRequest
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
    api_instance = fineract_client.PeriodicAccrualAccountingApi(api_client)
    post_runaccruals_request = fineract_client.PostRunaccrualsRequest() # PostRunaccrualsRequest | 

    try:
        # Executes Periodic Accrual Accounting
        api_instance.execute_periodic_accrual_accounting(post_runaccruals_request)
    except Exception as e:
        print("Exception when calling PeriodicAccrualAccountingApi->execute_periodic_accrual_accounting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_runaccruals_request** | [**PostRunaccrualsRequest**](PostRunaccrualsRequest.md)|  | 

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

