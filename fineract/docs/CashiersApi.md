# fineract_client.CashiersApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cashier_data**](CashiersApi.md#get_cashier_data) | **GET** /v1/cashiers | 


# **get_cashier_data**
> str get_cashier_data(office_id=office_id, teller_id=teller_id, staff_id=staff_id, var_date=var_date)



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
    api_instance = fineract_client.CashiersApi(api_client)
    office_id = 56 # int |  (optional)
    teller_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    var_date = 'var_date_example' # str |  (optional)

    try:
        api_response = api_instance.get_cashier_data(office_id=office_id, teller_id=teller_id, staff_id=staff_id, var_date=var_date)
        print("The response of CashiersApi->get_cashier_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashiersApi->get_cashier_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **teller_id** | **int**|  | [optional] 
 **staff_id** | **int**|  | [optional] 
 **var_date** | **str**|  | [optional] 

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

