# fineract_client.FundsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fund**](FundsApi.md#create_fund) | **POST** /v1/funds | Create a Fund
[**retrieve_fund**](FundsApi.md#retrieve_fund) | **GET** /v1/funds/{fundId} | Retrieve a Fund
[**retrieve_funds**](FundsApi.md#retrieve_funds) | **GET** /v1/funds | Retrieve Funds
[**update_fund**](FundsApi.md#update_fund) | **PUT** /v1/funds/{fundId} | Update a Fund


# **create_fund**
> PostFundsResponse create_fund(post_funds_request)

Create a Fund

Creates a Fund

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_funds_request import PostFundsRequest
from fineract_client.models.post_funds_response import PostFundsResponse
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
    api_instance = fineract_client.FundsApi(api_client)
    post_funds_request = fineract_client.PostFundsRequest() # PostFundsRequest | 

    try:
        # Create a Fund
        api_response = api_instance.create_fund(post_funds_request)
        print("The response of FundsApi->create_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->create_fund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_funds_request** | [**PostFundsRequest**](PostFundsRequest.md)|  | 

### Return type

[**PostFundsResponse**](PostFundsResponse.md)

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

# **retrieve_fund**
> GetFundsResponse retrieve_fund(fund_id)

Retrieve a Fund

Returns the details of a Fund.  Example Requests:  funds/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_funds_response import GetFundsResponse
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
    api_instance = fineract_client.FundsApi(api_client)
    fund_id = 56 # int | fundId

    try:
        # Retrieve a Fund
        api_response = api_instance.retrieve_fund(fund_id)
        print("The response of FundsApi->retrieve_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->retrieve_fund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fund_id** | **int**| fundId | 

### Return type

[**GetFundsResponse**](GetFundsResponse.md)

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

# **retrieve_funds**
> List[GetFundsResponse] retrieve_funds()

Retrieve Funds

Returns the list of funds.  Example Requests:  funds

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_funds_response import GetFundsResponse
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
    api_instance = fineract_client.FundsApi(api_client)

    try:
        # Retrieve Funds
        api_response = api_instance.retrieve_funds()
        print("The response of FundsApi->retrieve_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->retrieve_funds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFundsResponse]**](GetFundsResponse.md)

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

# **update_fund**
> PutFundsFundIdResponse update_fund(fund_id, put_funds_fund_id_request)

Update a Fund

Updates the details of a fund.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_funds_fund_id_request import PutFundsFundIdRequest
from fineract_client.models.put_funds_fund_id_response import PutFundsFundIdResponse
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
    api_instance = fineract_client.FundsApi(api_client)
    fund_id = 56 # int | fundId
    put_funds_fund_id_request = fineract_client.PutFundsFundIdRequest() # PutFundsFundIdRequest | 

    try:
        # Update a Fund
        api_response = api_instance.update_fund(fund_id, put_funds_fund_id_request)
        print("The response of FundsApi->update_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->update_fund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fund_id** | **int**| fundId | 
 **put_funds_fund_id_request** | [**PutFundsFundIdRequest**](PutFundsFundIdRequest.md)|  | 

### Return type

[**PutFundsFundIdResponse**](PutFundsFundIdResponse.md)

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

