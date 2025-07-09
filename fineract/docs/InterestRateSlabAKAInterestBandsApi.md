# fineract_client.InterestRateSlabAKAInterestBandsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create9**](InterestRateSlabAKAInterestBandsApi.md#create9) | **POST** /v1/interestratecharts/{chartId}/chartslabs | Create a Slab
[**delete13**](InterestRateSlabAKAInterestBandsApi.md#delete13) | **DELETE** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Delete a Slab
[**retrieve_all25**](InterestRateSlabAKAInterestBandsApi.md#retrieve_all25) | **GET** /v1/interestratecharts/{chartId}/chartslabs | Retrieve all Slabs
[**retrieve_one16**](InterestRateSlabAKAInterestBandsApi.md#retrieve_one16) | **GET** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Retrieve a Slab
[**template8**](InterestRateSlabAKAInterestBandsApi.md#template8) | **GET** /v1/interestratecharts/{chartId}/chartslabs/template | 
[**update14**](InterestRateSlabAKAInterestBandsApi.md#update14) | **PUT** /v1/interestratecharts/{chartId}/chartslabs/{chartSlabId} | Update a Slab


# **create9**
> PostInterestRateChartsChartIdChartSlabsResponse create9(chart_id, post_interest_rate_charts_chart_id_chart_slabs_request)

Create a Slab

Creates a new interest rate slab for an interest rate chart. Mandatory Fields periodType, fromPeriod, annualInterestRate Optional Fields toPeriod and description Example Requests:  interestratecharts/1/chartslabs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_interest_rate_charts_chart_id_chart_slabs_request import PostInterestRateChartsChartIdChartSlabsRequest
from fineract_client.models.post_interest_rate_charts_chart_id_chart_slabs_response import PostInterestRateChartsChartIdChartSlabsResponse
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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId
    post_interest_rate_charts_chart_id_chart_slabs_request = fineract_client.PostInterestRateChartsChartIdChartSlabsRequest() # PostInterestRateChartsChartIdChartSlabsRequest | 

    try:
        # Create a Slab
        api_response = api_instance.create9(chart_id, post_interest_rate_charts_chart_id_chart_slabs_request)
        print("The response of InterestRateSlabAKAInterestBandsApi->create9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateSlabAKAInterestBandsApi->create9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 
 **post_interest_rate_charts_chart_id_chart_slabs_request** | [**PostInterestRateChartsChartIdChartSlabsRequest**](PostInterestRateChartsChartIdChartSlabsRequest.md)|  | 

### Return type

[**PostInterestRateChartsChartIdChartSlabsResponse**](PostInterestRateChartsChartIdChartSlabsResponse.md)

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

# **delete13**
> DeleteInterestRateChartsChartIdChartSlabsResponse delete13(chart_id, chart_slab_id)

Delete a Slab

Delete a Slab from a chart

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_interest_rate_charts_chart_id_chart_slabs_response import DeleteInterestRateChartsChartIdChartSlabsResponse
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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId
    chart_slab_id = 56 # int | chartSlabId

    try:
        # Delete a Slab
        api_response = api_instance.delete13(chart_id, chart_slab_id)
        print("The response of InterestRateSlabAKAInterestBandsApi->delete13:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all25**
> List[GetInterestRateChartsChartIdChartSlabsResponse] retrieve_all25(chart_id)

Retrieve all Slabs

Retrieve list of slabs associated with a chart  Example Requests:  interestratecharts/1/chartslabs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_interest_rate_charts_chart_id_chart_slabs_response import GetInterestRateChartsChartIdChartSlabsResponse
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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId

    try:
        # Retrieve all Slabs
        api_response = api_instance.retrieve_all25(chart_id)
        print("The response of InterestRateSlabAKAInterestBandsApi->retrieve_all25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateSlabAKAInterestBandsApi->retrieve_all25: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 

### Return type

[**List[GetInterestRateChartsChartIdChartSlabsResponse]**](GetInterestRateChartsChartIdChartSlabsResponse.md)

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

# **retrieve_one16**
> GetInterestRateChartsChartIdChartSlabsResponse retrieve_one16(chart_id, chart_slab_id)

Retrieve a Slab

Retrieve a slab associated with an Interest rate chart  Example Requests:  interestratecharts/1/chartslabs/1 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_interest_rate_charts_chart_id_chart_slabs_response import GetInterestRateChartsChartIdChartSlabsResponse
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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId
    chart_slab_id = 56 # int | chartSlabId

    try:
        # Retrieve a Slab
        api_response = api_instance.retrieve_one16(chart_id, chart_slab_id)
        print("The response of InterestRateSlabAKAInterestBandsApi->retrieve_one16:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template8**
> str template8(chart_id)



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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId

    try:
        api_response = api_instance.template8(chart_id)
        print("The response of InterestRateSlabAKAInterestBandsApi->template8:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update14**
> PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse update14(chart_id, chart_slab_id, put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_request)

Update a Slab

It updates the Slab from chart

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_request import PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest
from fineract_client.models.put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_response import PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse
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
    api_instance = fineract_client.InterestRateSlabAKAInterestBandsApi(api_client)
    chart_id = 56 # int | chartId
    chart_slab_id = 56 # int | chartSlabId
    put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_request = fineract_client.PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest() # PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest | 

    try:
        # Update a Slab
        api_response = api_instance.update14(chart_id, chart_slab_id, put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_request)
        print("The response of InterestRateSlabAKAInterestBandsApi->update14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterestRateSlabAKAInterestBandsApi->update14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_id** | **int**| chartId | 
 **chart_slab_id** | **int**| chartSlabId | 
 **put_interest_rate_charts_chart_id_chart_slabs_chart_slab_id_request** | [**PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest**](PutInterestRateChartsChartIdChartSlabsChartSlabIdRequest.md)|  | 

### Return type

[**PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse**](PutInterestRateChartsChartIdChartSlabsChartSlabIdResponse.md)

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

