# fineract_client.FixedDepositAccountApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_closure_template**](FixedDepositAccountApi.md#account_closure_template) | **GET** /v1/fixeddepositaccounts/{accountId}/template | 
[**calculate_fixed_deposit_interest**](FixedDepositAccountApi.md#calculate_fixed_deposit_interest) | **GET** /v1/fixeddepositaccounts/calculate-fd-interest | 
[**delete15**](FixedDepositAccountApi.md#delete15) | **DELETE** /v1/fixeddepositaccounts/{accountId} | Delete a fixed deposit application
[**get_fixed_deposit_template**](FixedDepositAccountApi.md#get_fixed_deposit_template) | **GET** /v1/fixeddepositaccounts/downloadtemplate | 
[**get_fixed_deposit_transaction_template**](FixedDepositAccountApi.md#get_fixed_deposit_transaction_template) | **GET** /v1/fixeddepositaccounts/transaction/downloadtemplate | 
[**handle_commands4**](FixedDepositAccountApi.md#handle_commands4) | **POST** /v1/fixeddepositaccounts/{accountId} | Approve fixed deposit application | Undo approval fixed deposit application | Reject fixed deposit application | Withdraw fixed deposit application | Activate a fixed deposit account | Close a fixed deposit account | Premature Close a fixed deposit account | Calculate Premature amount on Fixed deposit account | Calculate Interest on Fixed Deposit Account | Post Interest on Fixed Deposit Account
[**post_fixed_deposit_template**](FixedDepositAccountApi.md#post_fixed_deposit_template) | **POST** /v1/fixeddepositaccounts/uploadtemplate | 
[**post_fixed_deposit_transaction_template**](FixedDepositAccountApi.md#post_fixed_deposit_transaction_template) | **POST** /v1/fixeddepositaccounts/transaction/uploadtemplate | 
[**retrieve_all29**](FixedDepositAccountApi.md#retrieve_all29) | **GET** /v1/fixeddepositaccounts | List Fixed deposit applications/accounts
[**retrieve_one19**](FixedDepositAccountApi.md#retrieve_one19) | **GET** /v1/fixeddepositaccounts/{accountId} | Retrieve a fixed deposit application/account
[**submit_application**](FixedDepositAccountApi.md#submit_application) | **POST** /v1/fixeddepositaccounts | Submit new fixed deposit application
[**template12**](FixedDepositAccountApi.md#template12) | **GET** /v1/fixeddepositaccounts/template | Retrieve Fixed Deposit Account Template
[**update16**](FixedDepositAccountApi.md#update16) | **PUT** /v1/fixeddepositaccounts/{accountId} | Modify a fixed deposit application


# **account_closure_template**
> str account_closure_template(account_id, command=command)



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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    account_id = 56 # int | accountId
    command = 'command_example' # str | command (optional)

    try:
        api_response = api_instance.account_closure_template(account_id, command=command)
        print("The response of FixedDepositAccountApi->account_closure_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->account_closure_template: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_fixed_deposit_interest**
> CalculateFixedDepositInterestResponse calculate_fixed_deposit_interest(principal_amount=principal_amount, annual_interest_rate=annual_interest_rate, tenure_in_months=tenure_in_months, interest_compounding_period_in_months=interest_compounding_period_in_months, interest_posting_period_in_months=interest_posting_period_in_months)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.calculate_fixed_deposit_interest_response import CalculateFixedDepositInterestResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    principal_amount = 3.4 # float | BigDecimal principalAmount (optional)
    annual_interest_rate = 3.4 # float | annualInterestRate (optional)
    tenure_in_months = 56 # int | tenureInMonths (optional)
    interest_compounding_period_in_months = 56 # int | interestCompoundingPeriodInMonths (optional)
    interest_posting_period_in_months = 56 # int | interestPostingPeriodInMonths (optional)

    try:
        api_response = api_instance.calculate_fixed_deposit_interest(principal_amount=principal_amount, annual_interest_rate=annual_interest_rate, tenure_in_months=tenure_in_months, interest_compounding_period_in_months=interest_compounding_period_in_months, interest_posting_period_in_months=interest_posting_period_in_months)
        print("The response of FixedDepositAccountApi->calculate_fixed_deposit_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->calculate_fixed_deposit_interest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_amount** | **float**| BigDecimal principalAmount | [optional] 
 **annual_interest_rate** | **float**| annualInterestRate | [optional] 
 **tenure_in_months** | **int**| tenureInMonths | [optional] 
 **interest_compounding_period_in_months** | **int**| interestCompoundingPeriodInMonths | [optional] 
 **interest_posting_period_in_months** | **int**| interestPostingPeriodInMonths | [optional] 

### Return type

[**CalculateFixedDepositInterestResponse**](CalculateFixedDepositInterestResponse.md)

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

# **delete15**
> DeleteFixedDepositAccountsAccountIdResponse delete15(account_id)

Delete a fixed deposit application

At present we support hard delete of fixed deposit application so long as its in 'Submitted and pending approval' state. One the application is moves past this state, it is not possible to do a 'hard' delete of the application or the account. An API endpoint will be added to close/de-activate the fixed deposit account.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_fixed_deposit_accounts_account_id_response import DeleteFixedDepositAccountsAccountIdResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    account_id = 56 # int | accountId

    try:
        # Delete a fixed deposit application
        api_response = api_instance.delete15(account_id)
        print("The response of FixedDepositAccountApi->delete15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->delete15: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 

### Return type

[**DeleteFixedDepositAccountsAccountIdResponse**](DeleteFixedDepositAccountsAccountIdResponse.md)

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

# **get_fixed_deposit_template**
> get_fixed_deposit_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    office_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_fixed_deposit_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->get_fixed_deposit_template: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fixed_deposit_transaction_template**
> get_fixed_deposit_transaction_template(office_id=office_id, date_format=date_format)



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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    office_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_fixed_deposit_transaction_template(office_id=office_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->get_fixed_deposit_transaction_template: %s\n" % e)
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

# **handle_commands4**
> PostFixedDepositAccountsAccountIdResponse handle_commands4(account_id, body, command=command)

Approve fixed deposit application | Undo approval fixed deposit application | Reject fixed deposit application | Withdraw fixed deposit application | Activate a fixed deposit account | Close a fixed deposit account | Premature Close a fixed deposit account | Calculate Premature amount on Fixed deposit account | Calculate Interest on Fixed Deposit Account | Post Interest on Fixed Deposit Account

Approve fixed deposit application:  Approves fixed deposit application so long as its in 'Submitted and pending approval' state.  Undo approval fixed deposit application:  Will move 'approved' fixed deposit application back to 'Submitted and pending approval' state.  Reject fixed deposit application:  Rejects fixed deposit application so long as its in 'Submitted and pending approval' state.  Withdraw fixed deposit application:  Used when an applicant withdraws from the fixed deposit application. It must be in 'Submitted and pending approval' state.  Close a fixed deposit account:  Results in a Matured fixed deposit account being converted into a 'closed' fixed deposit account.  Premature Close a fixed deposit account:  Results in an Active fixed deposit account being converted into a 'Premature Closed' fixed deposit account with options to withdraw prematured amount. (premature amount is calculated using interest rate chart applicable along with penal interest if any.)  Calculate Premature amount on Fixed deposit account:  Calculate premature amount on fixed deposit account till premature close date. Premature amount is calculated based on interest chart and penal interest applicable.  Calculate Interest on Fixed Deposit Account:  Calculates interest earned on a fixed deposit account based on todays date. It does not attempt to post or credit the interest on the account. That is responsibility of the Post Interest API that will likely be called by overnight process.  Post Interest on Fixed Deposit Account:  Calculates and Posts interest earned on a fixed deposit account based on today's date and whether an interest posting or crediting event is due.  Showing request/response for Calculate Interest on Fixed Deposit Account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_fixed_deposit_accounts_account_id_response import PostFixedDepositAccountsAccountIdResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    account_id = 56 # int | accountId
    body = None # object | 
    command = 'command_example' # str | command (optional)

    try:
        # Approve fixed deposit application | Undo approval fixed deposit application | Reject fixed deposit application | Withdraw fixed deposit application | Activate a fixed deposit account | Close a fixed deposit account | Premature Close a fixed deposit account | Calculate Premature amount on Fixed deposit account | Calculate Interest on Fixed Deposit Account | Post Interest on Fixed Deposit Account
        api_response = api_instance.handle_commands4(account_id, body, command=command)
        print("The response of FixedDepositAccountApi->handle_commands4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->handle_commands4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **body** | **object**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostFixedDepositAccountsAccountIdResponse**](PostFixedDepositAccountsAccountIdResponse.md)

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

# **post_fixed_deposit_template**
> str post_fixed_deposit_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_fixed_deposit_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of FixedDepositAccountApi->post_fixed_deposit_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->post_fixed_deposit_template: %s\n" % e)
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

# **post_fixed_deposit_transaction_template**
> str post_fixed_deposit_transaction_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_fixed_deposit_transaction_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of FixedDepositAccountApi->post_fixed_deposit_transaction_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->post_fixed_deposit_transaction_template: %s\n" % e)
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

# **retrieve_all29**
> List[GetFixedDepositAccountsResponse] retrieve_all29(paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Fixed deposit applications/accounts

Lists Fixed Deposit Accounts  Example Requests:    fixeddepositaccounts    fixeddepositaccounts?fields=name

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_fixed_deposit_accounts_response import GetFixedDepositAccountsResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    paged = True # bool | paged (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # List Fixed deposit applications/accounts
        api_response = api_instance.retrieve_all29(paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of FixedDepositAccountApi->retrieve_all29:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->retrieve_all29: %s\n" % e)
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

[**List[GetFixedDepositAccountsResponse]**](GetFixedDepositAccountsResponse.md)

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

# **retrieve_one19**
> GetFixedDepositAccountsAccountIdResponse retrieve_one19(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)

Retrieve a fixed deposit application/account

Retrieves a fixed deposit application/account  Example Requests :    fixeddepositaccounts/1  fixeddepositaccounts/1?associations=all

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_fixed_deposit_accounts_account_id_response import GetFixedDepositAccountsAccountIdResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    account_id = 56 # int | accountId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')

    try:
        # Retrieve a fixed deposit application/account
        api_response = api_instance.retrieve_one19(account_id, staff_in_selected_office_only=staff_in_selected_office_only, charge_status=charge_status)
        print("The response of FixedDepositAccountApi->retrieve_one19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->retrieve_one19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]

### Return type

[**GetFixedDepositAccountsAccountIdResponse**](GetFixedDepositAccountsAccountIdResponse.md)

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

# **submit_application**
> PostFixedDepositAccountsResponse submit_application(post_fixed_deposit_accounts_request)

Submit new fixed deposit application

Submits a new fixed deposit applicationMandatory Fields: clientId or groupId, productId, submittedOnDate, depositAmount, depositPeriod, depositPeriodFrequencyId  Optional Fields: accountNo, externalId, fieldOfficerId,linkAccountId(if provided initial deposit amount will be collected from this account),transferInterestToSavings(By enabling this flag all interest postings will be transferred to linked saving account )

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_fixed_deposit_accounts_request import PostFixedDepositAccountsRequest
from fineract_client.models.post_fixed_deposit_accounts_response import PostFixedDepositAccountsResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    post_fixed_deposit_accounts_request = fineract_client.PostFixedDepositAccountsRequest() # PostFixedDepositAccountsRequest | 

    try:
        # Submit new fixed deposit application
        api_response = api_instance.submit_application(post_fixed_deposit_accounts_request)
        print("The response of FixedDepositAccountApi->submit_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->submit_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_fixed_deposit_accounts_request** | [**PostFixedDepositAccountsRequest**](PostFixedDepositAccountsRequest.md)|  | 

### Return type

[**PostFixedDepositAccountsResponse**](PostFixedDepositAccountsResponse.md)

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

# **template12**
> GetFixedDepositAccountsTemplateResponse template12(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve Fixed Deposit Account Template

This is a convenience resource. It can be useful when building maintenance user interface screens for fixed deposit applications. The template data returned consists of any or all of:    Field Defaults  Allowed Value ListsExample Requests:    fixeddepositaccounts/template?clientId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_fixed_deposit_accounts_template_response import GetFixedDepositAccountsTemplateResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    client_id = 56 # int | clientId (optional)
    group_id = 56 # int | groupId (optional)
    product_id = 56 # int | productId (optional)
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve Fixed Deposit Account Template
        api_response = api_instance.template12(client_id=client_id, group_id=group_id, product_id=product_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of FixedDepositAccountApi->template12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->template12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **product_id** | **int**| productId | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetFixedDepositAccountsTemplateResponse**](GetFixedDepositAccountsTemplateResponse.md)

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

# **update16**
> PutFixedDepositAccountsAccountIdResponse update16(account_id, put_fixed_deposit_accounts_account_id_request)

Modify a fixed deposit application

Fixed deposit application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method. Specific api endpoints will be created to allow change of interest detail such as rate, compounding period, posting period etc

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_fixed_deposit_accounts_account_id_request import PutFixedDepositAccountsAccountIdRequest
from fineract_client.models.put_fixed_deposit_accounts_account_id_response import PutFixedDepositAccountsAccountIdResponse
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
    api_instance = fineract_client.FixedDepositAccountApi(api_client)
    account_id = 56 # int | accountId
    put_fixed_deposit_accounts_account_id_request = fineract_client.PutFixedDepositAccountsAccountIdRequest() # PutFixedDepositAccountsAccountIdRequest | 

    try:
        # Modify a fixed deposit application
        api_response = api_instance.update16(account_id, put_fixed_deposit_accounts_account_id_request)
        print("The response of FixedDepositAccountApi->update16:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositAccountApi->update16: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **put_fixed_deposit_accounts_account_id_request** | [**PutFixedDepositAccountsAccountIdRequest**](PutFixedDepositAccountsAccountIdRequest.md)|  | 

### Return type

[**PutFixedDepositAccountsAccountIdResponse**](PutFixedDepositAccountsAccountIdResponse.md)

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

