# fineract_client.ExternalAssetOwnersApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_transfer**](ExternalAssetOwnersApi.md#get_active_transfer) | **GET** /v1/external-asset-owners/transfers/active-transfer | Retrieve Active Asset Owner Transfer
[**get_journal_entries_of_owner**](ExternalAssetOwnersApi.md#get_journal_entries_of_owner) | **GET** /v1/external-asset-owners/owners/external-id/{ownerExternalId}/journal-entries | Retrieve Journal Entries of Owner
[**get_journal_entries_of_transfer**](ExternalAssetOwnersApi.md#get_journal_entries_of_transfer) | **GET** /v1/external-asset-owners/transfers/{transferId}/journal-entries | Retrieve Journal Entries of Transfer
[**get_transfers**](ExternalAssetOwnersApi.md#get_transfers) | **GET** /v1/external-asset-owners/transfers | Retrieve External Asset Owner Transfers
[**search_investor_data**](ExternalAssetOwnersApi.md#search_investor_data) | **POST** /v1/external-asset-owners/search | Search External Asset Owner Transfers by text or date ranges to settlement or effective dates
[**transfer_request_with_id**](ExternalAssetOwnersApi.md#transfer_request_with_id) | **POST** /v1/external-asset-owners/transfers/{id} | 
[**transfer_request_with_id1**](ExternalAssetOwnersApi.md#transfer_request_with_id1) | **POST** /v1/external-asset-owners/transfers/external-id/{externalId} | 
[**transfer_request_with_loan_external_id**](ExternalAssetOwnersApi.md#transfer_request_with_loan_external_id) | **POST** /v1/external-asset-owners/transfers/loans/external-id/{loanExternalId} | 
[**transfer_request_with_loan_id**](ExternalAssetOwnersApi.md#transfer_request_with_loan_id) | **POST** /v1/external-asset-owners/transfers/loans/{loanId} | 


# **get_active_transfer**
> ExternalTransferData get_active_transfer(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id)

Retrieve Active Asset Owner Transfer

Retrieve Active External Asset Owner Transfer by transferExternalId, loanId or loanExternalId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.external_transfer_data import ExternalTransferData
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    transfer_external_id = 'transfer_external_id_example' # str | transferExternalId (optional)
    loan_id = 56 # int | loanId (optional)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId (optional)

    try:
        # Retrieve Active Asset Owner Transfer
        api_response = api_instance.get_active_transfer(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id)
        print("The response of ExternalAssetOwnersApi->get_active_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->get_active_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_external_id** | **str**| transferExternalId | [optional] 
 **loan_id** | **int**| loanId | [optional] 
 **loan_external_id** | **str**| loanExternalId | [optional] 

### Return type

[**ExternalTransferData**](ExternalTransferData.md)

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

# **get_journal_entries_of_owner**
> ExternalOwnerJournalEntryData get_journal_entries_of_owner(owner_external_id, offset=offset, limit=limit)

Retrieve Journal Entries of Owner

Retrieve Journal entries of owner by owner externalId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.external_owner_journal_entry_data import ExternalOwnerJournalEntryData
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    owner_external_id = 'owner_external_id_example' # str | ownerExternalId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # Retrieve Journal Entries of Owner
        api_response = api_instance.get_journal_entries_of_owner(owner_external_id, offset=offset, limit=limit)
        print("The response of ExternalAssetOwnersApi->get_journal_entries_of_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->get_journal_entries_of_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_external_id** | **str**| ownerExternalId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**ExternalOwnerJournalEntryData**](ExternalOwnerJournalEntryData.md)

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

# **get_journal_entries_of_transfer**
> ExternalOwnerTransferJournalEntryData get_journal_entries_of_transfer(transfer_id, offset=offset, limit=limit)

Retrieve Journal Entries of Transfer

Retrieve Journal entries of transfer by transferId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.external_owner_transfer_journal_entry_data import ExternalOwnerTransferJournalEntryData
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    transfer_id = 56 # int | transferId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # Retrieve Journal Entries of Transfer
        api_response = api_instance.get_journal_entries_of_transfer(transfer_id, offset=offset, limit=limit)
        print("The response of ExternalAssetOwnersApi->get_journal_entries_of_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->get_journal_entries_of_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**| transferId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**ExternalOwnerTransferJournalEntryData**](ExternalOwnerTransferJournalEntryData.md)

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

# **get_transfers**
> PageExternalTransferData get_transfers(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id, offset=offset, limit=limit)

Retrieve External Asset Owner Transfers

Retrieve External Asset Owner Transfer items by transferExternalId, loanId or loanExternalId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.page_external_transfer_data import PageExternalTransferData
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    transfer_external_id = 'transfer_external_id_example' # str | transferExternalId (optional)
    loan_id = 56 # int | loanId (optional)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # Retrieve External Asset Owner Transfers
        api_response = api_instance.get_transfers(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id, offset=offset, limit=limit)
        print("The response of ExternalAssetOwnersApi->get_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->get_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_external_id** | **str**| transferExternalId | [optional] 
 **loan_id** | **int**| loanId | [optional] 
 **loan_external_id** | **str**| loanExternalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**PageExternalTransferData**](PageExternalTransferData.md)

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

# **search_investor_data**
> PageExternalTransferData search_investor_data(paged_request_external_asset_owner_search_request=paged_request_external_asset_owner_search_request)

Search External Asset Owner Transfers by text or date ranges to settlement or effective dates

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.page_external_transfer_data import PageExternalTransferData
from fineract_client.models.paged_request_external_asset_owner_search_request import PagedRequestExternalAssetOwnerSearchRequest
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    paged_request_external_asset_owner_search_request = fineract_client.PagedRequestExternalAssetOwnerSearchRequest() # PagedRequestExternalAssetOwnerSearchRequest |  (optional)

    try:
        # Search External Asset Owner Transfers by text or date ranges to settlement or effective dates
        api_response = api_instance.search_investor_data(paged_request_external_asset_owner_search_request=paged_request_external_asset_owner_search_request)
        print("The response of ExternalAssetOwnersApi->search_investor_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->search_investor_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paged_request_external_asset_owner_search_request** | [**PagedRequestExternalAssetOwnerSearchRequest**](PagedRequestExternalAssetOwnerSearchRequest.md)|  | [optional] 

### Return type

[**PageExternalTransferData**](PageExternalTransferData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_id**
> PostInitiateTransferResponse transfer_request_with_id(id, command=command)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_initiate_transfer_response import PostInitiateTransferResponse
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    id = 56 # int | 
    command = 'command_example' # str | command (optional)

    try:
        api_response = api_instance.transfer_request_with_id(id, command=command)
        print("The response of ExternalAssetOwnersApi->transfer_request_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Transfer cannot be initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_id1**
> PostInitiateTransferResponse transfer_request_with_id1(external_id, command=command)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_initiate_transfer_response import PostInitiateTransferResponse
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    external_id = 'external_id_example' # str | 
    command = 'command_example' # str | command (optional)

    try:
        api_response = api_instance.transfer_request_with_id1(external_id, command=command)
        print("The response of ExternalAssetOwnersApi->transfer_request_with_id1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_id1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Transfer cannot be initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_loan_external_id**
> PostInitiateTransferResponse transfer_request_with_loan_external_id(loan_external_id, post_initiate_transfer_request, command=command)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_initiate_transfer_request import PostInitiateTransferRequest
from fineract_client.models.post_initiate_transfer_response import PostInitiateTransferResponse
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | 
    post_initiate_transfer_request = fineract_client.PostInitiateTransferRequest() # PostInitiateTransferRequest | 
    command = 'command_example' # str | command (optional)

    try:
        api_response = api_instance.transfer_request_with_loan_external_id(loan_external_id, post_initiate_transfer_request, command=command)
        print("The response of ExternalAssetOwnersApi->transfer_request_with_loan_external_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_loan_external_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**|  | 
 **post_initiate_transfer_request** | [**PostInitiateTransferRequest**](PostInitiateTransferRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Transfer cannot be initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_loan_id**
> PostInitiateTransferResponse transfer_request_with_loan_id(loan_id, post_initiate_transfer_request, command=command)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_initiate_transfer_request import PostInitiateTransferRequest
from fineract_client.models.post_initiate_transfer_response import PostInitiateTransferResponse
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
    api_instance = fineract_client.ExternalAssetOwnersApi(api_client)
    loan_id = 56 # int | 
    post_initiate_transfer_request = fineract_client.PostInitiateTransferRequest() # PostInitiateTransferRequest | 
    command = 'command_example' # str | command (optional)

    try:
        api_response = api_instance.transfer_request_with_loan_id(loan_id, post_initiate_transfer_request, command=command)
        print("The response of ExternalAssetOwnersApi->transfer_request_with_loan_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_loan_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **post_initiate_transfer_request** | [**PostInitiateTransferRequest**](PostInitiateTransferRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Transfer cannot be initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

