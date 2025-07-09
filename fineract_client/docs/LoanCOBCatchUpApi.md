# fineract_client.LoanCOBCatchUpApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_loan_cob_catch_up**](LoanCOBCatchUpApi.md#execute_loan_cob_catch_up) | **POST** /v1/loans/catch-up | Executes Loan COB Catch Up
[**get_oldest_cob_processed_loan**](LoanCOBCatchUpApi.md#get_oldest_cob_processed_loan) | **GET** /v1/loans/oldest-cob-closed | Retrieves the oldest COB processed loan
[**is_catch_up_running**](LoanCOBCatchUpApi.md#is_catch_up_running) | **GET** /v1/loans/is-catch-up-running | Retrieves whether Loan COB catch up is running


# **execute_loan_cob_catch_up**
> execute_loan_cob_catch_up()

Executes Loan COB Catch Up

Executes the Loan COB job on every day from the oldest Loan to the current COB business date

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
    api_instance = fineract_client.LoanCOBCatchUpApi(api_client)

    try:
        # Executes Loan COB Catch Up
        api_instance.execute_loan_cob_catch_up()
    except Exception as e:
        print("Exception when calling LoanCOBCatchUpApi->execute_loan_cob_catch_up: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All loans are up to date |  -  |
**202** | Catch Up has been started |  -  |
**400** | Catch Up is already running |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oldest_cob_processed_loan**
> GetOldestCOBProcessedLoanResponse get_oldest_cob_processed_loan()

Retrieves the oldest COB processed loan

Retrieves the COB business date and the oldest COB processed loan

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_oldest_cob_processed_loan_response import GetOldestCOBProcessedLoanResponse
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
    api_instance = fineract_client.LoanCOBCatchUpApi(api_client)

    try:
        # Retrieves the oldest COB processed loan
        api_response = api_instance.get_oldest_cob_processed_loan()
        print("The response of LoanCOBCatchUpApi->get_oldest_cob_processed_loan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCOBCatchUpApi->get_oldest_cob_processed_loan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOldestCOBProcessedLoanResponse**](GetOldestCOBProcessedLoanResponse.md)

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

# **is_catch_up_running**
> IsCatchUpRunningResponse is_catch_up_running()

Retrieves whether Loan COB catch up is running

Retrieves whether Loan COB catch up is running, and the current execution date if it is running.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.is_catch_up_running_response import IsCatchUpRunningResponse
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
    api_instance = fineract_client.LoanCOBCatchUpApi(api_client)

    try:
        # Retrieves whether Loan COB catch up is running
        api_response = api_instance.is_catch_up_running()
        print("The response of LoanCOBCatchUpApi->is_catch_up_running:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCOBCatchUpApi->is_catch_up_running: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IsCatchUpRunningResponse**](IsCatchUpRunningResponse.md)

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

