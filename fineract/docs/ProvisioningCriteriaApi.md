# fineract_client.ProvisioningCriteriaApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_criteria**](ProvisioningCriteriaApi.md#create_provisioning_criteria) | **POST** /v1/provisioningcriteria | Create a new Provisioning Criteria
[**delete_provisioning_criteria**](ProvisioningCriteriaApi.md#delete_provisioning_criteria) | **DELETE** /v1/provisioningcriteria/{criteriaId} | Deletes Provisioning Criteria
[**retrieve_all_provisioning_criterias**](ProvisioningCriteriaApi.md#retrieve_all_provisioning_criterias) | **GET** /v1/provisioningcriteria | Retrieves all created Provisioning Criterias
[**retrieve_provisioning_criteria**](ProvisioningCriteriaApi.md#retrieve_provisioning_criteria) | **GET** /v1/provisioningcriteria/{criteriaId} | Retrieves a Provisioning Criteria
[**retrieve_template3**](ProvisioningCriteriaApi.md#retrieve_template3) | **GET** /v1/provisioningcriteria/template | 
[**update_provisioning_criteria**](ProvisioningCriteriaApi.md#update_provisioning_criteria) | **PUT** /v1/provisioningcriteria/{criteriaId} | Updates a new Provisioning Criteria


# **create_provisioning_criteria**
> PostProvisioningCriteriaResponse create_provisioning_criteria(post_provisioning_criteria_request)

Create a new Provisioning Criteria

Creates a new Provisioning Criteria

Mandatory Fields: 
criteriaName
provisioningcriteria

Optional Fields: 
loanProducts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_provisioning_criteria_request import PostProvisioningCriteriaRequest
from fineract_client.models.post_provisioning_criteria_response import PostProvisioningCriteriaResponse
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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)
    post_provisioning_criteria_request = fineract_client.PostProvisioningCriteriaRequest() # PostProvisioningCriteriaRequest | 

    try:
        # Create a new Provisioning Criteria
        api_response = api_instance.create_provisioning_criteria(post_provisioning_criteria_request)
        print("The response of ProvisioningCriteriaApi->create_provisioning_criteria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->create_provisioning_criteria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_provisioning_criteria_request** | [**PostProvisioningCriteriaRequest**](PostProvisioningCriteriaRequest.md)|  | 

### Return type

[**PostProvisioningCriteriaResponse**](PostProvisioningCriteriaResponse.md)

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

# **delete_provisioning_criteria**
> DeleteProvisioningCriteriaResponse delete_provisioning_criteria(criteria_id)

Deletes Provisioning Criteria

Deletes Provisioning Criteria

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_provisioning_criteria_response import DeleteProvisioningCriteriaResponse
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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)
    criteria_id = 56 # int | criteriaId

    try:
        # Deletes Provisioning Criteria
        api_response = api_instance.delete_provisioning_criteria(criteria_id)
        print("The response of ProvisioningCriteriaApi->delete_provisioning_criteria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->delete_provisioning_criteria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria_id** | **int**| criteriaId | 

### Return type

[**DeleteProvisioningCriteriaResponse**](DeleteProvisioningCriteriaResponse.md)

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

# **retrieve_all_provisioning_criterias**
> List[GetProvisioningCriteriaResponse] retrieve_all_provisioning_criterias()

Retrieves all created Provisioning Criterias

Retrieves all created Provisioning Criterias

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_provisioning_criteria_response import GetProvisioningCriteriaResponse
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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)

    try:
        # Retrieves all created Provisioning Criterias
        api_response = api_instance.retrieve_all_provisioning_criterias()
        print("The response of ProvisioningCriteriaApi->retrieve_all_provisioning_criterias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->retrieve_all_provisioning_criterias: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetProvisioningCriteriaResponse]**](GetProvisioningCriteriaResponse.md)

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

# **retrieve_provisioning_criteria**
> GetProvisioningCriteriaCriteriaIdResponse retrieve_provisioning_criteria(criteria_id)

Retrieves a Provisioning Criteria

Retrieves a Provisioning Criteria

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_provisioning_criteria_criteria_id_response import GetProvisioningCriteriaCriteriaIdResponse
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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)
    criteria_id = 56 # int | criteriaId

    try:
        # Retrieves a Provisioning Criteria
        api_response = api_instance.retrieve_provisioning_criteria(criteria_id)
        print("The response of ProvisioningCriteriaApi->retrieve_provisioning_criteria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->retrieve_provisioning_criteria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria_id** | **int**| criteriaId | 

### Return type

[**GetProvisioningCriteriaCriteriaIdResponse**](GetProvisioningCriteriaCriteriaIdResponse.md)

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

# **retrieve_template3**
> str retrieve_template3()

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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)

    try:
        api_response = api_instance.retrieve_template3()
        print("The response of ProvisioningCriteriaApi->retrieve_template3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->retrieve_template3: %s\n" % e)
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

# **update_provisioning_criteria**
> PutProvisioningCriteriaResponse update_provisioning_criteria(criteria_id, put_provisioning_criteria_request)

Updates a new Provisioning Criteria

Updates a new Provisioning Criteria

Optional Fields
criteriaName, loanProducts, provisioningcriteria

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_provisioning_criteria_request import PutProvisioningCriteriaRequest
from fineract_client.models.put_provisioning_criteria_response import PutProvisioningCriteriaResponse
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
    api_instance = fineract_client.ProvisioningCriteriaApi(api_client)
    criteria_id = 56 # int | criteriaId
    put_provisioning_criteria_request = fineract_client.PutProvisioningCriteriaRequest() # PutProvisioningCriteriaRequest | 

    try:
        # Updates a new Provisioning Criteria
        api_response = api_instance.update_provisioning_criteria(criteria_id, put_provisioning_criteria_request)
        print("The response of ProvisioningCriteriaApi->update_provisioning_criteria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningCriteriaApi->update_provisioning_criteria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria_id** | **int**| criteriaId | 
 **put_provisioning_criteria_request** | [**PutProvisioningCriteriaRequest**](PutProvisioningCriteriaRequest.md)|  | 

### Return type

[**PutProvisioningCriteriaResponse**](PutProvisioningCriteriaResponse.md)

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

