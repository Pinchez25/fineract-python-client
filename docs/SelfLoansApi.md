# fineract_client.SelfLoansApi

All URIs are relative to */fineract-provider/api/v1*

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
> PostSelfLoansResponse calculate_loan_schedule_or_submit_loan_application1(body, command=command)

Calculate Loan Repayment Schedule | Submit a new Loan Application

Calculate Loan Repayment Schedule:  Calculates Loan Repayment Schedule  Mandatory Fields: productId, principal, loanTermFrequency, loanTermFrequencyType, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, amortizationType, interestType, interestCalculationPeriodType, expectedDisbursementDate, transactionProcessingStrategyCode  Submit a new Loan Application:  Mandatory Fields: clientId, productId, principal, loanTermFrequency, loanTermFrequencyType, loanType, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, amortizationType, interestType, interestCalculationPeriodType, transactionProcessingStrategyCode, expectedDisbursementDate, submittedOnDate, loanType  Additional Mandatory Fields if interest recalculation is enabled for product and Rest frequency not same as repayment period: recalculationRestFrequencyDate  Additional Mandatory Fields if interest recalculation with interest/fee compounding is enabled for product and compounding frequency not same as repayment period: recalculationCompoundingFrequencyDate  Additional Mandatory Field if Entity-Datatable Check is enabled for the entity of type loan: datatables  Optional Fields: graceOnPrincipalPayment, graceOnInterestPayment, graceOnInterestCharged, linkAccountId, allowPartialPeriodInterestCalcualtion, fixedEmiAmount, maxOutstandingLoanBalance, disbursementData, graceOnArrearsAgeing, createStandingInstructionAtDisbursement (requires linkedAccountId if set to true)  Showing request/response for 'Submit a new Loan Application'

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSelfLoansRequest() # PostSelfLoansRequest | 
command = 'command_example' # str | command (optional)

try:
    # Calculate Loan Repayment Schedule | Submit a new Loan Application
    api_response = api_instance.calculate_loan_schedule_or_submit_loan_application1(body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfLoansApi->calculate_loan_schedule_or_submit_loan_application1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSelfLoansRequest**](PostSelfLoansRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSelfLoansResponse**](PostSelfLoansResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_loan_application2**
> PutSelfLoansLoanIdResponse modify_loan_application2(body, loan_id)

Update a Loan Application

Loan application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method.

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutSelfLoansLoanIdRequest() # PutSelfLoansLoanIdRequest | 
loan_id = 789 # int | loanId

try:
    # Update a Loan Application
    api_response = api_instance.modify_loan_application2(body, loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfLoansApi->modify_loan_application2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSelfLoansLoanIdRequest**](PutSelfLoansLoanIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 

### Return type

[**PutSelfLoansLoanIdResponse**](PutSelfLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_loan_charges2**
> list[GetSelfLoansLoanIdChargesResponse] retrieve_all_loan_charges2(loan_id)

List Loan Charges

Lists loan Charges  Example Requests:  self/loans/1/charges   self/loans/1/charges?fields=name,amountOrPercentage

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # List Loan Charges
    api_response = api_instance.retrieve_all_loan_charges2(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfLoansApi->retrieve_all_loan_charges2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetSelfLoansLoanIdChargesResponse]**](GetSelfLoansLoanIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_guarantor_details2**
> str retrieve_guarantor_details2(loan_id)



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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 

try:
    api_response = api_instance.retrieve_guarantor_details2(loan_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan2**
> GetSelfLoansLoanIdResponse retrieve_loan2(loan_id)

Retrieve a Loan

Retrieves a Loan  Example Requests:  self/loans/1   self/loans/1?fields=id,principal,annualInterestRate   self/loans/1?fields=id,principal,annualInterestRate&associations=repaymentSchedule,transactions

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Retrieve a Loan
    api_response = api_instance.retrieve_loan2(loan_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan_charge4**
> GetSelfLoansLoanIdChargesResponse retrieve_loan_charge4(loan_id, charge_id)

Retrieve a Loan Charge

Retrieves a Loan Charge  Example Requests:  self/loans/1/charges/1   self/loans/1/charges/1?fields=name,amountOrPercentage

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
charge_id = 789 # int | chargeId

try:
    # Retrieve a Loan Charge
    api_response = api_instance.retrieve_loan_charge4(loan_id, charge_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction1**
> GetSelfLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction1(loan_id, transaction_id, fields=fields)

Retrieve a Loan Transaction Details

Retrieves a Loan Transaction DetailsExample Request:  self/loans/5/transactions/3

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
transaction_id = 789 # int | transactionId
fields = 'fields_example' # str | Optional Loan Transaction attribute list to be in the response (optional)

try:
    # Retrieve a Loan Transaction Details
    api_response = api_instance.retrieve_transaction1(loan_id, transaction_id, fields=fields)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_transitions2**
> PostSelfLoansLoanIdResponse state_transitions2(body, loan_id, command=command)

Applicant Withdraws from Loan Application

Applicant Withdraws from Loan Application  Mandatory Fields: withdrawnOnDate

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSelfLoansLoanIdRequest() # PostSelfLoansLoanIdRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Applicant Withdraws from Loan Application
    api_response = api_instance.state_transitions2(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfLoansApi->state_transitions2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSelfLoansLoanIdRequest**](PostSelfLoansLoanIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSelfLoansLoanIdResponse**](PostSelfLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template17**
> GetSelfLoansTemplateResponse template17(client_id=client_id, product_id=product_id, template_type=template_type)

Retrieve Loan Details Template

Retrieves Loan Details Template  This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists  Example Requests:  self/loans/template?templateType=individual&clientId=1   self/loans/template?templateType=individual&clientId=1&productId=1

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
api_instance = fineract_client.SelfLoansApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId (optional)
product_id = 789 # int | productId (optional)
template_type = 'template_type_example' # str | templateType (optional)

try:
    # Retrieve Loan Details Template
    api_response = api_instance.template17(client_id=client_id, product_id=product_id, template_type=template_type)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

