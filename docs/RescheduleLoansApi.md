# fineract_client.RescheduleLoansApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_reschedule_request**](RescheduleLoansApi.md#create_loan_reschedule_request) | **POST** /v1/rescheduleloans | Create loan reschedule request
[**read_loan_reschedule_request**](RescheduleLoansApi.md#read_loan_reschedule_request) | **GET** /v1/rescheduleloans/{scheduleId} | Retrieve loan reschedule request by schedule id
[**retrieve_all_reschedule_request**](RescheduleLoansApi.md#retrieve_all_reschedule_request) | **GET** /v1/rescheduleloans | Retrieve all reschedule requests
[**retrieve_template10**](RescheduleLoansApi.md#retrieve_template10) | **GET** /v1/rescheduleloans/template | Retrieve all reschedule loan reasons
[**update_loan_reschedule_request**](RescheduleLoansApi.md#update_loan_reschedule_request) | **POST** /v1/rescheduleloans/{scheduleId} | Update loan reschedule request

# **create_loan_reschedule_request**
> PostCreateRescheduleLoansResponse create_loan_reschedule_request(body)

Create loan reschedule request

Create a loan reschedule request.

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
api_instance = fineract_client.RescheduleLoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostCreateRescheduleLoansRequest() # PostCreateRescheduleLoansRequest | 

try:
    # Create loan reschedule request
    api_response = api_instance.create_loan_reschedule_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RescheduleLoansApi->create_loan_reschedule_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCreateRescheduleLoansRequest**](PostCreateRescheduleLoansRequest.md)|  | 

### Return type

[**PostCreateRescheduleLoansResponse**](PostCreateRescheduleLoansResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_loan_reschedule_request**
> GetLoanRescheduleRequestResponse read_loan_reschedule_request(schedule_id, command=command)

Retrieve loan reschedule request by schedule id

Retrieve loan reschedule request by schedule id

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
api_instance = fineract_client.RescheduleLoansApi(fineract_client.ApiClient(configuration))
schedule_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    # Retrieve loan reschedule request by schedule id
    api_response = api_instance.read_loan_reschedule_request(schedule_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RescheduleLoansApi->read_loan_reschedule_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**GetLoanRescheduleRequestResponse**](GetLoanRescheduleRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_reschedule_request**
> list[GetLoanRescheduleRequestResponse] retrieve_all_reschedule_request(command=command, loan_id=loan_id)

Retrieve all reschedule requests

Retrieve all reschedule requests.

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
api_instance = fineract_client.RescheduleLoansApi(fineract_client.ApiClient(configuration))
command = 'command_example' # str |  (optional)
loan_id = 789 # int |  (optional)

try:
    # Retrieve all reschedule requests
    api_response = api_instance.retrieve_all_reschedule_request(command=command, loan_id=loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RescheduleLoansApi->retrieve_all_reschedule_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**|  | [optional] 
 **loan_id** | **int**|  | [optional] 

### Return type

[**list[GetLoanRescheduleRequestResponse]**](GetLoanRescheduleRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template10**
> GetRescheduleReasonsTemplateResponse retrieve_template10()

Retrieve all reschedule loan reasons

Retrieve all reschedule loan reasons as a template

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
api_instance = fineract_client.RescheduleLoansApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve all reschedule loan reasons
    api_response = api_instance.retrieve_template10()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RescheduleLoansApi->retrieve_template10: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRescheduleReasonsTemplateResponse**](GetRescheduleReasonsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_reschedule_request**
> PostUpdateRescheduleLoansResponse update_loan_reschedule_request(body, schedule_id, command=command)

Update loan reschedule request

Update a loan reschedule request by either approving/rejecting it.

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
api_instance = fineract_client.RescheduleLoansApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostUpdateRescheduleLoansRequest() # PostUpdateRescheduleLoansRequest | 
schedule_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    # Update loan reschedule request
    api_response = api_instance.update_loan_reschedule_request(body, schedule_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RescheduleLoansApi->update_loan_reschedule_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUpdateRescheduleLoansRequest**](PostUpdateRescheduleLoansRequest.md)|  | 
 **schedule_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**PostUpdateRescheduleLoansResponse**](PostUpdateRescheduleLoansResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

