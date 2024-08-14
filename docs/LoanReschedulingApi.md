# fineract_client.LoanReschedulingApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_loan_schedule_or_submit_variable_schedule**](LoanReschedulingApi.md#calculate_loan_schedule_or_submit_variable_schedule) | **POST** /v1/loans/{loanId}/schedule | Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations

# **calculate_loan_schedule_or_submit_variable_schedule**
> PostLoansLoanIdScheduleResponse calculate_loan_schedule_or_submit_variable_schedule(body, loan_id, command=command)

Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations

Calculate loan repayment schedule based on Loan term variations:  Mandatory Fields: exceptions,locale,dateFormat  Updates loan repayment schedule based on Loan term variations:  Mandatory Fields: exceptions,locale,dateFormat  Updates loan repayment schedule by removing Loan term variations:  It updates the loan repayment schedule by removing Loan term variations  Showing request/response for 'Updates loan repayment schedule by removing Loan term variations'

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
api_instance = fineract_client.LoanReschedulingApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdScheduleRequest() # PostLoansLoanIdScheduleRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations
    api_response = api_instance.calculate_loan_schedule_or_submit_variable_schedule(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanReschedulingApi->calculate_loan_schedule_or_submit_variable_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdScheduleRequest**](PostLoansLoanIdScheduleRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdScheduleResponse**](PostLoansLoanIdScheduleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

