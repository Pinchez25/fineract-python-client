# fineract_client.SelfDividendApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dividend_detail**](SelfDividendApi.md#create_dividend_detail) | **POST** /v1/shareproduct/{productId}/dividend | 
[**delete_dividend_detail**](SelfDividendApi.md#delete_dividend_detail) | **DELETE** /v1/shareproduct/{productId}/dividend/{dividendId} | 
[**retrieve_all39**](SelfDividendApi.md#retrieve_all39) | **GET** /v1/shareproduct/{productId}/dividend | 
[**retrieve_dividend_details**](SelfDividendApi.md#retrieve_dividend_details) | **GET** /v1/shareproduct/{productId}/dividend/{dividendId} | 
[**update_dividend_detail**](SelfDividendApi.md#update_dividend_detail) | **PUT** /v1/shareproduct/{productId}/dividend/{dividendId} | 


# **create_dividend_detail**
> str create_dividend_detail(product_id, body=body)

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
    api_instance = fineract_client.SelfDividendApi(api_client)
    product_id = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.create_dividend_detail(product_id, body=body)
        print("The response of SelfDividendApi->create_dividend_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfDividendApi->create_dividend_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dividend_detail**
> str delete_dividend_detail(product_id, dividend_id)

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
    api_instance = fineract_client.SelfDividendApi(api_client)
    product_id = 56 # int | 
    dividend_id = 56 # int | 

    try:
        api_response = api_instance.delete_dividend_detail(product_id, dividend_id)
        print("The response of SelfDividendApi->delete_dividend_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfDividendApi->delete_dividend_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **dividend_id** | **int**|  | 

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

# **retrieve_all39**
> str retrieve_all39(product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, status=status)

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
    api_instance = fineract_client.SelfDividendApi(api_client)
    product_id = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)
    status = 56 # int |  (optional)

    try:
        api_response = api_instance.retrieve_all39(product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, status=status)
        print("The response of SelfDividendApi->retrieve_all39:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfDividendApi->retrieve_all39: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **status** | **int**|  | [optional] 

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

# **retrieve_dividend_details**
> str retrieve_dividend_details(dividend_id, product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no)

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
    api_instance = fineract_client.SelfDividendApi(api_client)
    dividend_id = 56 # int | 
    product_id = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)
    account_no = 'account_no_example' # str |  (optional)

    try:
        api_response = api_instance.retrieve_dividend_details(dividend_id, product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no)
        print("The response of SelfDividendApi->retrieve_dividend_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfDividendApi->retrieve_dividend_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dividend_id** | **int**|  | 
 **product_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **account_no** | **str**|  | [optional] 

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

# **update_dividend_detail**
> str update_dividend_detail(product_id, dividend_id, command=command, body=body)

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
    api_instance = fineract_client.SelfDividendApi(api_client)
    product_id = 56 # int | 
    dividend_id = 56 # int | 
    command = 'command_example' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.update_dividend_detail(product_id, dividend_id, command=command, body=body)
        print("The response of SelfDividendApi->update_dividend_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfDividendApi->update_dividend_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **dividend_id** | **int**|  | 
 **command** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

