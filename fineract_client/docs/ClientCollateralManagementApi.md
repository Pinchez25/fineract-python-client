# fineract_client.ClientCollateralManagementApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_collateral**](ClientCollateralManagementApi.md#add_collateral) | **POST** /v1/clients/{clientId}/collaterals | Add New Collateral For a Client
[**delete_collateral1**](ClientCollateralManagementApi.md#delete_collateral1) | **DELETE** /v1/clients/{clientId}/collaterals/{collateralId} | Delete Client Collateral
[**get_client_collateral**](ClientCollateralManagementApi.md#get_client_collateral) | **GET** /v1/clients/{clientId}/collaterals | Get Clients Collateral Products
[**get_client_collateral_data**](ClientCollateralManagementApi.md#get_client_collateral_data) | **GET** /v1/clients/{clientId}/collaterals/{clientCollateralId} | Get Client Collateral Data
[**get_client_collateral_template**](ClientCollateralManagementApi.md#get_client_collateral_template) | **GET** /v1/clients/{clientId}/collaterals/template | Get Client Collateral Template
[**update_collateral1**](ClientCollateralManagementApi.md#update_collateral1) | **PUT** /v1/clients/{clientId}/collaterals/{collateralId} | Update New Collateral of a Client


# **add_collateral**
> PostClientCollateralResponse add_collateral(client_id, post_client_collateral_request)

Add New Collateral For a Client

Add New Collateral For a Client

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_client_collateral_request import PostClientCollateralRequest
from fineract_client.models.post_client_collateral_response import PostClientCollateralResponse
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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId
    post_client_collateral_request = fineract_client.PostClientCollateralRequest() # PostClientCollateralRequest | 

    try:
        # Add New Collateral For a Client
        api_response = api_instance.add_collateral(client_id, post_client_collateral_request)
        print("The response of ClientCollateralManagementApi->add_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->add_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **post_client_collateral_request** | [**PostClientCollateralRequest**](PostClientCollateralRequest.md)|  | 

### Return type

[**PostClientCollateralResponse**](PostClientCollateralResponse.md)

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

# **delete_collateral1**
> DeleteClientCollateralResponse delete_collateral1(client_id, collateral_id)

Delete Client Collateral

Delete Client Collateral

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_client_collateral_response import DeleteClientCollateralResponse
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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId
    collateral_id = 56 # int | collateralId

    try:
        # Delete Client Collateral
        api_response = api_instance.delete_collateral1(client_id, collateral_id)
        print("The response of ClientCollateralManagementApi->delete_collateral1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->delete_collateral1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**DeleteClientCollateralResponse**](DeleteClientCollateralResponse.md)

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

# **get_client_collateral**
> List[object] get_client_collateral(client_id, prod_id=prod_id)

Get Clients Collateral Products

Get Collateral Product of a Client

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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId
    prod_id = 56 # int | prodId (optional)

    try:
        # Get Clients Collateral Products
        api_response = api_instance.get_client_collateral(client_id, prod_id=prod_id)
        print("The response of ClientCollateralManagementApi->get_client_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->get_client_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **prod_id** | **int**| prodId | [optional] 

### Return type

**List[object]**

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

# **get_client_collateral_data**
> object get_client_collateral_data(client_id, client_collateral_id)

Get Client Collateral Data

Get Client Collateral Data

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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId
    client_collateral_id = 56 # int | clientCollateralId

    try:
        # Get Client Collateral Data
        api_response = api_instance.get_client_collateral_data(client_id, client_collateral_id)
        print("The response of ClientCollateralManagementApi->get_client_collateral_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->get_client_collateral_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **client_collateral_id** | **int**| clientCollateralId | 

### Return type

**object**

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

# **get_client_collateral_template**
> List[GetLoanCollateralManagementTemplate] get_client_collateral_template(client_id)

Get Client Collateral Template

Get Client Collateral Template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_collateral_management_template import GetLoanCollateralManagementTemplate
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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId

    try:
        # Get Client Collateral Template
        api_response = api_instance.get_client_collateral_template(client_id)
        print("The response of ClientCollateralManagementApi->get_client_collateral_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->get_client_collateral_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**List[GetLoanCollateralManagementTemplate]**](GetLoanCollateralManagementTemplate.md)

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

# **update_collateral1**
> PutClientCollateralResponse update_collateral1(client_id, collateral_id, put_client_collateral_request)

Update New Collateral of a Client

Update New Collateral of a Client

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_client_collateral_request import PutClientCollateralRequest
from fineract_client.models.put_client_collateral_response import PutClientCollateralResponse
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
    api_instance = fineract_client.ClientCollateralManagementApi(api_client)
    client_id = 56 # int | clientId
    collateral_id = 56 # int | collateralId
    put_client_collateral_request = fineract_client.PutClientCollateralRequest() # PutClientCollateralRequest | 

    try:
        # Update New Collateral of a Client
        api_response = api_instance.update_collateral1(client_id, collateral_id, put_client_collateral_request)
        print("The response of ClientCollateralManagementApi->update_collateral1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCollateralManagementApi->update_collateral1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **collateral_id** | **int**| collateralId | 
 **put_client_collateral_request** | [**PutClientCollateralRequest**](PutClientCollateralRequest.md)|  | 

### Return type

[**PutClientCollateralResponse**](PutClientCollateralResponse.md)

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

