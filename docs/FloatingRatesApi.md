# fineract_client.FloatingRatesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_floating_rate**](FloatingRatesApi.md#create_floating_rate) | **POST** /v1/floatingrates | Create a new Floating Rate
[**retrieve_all22**](FloatingRatesApi.md#retrieve_all22) | **GET** /v1/floatingrates | List Floating Rates
[**retrieve_one13**](FloatingRatesApi.md#retrieve_one13) | **GET** /v1/floatingrates/{floatingRateId} | Retrieve Floating Rate
[**update_floating_rate**](FloatingRatesApi.md#update_floating_rate) | **PUT** /v1/floatingrates/{floatingRateId} | Update Floating Rate

# **create_floating_rate**
> PostFloatingRatesResponse create_floating_rate(body)

Create a new Floating Rate

Creates a new Floating Rate Mandatory Fields: name Optional Fields: isBaseLendingRate, isActive, ratePeriods

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
api_instance = fineract_client.FloatingRatesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostFloatingRatesRequest() # PostFloatingRatesRequest | 

try:
    # Create a new Floating Rate
    api_response = api_instance.create_floating_rate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloatingRatesApi->create_floating_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostFloatingRatesRequest**](PostFloatingRatesRequest.md)|  | 

### Return type

[**PostFloatingRatesResponse**](PostFloatingRatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all22**
> list[GetFloatingRatesResponse] retrieve_all22()

List Floating Rates

Lists Floating Rates

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
api_instance = fineract_client.FloatingRatesApi(fineract_client.ApiClient(configuration))

try:
    # List Floating Rates
    api_response = api_instance.retrieve_all22()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloatingRatesApi->retrieve_all22: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetFloatingRatesResponse]**](GetFloatingRatesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one13**
> GetFloatingRatesFloatingRateIdResponse retrieve_one13(floating_rate_id)

Retrieve Floating Rate

Retrieves Floating Rate

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
api_instance = fineract_client.FloatingRatesApi(fineract_client.ApiClient(configuration))
floating_rate_id = 789 # int | floatingRateId

try:
    # Retrieve Floating Rate
    api_response = api_instance.retrieve_one13(floating_rate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloatingRatesApi->retrieve_one13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_rate_id** | **int**| floatingRateId | 

### Return type

[**GetFloatingRatesFloatingRateIdResponse**](GetFloatingRatesFloatingRateIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_floating_rate**
> PutFloatingRatesFloatingRateIdResponse update_floating_rate(body, floating_rate_id)

Update Floating Rate

Updates new Floating Rate. Rate Periods in the past cannot be modified. All the future rateperiods would be replaced with the new ratePeriods data sent.

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
api_instance = fineract_client.FloatingRatesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutFloatingRatesFloatingRateIdRequest() # PutFloatingRatesFloatingRateIdRequest | 
floating_rate_id = 789 # int | floatingRateId

try:
    # Update Floating Rate
    api_response = api_instance.update_floating_rate(body, floating_rate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FloatingRatesApi->update_floating_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutFloatingRatesFloatingRateIdRequest**](PutFloatingRatesFloatingRateIdRequest.md)|  | 
 **floating_rate_id** | **int**| floatingRateId | 

### Return type

[**PutFloatingRatesFloatingRateIdResponse**](PutFloatingRatesFloatingRateIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

