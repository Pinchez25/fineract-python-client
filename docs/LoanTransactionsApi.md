# fineract_client.LoanTransactionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_loan_transaction**](LoanTransactionsApi.md#adjust_loan_transaction) | **POST** /v1/loans/{loanId}/transactions/{transactionId} | Adjust a Transaction
[**adjust_loan_transaction1**](LoanTransactionsApi.md#adjust_loan_transaction1) | **POST** /v1/loans/{loanId}/transactions/external-id/{externalTransactionId} | Adjust a Transaction
[**adjust_loan_transaction2**](LoanTransactionsApi.md#adjust_loan_transaction2) | **POST** /v1/loans/external-id/{loanExternalId}/transactions/{transactionId} | Adjust a Transaction
[**adjust_loan_transaction3**](LoanTransactionsApi.md#adjust_loan_transaction3) | **POST** /v1/loans/external-id/{loanExternalId}/transactions/external-id/{externalTransactionId} | Adjust a Transaction
[**execute_loan_transaction**](LoanTransactionsApi.md#execute_loan_transaction) | **POST** /v1/loans/{loanId}/transactions | Significant Loan Transactions
[**execute_loan_transaction1**](LoanTransactionsApi.md#execute_loan_transaction1) | **POST** /v1/loans/external-id/{loanExternalId}/transactions | Significant Loan Transactions
[**retrieve_transaction**](LoanTransactionsApi.md#retrieve_transaction) | **GET** /v1/loans/{loanId}/transactions/{transactionId} | Retrieve a Transaction Details
[**retrieve_transaction_by_loan_external_id_and_transaction_external_id**](LoanTransactionsApi.md#retrieve_transaction_by_loan_external_id_and_transaction_external_id) | **GET** /v1/loans/external-id/{loanExternalId}/transactions/external-id/{externalTransactionId} | Retrieve a Transaction Details
[**retrieve_transaction_by_loan_external_id_and_transaction_id**](LoanTransactionsApi.md#retrieve_transaction_by_loan_external_id_and_transaction_id) | **GET** /v1/loans/external-id/{loanExternalId}/transactions/{transactionId} | Retrieve a Transaction Details
[**retrieve_transaction_by_transaction_external_id**](LoanTransactionsApi.md#retrieve_transaction_by_transaction_external_id) | **GET** /v1/loans/{loanId}/transactions/external-id/{externalTransactionId} | Retrieve a Transaction Details
[**retrieve_transaction_template**](LoanTransactionsApi.md#retrieve_transaction_template) | **GET** /v1/loans/{loanId}/transactions/template | Retrieve Loan Transaction Template
[**retrieve_transaction_template1**](LoanTransactionsApi.md#retrieve_transaction_template1) | **GET** /v1/loans/external-id/{loanExternalId}/transactions/template | Retrieve Loan Transaction Template
[**undo_waive_charge**](LoanTransactionsApi.md#undo_waive_charge) | **PUT** /v1/loans/{loanId}/transactions/{transactionId} | Undo a Waive Charge Transaction
[**undo_waive_charge1**](LoanTransactionsApi.md#undo_waive_charge1) | **PUT** /v1/loans/{loanId}/transactions/external-id/{transactionExternalId} | Undo a Waive Charge Transaction
[**undo_waive_charge2**](LoanTransactionsApi.md#undo_waive_charge2) | **PUT** /v1/loans/external-id/{loanExternalId}/transactions/{transactionId} | Undo a Waive Charge Transaction
[**undo_waive_charge3**](LoanTransactionsApi.md#undo_waive_charge3) | **PUT** /v1/loans/external-id/{loanExternalId}/transactions/external-id/{transactionExternalId} | Undo a Waive Charge Transaction

# **adjust_loan_transaction**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction(body, loan_id, transaction_id, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
loan_id = 789 # int | loanId
transaction_id = 789 # int | transactionId
command = 'command_example' # str | command (optional)

try:
    # Adjust a Transaction
    api_response = api_instance.adjust_loan_transaction(body, loan_id, transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->adjust_loan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_loan_transaction1**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction1(body, loan_id, external_transaction_id, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
loan_id = 789 # int | loanId
external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
command = 'command_example' # str | command (optional)

try:
    # Adjust a Transaction
    api_response = api_instance.adjust_loan_transaction1(body, loan_id, external_transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->adjust_loan_transaction1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_loan_transaction2**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction2(body, loan_external_id, transaction_id, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
transaction_id = 789 # int | transactionId
command = 'command_example' # str | command (optional)

try:
    # Adjust a Transaction
    api_response = api_instance.adjust_loan_transaction2(body, loan_external_id, transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->adjust_loan_transaction2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_id** | **int**| transactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_loan_transaction3**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction3(body, loan_external_id, external_transaction_id, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
command = 'command_example' # str | command (optional)

try:
    # Adjust a Transaction
    api_response = api_instance.adjust_loan_transaction3(body, loan_external_id, external_transaction_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->adjust_loan_transaction3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_transaction**
> PostLoansLoanIdTransactionsResponse execute_loan_transaction(body, loan_id, command=command)

Significant Loan Transactions

This API covers the major loan transaction functionality  Example Requests:  loans/1/transactions?command=repayment | Make a Repayment |  loans/1/transactions?command=merchantIssuedRefund | Merchant Issued Refund |  loans/1/transactions?command=payoutRefund | Payout Refund |  loans/1/transactions?command=goodwillCredit | Goodwil Credit |  loans/1/transactions?command=chargeRefund | Charge Refund |  loans/1/transactions?command=waiveinterest | Waive Interest |  loans/1/transactions?command=writeoff | Write-off Loan |  loans/1/transactions?command=close-rescheduled | Close Rescheduled Loan |  loans/1/transactions?command=close | Close Loan |  loans/1/transactions?command=undowriteoff | Undo Loan Write-off |  loans/1/transactions?command=recoverypayment | Make Recovery Payment |  loans/1/transactions?command=refundByCash | Make a Refund of an Active Loan by Cash |  loans/1/transactions?command=foreclosure | Foreclosure of an Active Loan |  loans/1/transactions?command=creditBalanceRefund | Credit Balance Refund |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=charge-off | Charge-off Loan |   loans/1/transactions?command=downPayment | Down Payment | 

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsRequest() # PostLoansLoanIdTransactionsRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Significant Loan Transactions
    api_response = api_instance.execute_loan_transaction(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->execute_loan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsRequest**](PostLoansLoanIdTransactionsRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_transaction1**
> PostLoansLoanIdTransactionsResponse execute_loan_transaction1(body, loan_external_id, command=command)

Significant Loan Transactions

This API covers the major loan transaction functionality  Example Requests:  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=repayment | Make a Repayment |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=merchantIssuedRefund | Merchant Issued Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=payoutRefund | Payout Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=goodwillCredit | Goodwil Credit |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=chargeRefund | Charge Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=waiveinterest | Waive Interest |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=writeoff | Write-off Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=close-rescheduled | Close Rescheduled Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=close | Close Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=undowriteoff | Undo Loan Write-off |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=recoverypayment | Make Recovery Payment |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=refundByCash | Make a Refund of an Active Loan by Cash |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=foreclosure | Foreclosure of an Active Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=creditBalanceRefund | Credit Balance Refund |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=charge-off | Charge-off Loan |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=downPayment | Down Payment | 

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdTransactionsRequest() # PostLoansLoanIdTransactionsRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
command = 'command_example' # str | command (optional)

try:
    # Significant Loan Transactions
    api_response = api_instance.execute_loan_transaction1(body, loan_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->execute_loan_transaction1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdTransactionsRequest**](PostLoansLoanIdTransactionsRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction(loan_id, transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/3

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
transaction_id = 789 # int | transactionId
fields = 'fields_example' # str | Optional Loan Transaction attribute list to be in the response (optional)

try:
    # Retrieve a Transaction Details
    api_response = api_instance.retrieve_transaction(loan_id, transaction_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 
 **fields** | **str**| Optional Loan Transaction attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTransactionIdResponse**](GetLoansLoanIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_loan_external_id_and_transaction_external_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_loan_external_id_and_transaction_external_id(loan_external_id, external_transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/external-id/5dd80a7c-ccba-4446-b378-01eb6f53e871

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
fields = 'fields_example' # str | Optional Loan Transaction attribute list to be in the response (optional)

try:
    # Retrieve a Transaction Details
    api_response = api_instance.retrieve_transaction_by_loan_external_id_and_transaction_external_id(loan_external_id, external_transaction_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction_by_loan_external_id_and_transaction_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **fields** | **str**| Optional Loan Transaction attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTransactionIdResponse**](GetLoansLoanIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_loan_external_id_and_transaction_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_loan_external_id_and_transaction_id(loan_external_id, transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/3

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
transaction_id = 789 # int | transactionId
fields = 'fields_example' # str | Optional Loan Transaction attribute list to be in the response (optional)

try:
    # Retrieve a Transaction Details
    api_response = api_instance.retrieve_transaction_by_loan_external_id_and_transaction_id(loan_external_id, transaction_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction_by_loan_external_id_and_transaction_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_id** | **int**| transactionId | 
 **fields** | **str**| Optional Loan Transaction attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTransactionIdResponse**](GetLoansLoanIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_transaction_external_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_transaction_external_id(loan_id, external_transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/external-id/5dd80a7c-ccba-4446-b378-01eb6f53e871

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
fields = 'fields_example' # str | Optional Loan Transaction attribute list to be in the response (optional)

try:
    # Retrieve a Transaction Details
    api_response = api_instance.retrieve_transaction_by_transaction_external_id(loan_id, external_transaction_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction_by_transaction_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **fields** | **str**| Optional Loan Transaction attribute list to be in the response | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTransactionIdResponse**](GetLoansLoanIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_template**
> GetLoansLoanIdTransactionsTemplateResponse retrieve_transaction_template(loan_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)

Retrieve Loan Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  loans/1/transactions/template?command=repaymentloans/1/transactions/template?command=merchantIssuedRefundloans/1/transactions/template?command=payoutRefundloans/1/transactions/template?command=goodwillCredit loans/1/transactions/template?command=waiveinterest loans/1/transactions/template?command=writeoff loans/1/transactions/template?command=close-rescheduled loans/1/transactions/template?command=close loans/1/transactions/template?command=disburse loans/1/transactions/template?command=disburseToSavings loans/1/transactions/template?command=recoverypayment loans/1/transactions/template?command=prepayLoan loans/1/transactions/template?command=refundbycash loans/1/transactions/template?command=refundbytransfer loans/1/transactions/template?command=foreclosure loans/1/transactions/template?command=interestPaymentWaiver loans/1/transactions/template?command=creditBalanceRefund (returned 'amount' field will have the overpaid value) loans/1/transactions/template?command=charge-off loans/1/transactions/template?command=downPayment 

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)
date_format = 'date_format_example' # str | dateFormat (optional)
transaction_date = fineract_client.DateParam() # DateParam | transactionDate (optional)
locale = 'locale_example' # str | locale (optional)

try:
    # Retrieve Loan Transaction Template
    api_response = api_instance.retrieve_transaction_template(loan_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **transaction_date** | [**DateParam**](.md)| transactionDate | [optional] 
 **locale** | **str**| locale | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTemplateResponse**](GetLoansLoanIdTransactionsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_template1**
> GetLoansLoanIdTransactionsTemplateResponse retrieve_transaction_template1(loan_external_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)

Retrieve Loan Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  loans/1/transactions/template?command=repaymentloans/1/transactions/template?command=merchantIssuedRefundloans/1/transactions/template?command=payoutRefundloans/1/transactions/template?command=goodwillCredit loans/1/transactions/template?command=waiveinterest loans/1/transactions/template?command=writeoff loans/1/transactions/template?command=close-rescheduled loans/1/transactions/template?command=close loans/1/transactions/template?command=disburse loans/1/transactions/template?command=disburseToSavings loans/1/transactions/template?command=recoverypayment loans/1/transactions/template?command=prepayLoan loans/1/transactions/template?command=refundbycash loans/1/transactions/template?command=refundbytransfer loans/1/transactions/template?command=foreclosure loans/1/transactions/template?command=interestPaymentWaiver loans/1/transactions/template?command=creditBalanceRefund (returned 'amount' field will have the overpaid value) loans/1/transactions/template?command=charge-off loans/1/transactions/template?command=downPayment 

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
command = 'command_example' # str | command (optional)
date_format = 'date_format_example' # str | dateFormat (optional)
transaction_date = fineract_client.DateParam() # DateParam | transactionDate (optional)
locale = 'locale_example' # str | locale (optional)

try:
    # Retrieve Loan Transaction Template
    api_response = api_instance.retrieve_transaction_template1(loan_external_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->retrieve_transaction_template1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **transaction_date** | [**DateParam**](.md)| transactionDate | [optional] 
 **locale** | **str**| locale | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTemplateResponse**](GetLoansLoanIdTransactionsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undo_waive_charge**
> PutChargeTransactionChangesResponse undo_waive_charge(body, loan_id, transaction_id)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 
loan_id = 789 # int | loanId
transaction_id = 789 # int | transactionId

try:
    # Undo a Waive Charge Transaction
    api_response = api_instance.undo_waive_charge(body, loan_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->undo_waive_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undo_waive_charge1**
> PutChargeTransactionChangesResponse undo_waive_charge1(body, loan_id, transaction_external_id)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 
loan_id = 789 # int | loanId
transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId

try:
    # Undo a Waive Charge Transaction
    api_response = api_instance.undo_waive_charge1(body, loan_id, transaction_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->undo_waive_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **transaction_external_id** | **str**| transactionExternalId | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undo_waive_charge2**
> PutChargeTransactionChangesResponse undo_waive_charge2(body, loan_external_id, transaction_id)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
transaction_id = 789 # int | transactionId

try:
    # Undo a Waive Charge Transaction
    api_response = api_instance.undo_waive_charge2(body, loan_external_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->undo_waive_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undo_waive_charge3**
> PutChargeTransactionChangesResponse undo_waive_charge3(body, loan_external_id, transaction_external_id)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

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
api_instance = fineract_client.LoanTransactionsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId

try:
    # Undo a Waive Charge Transaction
    api_response = api_instance.undo_waive_charge3(body, loan_external_id, transaction_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanTransactionsApi->undo_waive_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_external_id** | **str**| transactionExternalId | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

