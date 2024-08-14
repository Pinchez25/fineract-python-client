# fineract_client.ExternalAssetOwnersApi

All URIs are relative to */fineract-provider/api/v1*

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
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
transfer_external_id = 'transfer_external_id_example' # str | transferExternalId (optional)
loan_id = 789 # int | loanId (optional)
loan_external_id = 'loan_external_id_example' # str | loanExternalId (optional)

try:
    # Retrieve Active Asset Owner Transfer
    api_response = api_instance.get_active_transfer(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_entries_of_owner**
> ExternalOwnerJournalEntryData get_journal_entries_of_owner(owner_external_id, offset=offset, limit=limit)

Retrieve Journal Entries of Owner

Retrieve Journal entries of owner by owner externalId

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
owner_external_id = 'owner_external_id_example' # str | ownerExternalId
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # Retrieve Journal Entries of Owner
    api_response = api_instance.get_journal_entries_of_owner(owner_external_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_entries_of_transfer**
> ExternalOwnerTransferJournalEntryData get_journal_entries_of_transfer(transfer_id, offset=offset, limit=limit)

Retrieve Journal Entries of Transfer

Retrieve Journal entries of transfer by transferId

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
transfer_id = 789 # int | transferId
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # Retrieve Journal Entries of Transfer
    api_response = api_instance.get_journal_entries_of_transfer(transfer_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfers**
> PageExternalTransferData get_transfers(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id, offset=offset, limit=limit)

Retrieve External Asset Owner Transfers

Retrieve External Asset Owner Transfer items by transferExternalId, loanId or loanExternalId

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
transfer_external_id = 'transfer_external_id_example' # str | transferExternalId (optional)
loan_id = 789 # int | loanId (optional)
loan_external_id = 'loan_external_id_example' # str | loanExternalId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # Retrieve External Asset Owner Transfers
    api_response = api_instance.get_transfers(transfer_external_id=transfer_external_id, loan_id=loan_id, loan_external_id=loan_external_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_investor_data**
> PageExternalTransferData search_investor_data(body=body)

Search External Asset Owner Transfers by text or date ranges to settlement or effective dates

### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
body = fineract_client.PagedRequestExternalAssetOwnerSearchRequest() # PagedRequestExternalAssetOwnerSearchRequest |  (optional)

try:
    # Search External Asset Owner Transfers by text or date ranges to settlement or effective dates
    api_response = api_instance.search_investor_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAssetOwnersApi->search_investor_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PagedRequestExternalAssetOwnerSearchRequest**](PagedRequestExternalAssetOwnerSearchRequest.md)|  | [optional] 

### Return type

[**PageExternalTransferData**](PageExternalTransferData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_id**
> PostInitiateTransferResponse transfer_request_with_id(id, command=command)



### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
id = 789 # int | 
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.transfer_request_with_id(id, command=command)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_id1**
> PostInitiateTransferResponse transfer_request_with_id1(external_id, command=command)



### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
external_id = 'external_id_example' # str | 
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.transfer_request_with_id1(external_id, command=command)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_loan_external_id**
> PostInitiateTransferResponse transfer_request_with_loan_external_id(body, loan_external_id, command=command)



### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostInitiateTransferRequest() # PostInitiateTransferRequest | 
loan_external_id = 'loan_external_id_example' # str | 
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.transfer_request_with_loan_external_id(body, loan_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_loan_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostInitiateTransferRequest**](PostInitiateTransferRequest.md)|  | 
 **loan_external_id** | **str**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_with_loan_id**
> PostInitiateTransferResponse transfer_request_with_loan_id(body, loan_id, command=command)



### Example
```python
from __future__ import print_function
import time
import fineract_client
from fineract_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tenantid
configuration = fineract_client.Configuration()
configuration.api_key['fineract-platform-tenantid'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['fineract-platform-tenantid'] = 'Bearer'

# create an instance of the API class
api_instance = fineract_client.ExternalAssetOwnersApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostInitiateTransferRequest() # PostInitiateTransferRequest | 
loan_id = 789 # int | 
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.transfer_request_with_loan_id(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalAssetOwnersApi->transfer_request_with_loan_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostInitiateTransferRequest**](PostInitiateTransferRequest.md)|  | 
 **loan_id** | **int**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostInitiateTransferResponse**](PostInitiateTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

