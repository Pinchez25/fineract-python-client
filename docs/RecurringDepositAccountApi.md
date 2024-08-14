# fineract_client.RecurringDepositAccountApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_closure_template1**](RecurringDepositAccountApi.md#account_closure_template1) | **GET** /v1/recurringdepositaccounts/{accountId}/template | 
[**delete17**](RecurringDepositAccountApi.md#delete17) | **DELETE** /v1/recurringdepositaccounts/{accountId} | Delete a recurring deposit application
[**get_recurring_deposit_template**](RecurringDepositAccountApi.md#get_recurring_deposit_template) | **GET** /v1/recurringdepositaccounts/downloadtemplate | 
[**get_recurring_deposit_transaction_template**](RecurringDepositAccountApi.md#get_recurring_deposit_transaction_template) | **GET** /v1/recurringdepositaccounts/transactions/downloadtemplate | 
[**handle_commands5**](RecurringDepositAccountApi.md#handle_commands5) | **POST** /v1/recurringdepositaccounts/{accountId} | Approve recurring deposit application | Undo approval recurring deposit application | Reject recurring deposit application | Withdraw recurring deposit application | Activate a recurring deposit account | Update the recommended deposit amount for a recurring deposit account | Close a recurring deposit account | Premature Close a recurring deposit account | Calculate Premature amount on Recurring deposit account | Calculate Interest on recurring Deposit Account | Post Interest on recurring Deposit Account
[**post_recurring_deposit_template**](RecurringDepositAccountApi.md#post_recurring_deposit_template) | **POST** /v1/recurringdepositaccounts/uploadtemplate | 
[**post_recurring_deposit_transactions_template**](RecurringDepositAccountApi.md#post_recurring_deposit_transactions_template) | **POST** /v1/recurringdepositaccounts/transactions/uploadtemplate | 
[**retrieve_all31**](RecurringDepositAccountApi.md#retrieve_all31) | **GET** /v1/recurringdepositaccounts | List Recurring deposit applications/accounts
[**retrieve_one22**](RecurringDepositAccountApi.md#retrieve_one22) | **GET** /v1/recurringdepositaccounts/{accountId} | Retrieve a recurring deposit application/account
[**submit_application1**](RecurringDepositAccountApi.md#submit_application1) | **POST** /v1/recurringdepositaccounts | Submit new recurring deposit application
[**template13**](RecurringDepositAccountApi.md#template13) | **GET** /v1/recurringdepositaccounts/template | Retrieve recurring Deposit Account Template
[**update18**](RecurringDepositAccountApi.md#update18) | **PUT** /v1/recurringdepositaccounts/{accountId} | Modify a recurring deposit application

# **account_closure_template1**
> str account_closure_template1(account_id, command=command)



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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.account_closure_template1(account_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->account_closure_template1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **command** | **str**| command | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete17**
> DeleteRecurringDepositAccountsResponse delete17(account_id)

Delete a recurring deposit application

At present we support hard delete of recurring deposit application so long as its in 'Submitted and pending approval' state. One the application is moves past this state, it is not possible to do a 'hard' delete of the application or the account. An API endpoint will be added to close/de-activate the recurring deposit account.

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId

try:
    # Delete a recurring deposit application
    api_response = api_instance.delete17(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->delete17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 

### Return type

[**DeleteRecurringDepositAccountsResponse**](DeleteRecurringDepositAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_deposit_template**
> get_recurring_deposit_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
staff_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_recurring_deposit_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->get_recurring_deposit_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **staff_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_deposit_transaction_template**
> get_recurring_deposit_transaction_template(office_id=office_id, date_format=date_format)



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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_recurring_deposit_transaction_template(office_id=office_id, date_format=date_format)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->get_recurring_deposit_transaction_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands5**
> PostRecurringDepositAccountsAccountIdResponse handle_commands5(body, account_id, command=command)

Approve recurring deposit application | Undo approval recurring deposit application | Reject recurring deposit application | Withdraw recurring deposit application | Activate a recurring deposit account | Update the recommended deposit amount for a recurring deposit account | Close a recurring deposit account | Premature Close a recurring deposit account | Calculate Premature amount on Recurring deposit account | Calculate Interest on recurring Deposit Account | Post Interest on recurring Deposit Account

Approve recurring deposit application:  Approves recurring deposit application so long as its in 'Submitted and pending approval' state.  Undo approval recurring deposit application:  Will move 'approved' recurring deposit application back to 'Submitted and pending approval' state.  Reject recurring deposit application  Rejects recurring deposit application so long as its in 'Submitted and pending approval' state.  Withdraw recurring deposit application:  Used when an applicant withdraws from the recurring deposit application. It must be in 'Submitted and pending approval' state.  Activate a recurring deposit account:  Results in an approved recurring deposit application being converted into an 'active' recurring deposit account.  Update the recommended deposit amount for a recurring deposit account:  Updates the recommended deposit amount for a RD account as on the effective date.  Close a recurring deposit account  Results in a Matured recurring deposit account being converted into a 'closed' recurring deposit account.  On account close allowed actions are.Premature Close a recurring deposit account:  Results in an Active recurring deposit account being converted into a 'Premature Closed' recurring deposit account with options to withdraw prematured amount. (premature amount is calculated using interest rate chart applicable along with penal interest if any.)  On account premature closure allowed actions are.  Calculate Premature amount on Recurring deposit account:  Calculate premature amount on recurring deposit till premature close date. Premature amount is calculated based on interest chart and penal interest applicable if any.  Calculate Interest on recurring Deposit Account:  Calculates interest earned on a recurring deposit account based on todays date. It does not attempt to post or credit the interest on the account. That is responsibility of the Post Interest API that will likely be called by overnight process.  Post Interest on recurring Deposit Account:  Calculates and Posts interest earned on a recurring deposit account based on todays date and whether an interest posting or crediting event is due.  Showing request/response for 'Post Interest on recurring Deposit Account'

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostRecurringDepositAccountsAccountIdRequest() # PostRecurringDepositAccountsAccountIdRequest | 
account_id = 789 # int | accountId
command = 'command_example' # str | command (optional)

try:
    # Approve recurring deposit application | Undo approval recurring deposit application | Reject recurring deposit application | Withdraw recurring deposit application | Activate a recurring deposit account | Update the recommended deposit amount for a recurring deposit account | Close a recurring deposit account | Premature Close a recurring deposit account | Calculate Premature amount on Recurring deposit account | Calculate Interest on recurring Deposit Account | Post Interest on recurring Deposit Account
    api_response = api_instance.handle_commands5(body, account_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->handle_commands5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRecurringDepositAccountsAccountIdRequest**](PostRecurringDepositAccountsAccountIdRequest.md)|  | 
 **account_id** | **int**| accountId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRecurringDepositAccountsAccountIdResponse**](PostRecurringDepositAccountsAccountIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_recurring_deposit_template**
> str post_recurring_deposit_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_recurring_deposit_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->post_recurring_deposit_template: %s\n" % e)
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

# **post_recurring_deposit_transactions_template**
> str post_recurring_deposit_transactions_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_recurring_deposit_transactions_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->post_recurring_deposit_transactions_template: %s\n" % e)
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

# **retrieve_all31**
> list[GetRecurringDepositAccountsResponse] retrieve_all31(paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Recurring deposit applications/accounts

Lists Recurring deposit applications/accounts  Example Requests:  recurringdepositaccounts   recurringdepositaccounts?fields=name

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
paged = true # bool | paged (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # List Recurring deposit applications/accounts
    api_response = api_instance.retrieve_all31(paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->retrieve_all31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paged** | **bool**| paged | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**list[GetRecurringDepositAccountsResponse]**](GetRecurringDepositAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one22**
> GetRecurringDepositAccountsAccountIdResponse retrieve_one22(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)

Retrieve a recurring deposit application/account

Retrieves a recurring deposit application/account  Example Requests :  recurringdepositaccounts/1   recurringdepositaccounts/1?associations=all

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)
charge_status = 'all' # str | chargeStatus (optional) (default to all)

try:
    # Retrieve a recurring deposit application/account
    api_response = api_instance.retrieve_one22(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->retrieve_one22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]
 **charge_status** | **str**| chargeStatus | [optional] [default to all]

### Return type

[**GetRecurringDepositAccountsAccountIdResponse**](GetRecurringDepositAccountsAccountIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_application1**
> PostRecurringDepositAccountsResponse submit_application1(body)

Submit new recurring deposit application

Submits new recurring deposit application  Mandatory Fields: clientId or groupId, productId, submittedOnDate, depositAmount, depositPeriod, depositPeriodFrequencyId  Optional Fields: accountNo, externalId, fieldOfficerId,linkAccountId(if provided initial deposit amount will be collected from this account),transferInterestToSavings(By enabling this flag all interest postings will be transferred to linked saving account )  Inherited from Product (if not provided): interestCompoundingPeriodType, interestCalculationType, interestCalculationDaysInYearType, lockinPeriodFrequency, lockinPeriodFrequencyType, preClosurePenalApplicable, preClosurePenalInterest, preClosurePenalInterestOnTypeId, charts, withHoldTax

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostRecurringDepositAccountsRequest() # PostRecurringDepositAccountsRequest | 

try:
    # Submit new recurring deposit application
    api_response = api_instance.submit_application1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->submit_application1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRecurringDepositAccountsRequest**](PostRecurringDepositAccountsRequest.md)|  | 

### Return type

[**PostRecurringDepositAccountsResponse**](PostRecurringDepositAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template13**
> GetRecurringDepositAccountsTemplateResponse template13(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve recurring Deposit Account Template

This is a convenience resource. It can be useful when building maintenance user interface screens for recurring deposit applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  recurringdepositaccounts/template?clientId=1   recurringdepositaccounts/template?clientId=1&productId=1

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId (optional)
group_id = 789 # int | groupId (optional)
product_id = 789 # int | productId (optional)
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)

try:
    # Retrieve recurring Deposit Account Template
    api_response = api_instance.template13(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->template13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **product_id** | **int**| productId | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]

### Return type

[**GetRecurringDepositAccountsTemplateResponse**](GetRecurringDepositAccountsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update18**
> PutRecurringDepositAccountsAccountIdResponse update18(body, account_id)

Modify a recurring deposit application

Recurring deposit application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method. Specific api endpoints will be created to allow change of interest detail such as rate, compounding period, posting period etc

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
api_instance = fineract_client.RecurringDepositAccountApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutRecurringDepositAccountsAccountIdRequest() # PutRecurringDepositAccountsAccountIdRequest | 
account_id = 789 # int | accountId

try:
    # Modify a recurring deposit application
    api_response = api_instance.update18(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurringDepositAccountApi->update18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutRecurringDepositAccountsAccountIdRequest**](PutRecurringDepositAccountsAccountIdRequest.md)|  | 
 **account_id** | **int**| accountId | 

### Return type

[**PutRecurringDepositAccountsAccountIdResponse**](PutRecurringDepositAccountsAccountIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

