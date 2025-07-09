# fineract_client.TaxComponentsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_compoent**](TaxComponentsApi.md#create_tax_compoent) | **POST** /v1/taxes/component | Create a new Tax Component
[**retrieve_all_tax_components**](TaxComponentsApi.md#retrieve_all_tax_components) | **GET** /v1/taxes/component | List Tax Components
[**retrieve_tax_component**](TaxComponentsApi.md#retrieve_tax_component) | **GET** /v1/taxes/component/{taxComponentId} | Retrieve Tax Component
[**retrieve_template21**](TaxComponentsApi.md#retrieve_template21) | **GET** /v1/taxes/component/template | 
[**update_tax_compoent**](TaxComponentsApi.md#update_tax_compoent) | **PUT** /v1/taxes/component/{taxComponentId} | Update Tax Component


# **create_tax_compoent**
> PostTaxesComponentsResponse create_tax_compoent(post_taxes_components_request)

Create a new Tax Component

Creates a new Tax Component  Mandatory Fields: name, percentage  Optional Fields: debitAccountType, debitAcountId, creditAccountType, creditAcountId, startDate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_taxes_components_request import PostTaxesComponentsRequest
from fineract_client.models.post_taxes_components_response import PostTaxesComponentsResponse
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
    api_instance = fineract_client.TaxComponentsApi(api_client)
    post_taxes_components_request = fineract_client.PostTaxesComponentsRequest() # PostTaxesComponentsRequest | 

    try:
        # Create a new Tax Component
        api_response = api_instance.create_tax_compoent(post_taxes_components_request)
        print("The response of TaxComponentsApi->create_tax_compoent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxComponentsApi->create_tax_compoent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_taxes_components_request** | [**PostTaxesComponentsRequest**](PostTaxesComponentsRequest.md)|  | 

### Return type

[**PostTaxesComponentsResponse**](PostTaxesComponentsResponse.md)

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

# **retrieve_all_tax_components**
> List[GetTaxesComponentsResponse] retrieve_all_tax_components()

List Tax Components

List Tax Components

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_taxes_components_response import GetTaxesComponentsResponse
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
    api_instance = fineract_client.TaxComponentsApi(api_client)

    try:
        # List Tax Components
        api_response = api_instance.retrieve_all_tax_components()
        print("The response of TaxComponentsApi->retrieve_all_tax_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxComponentsApi->retrieve_all_tax_components: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetTaxesComponentsResponse]**](GetTaxesComponentsResponse.md)

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

# **retrieve_tax_component**
> GetTaxesComponentsResponse retrieve_tax_component(tax_component_id)

Retrieve Tax Component

Retrieve Tax Component

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_taxes_components_response import GetTaxesComponentsResponse
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
    api_instance = fineract_client.TaxComponentsApi(api_client)
    tax_component_id = 56 # int | taxComponentId

    try:
        # Retrieve Tax Component
        api_response = api_instance.retrieve_tax_component(tax_component_id)
        print("The response of TaxComponentsApi->retrieve_tax_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxComponentsApi->retrieve_tax_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_component_id** | **int**| taxComponentId | 

### Return type

[**GetTaxesComponentsResponse**](GetTaxesComponentsResponse.md)

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

# **retrieve_template21**
> str retrieve_template21()



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
    api_instance = fineract_client.TaxComponentsApi(api_client)

    try:
        api_response = api_instance.retrieve_template21()
        print("The response of TaxComponentsApi->retrieve_template21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxComponentsApi->retrieve_template21: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **update_tax_compoent**
> PutTaxesComponentsTaxComponentIdResponse update_tax_compoent(tax_component_id, put_taxes_components_tax_component_id_request)

Update Tax Component

Updates Tax component. Debit and credit account details cannot be modified. All the future tax components would be replaced with the new percentage.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_taxes_components_tax_component_id_request import PutTaxesComponentsTaxComponentIdRequest
from fineract_client.models.put_taxes_components_tax_component_id_response import PutTaxesComponentsTaxComponentIdResponse
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
    api_instance = fineract_client.TaxComponentsApi(api_client)
    tax_component_id = 56 # int | taxComponentId
    put_taxes_components_tax_component_id_request = fineract_client.PutTaxesComponentsTaxComponentIdRequest() # PutTaxesComponentsTaxComponentIdRequest | 

    try:
        # Update Tax Component
        api_response = api_instance.update_tax_compoent(tax_component_id, put_taxes_components_tax_component_id_request)
        print("The response of TaxComponentsApi->update_tax_compoent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxComponentsApi->update_tax_compoent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_component_id** | **int**| taxComponentId | 
 **put_taxes_components_tax_component_id_request** | [**PutTaxesComponentsTaxComponentIdRequest**](PutTaxesComponentsTaxComponentIdRequest.md)|  | 

### Return type

[**PutTaxesComponentsTaxComponentIdResponse**](PutTaxesComponentsTaxComponentIdResponse.md)

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

