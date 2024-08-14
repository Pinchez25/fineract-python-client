# fineract_client.LoanCOBCatchUpApi

All URIs are relative to */fineract-provider/api/v1*

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
api_instance = fineract_client.LoanCOBCatchUpApi(fineract_client.ApiClient(configuration))

try:
    # Executes Loan COB Catch Up
    api_instance.execute_loan_cob_catch_up()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oldest_cob_processed_loan**
> GetOldestCOBProcessedLoanResponse get_oldest_cob_processed_loan()

Retrieves the oldest COB processed loan

Retrieves the COB business date and the oldest COB processed loan

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
api_instance = fineract_client.LoanCOBCatchUpApi(fineract_client.ApiClient(configuration))

try:
    # Retrieves the oldest COB processed loan
    api_response = api_instance.get_oldest_cob_processed_loan()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_catch_up_running**
> IsCatchUpRunningResponse is_catch_up_running()

Retrieves whether Loan COB catch up is running

Retrieves whether Loan COB catch up is running, and the current execution date if it is running.

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
api_instance = fineract_client.LoanCOBCatchUpApi(fineract_client.ApiClient(configuration))

try:
    # Retrieves whether Loan COB catch up is running
    api_response = api_instance.is_catch_up_running()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

