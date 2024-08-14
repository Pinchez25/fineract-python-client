# fineract_client.TellerCashManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_cash_to_cashier**](TellerCashManagementApi.md#allocate_cash_to_cashier) | **POST** /v1/tellers/{tellerId}/cashiers/{cashierId}/allocate | Allocate Cash To Cashier
[**create_cashier**](TellerCashManagementApi.md#create_cashier) | **POST** /v1/tellers/{tellerId}/cashiers | Create Cashiers
[**create_teller**](TellerCashManagementApi.md#create_teller) | **POST** /v1/tellers | Create teller
[**delete_cashier**](TellerCashManagementApi.md#delete_cashier) | **DELETE** /v1/tellers/{tellerId}/cashiers/{cashierId} | Delete Cashier
[**delete_teller**](TellerCashManagementApi.md#delete_teller) | **DELETE** /v1/tellers/{tellerId} | 
[**find_cashier_data**](TellerCashManagementApi.md#find_cashier_data) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId} | Retrieve a cashier
[**find_teller**](TellerCashManagementApi.md#find_teller) | **GET** /v1/tellers/{tellerId} | Retrieve tellers
[**find_transaction_data**](TellerCashManagementApi.md#find_transaction_data) | **GET** /v1/tellers/{tellerId}/transactions/{transactionId} | 
[**get_cashier_data1**](TellerCashManagementApi.md#get_cashier_data1) | **GET** /v1/tellers/{tellerId}/cashiers | List Cashiers
[**get_cashier_template**](TellerCashManagementApi.md#get_cashier_template) | **GET** /v1/tellers/{tellerId}/cashiers/template | Find Cashiers
[**get_cashier_txn_template**](TellerCashManagementApi.md#get_cashier_txn_template) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/transactions/template | Retrieve Cashier Transaction Template
[**get_journal_data**](TellerCashManagementApi.md#get_journal_data) | **GET** /v1/tellers/{tellerId}/journals | 
[**get_teller_data**](TellerCashManagementApi.md#get_teller_data) | **GET** /v1/tellers | List all tellers
[**get_transaction_data**](TellerCashManagementApi.md#get_transaction_data) | **GET** /v1/tellers/{tellerId}/transactions | 
[**get_transactions_for_cashier**](TellerCashManagementApi.md#get_transactions_for_cashier) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/transactions | Retrieve Cashier Transaction
[**get_transactions_wtih_summary_for_cashier**](TellerCashManagementApi.md#get_transactions_wtih_summary_for_cashier) | **GET** /v1/tellers/{tellerId}/cashiers/{cashierId}/summaryandtransactions | Transactions Wtih Summary For Cashier
[**settle_cash_from_cashier**](TellerCashManagementApi.md#settle_cash_from_cashier) | **POST** /v1/tellers/{tellerId}/cashiers/{cashierId}/settle | Settle Cash From Cashier
[**update_cashier**](TellerCashManagementApi.md#update_cashier) | **PUT** /v1/tellers/{tellerId}/cashiers/{cashierId} | Update Cashier
[**update_teller**](TellerCashManagementApi.md#update_teller) | **PUT** /v1/tellers/{tellerId} | Update teller

# **allocate_cash_to_cashier**
> PostTellersTellerIdCashiersCashierIdAllocateResponse allocate_cash_to_cashier(body, teller_id, cashier_id)

Allocate Cash To Cashier

Mandatory Fields:  Date, Amount, Currency, Notes/Comments

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTellersTellerIdCashiersCashierIdAllocateRequest() # PostTellersTellerIdCashiersCashierIdAllocateRequest | 
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Allocate Cash To Cashier
    api_response = api_instance.allocate_cash_to_cashier(body, teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->allocate_cash_to_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTellersTellerIdCashiersCashierIdAllocateRequest**](PostTellersTellerIdCashiersCashierIdAllocateRequest.md)|  | 
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**PostTellersTellerIdCashiersCashierIdAllocateResponse**](PostTellersTellerIdCashiersCashierIdAllocateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json, text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cashier**
> PostTellersTellerIdCashiersResponse create_cashier(body, teller_id)

Create Cashiers

Mandatory Fields:  Cashier/staff, Fromm Date, To Date, Full Day or From time and To time    Optional Fields:  Description/Notes

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTellersTellerIdCashiersRequest() # PostTellersTellerIdCashiersRequest | 
teller_id = 789 # int | tellerId

try:
    # Create Cashiers
    api_response = api_instance.create_cashier(body, teller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->create_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTellersTellerIdCashiersRequest**](PostTellersTellerIdCashiersRequest.md)|  | 
 **teller_id** | **int**| tellerId | 

### Return type

[**PostTellersTellerIdCashiersResponse**](PostTellersTellerIdCashiersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_teller**
> PostTellersResponse create_teller(body)

Create teller

Mandatory Fields Teller name, OfficeId, Description, Start Date, Status Optional Fields End Date

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTellersRequest() # PostTellersRequest | 

try:
    # Create teller
    api_response = api_instance.create_teller(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->create_teller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTellersRequest**](PostTellersRequest.md)|  | 

### Return type

[**PostTellersResponse**](PostTellersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cashier**
> DeleteTellersTellerIdCashiersCashierIdResponse delete_cashier(teller_id, cashier_id)

Delete Cashier

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Delete Cashier
    api_response = api_instance.delete_cashier(teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->delete_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**DeleteTellersTellerIdCashiersCashierIdResponse**](DeleteTellersTellerIdCashiersCashierIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_teller**
> str delete_teller(teller_id)



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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId

try:
    api_response = api_instance.delete_teller(teller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->delete_teller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_cashier_data**
> GetTellersTellerIdCashiersCashierIdResponse find_cashier_data(teller_id, cashier_id)

Retrieve a cashier

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Retrieve a cashier
    api_response = api_instance.find_cashier_data(teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->find_cashier_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**GetTellersTellerIdCashiersCashierIdResponse**](GetTellersTellerIdCashiersCashierIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_teller**
> GetTellersResponse find_teller(teller_id)

Retrieve tellers

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId

try:
    # Retrieve tellers
    api_response = api_instance.find_teller(teller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->find_teller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

### Return type

[**GetTellersResponse**](GetTellersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_transaction_data**
> str find_transaction_data(teller_id, transaction_id)



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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
transaction_id = 789 # int | transactionId

try:
    api_response = api_instance.find_transaction_data(teller_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->find_transaction_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **transaction_id** | **int**| transactionId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cashier_data1**
> GetTellersTellerIdCashiersResponse get_cashier_data1(teller_id, fromdate=fromdate, todate=todate)

List Cashiers

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
fromdate = 'fromdate_example' # str | fromdate (optional)
todate = 'todate_example' # str | todate (optional)

try:
    # List Cashiers
    api_response = api_instance.get_cashier_data1(teller_id, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_cashier_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **fromdate** | **str**| fromdate | [optional] 
 **todate** | **str**| todate | [optional] 

### Return type

[**GetTellersTellerIdCashiersResponse**](GetTellersTellerIdCashiersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cashier_template**
> GetTellersTellerIdCashiersTemplateResponse get_cashier_template(teller_id)

Find Cashiers

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId

try:
    # Find Cashiers
    api_response = api_instance.get_cashier_template(teller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_cashier_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 

### Return type

[**GetTellersTellerIdCashiersTemplateResponse**](GetTellersTellerIdCashiersTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cashier_txn_template**
> GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse get_cashier_txn_template(teller_id, cashier_id)

Retrieve Cashier Transaction Template

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Retrieve Cashier Transaction Template
    api_response = api_instance.get_cashier_txn_template(teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_cashier_txn_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse**](GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_data**
> str get_journal_data(teller_id, cashier_id=cashier_id, date_range=date_range)



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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId (optional)
date_range = 'date_range_example' # str | dateRange (optional)

try:
    api_response = api_instance.get_journal_data(teller_id, cashier_id=cashier_id, date_range=date_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_journal_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | [optional] 
 **date_range** | **str**| dateRange | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teller_data**
> list[GetTellersResponse] get_teller_data(office_id=office_id)

List all tellers

Retrieves list tellers

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)

try:
    # List all tellers
    api_response = api_instance.get_teller_data(office_id=office_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_teller_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 

### Return type

[**list[GetTellersResponse]**](GetTellersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_data**
> str get_transaction_data(teller_id, date_range=date_range)



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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
date_range = 'date_range_example' # str | dateRange (optional)

try:
    api_response = api_instance.get_transaction_data(teller_id, date_range=date_range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_transaction_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **date_range** | **str**| dateRange | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_for_cashier**
> list[GetTellersTellerIdCashiersCashiersIdTransactionsResponse] get_transactions_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Retrieve Cashier Transaction

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId
currency_code = 'currency_code_example' # str | currencyCode (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # Retrieve Cashier Transaction
    api_response = api_instance.get_transactions_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_transactions_for_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **currency_code** | **str**| currencyCode | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**list[GetTellersTellerIdCashiersCashiersIdTransactionsResponse]**](GetTellersTellerIdCashiersCashiersIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_wtih_summary_for_cashier**
> GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse get_transactions_wtih_summary_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Transactions Wtih Summary For Cashier

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId
currency_code = 'currency_code_example' # str | currencyCode (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # Transactions Wtih Summary For Cashier
    api_response = api_instance.get_transactions_wtih_summary_for_cashier(teller_id, cashier_id, currency_code=currency_code, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->get_transactions_wtih_summary_for_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 
 **currency_code** | **str**| currencyCode | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse**](GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_cash_from_cashier**
> PostTellersTellerIdCashiersCashierIdSettleResponse settle_cash_from_cashier(body, teller_id, cashier_id)

Settle Cash From Cashier

Mandatory Fields Date, Amount, Currency, Notes/Comments

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTellersTellerIdCashiersCashierIdSettleRequest() # PostTellersTellerIdCashiersCashierIdSettleRequest | 
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Settle Cash From Cashier
    api_response = api_instance.settle_cash_from_cashier(body, teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->settle_cash_from_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTellersTellerIdCashiersCashierIdSettleRequest**](PostTellersTellerIdCashiersCashierIdSettleRequest.md)|  | 
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**PostTellersTellerIdCashiersCashierIdSettleResponse**](PostTellersTellerIdCashiersCashierIdSettleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json, text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cashier**
> PutTellersTellerIdCashiersCashierIdResponse update_cashier(body, teller_id, cashier_id)

Update Cashier

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutTellersTellerIdCashiersCashierIdRequest() # PutTellersTellerIdCashiersCashierIdRequest | 
teller_id = 789 # int | tellerId
cashier_id = 789 # int | cashierId

try:
    # Update Cashier
    api_response = api_instance.update_cashier(body, teller_id, cashier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->update_cashier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutTellersTellerIdCashiersCashierIdRequest**](PutTellersTellerIdCashiersCashierIdRequest.md)|  | 
 **teller_id** | **int**| tellerId | 
 **cashier_id** | **int**| cashierId | 

### Return type

[**PutTellersTellerIdCashiersCashierIdResponse**](PutTellersTellerIdCashiersCashierIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_teller**
> PutTellersResponse update_teller(body, teller_id)

Update teller

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
api_instance = fineract_client.TellerCashManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutTellersRequest() # PutTellersRequest | 
teller_id = 789 # int | tellerId

try:
    # Update teller
    api_response = api_instance.update_teller(body, teller_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TellerCashManagementApi->update_teller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutTellersRequest**](PutTellersRequest.md)|  | 
 **teller_id** | **int**| tellerId | 

### Return type

[**PutTellersResponse**](PutTellersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

