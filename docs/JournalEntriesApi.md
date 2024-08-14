# fineract_client.JournalEntriesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_journal_entry**](JournalEntriesApi.md#create_gl_journal_entry) | **POST** /v1/journalentries | Create \&quot;Balanced\&quot; Journal Entries
[**create_reversal_journal_entry**](JournalEntriesApi.md#create_reversal_journal_entry) | **POST** /v1/journalentries/{transactionId} | Update Running balances for Journal Entries
[**get_journal_entries_template**](JournalEntriesApi.md#get_journal_entries_template) | **GET** /v1/journalentries/downloadtemplate | 
[**post_journal_entries_template**](JournalEntriesApi.md#post_journal_entries_template) | **POST** /v1/journalentries/uploadtemplate | 
[**retrieve_all1**](JournalEntriesApi.md#retrieve_all1) | **GET** /v1/journalentries | List Journal Entries
[**retrieve_journal_entries**](JournalEntriesApi.md#retrieve_journal_entries) | **GET** /v1/journalentries/provisioning | 
[**retrieve_journal_entry_by_id**](JournalEntriesApi.md#retrieve_journal_entry_by_id) | **GET** /v1/journalentries/{journalEntryId} | Retrieve a single Entry
[**retrieve_opening_balance**](JournalEntriesApi.md#retrieve_opening_balance) | **GET** /v1/journalentries/openingbalance | 

# **create_gl_journal_entry**
> PostJournalEntriesResponse create_gl_journal_entry(body=body, command=command)

Create \"Balanced\" Journal Entries

Note: A Balanced (simple) Journal entry would have atleast one \"Debit\" and one \"Credit\" entry whose amounts are equal  Compound Journal entries may have \"n\" debits and \"m\" credits where both \"m\" and \"n\" are greater than 0 and the net sum or all debits and credits are equal    Mandatory Fields officeId, transactionDate   credits- glAccountId, amount, comments    debits-  glAccountId, amount, comments    Optional Fields paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber

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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
body = fineract_client.JournalEntryCommand() # JournalEntryCommand |  (optional)
command = 'command_example' # str | command (optional)

try:
    # Create \"Balanced\" Journal Entries
    api_response = api_instance.create_gl_journal_entry(body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->create_gl_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JournalEntryCommand**](JournalEntryCommand.md)|  | [optional] 
 **command** | **str**| command | [optional] 

### Return type

[**PostJournalEntriesResponse**](PostJournalEntriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reversal_journal_entry**
> PostJournalEntriesTransactionIdResponse create_reversal_journal_entry(transaction_id, body=body, command=command)

Update Running balances for Journal Entries

This API calculates the running balances for office. If office ID not provided this API calculates running balances for all offices.  Mandatory Fields officeId

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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | transactionId
body = fineract_client.PostJournalEntriesTransactionIdRequest() # PostJournalEntriesTransactionIdRequest |  (optional)
command = 'command_example' # str | command (optional)

try:
    # Update Running balances for Journal Entries
    api_response = api_instance.create_reversal_journal_entry(transaction_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->create_reversal_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transactionId | 
 **body** | [**PostJournalEntriesTransactionIdRequest**](PostJournalEntriesTransactionIdRequest.md)|  | [optional] 
 **command** | **str**| command | [optional] 

### Return type

[**PostJournalEntriesTransactionIdResponse**](PostJournalEntriesTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_entries_template**
> get_journal_entries_template(office_id=office_id, date_format=date_format)



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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_journal_entries_template(office_id=office_id, date_format=date_format)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->get_journal_entries_template: %s\n" % e)
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

# **post_journal_entries_template**
> str post_journal_entries_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_journal_entries_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->post_journal_entries_template: %s\n" % e)
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

# **retrieve_all1**
> GetJournalEntriesTransactionIdResponse retrieve_all1(office_id=office_id, gl_account_id=gl_account_id, manual_entries_only=manual_entries_only, from_date=from_date, to_date=to_date, submitted_on_date_from=submitted_on_date_from, submitted_on_date_to=submitted_on_date_to, transaction_id=transaction_id, entity_type=entity_type, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format, loan_id=loan_id, savings_id=savings_id, running_balance=running_balance, transaction_details=transaction_details)

List Journal Entries

The list capability of journal entries can support pagination and sorting.  Example Requests:  journalentries  journalentries?transactionId=PB37X8Y21EQUY4S  journalentries?officeId=1&manualEntriesOnly=true&fromDate=1 July 2013&toDate=15 July 2013&dateFormat=dd MMMM yyyy&locale=en  journalentries?fields=officeName,glAccountName,transactionDate  journalentries?offset=10&limit=50  journalentries?orderBy=transactionId&sortOrder=DESC  journalentries?runningBalance=true  journalentries?transactionDetails=true  journalentries?loanId=12  journalentries?savingsId=24

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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)
gl_account_id = 789 # int | glAccountId (optional)
manual_entries_only = true # bool | manualEntriesOnly (optional)
from_date = fineract_client.DateParam() # DateParam | fromDate (optional)
to_date = fineract_client.DateParam() # DateParam | toDate (optional)
submitted_on_date_from = fineract_client.DateParam() # DateParam | submittedOnDateFrom (optional)
submitted_on_date_to = fineract_client.DateParam() # DateParam | submittedOnDateTo (optional)
transaction_id = 'transaction_id_example' # str | transactionId (optional)
entity_type = 56 # int | entityType (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
locale = 'locale_example' # str | locale (optional)
date_format = 'date_format_example' # str | dateFormat (optional)
loan_id = 789 # int | loanId (optional)
savings_id = 789 # int | savingsId (optional)
running_balance = true # bool | runningBalance (optional)
transaction_details = true # bool | transactionDetails (optional)

try:
    # List Journal Entries
    api_response = api_instance.retrieve_all1(office_id=office_id, gl_account_id=gl_account_id, manual_entries_only=manual_entries_only, from_date=from_date, to_date=to_date, submitted_on_date_from=submitted_on_date_from, submitted_on_date_to=submitted_on_date_to, transaction_id=transaction_id, entity_type=entity_type, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format, loan_id=loan_id, savings_id=savings_id, running_balance=running_balance, transaction_details=transaction_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->retrieve_all1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **gl_account_id** | **int**| glAccountId | [optional] 
 **manual_entries_only** | **bool**| manualEntriesOnly | [optional] 
 **from_date** | [**DateParam**](.md)| fromDate | [optional] 
 **to_date** | [**DateParam**](.md)| toDate | [optional] 
 **submitted_on_date_from** | [**DateParam**](.md)| submittedOnDateFrom | [optional] 
 **submitted_on_date_to** | [**DateParam**](.md)| submittedOnDateTo | [optional] 
 **transaction_id** | **str**| transactionId | [optional] 
 **entity_type** | **int**| entityType | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **locale** | **str**| locale | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **loan_id** | **int**| loanId | [optional] 
 **savings_id** | **int**| savingsId | [optional] 
 **running_balance** | **bool**| runningBalance | [optional] 
 **transaction_details** | **bool**| transactionDetails | [optional] 

### Return type

[**GetJournalEntriesTransactionIdResponse**](GetJournalEntriesTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_journal_entries**
> str retrieve_journal_entries(offset=offset, limit=limit, entry_id=entry_id)



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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
entry_id = 789 # int |  (optional)

try:
    api_response = api_instance.retrieve_journal_entries(offset=offset, limit=limit, entry_id=entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->retrieve_journal_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **entry_id** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_journal_entry_by_id**
> JournalEntryTransactionItem retrieve_journal_entry_by_id(journal_entry_id, running_balance=running_balance, transaction_details=transaction_details)

Retrieve a single Entry

Example Requests:  journalentries/1    journalentries/1?fields=officeName,glAccountId,entryType,amount  journalentries/1?runningBalance=true  journalentries/1?transactionDetails=true

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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
journal_entry_id = 789 # int | journalEntryId
running_balance = true # bool | runningBalance (optional)
transaction_details = true # bool | transactionDetails (optional)

try:
    # Retrieve a single Entry
    api_response = api_instance.retrieve_journal_entry_by_id(journal_entry_id, running_balance=running_balance, transaction_details=transaction_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->retrieve_journal_entry_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_entry_id** | **int**| journalEntryId | 
 **running_balance** | **bool**| runningBalance | [optional] 
 **transaction_details** | **bool**| transactionDetails | [optional] 

### Return type

[**JournalEntryTransactionItem**](JournalEntryTransactionItem.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_opening_balance**
> str retrieve_opening_balance(office_id=office_id, currency_code=currency_code)



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
api_instance = fineract_client.JournalEntriesApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
currency_code = 'currency_code_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_opening_balance(office_id=office_id, currency_code=currency_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalEntriesApi->retrieve_opening_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **currency_code** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

