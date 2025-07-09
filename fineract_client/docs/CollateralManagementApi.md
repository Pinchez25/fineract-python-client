# fineract_client.CollateralManagementApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collateral1**](CollateralManagementApi.md#create_collateral1) | **POST** /v1/collateral-management | Create a new collateral
[**delete_collateral2**](CollateralManagementApi.md#delete_collateral2) | **DELETE** /v1/collateral-management/{collateralId} | Delete a Collateral
[**get_all_collaterals**](CollateralManagementApi.md#get_all_collaterals) | **GET** /v1/collateral-management | Get All Collaterals
[**get_collateral**](CollateralManagementApi.md#get_collateral) | **GET** /v1/collateral-management/{collateralId} | Get Collateral
[**get_collateral_template**](CollateralManagementApi.md#get_collateral_template) | **GET** /v1/collateral-management/template | Get Collateral Template
[**update_collateral2**](CollateralManagementApi.md#update_collateral2) | **PUT** /v1/collateral-management/{collateralId} | Update Collateral


# **create_collateral1**
> PostCollateralManagementProductResponse create_collateral1(post_collateral_management_product_request)

Create a new collateral

Collateral Creation

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_collateral_management_product_request import PostCollateralManagementProductRequest
from fineract_client.models.post_collateral_management_product_response import PostCollateralManagementProductResponse
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
    api_instance = fineract_client.CollateralManagementApi(api_client)
    post_collateral_management_product_request = fineract_client.PostCollateralManagementProductRequest() # PostCollateralManagementProductRequest | 

    try:
        # Create a new collateral
        api_response = api_instance.create_collateral1(post_collateral_management_product_request)
        print("The response of CollateralManagementApi->create_collateral1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->create_collateral1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_collateral_management_product_request** | [**PostCollateralManagementProductRequest**](PostCollateralManagementProductRequest.md)|  | 

### Return type

[**PostCollateralManagementProductResponse**](PostCollateralManagementProductResponse.md)

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

# **delete_collateral2**
> DeleteCollateralProductResponse delete_collateral2(collateral_id)

Delete a Collateral

Delete Collateral

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_collateral_product_response import DeleteCollateralProductResponse
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
    api_instance = fineract_client.CollateralManagementApi(api_client)
    collateral_id = 56 # int | collateralId

    try:
        # Delete a Collateral
        api_response = api_instance.delete_collateral2(collateral_id)
        print("The response of CollateralManagementApi->delete_collateral2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->delete_collateral2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 

### Return type

[**DeleteCollateralProductResponse**](DeleteCollateralProductResponse.md)

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

# **get_all_collaterals**
> List[GetCollateralManagementsResponse] get_all_collaterals()

Get All Collaterals

Fetch all Collateral Products

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_collateral_managements_response import GetCollateralManagementsResponse
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
    api_instance = fineract_client.CollateralManagementApi(api_client)

    try:
        # Get All Collaterals
        api_response = api_instance.get_all_collaterals()
        print("The response of CollateralManagementApi->get_all_collaterals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->get_all_collaterals: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetCollateralManagementsResponse]**](GetCollateralManagementsResponse.md)

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

# **get_collateral**
> GetCollateralManagementsResponse get_collateral(collateral_id)

Get Collateral

Fetch Collateral

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_collateral_managements_response import GetCollateralManagementsResponse
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
    api_instance = fineract_client.CollateralManagementApi(api_client)
    collateral_id = 56 # int | collateralId

    try:
        # Get Collateral
        api_response = api_instance.get_collateral(collateral_id)
        print("The response of CollateralManagementApi->get_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->get_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 

### Return type

[**GetCollateralManagementsResponse**](GetCollateralManagementsResponse.md)

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

# **get_collateral_template**
> List[GetCollateralProductTemplate] get_collateral_template()

Get Collateral Template

Get Collateral Template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_collateral_product_template import GetCollateralProductTemplate
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
    api_instance = fineract_client.CollateralManagementApi(api_client)

    try:
        # Get Collateral Template
        api_response = api_instance.get_collateral_template()
        print("The response of CollateralManagementApi->get_collateral_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->get_collateral_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetCollateralProductTemplate]**](GetCollateralProductTemplate.md)

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

# **update_collateral2**
> PutCollateralProductResponse update_collateral2(collateral_id, put_collateral_product_request)

Update Collateral

Update Collateral

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_collateral_product_request import PutCollateralProductRequest
from fineract_client.models.put_collateral_product_response import PutCollateralProductResponse
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
    api_instance = fineract_client.CollateralManagementApi(api_client)
    collateral_id = 56 # int | collateralId
    put_collateral_product_request = fineract_client.PutCollateralProductRequest() # PutCollateralProductRequest | 

    try:
        # Update Collateral
        api_response = api_instance.update_collateral2(collateral_id, put_collateral_product_request)
        print("The response of CollateralManagementApi->update_collateral2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollateralManagementApi->update_collateral2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 
 **put_collateral_product_request** | [**PutCollateralProductRequest**](PutCollateralProductRequest.md)|  | 

### Return type

[**PutCollateralProductResponse**](PutCollateralProductResponse.md)

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

