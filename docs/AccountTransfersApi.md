# fineract_client.AccountTransfersApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](AccountTransfersApi.md#create4) | **POST** /v1/accounttransfers | Create new Transfer
[**retrieve_all18**](AccountTransfersApi.md#retrieve_all18) | **GET** /v1/accounttransfers | List account transfers
[**retrieve_one9**](AccountTransfersApi.md#retrieve_one9) | **GET** /v1/accounttransfers/{transferId} | Retrieve account transfer
[**template5**](AccountTransfersApi.md#template5) | **GET** /v1/accounttransfers/template | Retrieve Account Transfer Template
[**template_refund_by_transfer**](AccountTransfersApi.md#template_refund_by_transfer) | **GET** /v1/accounttransfers/templateRefundByTransfer | Retrieve Refund of an Active Loan by Transfer Template
[**template_refund_by_transfer_post**](AccountTransfersApi.md#template_refund_by_transfer_post) | **POST** /v1/accounttransfers/refundByTransfer | Refund of an Active Loan by Transfer

# **create4**
> PostAccountTransfersResponse create4(body)

Create new Transfer

Ability to create new transfer of monetary funds from one account to another.

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostAccountTransfersRequest() # PostAccountTransfersRequest | 

try:
    # Create new Transfer
    api_response = api_instance.create4(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountTransfersApi->create4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountTransfersRequest**](PostAccountTransfersRequest.md)|  | 

### Return type

[**PostAccountTransfersResponse**](PostAccountTransfersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all18**
> GetAccountTransfersResponse retrieve_all18(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_detail_id=account_detail_id)

List account transfers

Lists account's transfers  Example Requests:    accounttransfers

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
account_detail_id = 789 # int | accountDetailId (optional)

try:
    # List account transfers
    api_response = api_instance.retrieve_all18(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_detail_id=account_detail_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one9**
> GetAccountTransfersPageItems retrieve_one9(transfer_id)

Retrieve account transfer

Retrieves account transfer  Example Requests :    accounttransfers/1

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
transfer_id = 789 # int | transferId

try:
    # Retrieve account transfer
    api_response = api_instance.retrieve_one9(transfer_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template5**
> GetAccountTransfersTemplateResponse template5(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)

Retrieve Account Transfer Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:    Field Defaults  Allowed Value Lists  Example Requests:    accounttransfers/template?fromAccountType=2&fromOfficeId=1    accounttransfers/template?fromAccountType=2&fromOfficeId=1&fromClientId=1    accounttransfers/template?fromClientId=1&fromAccountType=2&fromAccountId=1

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
from_office_id = 789 # int | fromOfficeId (optional)
from_client_id = 789 # int | fromClientId (optional)
from_account_id = 789 # int | fromAccountId (optional)
from_account_type = 56 # int | fromAccountType (optional)
to_office_id = 789 # int | toOfficeId (optional)
to_client_id = 789 # int | toClientId (optional)
to_account_id = 789 # int | toAccountId (optional)
to_account_type = 56 # int | toAccountType (optional)

try:
    # Retrieve Account Transfer Template
    api_response = api_instance.template5(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_refund_by_transfer**
> GetAccountTransfersTemplateRefundByTransferResponse template_refund_by_transfer(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)

Retrieve Refund of an Active Loan by Transfer Template

Retrieves Refund of an Active Loan by Transfer TemplateExample Requests :    accounttransfers/templateRefundByTransfer?fromAccountId=2&fromAccountType=1& toAccountId=1&toAccountType=2&toClientId=1&toOfficeId=1

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
from_office_id = 789 # int | fromOfficeId (optional)
from_client_id = 789 # int | fromClientId (optional)
from_account_id = 789 # int | fromAccountId (optional)
from_account_type = 56 # int | fromAccountType (optional)
to_office_id = 789 # int | toOfficeId (optional)
to_client_id = 789 # int | toClientId (optional)
to_account_id = 789 # int | toAccountId (optional)
to_account_type = 56 # int | toAccountType (optional)

try:
    # Retrieve Refund of an Active Loan by Transfer Template
    api_response = api_instance.template_refund_by_transfer(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_refund_by_transfer_post**
> PostAccountTransfersRefundByTransferResponse template_refund_by_transfer_post(body)

Refund of an Active Loan by Transfer

Ability to refund an active loan by transferring to a savings account.

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
api_instance = fineract_client.AccountTransfersApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostAccountTransfersRefundByTransferRequest() # PostAccountTransfersRefundByTransferRequest | 

try:
    # Refund of an Active Loan by Transfer
    api_response = api_instance.template_refund_by_transfer_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountTransfersApi->template_refund_by_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountTransfersRefundByTransferRequest**](PostAccountTransfersRefundByTransferRequest.md)|  | 

### Return type

[**PostAccountTransfersRefundByTransferResponse**](PostAccountTransfersRefundByTransferResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

