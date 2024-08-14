# fineract_client.InterestRateSlabAKAInterestBandsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create9**](InterestRateSlabAKAInterestBandsApi.md#create9) | **POST** /v1/interestratecharts/{chartId}/chartslabs | Create a Slab
[**delete13**](InterestRateSlabAKAInterestBandsApi.md#delete13) | **DELETE** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Delete a Slab
[**retrieve_all25**](InterestRateSlabAKAInterestBandsApi.md#retrieve_all25) | **GET** /v1/interestratecharts/{chartId}/chartslabs | Retrieve all Slabs
[**retrieve_one16**](InterestRateSlabAKAInterestBandsApi.md#retrieve_one16) | **GET** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Retrieve a Slab
[**template8**](InterestRateSlabAKAInterestBandsApi.md#template8) | **GET** /v1/interestratecharts/{chartId}/chartslabs/template | 
[**update14**](InterestRateSlabAKAInterestBandsApi.md#update14) | **PUT** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Update a Slab

# **create9**
> PostInterestRateChartsChartIdChartSlabsResponse create9(body, chart_id)

Create a Slab

Creates a new interest rate slab for an interest rate chart. Mandatory Fields periodType, fromPeriod, annualInterestRate Optional Fields toPeriod and description Example Requests:  interestratecharts/1/chartslabs

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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostInterestRateChartsChartIdChartSlabsRequest() # PostInterestRateChartsChartIdChartSlabsRequest | 
chart_id = 789 # int | chartId

try:
    # Create a Slab
    api_response = api_instance.create9(body, chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->create9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostInterestRateChartsChartIdChartSlabsRequest**](PostInterestRateChartsChartIdChartSlabsRequest.md)|  | 
 **chart_id** | **int**| chartId | 

### Return type

[**PostInterestRateChartsChartIdChartSlabsResponse**](PostInterestRateChartsChartIdChartSlabsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete13**
> DeleteInterestRateChartsChartIdChartSlabsResponse delete13(chart_id, chart_slab_id)

Delete a Slab

Delete a Slab from a chart

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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId
chart_slab_id = 789 # int | chartSlabId

try:
    # Delete a Slab
    api_response = api_instance.delete13(chart_id, chart_slab_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->delete13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 
 **chart_slab_id** | **int**| chartSlabId | 

### Return type

[**DeleteInterestRateChartsChartIdChartSlabsResponse**](DeleteInterestRateChartsChartIdChartSlabsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all25**
> list[GetInterestRateChartsChartIdChartSlabsResponse] retrieve_all25(chart_id)

Retrieve all Slabs

Retrieve list of slabs associated with a chart  Example Requests:  interestratecharts/1/chartslabs

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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId

try:
    # Retrieve all Slabs
    api_response = api_instance.retrieve_all25(chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->retrieve_all25: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 

### Return type

[**list[GetInterestRateChartsChartIdChartSlabsResponse]**](GetInterestRateChartsChartIdChartSlabsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one16**
> GetInterestRateChartsChartIdChartSlabsResponse retrieve_one16(chart_id, chart_slab_id)

Retrieve a Slab

Retrieve a slab associated with an Interest rate chart  Example Requests:  interestratecharts/1/chartslabs/1 

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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId
chart_slab_id = 789 # int | chartSlabId

try:
    # Retrieve a Slab
    api_response = api_instance.retrieve_one16(chart_id, chart_slab_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->retrieve_one16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 
 **chart_slab_id** | **int**| chartSlabId | 

### Return type

[**GetInterestRateChartsChartIdChartSlabsResponse**](GetInterestRateChartsChartIdChartSlabsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template8**
> str template8(chart_id)



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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId

try:
    api_response = api_instance.template8(chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->template8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update14**
> PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse update14(body, chart_id, chart_slab_id)

Update a Slab

It updates the Slab from chart

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
api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest() # PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest | 
chart_id = 789 # int | chartId
chart_slab_id = 789 # int | chartSlabId

try:
    # Update a Slab
    api_response = api_instance.update14(body, chart_id, chart_slab_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateSlabAKAInterestBandsApi->update14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest**](PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest.md)|  | 
 **chart_id** | **int**| chartId | 
 **chart_slab_id** | **int**| chartSlabId | 

### Return type

[**PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse**](PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

