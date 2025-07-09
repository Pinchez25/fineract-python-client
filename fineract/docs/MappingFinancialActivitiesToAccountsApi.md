# fineract_client.MappingFinancialActivitiesToAccountsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_account**](MappingFinancialActivitiesToAccountsApi.md#create_gl_account) | **POST** /v1/financialactivityaccounts | Create a new Financial Activity to Accounts Mapping
[**delete_gl_account**](MappingFinancialActivitiesToAccountsApi.md#delete_gl_account) | **DELETE** /v1/financialactivityaccounts/{mappingId} | Delete a Financial Activity to Account Mapping
[**retreive**](MappingFinancialActivitiesToAccountsApi.md#retreive) | **GET** /v1/financialactivityaccounts/{mappingId} | Retrieve a Financial Activity to Account Mapping 
[**retrieve_all**](MappingFinancialActivitiesToAccountsApi.md#retrieve_all) | **GET** /v1/financialactivityaccounts | List Financial Activities to Accounts Mappings
[**retrieve_template**](MappingFinancialActivitiesToAccountsApi.md#retrieve_template) | **GET** /v1/financialactivityaccounts/template | 
[**update_gl_account**](MappingFinancialActivitiesToAccountsApi.md#update_gl_account) | **PUT** /v1/financialactivityaccounts/{mappingId} | Update a Financial Activity to Account Mapping


# **create_gl_account**
> PostFinancialActivityAccountsResponse create_gl_account(post_financial_activity_accounts_request=post_financial_activity_accounts_request)

Create a new Financial Activity to Accounts Mapping

Mandatory Fields financialActivityId, glAccountId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_financial_activity_accounts_request import PostFinancialActivityAccountsRequest
from fineract_client.models.post_financial_activity_accounts_response import PostFinancialActivityAccountsResponse
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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)
    post_financial_activity_accounts_request = fineract_client.PostFinancialActivityAccountsRequest() # PostFinancialActivityAccountsRequest |  (optional)

    try:
        # Create a new Financial Activity to Accounts Mapping
        api_response = api_instance.create_gl_account(post_financial_activity_accounts_request=post_financial_activity_accounts_request)
        print("The response of MappingFinancialActivitiesToAccountsApi->create_gl_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->create_gl_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_financial_activity_accounts_request** | [**PostFinancialActivityAccountsRequest**](PostFinancialActivityAccountsRequest.md)|  | [optional] 

### Return type

[**PostFinancialActivityAccountsResponse**](PostFinancialActivityAccountsResponse.md)

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

# **delete_gl_account**
> DeleteFinancialActivityAccountsResponse delete_gl_account(mapping_id)

Delete a Financial Activity to Account Mapping

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_financial_activity_accounts_response import DeleteFinancialActivityAccountsResponse
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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)
    mapping_id = 56 # int | mappingId

    try:
        # Delete a Financial Activity to Account Mapping
        api_response = api_instance.delete_gl_account(mapping_id)
        print("The response of MappingFinancialActivitiesToAccountsApi->delete_gl_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->delete_gl_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 

### Return type

[**DeleteFinancialActivityAccountsResponse**](DeleteFinancialActivityAccountsResponse.md)

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

# **retreive**
> GetFinancialActivityAccountsResponse retreive(mapping_id)

Retrieve a Financial Activity to Account Mapping 

Example Requests:  financialactivityaccounts/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_financial_activity_accounts_response import GetFinancialActivityAccountsResponse
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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)
    mapping_id = 56 # int | mappingId

    try:
        # Retrieve a Financial Activity to Account Mapping 
        api_response = api_instance.retreive(mapping_id)
        print("The response of MappingFinancialActivitiesToAccountsApi->retreive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->retreive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 

### Return type

[**GetFinancialActivityAccountsResponse**](GetFinancialActivityAccountsResponse.md)

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

# **retrieve_all**
> List[GetFinancialActivityAccountsResponse] retrieve_all()

List Financial Activities to Accounts Mappings

Example Requests:  financialactivityaccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_financial_activity_accounts_response import GetFinancialActivityAccountsResponse
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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)

    try:
        # List Financial Activities to Accounts Mappings
        api_response = api_instance.retrieve_all()
        print("The response of MappingFinancialActivitiesToAccountsApi->retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->retrieve_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFinancialActivityAccountsResponse]**](GetFinancialActivityAccountsResponse.md)

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

# **retrieve_template**
> str retrieve_template()



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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)

    try:
        api_response = api_instance.retrieve_template()
        print("The response of MappingFinancialActivitiesToAccountsApi->retrieve_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->retrieve_template: %s\n" % e)
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

# **update_gl_account**
> PutFinancialActivityAccountsResponse update_gl_account(mapping_id, post_financial_activity_accounts_request=post_financial_activity_accounts_request)

Update a Financial Activity to Account Mapping

the API updates the Ledger account linked to a Financial Activity 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_financial_activity_accounts_request import PostFinancialActivityAccountsRequest
from fineract_client.models.put_financial_activity_accounts_response import PutFinancialActivityAccountsResponse
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
    api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(api_client)
    mapping_id = 56 # int | mappingId
    post_financial_activity_accounts_request = fineract_client.PostFinancialActivityAccountsRequest() # PostFinancialActivityAccountsRequest |  (optional)

    try:
        # Update a Financial Activity to Account Mapping
        api_response = api_instance.update_gl_account(mapping_id, post_financial_activity_accounts_request=post_financial_activity_accounts_request)
        print("The response of MappingFinancialActivitiesToAccountsApi->update_gl_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingFinancialActivitiesToAccountsApi->update_gl_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 
 **post_financial_activity_accounts_request** | [**PostFinancialActivityAccountsRequest**](PostFinancialActivityAccountsRequest.md)|  | [optional] 

### Return type

[**PutFinancialActivityAccountsResponse**](PutFinancialActivityAccountsResponse.md)

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

