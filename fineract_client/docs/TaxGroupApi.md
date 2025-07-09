# fineract_client.TaxGroupApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_group**](TaxGroupApi.md#create_tax_group) | **POST** /v1/taxes/group | Create a new Tax Group
[**retrieve_all_tax_groups**](TaxGroupApi.md#retrieve_all_tax_groups) | **GET** /v1/taxes/group | List Tax Group
[**retrieve_tax_group**](TaxGroupApi.md#retrieve_tax_group) | **GET** /v1/taxes/group/{taxGroupId} | Retrieve Tax Group
[**retrieve_template22**](TaxGroupApi.md#retrieve_template22) | **GET** /v1/taxes/group/template | 
[**update_tax_group**](TaxGroupApi.md#update_tax_group) | **PUT** /v1/taxes/group/{taxGroupId} | Update Tax Group


# **create_tax_group**
> PostTaxesGroupResponse create_tax_group(post_taxes_group_request)

Create a new Tax Group

Create a new Tax Group
Mandatory Fields: name and taxComponents
Mandatory Fields in taxComponents: taxComponentId
Optional Fields in taxComponents: id, startDate and endDate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_taxes_group_request import PostTaxesGroupRequest
from fineract_client.models.post_taxes_group_response import PostTaxesGroupResponse
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
    api_instance = fineract_client.TaxGroupApi(api_client)
    post_taxes_group_request = fineract_client.PostTaxesGroupRequest() # PostTaxesGroupRequest | 

    try:
        # Create a new Tax Group
        api_response = api_instance.create_tax_group(post_taxes_group_request)
        print("The response of TaxGroupApi->create_tax_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxGroupApi->create_tax_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_taxes_group_request** | [**PostTaxesGroupRequest**](PostTaxesGroupRequest.md)|  | 

### Return type

[**PostTaxesGroupResponse**](PostTaxesGroupResponse.md)

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

# **retrieve_all_tax_groups**
> List[GetTaxesGroupResponse] retrieve_all_tax_groups()

List Tax Group

List Tax Group

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_taxes_group_response import GetTaxesGroupResponse
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
    api_instance = fineract_client.TaxGroupApi(api_client)

    try:
        # List Tax Group
        api_response = api_instance.retrieve_all_tax_groups()
        print("The response of TaxGroupApi->retrieve_all_tax_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxGroupApi->retrieve_all_tax_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetTaxesGroupResponse]**](GetTaxesGroupResponse.md)

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

# **retrieve_tax_group**
> GetTaxesGroupResponse retrieve_tax_group(tax_group_id)

Retrieve Tax Group

Retrieve Tax Group

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_taxes_group_response import GetTaxesGroupResponse
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
    api_instance = fineract_client.TaxGroupApi(api_client)
    tax_group_id = 56 # int | taxGroupId

    try:
        # Retrieve Tax Group
        api_response = api_instance.retrieve_tax_group(tax_group_id)
        print("The response of TaxGroupApi->retrieve_tax_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxGroupApi->retrieve_tax_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_group_id** | **int**| taxGroupId | 

### Return type

[**GetTaxesGroupResponse**](GetTaxesGroupResponse.md)

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

# **retrieve_template22**
> str retrieve_template22()

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
    api_instance = fineract_client.TaxGroupApi(api_client)

    try:
        api_response = api_instance.retrieve_template22()
        print("The response of TaxGroupApi->retrieve_template22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxGroupApi->retrieve_template22: %s\n" % e)
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

# **update_tax_group**
> PutTaxesGroupTaxGroupIdResponse update_tax_group(tax_group_id, put_taxes_group_tax_group_id_request)

Update Tax Group

Updates Tax Group. Only end date can be up-datable and can insert new tax components.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_taxes_group_tax_group_id_request import PutTaxesGroupTaxGroupIdRequest
from fineract_client.models.put_taxes_group_tax_group_id_response import PutTaxesGroupTaxGroupIdResponse
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
    api_instance = fineract_client.TaxGroupApi(api_client)
    tax_group_id = 56 # int | taxGroupId
    put_taxes_group_tax_group_id_request = fineract_client.PutTaxesGroupTaxGroupIdRequest() # PutTaxesGroupTaxGroupIdRequest | 

    try:
        # Update Tax Group
        api_response = api_instance.update_tax_group(tax_group_id, put_taxes_group_tax_group_id_request)
        print("The response of TaxGroupApi->update_tax_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxGroupApi->update_tax_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_group_id** | **int**| taxGroupId | 
 **put_taxes_group_tax_group_id_request** | [**PutTaxesGroupTaxGroupIdRequest**](PutTaxesGroupTaxGroupIdRequest.md)|  | 

### Return type

[**PutTaxesGroupTaxGroupIdResponse**](PutTaxesGroupTaxGroupIdResponse.md)

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

