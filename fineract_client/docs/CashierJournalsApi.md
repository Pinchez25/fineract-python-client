# fineract_client.CashierJournalsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_journal_data1**](CashierJournalsApi.md#get_journal_data1) | **GET** /v1/cashiersjournal | 


# **get_journal_data1**
> str get_journal_data1(office_id=office_id, teller_id=teller_id, cashier_id=cashier_id, date_range=date_range)

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
    api_instance = fineract_client.CashierJournalsApi(api_client)
    office_id = 56 # int |  (optional)
    teller_id = 56 # int |  (optional)
    cashier_id = 56 # int |  (optional)
    date_range = 'date_range_example' # str |  (optional)

    try:
        api_response = api_instance.get_journal_data1(office_id=office_id, teller_id=teller_id, cashier_id=cashier_id, date_range=date_range)
        print("The response of CashierJournalsApi->get_journal_data1:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

