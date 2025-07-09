# fineract_client.RepaymentWithPostDatedChecksApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_post_dated_check**](RepaymentWithPostDatedChecksApi.md#delete_post_dated_check) | **DELETE** /v1/loans/{loanId}/postdatedchecks/{postDatedCheckId} | Delete Post Dated Check
[**get_post_dated_check**](RepaymentWithPostDatedChecksApi.md#get_post_dated_check) | **GET** /v1/loans/{loanId}/postdatedchecks/{installmentId} | Get Post Dated Check
[**get_post_dated_checks**](RepaymentWithPostDatedChecksApi.md#get_post_dated_checks) | **GET** /v1/loans/{loanId}/postdatedchecks | Get All Post Dated Checks
[**update_post_dated_checks**](RepaymentWithPostDatedChecksApi.md#update_post_dated_checks) | **PUT** /v1/loans/{loanId}/postdatedchecks/{postDatedCheckId} | Update Post Dated Check, Bounced Check


# **delete_post_dated_check**
> List[DeletePostDatedCheck] delete_post_dated_check(post_dated_check_id, loan_id)

Delete Post Dated Check

Delete Post Dated Check

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_post_dated_check import DeletePostDatedCheck
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
    api_instance = fineract_client.RepaymentWithPostDatedChecksApi(api_client)
    post_dated_check_id = 56 # int | postDatedCheckId
    loan_id = 56 # int | loanId

    try:
        # Delete Post Dated Check
        api_response = api_instance.delete_post_dated_check(post_dated_check_id, loan_id)
        print("The response of RepaymentWithPostDatedChecksApi->delete_post_dated_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepaymentWithPostDatedChecksApi->delete_post_dated_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_dated_check_id** | **int**| postDatedCheckId | 
 **loan_id** | **int**| loanId | 

### Return type

[**List[DeletePostDatedCheck]**](DeletePostDatedCheck.md)

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

# **get_post_dated_check**
> List[GetPostDatedChecks] get_post_dated_check(installment_id, loan_id)

Get Post Dated Check

Get Post Dated Check

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_post_dated_checks import GetPostDatedChecks
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
    api_instance = fineract_client.RepaymentWithPostDatedChecksApi(api_client)
    installment_id = 56 # int | installmentId
    loan_id = 56 # int | loanId

    try:
        # Get Post Dated Check
        api_response = api_instance.get_post_dated_check(installment_id, loan_id)
        print("The response of RepaymentWithPostDatedChecksApi->get_post_dated_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepaymentWithPostDatedChecksApi->get_post_dated_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installment_id** | **int**| installmentId | 
 **loan_id** | **int**| loanId | 

### Return type

[**List[GetPostDatedChecks]**](GetPostDatedChecks.md)

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

# **get_post_dated_checks**
> List[GetPostDatedChecks] get_post_dated_checks(loan_id)

Get All Post Dated Checks

Get All Post dated Checks

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_post_dated_checks import GetPostDatedChecks
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
    api_instance = fineract_client.RepaymentWithPostDatedChecksApi(api_client)
    loan_id = 56 # int | loanId

    try:
        # Get All Post Dated Checks
        api_response = api_instance.get_post_dated_checks(loan_id)
        print("The response of RepaymentWithPostDatedChecksApi->get_post_dated_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepaymentWithPostDatedChecksApi->get_post_dated_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**List[GetPostDatedChecks]**](GetPostDatedChecks.md)

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

# **update_post_dated_checks**
> List[UpdatePostDatedCheckResponse] update_post_dated_checks(post_dated_check_id, loan_id, update_post_dated_check_request, edit_type=edit_type)

Update Post Dated Check, Bounced Check

Update Post Dated Check, Bounced Check

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.update_post_dated_check_request import UpdatePostDatedCheckRequest
from fineract_client.models.update_post_dated_check_response import UpdatePostDatedCheckResponse
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
    api_instance = fineract_client.RepaymentWithPostDatedChecksApi(api_client)
    post_dated_check_id = 56 # int | postDatedCheckId
    loan_id = 56 # int | loanId
    update_post_dated_check_request = fineract_client.UpdatePostDatedCheckRequest() # UpdatePostDatedCheckRequest | 
    edit_type = 'edit_type_example' # str | editType (optional)

    try:
        # Update Post Dated Check, Bounced Check
        api_response = api_instance.update_post_dated_checks(post_dated_check_id, loan_id, update_post_dated_check_request, edit_type=edit_type)
        print("The response of RepaymentWithPostDatedChecksApi->update_post_dated_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepaymentWithPostDatedChecksApi->update_post_dated_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_dated_check_id** | **int**| postDatedCheckId | 
 **loan_id** | **int**| loanId | 
 **update_post_dated_check_request** | [**UpdatePostDatedCheckRequest**](UpdatePostDatedCheckRequest.md)|  | 
 **edit_type** | **str**| editType | [optional] 

### Return type

[**List[UpdatePostDatedCheckResponse]**](UpdatePostDatedCheckResponse.md)

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

