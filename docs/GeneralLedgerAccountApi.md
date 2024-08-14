# fineract_client.GeneralLedgerAccountApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_account1**](GeneralLedgerAccountApi.md#create_gl_account1) | **POST** /v1/glaccounts | Create a General Ledger Account
[**delete_gl_account1**](GeneralLedgerAccountApi.md#delete_gl_account1) | **DELETE** /v1/glaccounts/{glAccountId} | Delete a GL Account
[**get_gl_accounts_template**](GeneralLedgerAccountApi.md#get_gl_accounts_template) | **GET** /v1/glaccounts/downloadtemplate | 
[**post_gl_accounts_template**](GeneralLedgerAccountApi.md#post_gl_accounts_template) | **POST** /v1/glaccounts/uploadtemplate | 
[**retreive_account**](GeneralLedgerAccountApi.md#retreive_account) | **GET** /v1/glaccounts/{glAccountId} | Retrieve a General Ledger Account
[**retrieve_all_accounts**](GeneralLedgerAccountApi.md#retrieve_all_accounts) | **GET** /v1/glaccounts | List General Ledger Accounts
[**retrieve_new_account_details**](GeneralLedgerAccountApi.md#retrieve_new_account_details) | **GET** /v1/glaccounts/template | Retrieve GL Accounts Template
[**update_gl_account1**](GeneralLedgerAccountApi.md#update_gl_account1) | **PUT** /v1/glaccounts/{glAccountId} | Update a GL Account

# **create_gl_account1**
> PostGLAccountsResponse create_gl_account1(body=body)

Create a General Ledger Account

Note: You may optionally create Hierarchical Chart of Accounts by using the \"parentId\" property of an Account Mandatory Fields:  name, glCode, type, usage and manualEntriesAllowed

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostGLAccountsRequest() # PostGLAccountsRequest |  (optional)

try:
    # Create a General Ledger Account
    api_response = api_instance.create_gl_account1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->create_gl_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGLAccountsRequest**](PostGLAccountsRequest.md)|  | [optional] 

### Return type

[**PostGLAccountsResponse**](PostGLAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gl_account1**
> DeleteGLAccountsRequest delete_gl_account1(gl_account_id)

Delete a GL Account

Deletes a GL Account

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
gl_account_id = 789 # int | glAccountId

try:
    # Delete a GL Account
    api_response = api_instance.delete_gl_account1(gl_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->delete_gl_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_id** | **int**| glAccountId | 

### Return type

[**DeleteGLAccountsRequest**](DeleteGLAccountsRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gl_accounts_template**
> get_gl_accounts_template(date_format=date_format)



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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_gl_accounts_template(date_format=date_format)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->get_gl_accounts_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_gl_accounts_template**
> str post_gl_accounts_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_gl_accounts_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->post_gl_accounts_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retreive_account**
> GetGLAccountsResponse retreive_account(gl_account_id, fetch_running_balance=fetch_running_balance)

Retrieve a General Ledger Account

Example Requests:  glaccounts/1   glaccounts/1?template=true   glaccounts/1?fields=name,glCode   glaccounts/1?fetchRunningBalance=true

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
gl_account_id = 789 # int | glAccountId
fetch_running_balance = true # bool | fetchRunningBalance (optional)

try:
    # Retrieve a General Ledger Account
    api_response = api_instance.retreive_account(gl_account_id, fetch_running_balance=fetch_running_balance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->retreive_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_id** | **int**| glAccountId | 
 **fetch_running_balance** | **bool**| fetchRunningBalance | [optional] 

### Return type

[**GetGLAccountsResponse**](GetGLAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_accounts**
> list[GetGLAccountsResponse] retrieve_all_accounts(type=type, search_param=search_param, usage=usage, manual_entries_allowed=manual_entries_allowed, disabled=disabled, fetch_running_balance=fetch_running_balance)

List General Ledger Accounts

ARGUMENTS type Integer optional manualEntriesAllowed boolean optional usage Integer optional disabled boolean optional parentId Long optional tagId Long optional Example Requests:  glaccounts   glaccounts?type=1&manualEntriesAllowed=true&usage=1&disabled=false  glaccounts?fetchRunningBalance=true

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
type = 56 # int | type (optional)
search_param = 'search_param_example' # str | searchParam (optional)
usage = 56 # int | usage (optional)
manual_entries_allowed = true # bool | manualEntriesAllowed (optional)
disabled = true # bool | disabled (optional)
fetch_running_balance = true # bool | fetchRunningBalance (optional)

try:
    # List General Ledger Accounts
    api_response = api_instance.retrieve_all_accounts(type=type, search_param=search_param, usage=usage, manual_entries_allowed=manual_entries_allowed, disabled=disabled, fetch_running_balance=fetch_running_balance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->retrieve_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| type | [optional] 
 **search_param** | **str**| searchParam | [optional] 
 **usage** | **int**| usage | [optional] 
 **manual_entries_allowed** | **bool**| manualEntriesAllowed | [optional] 
 **disabled** | **bool**| disabled | [optional] 
 **fetch_running_balance** | **bool**| fetchRunningBalance | [optional] 

### Return type

[**list[GetGLAccountsResponse]**](GetGLAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_new_account_details**
> GetGLAccountsTemplateResponse retrieve_new_account_details(type=type)

Retrieve GL Accounts Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  glaccounts/template glaccounts/template?type=1  type is optional and integer value from 1 to 5.  1.Assets  2.Liabilities  3.Equity  4.Income  5.Expenses

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
type = 56 # int | type (optional)

try:
    # Retrieve GL Accounts Template
    api_response = api_instance.retrieve_new_account_details(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->retrieve_new_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| type | [optional] 

### Return type

[**GetGLAccountsTemplateResponse**](GetGLAccountsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gl_account1**
> PutGLAccountsResponse update_gl_account1(gl_account_id, body=body)

Update a GL Account

Updates a GL Account

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
api_instance = fineract_client.GeneralLedgerAccountApi(fineract_client.ApiClient(configuration))
gl_account_id = 789 # int | glAccountId
body = fineract_client.PutGLAccountsRequest() # PutGLAccountsRequest |  (optional)

try:
    # Update a GL Account
    api_response = api_instance.update_gl_account1(gl_account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralLedgerAccountApi->update_gl_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gl_account_id** | **int**| glAccountId | 
 **body** | [**PutGLAccountsRequest**](PutGLAccountsRequest.md)|  | [optional] 

### Return type

[**PutGLAccountsResponse**](PutGLAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

