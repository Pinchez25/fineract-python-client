# fineract_client.CurrencyApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_currencies**](CurrencyApi.md#retrieve_currencies) | **GET** /v1/currencies | Retrieve Currency Configuration
[**update_currencies**](CurrencyApi.md#update_currencies) | **PUT** /v1/currencies | Update Currency Configuration

# **retrieve_currencies**
> GetCurrenciesResponse retrieve_currencies()

Retrieve Currency Configuration

Returns the list of currencies permitted for use AND the list of currencies not selected (but available for selection).  Example Requests:  currencies   currencies?fields=selectedCurrencyOptions

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
api_instance = fineract_client.CurrencyApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Currency Configuration
    api_response = api_instance.retrieve_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->retrieve_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCurrenciesResponse**](GetCurrenciesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currencies**
> PutCurrenciesResponse update_currencies(body)

Update Currency Configuration

Updates the list of currencies permitted for use.

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
api_instance = fineract_client.CurrencyApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutCurrenciesRequest() # PutCurrenciesRequest | 

try:
    # Update Currency Configuration
    api_response = api_instance.update_currencies(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->update_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCurrenciesRequest**](PutCurrenciesRequest.md)|  | 

### Return type

[**PutCurrenciesResponse**](PutCurrenciesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

