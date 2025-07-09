# fineract_client.InterestRateChartApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create10**](InterestRateChartApi.md#create10) | **POST** /v1/interestratecharts | Create a Chart
[**delete14**](InterestRateChartApi.md#delete14) | **DELETE** /v1/interestratecharts/{chartId} | Delete a Chart
[**retrieve_all26**](InterestRateChartApi.md#retrieve_all26) | **GET** /v1/interestratecharts | Retrieve all Charts
[**retrieve_one17**](InterestRateChartApi.md#retrieve_one17) | **GET** /v1/interestratecharts/{chartId} | Retrieve a Chart
[**template9**](InterestRateChartApi.md#template9) | **GET** /v1/interestratecharts/template | Retrieve Chart Details Template
[**update15**](InterestRateChartApi.md#update15) | **PUT** /v1/interestratecharts/{chartId} | Update a Chart


# **create10**
> PostInterestRateChartsResponse create10(post_interest_rate_charts_request)

Create a Chart

Creates a new chart which can be attached to a term deposit products (FD or RD).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_interest_rate_charts_request import PostInterestRateChartsRequest
from fineract_client.models.post_interest_rate_charts_response import PostInterestRateChartsResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)
    post_interest_rate_charts_request = fineract_client.PostInterestRateChartsRequest() # PostInterestRateChartsRequest | 

    try:
        # Create a Chart
        api_response = api_instance.create10(post_interest_rate_charts_request)
        print("The response of InterestRateChartApi->create10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateChartApi->create10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interest_rate_charts_request** | [**PostInterestRateChartsRequest**](PostInterestRateChartsRequest.md)|  | 

### Return type

[**PostInterestRateChartsResponse**](PostInterestRateChartsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete14**
> DeleteInterestRateChartsChartIdResponse delete14(chart_id)

Delete a Chart

It deletes the chart

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_interest_rate_charts_chart_id_response import DeleteInterestRateChartsChartIdResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)
    chart_id = 56 # int | chartId

    try:
        # Delete a Chart
        api_response = api_instance.delete14(chart_id)
        print("The response of InterestRateChartApi->delete14:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all26**
> List[GetInterestRateChartsResponse] retrieve_all26(product_id=product_id)

Retrieve all Charts

Retrieve list of charts associated with a term deposit product(FD or RD). Example Requests:  interestratecharts?productId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_interest_rate_charts_response import GetInterestRateChartsResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)
    product_id = 56 # int | productId (optional)

    try:
        # Retrieve all Charts
        api_response = api_instance.retrieve_all26(product_id=product_id)
        print("The response of InterestRateChartApi->retrieve_all26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateChartApi->retrieve_all26: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | [optional] 

### Return type

[**List[GetInterestRateChartsResponse]**](GetInterestRateChartsResponse.md)

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

# **retrieve_one17**
> GetInterestRateChartsResponse retrieve_one17(chart_id)

Retrieve a Chart

It retrieves the Interest Rate Chart Example Requests:  interestratecharts/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_interest_rate_charts_response import GetInterestRateChartsResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)
    chart_id = 56 # int | chartId

    try:
        # Retrieve a Chart
        api_response = api_instance.retrieve_one17(chart_id)
        print("The response of InterestRateChartApi->retrieve_one17:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template9**
> GetInterestRateChartsTemplateResponse template9()

Retrieve Chart Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for creating a chart. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  interestratecharts/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_interest_rate_charts_template_response import GetInterestRateChartsTemplateResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)

    try:
        # Retrieve Chart Details Template
        api_response = api_instance.template9()
        print("The response of InterestRateChartApi->template9:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update15**
> PutInterestRateChartsChartIdResponse update15(chart_id, put_interest_rate_charts_chart_id_request)

Update a Chart

It updates the chart

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_interest_rate_charts_chart_id_request import PutInterestRateChartsChartIdRequest
from fineract_client.models.put_interest_rate_charts_chart_id_response import PutInterestRateChartsChartIdResponse
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
    api_instance = fineract_client.InterestRateChartApi(api_client)
    chart_id = 56 # int | chartId
    put_interest_rate_charts_chart_id_request = fineract_client.PutInterestRateChartsChartIdRequest() # PutInterestRateChartsChartIdRequest | 

    try:
        # Update a Chart
        api_response = api_instance.update15(chart_id, put_interest_rate_charts_chart_id_request)
        print("The response of InterestRateChartApi->update15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateChartApi->update15: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 
 **put_interest_rate_charts_chart_id_request** | [**PutInterestRateChartsChartIdRequest**](PutInterestRateChartsChartIdRequest.md)|  | 

### Return type

[**PutInterestRateChartsChartIdResponse**](PutInterestRateChartsChartIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

