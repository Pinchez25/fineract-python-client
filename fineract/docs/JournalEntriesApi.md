# fineract_client.JournalEntriesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

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
> PostJournalEntriesResponse create_gl_journal_entry(command=command, journal_entry_command=journal_entry_command)

Create \"Balanced\" Journal Entries

Note: A Balanced (simple) Journal entry would have atleast one "Debit" and one "Credit" entry whose amounts are equal 
Compound Journal entries may have "n" debits and "m" credits where both "m" and "n" are greater than 0 and the net sum or all debits and credits are equal 


Mandatory Fields
officeId, transactionDate


credits- glAccountId, amount, comments

 
debits-  glAccountId, amount, comments

 
Optional Fields
paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.journal_entry_command import JournalEntryCommand
from fineract_client.models.post_journal_entries_response import PostJournalEntriesResponse
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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    command = 'command_example' # str | command (optional)
    journal_entry_command = fineract_client.JournalEntryCommand() # JournalEntryCommand |  (optional)

    try:
        # Create \"Balanced\" Journal Entries
        api_response = api_instance.create_gl_journal_entry(command=command, journal_entry_command=journal_entry_command)
        print("The response of JournalEntriesApi->create_gl_journal_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalEntriesApi->create_gl_journal_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| command | [optional] 
 **journal_entry_command** | [**JournalEntryCommand**](JournalEntryCommand.md)|  | [optional] 

### Return type

[**PostJournalEntriesResponse**](PostJournalEntriesResponse.md)

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

# **create_reversal_journal_entry**
> PostJournalEntriesTransactionIdResponse create_reversal_journal_entry(transaction_id, command=command, post_journal_entries_transaction_id_request=post_journal_entries_transaction_id_request)

Update Running balances for Journal Entries

This API calculates the running balances for office. If office ID not provided this API calculates running balances for all offices. 
Mandatory Fields
officeId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_journal_entries_transaction_id_request import PostJournalEntriesTransactionIdRequest
from fineract_client.models.post_journal_entries_transaction_id_response import PostJournalEntriesTransactionIdResponse
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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    transaction_id = 'transaction_id_example' # str | transactionId
    command = 'command_example' # str | command (optional)
    post_journal_entries_transaction_id_request = fineract_client.PostJournalEntriesTransactionIdRequest() # PostJournalEntriesTransactionIdRequest |  (optional)

    try:
        # Update Running balances for Journal Entries
        api_response = api_instance.create_reversal_journal_entry(transaction_id, command=command, post_journal_entries_transaction_id_request=post_journal_entries_transaction_id_request)
        print("The response of JournalEntriesApi->create_reversal_journal_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalEntriesApi->create_reversal_journal_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| transactionId | 
 **command** | **str**| command | [optional] 
 **post_journal_entries_transaction_id_request** | [**PostJournalEntriesTransactionIdRequest**](PostJournalEntriesTransactionIdRequest.md)|  | [optional] 

### Return type

[**PostJournalEntriesTransactionIdResponse**](PostJournalEntriesTransactionIdResponse.md)

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

# **get_journal_entries_template**
> get_journal_entries_template(office_id=office_id, date_format=date_format)

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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    office_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_journal_entries_template(office_id=office_id, date_format=date_format)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_journal_entries_template**
> str post_journal_entries_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)

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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_journal_entries_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of JournalEntriesApi->post_journal_entries_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalEntriesApi->post_journal_entries_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all1**
> GetJournalEntriesTransactionIdResponse retrieve_all1(office_id=office_id, gl_account_id=gl_account_id, manual_entries_only=manual_entries_only, from_date=from_date, to_date=to_date, submitted_on_date_from=submitted_on_date_from, submitted_on_date_to=submitted_on_date_to, transaction_id=transaction_id, entity_type=entity_type, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format, loan_id=loan_id, savings_id=savings_id, running_balance=running_balance, transaction_details=transaction_details)

List Journal Entries

The list capability of journal entries can support pagination and sorting.

Example Requests:

journalentries

journalentries?transactionId=PB37X8Y21EQUY4S

journalentries?officeId=1&manualEntriesOnly=true&fromDate=1 July 2013&toDate=15 July 2013&dateFormat=dd MMMM yyyy&locale=en

journalentries?fields=officeName,glAccountName,transactionDate

journalentries?offset=10&limit=50

journalentries?orderBy=transactionId&sortOrder=DESC

journalentries?runningBalance=true

journalentries?transactionDetails=true

journalentries?loanId=12

journalentries?savingsId=24

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_journal_entries_transaction_id_response import GetJournalEntriesTransactionIdResponse
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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    office_id = 56 # int | officeId (optional)
    gl_account_id = 56 # int | glAccountId (optional)
    manual_entries_only = True # bool | manualEntriesOnly (optional)
    from_date = None # object | fromDate (optional)
    to_date = None # object | toDate (optional)
    submitted_on_date_from = None # object | submittedOnDateFrom (optional)
    submitted_on_date_to = None # object | submittedOnDateTo (optional)
    transaction_id = 'transaction_id_example' # str | transactionId (optional)
    entity_type = 56 # int | entityType (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    locale = 'locale_example' # str | locale (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)
    loan_id = 56 # int | loanId (optional)
    savings_id = 56 # int | savingsId (optional)
    running_balance = True # bool | runningBalance (optional)
    transaction_details = True # bool | transactionDetails (optional)

    try:
        # List Journal Entries
        api_response = api_instance.retrieve_all1(office_id=office_id, gl_account_id=gl_account_id, manual_entries_only=manual_entries_only, from_date=from_date, to_date=to_date, submitted_on_date_from=submitted_on_date_from, submitted_on_date_to=submitted_on_date_to, transaction_id=transaction_id, entity_type=entity_type, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, locale=locale, date_format=date_format, loan_id=loan_id, savings_id=savings_id, running_balance=running_balance, transaction_details=transaction_details)
        print("The response of JournalEntriesApi->retrieve_all1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalEntriesApi->retrieve_all1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **gl_account_id** | **int**| glAccountId | [optional] 
 **manual_entries_only** | **bool**| manualEntriesOnly | [optional] 
 **from_date** | [**object**](.md)| fromDate | [optional] 
 **to_date** | [**object**](.md)| toDate | [optional] 
 **submitted_on_date_from** | [**object**](.md)| submittedOnDateFrom | [optional] 
 **submitted_on_date_to** | [**object**](.md)| submittedOnDateTo | [optional] 
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_journal_entries**
> str retrieve_journal_entries(offset=offset, limit=limit, entry_id=entry_id)

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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    entry_id = 56 # int |  (optional)

    try:
        api_response = api_instance.retrieve_journal_entries(offset=offset, limit=limit, entry_id=entry_id)
        print("The response of JournalEntriesApi->retrieve_journal_entries:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_journal_entry_by_id**
> JournalEntryTransactionItem retrieve_journal_entry_by_id(journal_entry_id, running_balance=running_balance, transaction_details=transaction_details)

Retrieve a single Entry

Example Requests:

journalentries/1



journalentries/1?fields=officeName,glAccountId,entryType,amount

journalentries/1?runningBalance=true

journalentries/1?transactionDetails=true

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.journal_entry_transaction_item import JournalEntryTransactionItem
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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    journal_entry_id = 56 # int | journalEntryId
    running_balance = True # bool | runningBalance (optional)
    transaction_details = True # bool | transactionDetails (optional)

    try:
        # Retrieve a single Entry
        api_response = api_instance.retrieve_journal_entry_by_id(journal_entry_id, running_balance=running_balance, transaction_details=transaction_details)
        print("The response of JournalEntriesApi->retrieve_journal_entry_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_opening_balance**
> str retrieve_opening_balance(office_id=office_id, currency_code=currency_code)

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
    api_instance = fineract_client.JournalEntriesApi(api_client)
    office_id = 56 # int |  (optional)
    currency_code = 'currency_code_example' # str |  (optional)

    try:
        api_response = api_instance.retrieve_opening_balance(office_id=office_id, currency_code=currency_code)
        print("The response of JournalEntriesApi->retrieve_opening_balance:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

