# fineract_client.AccountTransfersApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](AccountTransfersApi.md#create4) | **POST** /v1/accounttransfers | Create new Transfer
[**retrieve_all18**](AccountTransfersApi.md#retrieve_all18) | **GET** /v1/accounttransfers | List account transfers
[**retrieve_one9**](AccountTransfersApi.md#retrieve_one9) | **GET** /v1/accounttransfers/{transferId} | Retrieve account transfer
[**template5**](AccountTransfersApi.md#template5) | **GET** /v1/accounttransfers/template | Retrieve Account Transfer Template
[**template_refund_by_transfer**](AccountTransfersApi.md#template_refund_by_transfer) | **GET** /v1/accounttransfers/templateRefundByTransfer | Retrieve Refund of an Active Loan by Transfer Template
[**template_refund_by_transfer_post**](AccountTransfersApi.md#template_refund_by_transfer_post) | **POST** /v1/accounttransfers/refundByTransfer | Refund of an Active Loan by Transfer


# **create4**
> PostAccountTransfersResponse create4(post_account_transfers_request)

Create new Transfer

Ability to create new transfer of monetary funds from one account to another.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_account_transfers_request import PostAccountTransfersRequest
from fineract_client.models.post_account_transfers_response import PostAccountTransfersResponse
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    post_account_transfers_request = fineract_client.PostAccountTransfersRequest() # PostAccountTransfersRequest | 

    try:
        # Create new Transfer
        api_response = api_instance.create4(post_account_transfers_request)
        print("The response of AccountTransfersApi->create4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->create4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_account_transfers_request** | [**PostAccountTransfersRequest**](PostAccountTransfersRequest.md)|  | 

### Return type

[**PostAccountTransfersResponse**](PostAccountTransfersResponse.md)

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

# **retrieve_all18**
> GetAccountTransfersResponse retrieve_all18(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_detail_id=account_detail_id)

List account transfers

Lists account's transfers

Example Requests:



accounttransfers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_transfers_response import GetAccountTransfersResponse
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    external_id = 'external_id_example' # str | externalId (optional)
    offset = 56 # int | offset (optional)
    limit = limit # int |  (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    account_detail_id = 56 # int | accountDetailId (optional)

    try:
        # List account transfers
        api_response = api_instance.retrieve_all18(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_detail_id=account_detail_id)
        print("The response of AccountTransfersApi->retrieve_all18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->retrieve_all18: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **account_detail_id** | **int**| accountDetailId | [optional] 

### Return type

[**GetAccountTransfersResponse**](GetAccountTransfersResponse.md)

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

# **retrieve_one9**
> GetAccountTransfersPageItems retrieve_one9(transfer_id)

Retrieve account transfer

Retrieves account transfer

Example Requests :



accounttransfers/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_transfers_page_items import GetAccountTransfersPageItems
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    transfer_id = 56 # int | transferId

    try:
        # Retrieve account transfer
        api_response = api_instance.retrieve_one9(transfer_id)
        print("The response of AccountTransfersApi->retrieve_one9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->retrieve_one9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**| transferId | 

### Return type

[**GetAccountTransfersPageItems**](GetAccountTransfersPageItems.md)

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

# **template5**
> GetAccountTransfersTemplateResponse template5(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)

Retrieve Account Transfer Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:



Field Defaults

Allowed Value Lists

Example Requests:



accounttransfers/template?fromAccountType=2&fromOfficeId=1



accounttransfers/template?fromAccountType=2&fromOfficeId=1&fromClientId=1



accounttransfers/template?fromClientId=1&fromAccountType=2&fromAccountId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_transfers_template_response import GetAccountTransfersTemplateResponse
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    from_office_id = 56 # int | fromOfficeId (optional)
    from_client_id = 56 # int | fromClientId (optional)
    from_account_id = 56 # int | fromAccountId (optional)
    from_account_type = 56 # int | fromAccountType (optional)
    to_office_id = 56 # int | toOfficeId (optional)
    to_client_id = 56 # int | toClientId (optional)
    to_account_id = 56 # int | toAccountId (optional)
    to_account_type = 56 # int | toAccountType (optional)

    try:
        # Retrieve Account Transfer Template
        api_response = api_instance.template5(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)
        print("The response of AccountTransfersApi->template5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->template5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_office_id** | **int**| fromOfficeId | [optional] 
 **from_client_id** | **int**| fromClientId | [optional] 
 **from_account_id** | **int**| fromAccountId | [optional] 
 **from_account_type** | **int**| fromAccountType | [optional] 
 **to_office_id** | **int**| toOfficeId | [optional] 
 **to_client_id** | **int**| toClientId | [optional] 
 **to_account_id** | **int**| toAccountId | [optional] 
 **to_account_type** | **int**| toAccountType | [optional] 

### Return type

[**GetAccountTransfersTemplateResponse**](GetAccountTransfersTemplateResponse.md)

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

# **template_refund_by_transfer**
> GetAccountTransfersTemplateRefundByTransferResponse template_refund_by_transfer(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)

Retrieve Refund of an Active Loan by Transfer Template

Retrieves Refund of an Active Loan by Transfer TemplateExample Requests :



accounttransfers/templateRefundByTransfer?fromAccountId=2&fromAccountType=1& toAccountId=1&toAccountType=2&toClientId=1&toOfficeId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_transfers_template_refund_by_transfer_response import GetAccountTransfersTemplateRefundByTransferResponse
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    from_office_id = 56 # int | fromOfficeId (optional)
    from_client_id = 56 # int | fromClientId (optional)
    from_account_id = 56 # int | fromAccountId (optional)
    from_account_type = 56 # int | fromAccountType (optional)
    to_office_id = 56 # int | toOfficeId (optional)
    to_client_id = 56 # int | toClientId (optional)
    to_account_id = 56 # int | toAccountId (optional)
    to_account_type = 56 # int | toAccountType (optional)

    try:
        # Retrieve Refund of an Active Loan by Transfer Template
        api_response = api_instance.template_refund_by_transfer(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)
        print("The response of AccountTransfersApi->template_refund_by_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->template_refund_by_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_office_id** | **int**| fromOfficeId | [optional] 
 **from_client_id** | **int**| fromClientId | [optional] 
 **from_account_id** | **int**| fromAccountId | [optional] 
 **from_account_type** | **int**| fromAccountType | [optional] 
 **to_office_id** | **int**| toOfficeId | [optional] 
 **to_client_id** | **int**| toClientId | [optional] 
 **to_account_id** | **int**| toAccountId | [optional] 
 **to_account_type** | **int**| toAccountType | [optional] 

### Return type

[**GetAccountTransfersTemplateRefundByTransferResponse**](GetAccountTransfersTemplateRefundByTransferResponse.md)

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

# **template_refund_by_transfer_post**
> PostAccountTransfersRefundByTransferResponse template_refund_by_transfer_post(post_account_transfers_refund_by_transfer_request)

Refund of an Active Loan by Transfer

Ability to refund an active loan by transferring to a savings account.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_account_transfers_refund_by_transfer_request import PostAccountTransfersRefundByTransferRequest
from fineract_client.models.post_account_transfers_refund_by_transfer_response import PostAccountTransfersRefundByTransferResponse
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
    api_instance = fineract_client.AccountTransfersApi(api_client)
    post_account_transfers_refund_by_transfer_request = fineract_client.PostAccountTransfersRefundByTransferRequest() # PostAccountTransfersRefundByTransferRequest | 

    try:
        # Refund of an Active Loan by Transfer
        api_response = api_instance.template_refund_by_transfer_post(post_account_transfers_refund_by_transfer_request)
        print("The response of AccountTransfersApi->template_refund_by_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTransfersApi->template_refund_by_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_account_transfers_refund_by_transfer_request** | [**PostAccountTransfersRefundByTransferRequest**](PostAccountTransfersRefundByTransferRequest.md)|  | 

### Return type

[**PostAccountTransfersRefundByTransferResponse**](PostAccountTransfersRefundByTransferResponse.md)

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

