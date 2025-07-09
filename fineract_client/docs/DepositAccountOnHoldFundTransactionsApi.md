# fineract_client.DepositAccountOnHoldFundTransactionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all28**](DepositAccountOnHoldFundTransactionsApi.md#retrieve_all28) | **GET** /v1/savingsaccounts/{savingsId}/onholdtransactions | 


# **retrieve_all28**
> str retrieve_all28(savings_id, guarantor_funding_id=guarantor_funding_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.DepositAccountOnHoldFundTransactionsApi(api_client)
    savings_id = 56 # int | 
    guarantor_funding_id = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)

    try:
        api_response = api_instance.retrieve_all28(savings_id, guarantor_funding_id=guarantor_funding_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of DepositAccountOnHoldFundTransactionsApi->retrieve_all28:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

