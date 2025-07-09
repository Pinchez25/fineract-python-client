# fineract_client.SelfLoansApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_loan_schedule_or_submit_loan_application1**](SelfLoansApi.md#calculate_loan_schedule_or_submit_loan_application1) | **POST** /v1/self/loans | Calculate Loan Repayment Schedule | Submit a new Loan Application
[**modify_loan_application2**](SelfLoansApi.md#modify_loan_application2) | **PUT** /v1/self/loans/{loanId} | Update a Loan Application
[**retrieve_all_loan_charges2**](SelfLoansApi.md#retrieve_all_loan_charges2) | **GET** /v1/self/loans/{loanId}/charges | List Loan Charges
[**retrieve_guarantor_details2**](SelfLoansApi.md#retrieve_guarantor_details2) | **GET** /v1/self/loans/{loanId}/guarantors | 
[**retrieve_loan2**](SelfLoansApi.md#retrieve_loan2) | **GET** /v1/self/loans/{loanId} | Retrieve a Loan
[**retrieve_loan_charge4**](SelfLoansApi.md#retrieve_loan_charge4) | **GET** /v1/self/loans/{loanId}/charges/{chargeId} | Retrieve a Loan Charge
[**retrieve_transaction1**](SelfLoansApi.md#retrieve_transaction1) | **GET** /v1/self/loans/{loanId}/transactions/{transactionId} | Retrieve a Loan Transaction Details
[**state_transitions2**](SelfLoansApi.md#state_transitions2) | **POST** /v1/self/loans/{loanId} | Applicant Withdraws from Loan Application
[**template17**](SelfLoansApi.md#template17) | **GET** /v1/self/loans/template | Retrieve Loan Details Template


# **calculate_loan_schedule_or_submit_loan_application1**
> PostSelfLoansResponse calculate_loan_schedule_or_submit_loan_application1(post_self_loans_request, command=command)

Calculate Loan Repayment Schedule | Submit a new Loan Application

Calculate Loan Repayment Schedule:

Calculates Loan Repayment Schedule

Mandatory Fields: productId, principal, loanTermFrequency, loanTermFrequencyType, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, amortizationType, interestType, interestCalculationPeriodType, expectedDisbursementDate, transactionProcessingStrategyCode

Submit a new Loan Application:

Mandatory Fields: clientId, productId, principal, loanTermFrequency, loanTermFrequencyType, loanType, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, amortizationType, interestType, interestCalculationPeriodType, transactionProcessingStrategyCode, expectedDisbursementDate, submittedOnDate, loanType

Additional Mandatory Fields if interest recalculation is enabled for product and Rest frequency not same as repayment period: recalculationRestFrequencyDate

Additional Mandatory Fields if interest recalculation with interest/fee compounding is enabled for product and compounding frequency not same as repayment period: recalculationCompoundingFrequencyDate

Additional Mandatory Field if Entity-Datatable Check is enabled for the entity of type loan: datatables

Optional Fields: graceOnPrincipalPayment, graceOnInterestPayment, graceOnInterestCharged, linkAccountId, allowPartialPeriodInterestCalcualtion, fixedEmiAmount, maxOutstandingLoanBalance, disbursementData, graceOnArrearsAgeing, createStandingInstructionAtDisbursement (requires linkedAccountId if set to true)

Showing request/response for 'Submit a new Loan Application'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_self_loans_request import PostSelfLoansRequest
from fineract_client.models.post_self_loans_response import PostSelfLoansResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    post_self_loans_request = fineract_client.PostSelfLoansRequest() # PostSelfLoansRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Calculate Loan Repayment Schedule | Submit a new Loan Application
        api_response = api_instance.calculate_loan_schedule_or_submit_loan_application1(post_self_loans_request, command=command)
        print("The response of SelfLoansApi->calculate_loan_schedule_or_submit_loan_application1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->calculate_loan_schedule_or_submit_loan_application1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_self_loans_request** | [**PostSelfLoansRequest**](PostSelfLoansRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSelfLoansResponse**](PostSelfLoansResponse.md)

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

# **modify_loan_application2**
> PutSelfLoansLoanIdResponse modify_loan_application2(loan_id, put_self_loans_loan_id_request)

Update a Loan Application

Loan application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_self_loans_loan_id_request import PutSelfLoansLoanIdRequest
from fineract_client.models.put_self_loans_loan_id_response import PutSelfLoansLoanIdResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId
    put_self_loans_loan_id_request = fineract_client.PutSelfLoansLoanIdRequest() # PutSelfLoansLoanIdRequest | 

    try:
        # Update a Loan Application
        api_response = api_instance.modify_loan_application2(loan_id, put_self_loans_loan_id_request)
        print("The response of SelfLoansApi->modify_loan_application2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->modify_loan_application2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **put_self_loans_loan_id_request** | [**PutSelfLoansLoanIdRequest**](PutSelfLoansLoanIdRequest.md)|  | 

### Return type

[**PutSelfLoansLoanIdResponse**](PutSelfLoansLoanIdResponse.md)

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

# **retrieve_all_loan_charges2**
> List[GetSelfLoansLoanIdChargesResponse] retrieve_all_loan_charges2(loan_id)

List Loan Charges

Lists loan Charges

Example Requests:

self/loans/1/charges


self/loans/1/charges?fields=name,amountOrPercentage

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_loans_loan_id_charges_response import GetSelfLoansLoanIdChargesResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId

    try:
        # List Loan Charges
        api_response = api_instance.retrieve_all_loan_charges2(loan_id)
        print("The response of SelfLoansApi->retrieve_all_loan_charges2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->retrieve_all_loan_charges2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**List[GetSelfLoansLoanIdChargesResponse]**](GetSelfLoansLoanIdChargesResponse.md)

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

# **retrieve_guarantor_details2**
> str retrieve_guarantor_details2(loan_id)

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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | 

    try:
        api_response = api_instance.retrieve_guarantor_details2(loan_id)
        print("The response of SelfLoansApi->retrieve_guarantor_details2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->retrieve_guarantor_details2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 

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

# **retrieve_loan2**
> GetSelfLoansLoanIdResponse retrieve_loan2(loan_id)

Retrieve a Loan

Retrieves a Loan

Example Requests:

self/loans/1


self/loans/1?fields=id,principal,annualInterestRate


self/loans/1?fields=id,principal,annualInterestRate&associations=repaymentSchedule,transactions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_loans_loan_id_response import GetSelfLoansLoanIdResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId

    try:
        # Retrieve a Loan
        api_response = api_instance.retrieve_loan2(loan_id)
        print("The response of SelfLoansApi->retrieve_loan2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->retrieve_loan2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**GetSelfLoansLoanIdResponse**](GetSelfLoansLoanIdResponse.md)

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

# **retrieve_loan_charge4**
> GetSelfLoansLoanIdChargesResponse retrieve_loan_charge4(loan_id, charge_id)

Retrieve a Loan Charge

Retrieves a Loan Charge

Example Requests:

self/loans/1/charges/1


self/loans/1/charges/1?fields=name,amountOrPercentage

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_loans_loan_id_charges_response import GetSelfLoansLoanIdChargesResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId
    charge_id = 56 # int | chargeId

    try:
        # Retrieve a Loan Charge
        api_response = api_instance.retrieve_loan_charge4(loan_id, charge_id)
        print("The response of SelfLoansApi->retrieve_loan_charge4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->retrieve_loan_charge4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **charge_id** | **int**| chargeId | 

### Return type

[**GetSelfLoansLoanIdChargesResponse**](GetSelfLoansLoanIdChargesResponse.md)

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

# **retrieve_transaction1**
> GetSelfLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction1(loan_id, transaction_id, fields=fields)

Retrieve a Loan Transaction Details

Retrieves a Loan Transaction DetailsExample Request:

self/loans/5/transactions/3

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_loans_loan_id_transactions_transaction_id_response import GetSelfLoansLoanIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId
    transaction_id = 56 # int | transactionId
    fields = 'id,date,amount' # str | Optional Loan Transaction attribute list to be in the response (optional)

    try:
        # Retrieve a Loan Transaction Details
        api_response = api_instance.retrieve_transaction1(loan_id, transaction_id, fields=fields)
        print("The response of SelfLoansApi->retrieve_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->retrieve_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 
 **fields** | **str**| Optional Loan Transaction attribute list to be in the response | [optional] 

### Return type

[**GetSelfLoansLoanIdTransactionsTransactionIdResponse**](GetSelfLoansLoanIdTransactionsTransactionIdResponse.md)

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

# **state_transitions2**
> PostSelfLoansLoanIdResponse state_transitions2(loan_id, post_self_loans_loan_id_request, command=command)

Applicant Withdraws from Loan Application

Applicant Withdraws from Loan Application

Mandatory Fields: withdrawnOnDate

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_self_loans_loan_id_request import PostSelfLoansLoanIdRequest
from fineract_client.models.post_self_loans_loan_id_response import PostSelfLoansLoanIdResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    loan_id = 56 # int | loanId
    post_self_loans_loan_id_request = fineract_client.PostSelfLoansLoanIdRequest() # PostSelfLoansLoanIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Applicant Withdraws from Loan Application
        api_response = api_instance.state_transitions2(loan_id, post_self_loans_loan_id_request, command=command)
        print("The response of SelfLoansApi->state_transitions2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->state_transitions2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **post_self_loans_loan_id_request** | [**PostSelfLoansLoanIdRequest**](PostSelfLoansLoanIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSelfLoansLoanIdResponse**](PostSelfLoansLoanIdResponse.md)

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

# **template17**
> GetSelfLoansTemplateResponse template17(client_id=client_id, product_id=product_id, template_type=template_type)

Retrieve Loan Details Template

Retrieves Loan Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed description Lists

Example Requests:

self/loans/template?templateType=individual&clientId=1


self/loans/template?templateType=individual&clientId=1&productId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_self_loans_template_response import GetSelfLoansTemplateResponse
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
    api_instance = fineract_client.SelfLoansApi(api_client)
    client_id = 56 # int | clientId (optional)
    product_id = 56 # int | productId (optional)
    template_type = 'template_type_example' # str | templateType (optional)

    try:
        # Retrieve Loan Details Template
        api_response = api_instance.template17(client_id=client_id, product_id=product_id, template_type=template_type)
        print("The response of SelfLoansApi->template17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelfLoansApi->template17: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | [optional] 
 **product_id** | **int**| productId | [optional] 
 **template_type** | **str**| templateType | [optional] 

### Return type

[**GetSelfLoansTemplateResponse**](GetSelfLoansTemplateResponse.md)

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

