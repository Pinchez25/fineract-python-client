# fineract_client.SelfAccountTransferApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create14**](SelfAccountTransferApi.md#create14) | **POST** /v1/self/accounttransfers | Create new Transfer
[**template15**](SelfAccountTransferApi.md#template15) | **GET** /v1/self/accounttransfers/template | Retrieve Account Transfer Template


# **create14**
> List[PostNewTransferResponse] create14(type=type, body=body)

Create new Transfer

Ability to create new transfer of monetary funds from one account to another.


Example Requests:

 self/accounttransfers/


### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_new_transfer_response import PostNewTransferResponse
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
    api_instance = fineract_client.SelfAccountTransferApi(api_client)
    type = '' # str |  (optional) (default to '')
    body = 'body_example' # str |  (optional)

    try:
        # Create new Transfer
        api_response = api_instance.create14(type=type, body=body)
        print("The response of SelfAccountTransferApi->create14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfAccountTransferApi->create14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to &#39;&#39;]
 **body** | **str**|  | [optional] 

### Return type

[**List[PostNewTransferResponse]**](PostNewTransferResponse.md)

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

# **template15**
> List[GetAccountTransferTemplateResponse] template15(type=type)

Retrieve Account Transfer Template

Returns list of loan/savings accounts that can be used for account transfer


Example Requests:

self/accounttransfers/template


### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_transfer_template_response import GetAccountTransferTemplateResponse
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
    api_instance = fineract_client.SelfAccountTransferApi(api_client)
    type = '' # str |  (optional) (default to '')

    try:
        # Retrieve Account Transfer Template
        api_response = api_instance.template15(type=type)
        print("The response of SelfAccountTransferApi->template15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfAccountTransferApi->template15: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[GetAccountTransferTemplateResponse]**](GetAccountTransferTemplateResponse.md)

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

