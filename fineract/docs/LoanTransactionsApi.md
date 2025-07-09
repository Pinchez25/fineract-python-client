# fineract_client.LoanTransactionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

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
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction(loan_id, transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
from fineract_client.models.post_loans_loan_id_transactions_transaction_id_request import PostLoansLoanIdTransactionsTransactionIdRequest
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    transaction_id = 56 # int | transactionId
    post_loans_loan_id_transactions_transaction_id_request = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Adjust a Transaction
        api_response = api_instance.adjust_loan_transaction(loan_id, transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)
        print("The response of LoanTransactionsApi->adjust_loan_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->adjust_loan_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 
 **post_loans_loan_id_transactions_transaction_id_request** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **adjust_loan_transaction1**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction1(loan_id, external_transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
from fineract_client.models.post_loans_loan_id_transactions_transaction_id_request import PostLoansLoanIdTransactionsTransactionIdRequest
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
    post_loans_loan_id_transactions_transaction_id_request = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Adjust a Transaction
        api_response = api_instance.adjust_loan_transaction1(loan_id, external_transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)
        print("The response of LoanTransactionsApi->adjust_loan_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->adjust_loan_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **post_loans_loan_id_transactions_transaction_id_request** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **adjust_loan_transaction2**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction2(loan_external_id, transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
from fineract_client.models.post_loans_loan_id_transactions_transaction_id_request import PostLoansLoanIdTransactionsTransactionIdRequest
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    transaction_id = 56 # int | transactionId
    post_loans_loan_id_transactions_transaction_id_request = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Adjust a Transaction
        api_response = api_instance.adjust_loan_transaction2(loan_external_id, transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)
        print("The response of LoanTransactionsApi->adjust_loan_transaction2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->adjust_loan_transaction2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_id** | **int**| transactionId | 
 **post_loans_loan_id_transactions_transaction_id_request** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **adjust_loan_transaction3**
> PostLoansLoanIdTransactionsResponse adjust_loan_transaction3(loan_external_id, external_transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)

Adjust a Transaction

Note: there is no need to specify command={transactionType} parameter.  Mandatory Fields: transactionDate, transactionAmount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
from fineract_client.models.post_loans_loan_id_transactions_transaction_id_request import PostLoansLoanIdTransactionsTransactionIdRequest
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
    post_loans_loan_id_transactions_transaction_id_request = fineract_client.PostLoansLoanIdTransactionsTransactionIdRequest() # PostLoansLoanIdTransactionsTransactionIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Adjust a Transaction
        api_response = api_instance.adjust_loan_transaction3(loan_external_id, external_transaction_id, post_loans_loan_id_transactions_transaction_id_request, command=command)
        print("The response of LoanTransactionsApi->adjust_loan_transaction3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->adjust_loan_transaction3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **external_transaction_id** | **str**| externalTransactionId | 
 **post_loans_loan_id_transactions_transaction_id_request** | [**PostLoansLoanIdTransactionsTransactionIdRequest**](PostLoansLoanIdTransactionsTransactionIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **execute_loan_transaction**
> PostLoansLoanIdTransactionsResponse execute_loan_transaction(loan_id, post_loans_loan_id_transactions_request, command=command)

Significant Loan Transactions

This API covers the major loan transaction functionality  Example Requests:  loans/1/transactions?command=repayment | Make a Repayment |  loans/1/transactions?command=merchantIssuedRefund | Merchant Issued Refund |  loans/1/transactions?command=payoutRefund | Payout Refund |  loans/1/transactions?command=goodwillCredit | Goodwil Credit |  loans/1/transactions?command=chargeRefund | Charge Refund |  loans/1/transactions?command=waiveinterest | Waive Interest |  loans/1/transactions?command=writeoff | Write-off Loan |  loans/1/transactions?command=close-rescheduled | Close Rescheduled Loan |  loans/1/transactions?command=close | Close Loan |  loans/1/transactions?command=undowriteoff | Undo Loan Write-off |  loans/1/transactions?command=recoverypayment | Make Recovery Payment |  loans/1/transactions?command=refundByCash | Make a Refund of an Active Loan by Cash |  loans/1/transactions?command=foreclosure | Foreclosure of an Active Loan |  loans/1/transactions?command=creditBalanceRefund | Credit Balance Refund |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=charge-off | Charge-off Loan |   loans/1/transactions?command=downPayment | Down Payment | 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_request import PostLoansLoanIdTransactionsRequest
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    post_loans_loan_id_transactions_request = fineract_client.PostLoansLoanIdTransactionsRequest() # PostLoansLoanIdTransactionsRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Significant Loan Transactions
        api_response = api_instance.execute_loan_transaction(loan_id, post_loans_loan_id_transactions_request, command=command)
        print("The response of LoanTransactionsApi->execute_loan_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->execute_loan_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **post_loans_loan_id_transactions_request** | [**PostLoansLoanIdTransactionsRequest**](PostLoansLoanIdTransactionsRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **execute_loan_transaction1**
> PostLoansLoanIdTransactionsResponse execute_loan_transaction1(loan_external_id, post_loans_loan_id_transactions_request, command=command)

Significant Loan Transactions

This API covers the major loan transaction functionality  Example Requests:  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=repayment | Make a Repayment |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=merchantIssuedRefund | Merchant Issued Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=payoutRefund | Payout Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=goodwillCredit | Goodwil Credit |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=chargeRefund | Charge Refund |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=waiveinterest | Waive Interest |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=writeoff | Write-off Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=close-rescheduled | Close Rescheduled Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=close | Close Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=undowriteoff | Undo Loan Write-off |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=recoverypayment | Make Recovery Payment |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=refundByCash | Make a Refund of an Active Loan by Cash |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=foreclosure | Foreclosure of an Active Loan |  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=creditBalanceRefund | Credit Balance Refund |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=charge-off | Charge-off Loan |   loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions?command=downPayment | Down Payment | 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_transactions_request import PostLoansLoanIdTransactionsRequest
from fineract_client.models.post_loans_loan_id_transactions_response import PostLoansLoanIdTransactionsResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    post_loans_loan_id_transactions_request = fineract_client.PostLoansLoanIdTransactionsRequest() # PostLoansLoanIdTransactionsRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Significant Loan Transactions
        api_response = api_instance.execute_loan_transaction1(loan_external_id, post_loans_loan_id_transactions_request, command=command)
        print("The response of LoanTransactionsApi->execute_loan_transaction1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->execute_loan_transaction1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **post_loans_loan_id_transactions_request** | [**PostLoansLoanIdTransactionsRequest**](PostLoansLoanIdTransactionsRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdTransactionsResponse**](PostLoansLoanIdTransactionsResponse.md)

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

# **retrieve_transaction**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction(loan_id, transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/3

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_transaction_id_response import GetLoansLoanIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    transaction_id = 56 # int | transactionId
    fields = 'id,date,amount' # str | Optional Loan Transaction attribute list to be in the response (optional)

    try:
        # Retrieve a Transaction Details
        api_response = api_instance.retrieve_transaction(loan_id, transaction_id, fields=fields)
        print("The response of LoanTransactionsApi->retrieve_transaction:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_loan_external_id_and_transaction_external_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_loan_external_id_and_transaction_external_id(loan_external_id, external_transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/external-id/7dd80a7c-ycba-a446-t378-91eb6f53e854/transactions/external-id/5dd80a7c-ccba-4446-b378-01eb6f53e871

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_transaction_id_response import GetLoansLoanIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
    fields = 'id,date,amount' # str | Optional Loan Transaction attribute list to be in the response (optional)

    try:
        # Retrieve a Transaction Details
        api_response = api_instance.retrieve_transaction_by_loan_external_id_and_transaction_external_id(loan_external_id, external_transaction_id, fields=fields)
        print("The response of LoanTransactionsApi->retrieve_transaction_by_loan_external_id_and_transaction_external_id:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_loan_external_id_and_transaction_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_loan_external_id_and_transaction_id(loan_external_id, transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/3

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_transaction_id_response import GetLoansLoanIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    transaction_id = 56 # int | transactionId
    fields = 'id,date,amount' # str | Optional Loan Transaction attribute list to be in the response (optional)

    try:
        # Retrieve a Transaction Details
        api_response = api_instance.retrieve_transaction_by_loan_external_id_and_transaction_id(loan_external_id, transaction_id, fields=fields)
        print("The response of LoanTransactionsApi->retrieve_transaction_by_loan_external_id_and_transaction_id:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_by_transaction_external_id**
> GetLoansLoanIdTransactionsTransactionIdResponse retrieve_transaction_by_transaction_external_id(loan_id, external_transaction_id, fields=fields)

Retrieve a Transaction Details

Retrieves a Transaction Details  Example Request:  loans/5/transactions/external-id/5dd80a7c-ccba-4446-b378-01eb6f53e871

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_transaction_id_response import GetLoansLoanIdTransactionsTransactionIdResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    external_transaction_id = 'external_transaction_id_example' # str | externalTransactionId
    fields = 'id,date,amount' # str | Optional Loan Transaction attribute list to be in the response (optional)

    try:
        # Retrieve a Transaction Details
        api_response = api_instance.retrieve_transaction_by_transaction_external_id(loan_id, external_transaction_id, fields=fields)
        print("The response of LoanTransactionsApi->retrieve_transaction_by_transaction_external_id:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction_template**
> GetLoansLoanIdTransactionsTemplateResponse retrieve_transaction_template(loan_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)

Retrieve Loan Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  loans/1/transactions/template?command=repaymentloans/1/transactions/template?command=merchantIssuedRefundloans/1/transactions/template?command=payoutRefundloans/1/transactions/template?command=goodwillCredit loans/1/transactions/template?command=waiveinterest loans/1/transactions/template?command=writeoff loans/1/transactions/template?command=close-rescheduled loans/1/transactions/template?command=close loans/1/transactions/template?command=disburse loans/1/transactions/template?command=disburseToSavings loans/1/transactions/template?command=recoverypayment loans/1/transactions/template?command=prepayLoan loans/1/transactions/template?command=refundbycash loans/1/transactions/template?command=refundbytransfer loans/1/transactions/template?command=foreclosure loans/1/transactions/template?command=interestPaymentWaiver loans/1/transactions/template?command=creditBalanceRefund (returned 'amount' field will have the overpaid value) loans/1/transactions/template?command=charge-off loans/1/transactions/template?command=downPayment 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_template_response import GetLoansLoanIdTransactionsTemplateResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    command = 'command_example' # str | command (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)
    transaction_date = None # object | transactionDate (optional)
    locale = 'locale_example' # str | locale (optional)

    try:
        # Retrieve Loan Transaction Template
        api_response = api_instance.retrieve_transaction_template(loan_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)
        print("The response of LoanTransactionsApi->retrieve_transaction_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->retrieve_transaction_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **transaction_date** | [**object**](.md)| transactionDate | [optional] 
 **locale** | **str**| locale | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTemplateResponse**](GetLoansLoanIdTransactionsTemplateResponse.md)

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

# **retrieve_transaction_template1**
> GetLoansLoanIdTransactionsTemplateResponse retrieve_transaction_template1(loan_external_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)

Retrieve Loan Transaction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Requests:  loans/1/transactions/template?command=repaymentloans/1/transactions/template?command=merchantIssuedRefundloans/1/transactions/template?command=payoutRefundloans/1/transactions/template?command=goodwillCredit loans/1/transactions/template?command=waiveinterest loans/1/transactions/template?command=writeoff loans/1/transactions/template?command=close-rescheduled loans/1/transactions/template?command=close loans/1/transactions/template?command=disburse loans/1/transactions/template?command=disburseToSavings loans/1/transactions/template?command=recoverypayment loans/1/transactions/template?command=prepayLoan loans/1/transactions/template?command=refundbycash loans/1/transactions/template?command=refundbytransfer loans/1/transactions/template?command=foreclosure loans/1/transactions/template?command=interestPaymentWaiver loans/1/transactions/template?command=creditBalanceRefund (returned 'amount' field will have the overpaid value) loans/1/transactions/template?command=charge-off loans/1/transactions/template?command=downPayment 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_transactions_template_response import GetLoansLoanIdTransactionsTemplateResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    command = 'command_example' # str | command (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)
    transaction_date = None # object | transactionDate (optional)
    locale = 'locale_example' # str | locale (optional)

    try:
        # Retrieve Loan Transaction Template
        api_response = api_instance.retrieve_transaction_template1(loan_external_id, command=command, date_format=date_format, transaction_date=transaction_date, locale=locale)
        print("The response of LoanTransactionsApi->retrieve_transaction_template1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->retrieve_transaction_template1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **transaction_date** | [**object**](.md)| transactionDate | [optional] 
 **locale** | **str**| locale | [optional] 

### Return type

[**GetLoansLoanIdTransactionsTemplateResponse**](GetLoansLoanIdTransactionsTemplateResponse.md)

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

# **undo_waive_charge**
> PutChargeTransactionChangesResponse undo_waive_charge(loan_id, transaction_id, put_charge_transaction_changes_request)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_charge_transaction_changes_request import PutChargeTransactionChangesRequest
from fineract_client.models.put_charge_transaction_changes_response import PutChargeTransactionChangesResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    transaction_id = 56 # int | transactionId
    put_charge_transaction_changes_request = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 

    try:
        # Undo a Waive Charge Transaction
        api_response = api_instance.undo_waive_charge(loan_id, transaction_id, put_charge_transaction_changes_request)
        print("The response of LoanTransactionsApi->undo_waive_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->undo_waive_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **transaction_id** | **int**| transactionId | 
 **put_charge_transaction_changes_request** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

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

# **undo_waive_charge1**
> PutChargeTransactionChangesResponse undo_waive_charge1(loan_id, transaction_external_id, put_charge_transaction_changes_request)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_charge_transaction_changes_request import PutChargeTransactionChangesRequest
from fineract_client.models.put_charge_transaction_changes_response import PutChargeTransactionChangesResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_id = 56 # int | loanId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId
    put_charge_transaction_changes_request = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 

    try:
        # Undo a Waive Charge Transaction
        api_response = api_instance.undo_waive_charge1(loan_id, transaction_external_id, put_charge_transaction_changes_request)
        print("The response of LoanTransactionsApi->undo_waive_charge1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->undo_waive_charge1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **transaction_external_id** | **str**| transactionExternalId | 
 **put_charge_transaction_changes_request** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

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

# **undo_waive_charge2**
> PutChargeTransactionChangesResponse undo_waive_charge2(loan_external_id, transaction_id, put_charge_transaction_changes_request)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_charge_transaction_changes_request import PutChargeTransactionChangesRequest
from fineract_client.models.put_charge_transaction_changes_response import PutChargeTransactionChangesResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    transaction_id = 56 # int | transactionId
    put_charge_transaction_changes_request = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 

    try:
        # Undo a Waive Charge Transaction
        api_response = api_instance.undo_waive_charge2(loan_external_id, transaction_id, put_charge_transaction_changes_request)
        print("The response of LoanTransactionsApi->undo_waive_charge2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->undo_waive_charge2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_id** | **int**| transactionId | 
 **put_charge_transaction_changes_request** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

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

# **undo_waive_charge3**
> PutChargeTransactionChangesResponse undo_waive_charge3(loan_external_id, transaction_external_id, put_charge_transaction_changes_request)

Undo a Waive Charge Transaction

Undo a Waive Charge Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_charge_transaction_changes_request import PutChargeTransactionChangesRequest
from fineract_client.models.put_charge_transaction_changes_response import PutChargeTransactionChangesResponse
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
    api_instance = fineract_client.LoanTransactionsApi(api_client)
    loan_external_id = 'loan_external_id_example' # str | loanExternalId
    transaction_external_id = 'transaction_external_id_example' # str | transactionExternalId
    put_charge_transaction_changes_request = fineract_client.PutChargeTransactionChangesRequest() # PutChargeTransactionChangesRequest | 

    try:
        # Undo a Waive Charge Transaction
        api_response = api_instance.undo_waive_charge3(loan_external_id, transaction_external_id, put_charge_transaction_changes_request)
        print("The response of LoanTransactionsApi->undo_waive_charge3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanTransactionsApi->undo_waive_charge3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **transaction_external_id** | **str**| transactionExternalId | 
 **put_charge_transaction_changes_request** | [**PutChargeTransactionChangesRequest**](PutChargeTransactionChangesRequest.md)|  | 

### Return type

[**PutChargeTransactionChangesResponse**](PutChargeTransactionChangesResponse.md)

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

