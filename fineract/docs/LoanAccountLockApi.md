# fineract_client.LoanAccountLockApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_locked_accounts**](LoanAccountLockApi.md#retrieve_locked_accounts) | **GET** /v1/loans/locked | List locked loan accounts


# **retrieve_locked_accounts**
> GetLoanAccountLockResponse retrieve_locked_accounts(page=page, limit=limit)

List locked loan accounts

Returns the locked loan IDs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_account_lock_response import GetLoanAccountLockResponse
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
    api_instance = fineract_client.LoanAccountLockApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List locked loan accounts
        api_response = api_instance.retrieve_locked_accounts(page=page, limit=limit)
        print("The response of LoanAccountLockApi->retrieve_locked_accounts:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

