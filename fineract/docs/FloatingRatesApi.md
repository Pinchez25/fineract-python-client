# fineract_client.FloatingRatesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_floating_rate**](FloatingRatesApi.md#create_floating_rate) | **POST** /v1/floatingrates | Create a new Floating Rate
[**retrieve_all22**](FloatingRatesApi.md#retrieve_all22) | **GET** /v1/floatingrates | List Floating Rates
[**retrieve_one13**](FloatingRatesApi.md#retrieve_one13) | **GET** /v1/floatingrates/{floatingRateId} | Retrieve Floating Rate
[**update_floating_rate**](FloatingRatesApi.md#update_floating_rate) | **PUT** /v1/floatingrates/{floatingRateId} | Update Floating Rate


# **create_floating_rate**
> PostFloatingRatesResponse create_floating_rate(post_floating_rates_request)

Create a new Floating Rate

Creates a new Floating Rate Mandatory Fields: name Optional Fields: isBaseLendingRate, isActive, ratePeriods

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_floating_rates_request import PostFloatingRatesRequest
from fineract_client.models.post_floating_rates_response import PostFloatingRatesResponse
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
    api_instance = fineract_client.FloatingRatesApi(api_client)
    post_floating_rates_request = fineract_client.PostFloatingRatesRequest() # PostFloatingRatesRequest | 

    try:
        # Create a new Floating Rate
        api_response = api_instance.create_floating_rate(post_floating_rates_request)
        print("The response of FloatingRatesApi->create_floating_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingRatesApi->create_floating_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_floating_rates_request** | [**PostFloatingRatesRequest**](PostFloatingRatesRequest.md)|  | 

### Return type

[**PostFloatingRatesResponse**](PostFloatingRatesResponse.md)

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

# **retrieve_all22**
> List[GetFloatingRatesResponse] retrieve_all22()

List Floating Rates

Lists Floating Rates

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_floating_rates_response import GetFloatingRatesResponse
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
    api_instance = fineract_client.FloatingRatesApi(api_client)

    try:
        # List Floating Rates
        api_response = api_instance.retrieve_all22()
        print("The response of FloatingRatesApi->retrieve_all22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingRatesApi->retrieve_all22: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFloatingRatesResponse]**](GetFloatingRatesResponse.md)

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

# **retrieve_one13**
> GetFloatingRatesFloatingRateIdResponse retrieve_one13(floating_rate_id)

Retrieve Floating Rate

Retrieves Floating Rate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_floating_rates_floating_rate_id_response import GetFloatingRatesFloatingRateIdResponse
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
    api_instance = fineract_client.FloatingRatesApi(api_client)
    floating_rate_id = 56 # int | floatingRateId

    try:
        # Retrieve Floating Rate
        api_response = api_instance.retrieve_one13(floating_rate_id)
        print("The response of FloatingRatesApi->retrieve_one13:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_floating_rate**
> PutFloatingRatesFloatingRateIdResponse update_floating_rate(floating_rate_id, put_floating_rates_floating_rate_id_request)

Update Floating Rate

Updates new Floating Rate. Rate Periods in the past cannot be modified. All the future rateperiods would be replaced with the new ratePeriods data sent.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_floating_rates_floating_rate_id_request import PutFloatingRatesFloatingRateIdRequest
from fineract_client.models.put_floating_rates_floating_rate_id_response import PutFloatingRatesFloatingRateIdResponse
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
    api_instance = fineract_client.FloatingRatesApi(api_client)
    floating_rate_id = 56 # int | floatingRateId
    put_floating_rates_floating_rate_id_request = fineract_client.PutFloatingRatesFloatingRateIdRequest() # PutFloatingRatesFloatingRateIdRequest | 

    try:
        # Update Floating Rate
        api_response = api_instance.update_floating_rate(floating_rate_id, put_floating_rates_floating_rate_id_request)
        print("The response of FloatingRatesApi->update_floating_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingRatesApi->update_floating_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_rate_id** | **int**| floatingRateId | 
 **put_floating_rates_floating_rate_id_request** | [**PutFloatingRatesFloatingRateIdRequest**](PutFloatingRatesFloatingRateIdRequest.md)|  | 

### Return type

[**PutFloatingRatesFloatingRateIdResponse**](PutFloatingRatesFloatingRateIdResponse.md)

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

