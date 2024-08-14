# fineract_client.InterestRateChartApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create10**](InterestRateChartApi.md#create10) | **POST** /v1/interestratecharts | Create a Chart
[**delete14**](InterestRateChartApi.md#delete14) | **DELETE** /v1/interestratecharts/{chartId} | Delete a Chart
[**retrieve_all26**](InterestRateChartApi.md#retrieve_all26) | **GET** /v1/interestratecharts | Retrieve all Charts
[**retrieve_one17**](InterestRateChartApi.md#retrieve_one17) | **GET** /v1/interestratecharts/{chartId} | Retrieve a Chart
[**template9**](InterestRateChartApi.md#template9) | **GET** /v1/interestratecharts/template | Retrieve Chart Details Template
[**update15**](InterestRateChartApi.md#update15) | **PUT** /v1/interestratecharts/{chartId} | Update a Chart

# **create10**
> PostInterestRateChartsResponse create10(body)

Create a Chart

Creates a new chart which can be attached to a term deposit products (FD or RD).

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostInterestRateChartsRequest() # PostInterestRateChartsRequest | 

try:
    # Create a Chart
    api_response = api_instance.create10(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->create10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostInterestRateChartsRequest**](PostInterestRateChartsRequest.md)|  | 

### Return type

[**PostInterestRateChartsResponse**](PostInterestRateChartsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete14**
> DeleteInterestRateChartsChartIdResponse delete14(chart_id)

Delete a Chart

It deletes the chart

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId

try:
    # Delete a Chart
    api_response = api_instance.delete14(chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->delete14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 

### Return type

[**DeleteInterestRateChartsChartIdResponse**](DeleteInterestRateChartsChartIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all26**
> list[GetInterestRateChartsResponse] retrieve_all26(product_id=product_id)

Retrieve all Charts

Retrieve list of charts associated with a term deposit product(FD or RD). Example Requests:  interestratecharts?productId=1

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId (optional)

try:
    # Retrieve all Charts
    api_response = api_instance.retrieve_all26(product_id=product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->retrieve_all26: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | [optional] 

### Return type

[**list[GetInterestRateChartsResponse]**](GetInterestRateChartsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one17**
> GetInterestRateChartsResponse retrieve_one17(chart_id)

Retrieve a Chart

It retrieves the Interest Rate Chart Example Requests:  interestratecharts/1

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))
chart_id = 789 # int | chartId

try:
    # Retrieve a Chart
    api_response = api_instance.retrieve_one17(chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->retrieve_one17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 

### Return type

[**GetInterestRateChartsResponse**](GetInterestRateChartsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template9**
> GetInterestRateChartsTemplateResponse template9()

Retrieve Chart Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for creating a chart. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  interestratecharts/template

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Chart Details Template
    api_response = api_instance.template9()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->template9: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInterestRateChartsTemplateResponse**](GetInterestRateChartsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update15**
> PutInterestRateChartsChartIdResponse update15(body, chart_id)

Update a Chart

It updates the chart

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
api_instance = fineract_client.InterestRateChartApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutInterestRateChartsChartIdRequest() # PutInterestRateChartsChartIdRequest | 
chart_id = 789 # int | chartId

try:
    # Update a Chart
    api_response = api_instance.update15(body, chart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterestRateChartApi->update15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutInterestRateChartsChartIdRequest**](PutInterestRateChartsChartIdRequest.md)|  | 
 **chart_id** | **int**| chartId | 

### Return type

[**PutInterestRateChartsChartIdResponse**](PutInterestRateChartsChartIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

