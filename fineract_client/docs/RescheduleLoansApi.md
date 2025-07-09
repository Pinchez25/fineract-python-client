# fineract_client.RescheduleLoansApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_reschedule_request**](RescheduleLoansApi.md#create_loan_reschedule_request) | **POST** /v1/rescheduleloans | Create loan reschedule request
[**read_loan_reschedule_request**](RescheduleLoansApi.md#read_loan_reschedule_request) | **GET** /v1/rescheduleloans/{scheduleId} | Retrieve loan reschedule request by schedule id
[**retrieve_all_reschedule_request**](RescheduleLoansApi.md#retrieve_all_reschedule_request) | **GET** /v1/rescheduleloans | Retrieve all reschedule requests
[**retrieve_template10**](RescheduleLoansApi.md#retrieve_template10) | **GET** /v1/rescheduleloans/template | Retrieve all reschedule loan reasons
[**update_loan_reschedule_request**](RescheduleLoansApi.md#update_loan_reschedule_request) | **POST** /v1/rescheduleloans/{scheduleId} | Update loan reschedule request


# **create_loan_reschedule_request**
> PostCreateRescheduleLoansResponse create_loan_reschedule_request(post_create_reschedule_loans_request)

Create loan reschedule request

Create a loan reschedule request.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_create_reschedule_loans_request import PostCreateRescheduleLoansRequest
from fineract_client.models.post_create_reschedule_loans_response import PostCreateRescheduleLoansResponse
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
    api_instance = fineract_client.RescheduleLoansApi(api_client)
    post_create_reschedule_loans_request = fineract_client.PostCreateRescheduleLoansRequest() # PostCreateRescheduleLoansRequest | 

    try:
        # Create loan reschedule request
        api_response = api_instance.create_loan_reschedule_request(post_create_reschedule_loans_request)
        print("The response of RescheduleLoansApi->create_loan_reschedule_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RescheduleLoansApi->create_loan_reschedule_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_create_reschedule_loans_request** | [**PostCreateRescheduleLoansRequest**](PostCreateRescheduleLoansRequest.md)|  | 

### Return type

[**PostCreateRescheduleLoansResponse**](PostCreateRescheduleLoansResponse.md)

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

# **read_loan_reschedule_request**
> GetLoanRescheduleRequestResponse read_loan_reschedule_request(schedule_id, command=command)

Retrieve loan reschedule request by schedule id

Retrieve loan reschedule request by schedule id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_reschedule_request_response import GetLoanRescheduleRequestResponse
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
    api_instance = fineract_client.RescheduleLoansApi(api_client)
    schedule_id = 56 # int | 
    command = 'command_example' # str |  (optional)

    try:
        # Retrieve loan reschedule request by schedule id
        api_response = api_instance.read_loan_reschedule_request(schedule_id, command=command)
        print("The response of RescheduleLoansApi->read_loan_reschedule_request:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_reschedule_request**
> List[GetLoanRescheduleRequestResponse] retrieve_all_reschedule_request(command=command, loan_id=loan_id)

Retrieve all reschedule requests

Retrieve all reschedule requests.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_reschedule_request_response import GetLoanRescheduleRequestResponse
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
    api_instance = fineract_client.RescheduleLoansApi(api_client)
    command = 'command_example' # str |  (optional)
    loan_id = 56 # int |  (optional)

    try:
        # Retrieve all reschedule requests
        api_response = api_instance.retrieve_all_reschedule_request(command=command, loan_id=loan_id)
        print("The response of RescheduleLoansApi->retrieve_all_reschedule_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RescheduleLoansApi->retrieve_all_reschedule_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**|  | [optional] 
 **loan_id** | **int**|  | [optional] 

### Return type

[**List[GetLoanRescheduleRequestResponse]**](GetLoanRescheduleRequestResponse.md)

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

# **retrieve_template10**
> GetRescheduleReasonsTemplateResponse retrieve_template10()

Retrieve all reschedule loan reasons

Retrieve all reschedule loan reasons as a template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_reschedule_reasons_template_response import GetRescheduleReasonsTemplateResponse
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
    api_instance = fineract_client.RescheduleLoansApi(api_client)

    try:
        # Retrieve all reschedule loan reasons
        api_response = api_instance.retrieve_template10()
        print("The response of RescheduleLoansApi->retrieve_template10:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_reschedule_request**
> PostUpdateRescheduleLoansResponse update_loan_reschedule_request(schedule_id, post_update_reschedule_loans_request, command=command)

Update loan reschedule request

Update a loan reschedule request by either approving/rejecting it.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_update_reschedule_loans_request import PostUpdateRescheduleLoansRequest
from fineract_client.models.post_update_reschedule_loans_response import PostUpdateRescheduleLoansResponse
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
    api_instance = fineract_client.RescheduleLoansApi(api_client)
    schedule_id = 56 # int | 
    post_update_reschedule_loans_request = fineract_client.PostUpdateRescheduleLoansRequest() # PostUpdateRescheduleLoansRequest | 
    command = 'command_example' # str |  (optional)

    try:
        # Update loan reschedule request
        api_response = api_instance.update_loan_reschedule_request(schedule_id, post_update_reschedule_loans_request, command=command)
        print("The response of RescheduleLoansApi->update_loan_reschedule_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RescheduleLoansApi->update_loan_reschedule_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **int**|  | 
 **post_update_reschedule_loans_request** | [**PostUpdateRescheduleLoansRequest**](PostUpdateRescheduleLoansRequest.md)|  | 
 **command** | **str**|  | [optional] 

### Return type

[**PostUpdateRescheduleLoansResponse**](PostUpdateRescheduleLoansResponse.md)

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

