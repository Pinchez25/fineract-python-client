# fineract_client.LoanReschedulingApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_loan_schedule_or_submit_variable_schedule**](LoanReschedulingApi.md#calculate_loan_schedule_or_submit_variable_schedule) | **POST** /v1/loans/{loanId}/schedule | Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations


# **calculate_loan_schedule_or_submit_variable_schedule**
> PostLoansLoanIdScheduleResponse calculate_loan_schedule_or_submit_variable_schedule(loan_id, body, command=command)

Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations

Calculate loan repayment schedule based on Loan term variations:  Mandatory Fields: exceptions,locale,dateFormat  Updates loan repayment schedule based on Loan term variations:  Mandatory Fields: exceptions,locale,dateFormat  Updates loan repayment schedule by removing Loan term variations:  It updates the loan repayment schedule by removing Loan term variations  Showing request/response for 'Updates loan repayment schedule by removing Loan term variations'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_schedule_response import PostLoansLoanIdScheduleResponse
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
    api_instance = fineract_client.LoanReschedulingApi(api_client)
    loan_id = 56 # int | loanId
    body = None # object | 
    command = 'command_example' # str | command (optional)

    try:
        # Calculate loan repayment schedule based on Loan term variations | Updates loan repayment schedule based on Loan term variations | Updates loan repayment schedule by removing Loan term variations
        api_response = api_instance.calculate_loan_schedule_or_submit_variable_schedule(loan_id, body, command=command)
        print("The response of LoanReschedulingApi->calculate_loan_schedule_or_submit_variable_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanReschedulingApi->calculate_loan_schedule_or_submit_variable_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **body** | **object**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdScheduleResponse**](PostLoansLoanIdScheduleResponse.md)

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

