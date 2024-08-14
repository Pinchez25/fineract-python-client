# fineract_client.LoansApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_loan_schedule_or_submit_loan_application**](LoansApi.md#calculate_loan_schedule_or_submit_loan_application) | **POST** /v1/loans | Calculate loan repayment schedule | Submit a new Loan Application
[**create_loan_delinquency_action**](LoansApi.md#create_loan_delinquency_action) | **POST** /v1/loans/{loanId}/delinquency-actions | Adds a new delinquency action for a loan
[**create_loan_delinquency_action1**](LoansApi.md#create_loan_delinquency_action1) | **POST** /v1/loans/external-id/{loanExternalId}/delinquency-actions | Adds a new delinquency action for a loan
[**delete_loan_application**](LoansApi.md#delete_loan_application) | **DELETE** /v1/loans/{loanId} | Delete a Loan Application
[**delete_loan_application1**](LoansApi.md#delete_loan_application1) | **DELETE** /v1/loans/external-id/{loanExternalId} | Delete a Loan Application
[**get_delinquency_tag_history**](LoansApi.md#get_delinquency_tag_history) | **GET** /v1/loans/{loanId}/delinquencytags | Retrieve the Loan Delinquency Tag history using the Loan Id
[**get_delinquency_tag_history1**](LoansApi.md#get_delinquency_tag_history1) | **GET** /v1/loans/external-id/{loanExternalId}/delinquencytags | Retrieve the Loan Delinquency Tag history using the Loan Id
[**get_glim_repayment_template**](LoansApi.md#get_glim_repayment_template) | **GET** /v1/loans/glimAccount/{glimId} | 
[**get_loan_delinquency_actions**](LoansApi.md#get_loan_delinquency_actions) | **GET** /v1/loans/{loanId}/delinquency-actions | Retrieve delinquency actions related to the loan
[**get_loan_delinquency_actions1**](LoansApi.md#get_loan_delinquency_actions1) | **GET** /v1/loans/external-id/{loanExternalId}/delinquency-actions | Retrieve delinquency actions related to the loan
[**get_loan_repayment_template**](LoansApi.md#get_loan_repayment_template) | **GET** /v1/loans/repayments/downloadtemplate | 
[**get_loans_template**](LoansApi.md#get_loans_template) | **GET** /v1/loans/downloadtemplate | 
[**glim_state_transitions**](LoansApi.md#glim_state_transitions) | **POST** /v1/loans/glimAccount/{glimId} | Approve GLIM Application | Undo GLIM Application Approval | Reject GLIM Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
[**modify_loan_application**](LoansApi.md#modify_loan_application) | **PUT** /v1/loans/{loanId} | Modify a loan application
[**modify_loan_application1**](LoansApi.md#modify_loan_application1) | **PUT** /v1/loans/external-id/{loanExternalId} | Modify a loan application
[**post_loan_repayment_template**](LoansApi.md#post_loan_repayment_template) | **POST** /v1/loans/repayments/uploadtemplate | 
[**post_loan_template**](LoansApi.md#post_loan_template) | **POST** /v1/loans/uploadtemplate | 
[**retrieve_all27**](LoansApi.md#retrieve_all27) | **GET** /v1/loans | List Loans
[**retrieve_approval_template**](LoansApi.md#retrieve_approval_template) | **GET** /v1/loans/{loanId}/template | 
[**retrieve_approval_template1**](LoansApi.md#retrieve_approval_template1) | **GET** /v1/loans/external-id/{loanExternalId}/template | 
[**retrieve_loan**](LoansApi.md#retrieve_loan) | **GET** /v1/loans/{loanId} | Retrieve a Loan
[**retrieve_loan1**](LoansApi.md#retrieve_loan1) | **GET** /v1/loans/external-id/{loanExternalId} | Retrieve a Loan
[**state_transitions**](LoansApi.md#state_transitions) | **POST** /v1/loans/{loanId} | Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
[**state_transitions1**](LoansApi.md#state_transitions1) | **POST** /v1/loans/external-id/{loanExternalId} | Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
[**template10**](LoansApi.md#template10) | **GET** /v1/loans/template | Retrieve Loan Details Template

# **calculate_loan_schedule_or_submit_loan_application**
> PostLoansResponse calculate_loan_schedule_or_submit_loan_application(body, command=command)

Calculate loan repayment schedule | Submit a new Loan Application

It calculates the loan repayment Schedule Submits a new loan application Mandatory Fields: clientId, productId, principal, loanTermFrequency, loanTermFrequencyType, loanType, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, amortizationType, interestType, interestCalculationPeriodType, transactionProcessingStrategyCode, expectedDisbursementDate, submittedOnDate, loanType Optional Fields: graceOnPrincipalPayment, graceOnInterestPayment, graceOnInterestCharged, linkAccountId, allowPartialPeriodInterestCalcualtion, fixedEmiAmount, maxOutstandingLoanBalance, disbursementData, graceOnArrearsAgeing, createStandingInstructionAtDisbursement (requires linkedAccountId if set to true) Additional Mandatory Fields if interest recalculation is enabled for product and Rest frequency not same as repayment period: recalculationRestFrequencyDate Additional Mandatory Fields if interest recalculation with interest/fee compounding is enabled for product and compounding frequency not same as repayment period: recalculationCompoundingFrequencyDate Additional Mandatory Field if Entity-Datatable Check is enabled for the entity of type loan: datatables

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansRequest() # PostLoansRequest | 
command = 'command_example' # str | command (optional)

try:
    # Calculate loan repayment schedule | Submit a new Loan Application
    api_response = api_instance.calculate_loan_schedule_or_submit_loan_application(body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->calculate_loan_schedule_or_submit_loan_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansRequest**](PostLoansRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansResponse**](PostLoansResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_delinquency_action**
> PostLoansDelinquencyActionResponse create_loan_delinquency_action(body, loan_id)

Adds a new delinquency action for a loan

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansDelinquencyActionRequest() # PostLoansDelinquencyActionRequest | 
loan_id = 789 # int | loanId

try:
    # Adds a new delinquency action for a loan
    api_response = api_instance.create_loan_delinquency_action(body, loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->create_loan_delinquency_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansDelinquencyActionRequest**](PostLoansDelinquencyActionRequest.md)|  | 
 **loan_id** | **int**| loanId | 

### Return type

[**PostLoansDelinquencyActionResponse**](PostLoansDelinquencyActionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan_delinquency_action1**
> PostLoansDelinquencyActionResponse create_loan_delinquency_action1(body, loan_external_id)

Adds a new delinquency action for a loan

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansDelinquencyActionRequest() # PostLoansDelinquencyActionRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # Adds a new delinquency action for a loan
    api_response = api_instance.create_loan_delinquency_action1(body, loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->create_loan_delinquency_action1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansDelinquencyActionRequest**](PostLoansDelinquencyActionRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**PostLoansDelinquencyActionResponse**](PostLoansDelinquencyActionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_application**
> DeleteLoansLoanIdResponse delete_loan_application(loan_id)

Delete a Loan Application

Note: Only loans in \"Submitted and awaiting approval\" status can be deleted.

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Delete a Loan Application
    api_response = api_instance.delete_loan_application(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->delete_loan_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**DeleteLoansLoanIdResponse**](DeleteLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_application1**
> DeleteLoansLoanIdResponse delete_loan_application1(loan_external_id)

Delete a Loan Application

Note: Only loans in \"Submitted and awaiting approval\" status can be deleted.

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # Delete a Loan Application
    api_response = api_instance.delete_loan_application1(loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->delete_loan_application1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**DeleteLoansLoanIdResponse**](DeleteLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_tag_history**
> list[GetDelinquencyTagHistoryResponse] get_delinquency_tag_history(loan_id)

Retrieve the Loan Delinquency Tag history using the Loan Id

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Retrieve the Loan Delinquency Tag history using the Loan Id
    api_response = api_instance.get_delinquency_tag_history(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_delinquency_tag_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetDelinquencyTagHistoryResponse]**](GetDelinquencyTagHistoryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delinquency_tag_history1**
> list[GetDelinquencyTagHistoryResponse] get_delinquency_tag_history1(loan_external_id)

Retrieve the Loan Delinquency Tag history using the Loan Id

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # Retrieve the Loan Delinquency Tag history using the Loan Id
    api_response = api_instance.get_delinquency_tag_history1(loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_delinquency_tag_history1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**list[GetDelinquencyTagHistoryResponse]**](GetDelinquencyTagHistoryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_glim_repayment_template**
> str get_glim_repayment_template(glim_id)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
glim_id = 789 # int | 

try:
    api_response = api_instance.get_glim_repayment_template(glim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_glim_repayment_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glim_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_delinquency_actions**
> list[GetDelinquencyActionsResponse] get_loan_delinquency_actions(loan_id)

Retrieve delinquency actions related to the loan

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Retrieve delinquency actions related to the loan
    api_response = api_instance.get_loan_delinquency_actions(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_loan_delinquency_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetDelinquencyActionsResponse]**](GetDelinquencyActionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_delinquency_actions1**
> list[GetDelinquencyActionsResponse] get_loan_delinquency_actions1(loan_external_id)

Retrieve delinquency actions related to the loan

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # Retrieve delinquency actions related to the loan
    api_response = api_instance.get_loan_delinquency_actions1(loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->get_loan_delinquency_actions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**list[GetDelinquencyActionsResponse]**](GetDelinquencyActionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_repayment_template**
> get_loan_repayment_template(office_id=office_id, date_format=date_format)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_loan_repayment_template(office_id=office_id, date_format=date_format)
except ApiException as e:
    print("Exception when calling LoansApi->get_loan_repayment_template: %s\n" % e)
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

# **get_loans_template**
> get_loans_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
staff_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_loans_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
except ApiException as e:
    print("Exception when calling LoansApi->get_loans_template: %s\n" % e)
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

# **glim_state_transitions**
> PostLoansLoanIdResponse glim_state_transitions(body, glim_id, command=command)

Approve GLIM Application | Undo GLIM Application Approval | Reject GLIM Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal

Approve GLIM Application: Mandatory Fields: approvedOnDate Optional Fields: approvedLoanAmount and expectedDisbursementDate Approves the GLIM application  Undo GLIM Application Approval: Undoes the GLIM Application Approval  Reject GLIM Application: Mandatory Fields: rejectedOnDate Allows you to reject the GLIM application  Disburse Loan: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the Loan  Disburse Loan To Savings Account: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the loan to Saving Account  Undo Loan Disbursal: Undoes the Loan Disbursal 

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdRequest() # PostLoansLoanIdRequest | 
glim_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    # Approve GLIM Application | Undo GLIM Application Approval | Reject GLIM Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
    api_response = api_instance.glim_state_transitions(body, glim_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->glim_state_transitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdRequest**](PostLoansLoanIdRequest.md)|  | 
 **glim_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**PostLoansLoanIdResponse**](PostLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_loan_application**
> PutLoansLoanIdResponse modify_loan_application(body, loan_id, command=command)

Modify a loan application

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdRequest() # PutLoansLoanIdRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Modify a loan application
    api_response = api_instance.modify_loan_application(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->modify_loan_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdRequest**](PutLoansLoanIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PutLoansLoanIdResponse**](PutLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_loan_application1**
> PutLoansLoanIdResponse modify_loan_application1(body, loan_external_id, command=command)

Modify a loan application

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdRequest() # PutLoansLoanIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
command = 'command_example' # str | command (optional)

try:
    # Modify a loan application
    api_response = api_instance.modify_loan_application1(body, loan_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->modify_loan_application1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdRequest**](PutLoansLoanIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PutLoansLoanIdResponse**](PutLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_loan_repayment_template**
> str post_loan_repayment_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_loan_repayment_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->post_loan_repayment_template: %s\n" % e)
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

# **post_loan_template**
> str post_loan_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_loan_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->post_loan_template: %s\n" % e)
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

# **retrieve_all27**
> GetLoansResponse retrieve_all27(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no, status=status)

List Loans

The list capability of loans can support pagination and sorting. Example Requests:  loans  loans?fields=accountNo  loans?offset=10&limit=50  loans?orderBy=accountNo&sortOrder=DESC

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
account_no = 'account_no_example' # str | accountNo (optional)
status = 'status_example' # str | status (optional)

try:
    # List Loans
    api_response = api_instance.retrieve_all27(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->retrieve_all27: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **account_no** | **str**| accountNo | [optional] 
 **status** | **str**| status | [optional] 

### Return type

[**GetLoansResponse**](GetLoansResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_approval_template**
> GetLoansApprovalTemplateResponse retrieve_approval_template(loan_id, template_type=template_type)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
template_type = 'template_type_example' # str | templateType (optional)

try:
    api_response = api_instance.retrieve_approval_template(loan_id, template_type=template_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->retrieve_approval_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **template_type** | **str**| templateType | [optional] 

### Return type

[**GetLoansApprovalTemplateResponse**](GetLoansApprovalTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_approval_template1**
> GetLoansApprovalTemplateResponse retrieve_approval_template1(loan_external_id, template_type=template_type)



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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
template_type = 'template_type_example' # str | templateType (optional)

try:
    api_response = api_instance.retrieve_approval_template1(loan_external_id, template_type=template_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->retrieve_approval_template1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **template_type** | **str**| templateType | [optional] 

### Return type

[**GetLoansApprovalTemplateResponse**](GetLoansApprovalTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan**
> GetLoansLoanIdResponse retrieve_loan(loan_id, staff_in_selected_office_only=staff_in_selected_office_only, associations=associations, exclude=exclude, fields=fields)

Retrieve a Loan

Note: template=true parameter doesn't apply to this resource.Example Requests:  loans/1   loans/1?fields=id,principal,annualInterestRate   loans/1?associations=all  loans/1?associations=all&exclude=guarantors   loans/1?fields=id,principal,annualInterestRate&associations=repaymentSchedule,transactions

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)
associations = 'all' # str | Loan object relations to be included in the response (optional) (default to all)
exclude = 'exclude_example' # str | Optional Loan object relation list to be filtered in the response (optional)
fields = 'fields_example' # str | Optional Loan attribute list to be in the response (optional)

try:
    # Retrieve a Loan
    api_response = api_instance.retrieve_loan(loan_id, staff_in_selected_office_only=staff_in_selected_office_only, associations=associations, exclude=exclude, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->retrieve_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]
 **associations** | **str**| Loan object relations to be included in the response | [optional] [default to all]
 **exclude** | **str**| Optional Loan object relation list to be filtered in the response | [optional] 
 **fields** | **str**| Optional Loan attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdResponse**](GetLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan1**
> GetLoansLoanIdResponse retrieve_loan1(loan_external_id, staff_in_selected_office_only=staff_in_selected_office_only, associations=associations, exclude=exclude, fields=fields)

Retrieve a Loan

Note: template=true parameter doesn't apply to this resource.Example Requests:  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?fields=id,principal,annualInterestRate   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?associations=all  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?associations=all&exclude=guarantors   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854?fields=id,principal,annualInterestRate&associations=repaymentSchedule,transactions

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)
associations = 'all' # str | Loan object relations to be included in the response (optional) (default to all)
exclude = 'exclude_example' # str | Optional Loan object relation list to be filtered in the response (optional)
fields = 'fields_example' # str | Optional Loan attribute list to be in the response (optional)

try:
    # Retrieve a Loan
    api_response = api_instance.retrieve_loan1(loan_external_id, staff_in_selected_office_only=staff_in_selected_office_only, associations=associations, exclude=exclude, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->retrieve_loan1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]
 **associations** | **str**| Loan object relations to be included in the response | [optional] [default to all]
 **exclude** | **str**| Optional Loan object relation list to be filtered in the response | [optional] 
 **fields** | **str**| Optional Loan attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdResponse**](GetLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_transitions**
> PostLoansLoanIdResponse state_transitions(body, loan_id, command=command)

Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal

Approve Loan Application: Mandatory Fields: approvedOnDate Optional Fields: approvedLoanAmount and expectedDisbursementDate Approves the loan application  Recover Loan Guarantee: Recovers the loan guarantee  Undo Loan Application Approval: Undoes the Loan Application Approval  Assign a Loan Officer: Allows you to assign Loan Officer for existing Loan.  Unassign a Loan Officer: Allows you to unassign the Loan Officer.  Reject Loan Application: Mandatory Fields: rejectedOnDate Allows you to reject the loan application  Applicant Withdraws from Loan Application: Mandatory Fields: withdrawnOnDate Allows the applicant to withdraw the loan application  Disburse Loan: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the Loan  Disburse Loan To Savings Account: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the loan to Saving Account  Undo Loan Disbursal: Undoes the Loan Disbursal Showing request and response for Assign a Loan Officer

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdRequest() # PostLoansLoanIdRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
    api_response = api_instance.state_transitions(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->state_transitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdRequest**](PostLoansLoanIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdResponse**](PostLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_transitions1**
> PostLoansLoanIdResponse state_transitions1(body, loan_external_id, command=command)

Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal

Approve Loan Application: Mandatory Fields: approvedOnDate Optional Fields: approvedLoanAmount and expectedDisbursementDate Approves the loan application  Recover Loan Guarantee: Recovers the loan guarantee  Undo Loan Application Approval: Undoes the Loan Application Approval  Assign a Loan Officer: Allows you to assign Loan Officer for existing Loan.  Unassign a Loan Officer: Allows you to unassign the Loan Officer.  Reject Loan Application: Mandatory Fields: rejectedOnDate Allows you to reject the loan application  Applicant Withdraws from Loan Application: Mandatory Fields: withdrawnOnDate Allows the applicant to withdraw the loan application  Disburse Loan: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the Loan  Disburse Loan To Savings Account: Mandatory Fields: actualDisbursementDate Optional Fields: transactionAmount and fixedEmiAmount Disburses the loan to Saving Account  Undo Loan Disbursal: Undoes the Loan Disbursal Showing request and response for Assign a Loan Officer

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdRequest() # PostLoansLoanIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
command = 'command_example' # str | command (optional)

try:
    # Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal
    api_response = api_instance.state_transitions1(body, loan_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->state_transitions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdRequest**](PostLoansLoanIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdResponse**](PostLoansLoanIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template10**
> GetLoansTemplateResponse template10(client_id=client_id, group_id=group_id, product_id=product_id, template_type=template_type, staff_in_selected_office_only=staff_in_selected_office_only, active_only=active_only)

Retrieve Loan Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Requests:  loans/template?templateType=individual&clientId=1   loans/template?templateType=individual&clientId=1&productId=1

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
api_instance = fineract_client.LoansApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId (optional)
group_id = 789 # int | groupId (optional)
product_id = 789 # int | productId (optional)
template_type = 'template_type_example' # str | templateType (optional)
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)
active_only = false # bool | activeOnly (optional) (default to false)

try:
    # Retrieve Loan Details Template
    api_response = api_instance.template10(client_id=client_id, group_id=group_id, product_id=product_id, template_type=template_type, staff_in_selected_office_only=staff_in_selected_office_only, active_only=active_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->template10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **product_id** | **int**| productId | [optional] 
 **template_type** | **str**| templateType | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]
 **active_only** | **bool**| activeOnly | [optional] [default to false]

### Return type

[**GetLoansTemplateResponse**](GetLoansTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

