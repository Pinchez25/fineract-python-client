# fineract_client.SelfShareAccountsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account1**](SelfShareAccountsApi.md#create_account1) | **POST** /v1/self/shareaccounts | Submit new share application
[**retrieve_share_account**](SelfShareAccountsApi.md#retrieve_share_account) | **GET** /v1/self/shareaccounts/{accountId} | Retrieve a share application/account
[**template19**](SelfShareAccountsApi.md#template19) | **GET** /v1/self/shareaccounts/template | Retrieve Share Account Template


# **create_account1**
> List[PostNewShareApplicationResponse] create_account1(body=body)

Submit new share application

Mandatory fields:  clientId, productId, submittedDate, savingsAccountId, requestedShares, applicationDate   Optional Fields  accountNo, externalId   Inherited from Product (if not provided)  minimumActivePeriod, minimumActivePeriodFrequencyType, lockinPeriodFrequency, lockinPeriodFrequencyType.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_new_share_application_response import PostNewShareApplicationResponse
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
    api_instance = fineract_client.SelfShareAccountsApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Submit new share application
        api_response = api_instance.create_account1(body=body)
        print("The response of SelfShareAccountsApi->create_account1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfShareAccountsApi->create_account1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**List[PostNewShareApplicationResponse]**](PostNewShareApplicationResponse.md)

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

# **retrieve_share_account**
> str retrieve_share_account(account_id)

Retrieve a share application/account

   Example Requests:  self/shareaccounts/12 

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
    api_instance = fineract_client.SelfShareAccountsApi(api_client)
    account_id = 56 # int | 

    try:
        # Retrieve a share application/account
        api_response = api_instance.retrieve_share_account(account_id)
        print("The response of SelfShareAccountsApi->retrieve_share_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfShareAccountsApi->retrieve_share_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

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

# **template19**
> List[GetShareAccountsClientIdProductIdResponse] template19(client_id=client_id, product_id=product_id)

Retrieve Share Account Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of: Field Defaults  Allowed Value Lists   Arguments  clientId:Integer mandatory productId:Integer optionalIf entered, productId, productName and selectedProduct fields are returned. Example Requests:  self/shareaccounts/template?clientId=14  self/shareaccounts/template?clientId=14&productId=3 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_share_accounts_client_id_product_id_response import GetShareAccountsClientIdProductIdResponse
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
    api_instance = fineract_client.SelfShareAccountsApi(api_client)
    client_id = 56 # int |  (optional)
    product_id = 56 # int |  (optional)

    try:
        # Retrieve Share Account Template
        api_response = api_instance.template19(client_id=client_id, product_id=product_id)
        print("The response of SelfShareAccountsApi->template19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfShareAccountsApi->template19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | [optional] 
 **product_id** | **int**|  | [optional] 

### Return type

[**List[GetShareAccountsClientIdProductIdResponse]**](GetShareAccountsClientIdProductIdResponse.md)

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

