# fineract_client.RepaymentWithPostDatedChecksApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_post_dated_check**](RepaymentWithPostDatedChecksApi.md#delete_post_dated_check) | **DELETE** /v1/loans/{loanId}/postdatedchecks/{postDatedCheckId} | Delete Post Dated Check
[**get_post_dated_check**](RepaymentWithPostDatedChecksApi.md#get_post_dated_check) | **GET** /v1/loans/{loanId}/postdatedchecks/{installmentId} | Get Post Dated Check
[**get_post_dated_checks**](RepaymentWithPostDatedChecksApi.md#get_post_dated_checks) | **GET** /v1/loans/{loanId}/postdatedchecks | Get All Post Dated Checks
[**update_post_dated_checks**](RepaymentWithPostDatedChecksApi.md#update_post_dated_checks) | **PUT** /v1/loans/{loanId}/postdatedchecks/{postDatedCheckId} | Update Post Dated Check, Bounced Check

# **delete_post_dated_check**
> list[DeletePostDatedCheck] delete_post_dated_check(post_dated_check_id, loan_id)

Delete Post Dated Check

Delete Post Dated Check

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
api_instance = fineract_client.RepaymentWithPostDatedChecksApi(fineract_client.ApiClient(configuration))
post_dated_check_id = 789 # int | postDatedCheckId
loan_id = 789 # int | loanId

try:
    # Delete Post Dated Check
    api_response = api_instance.delete_post_dated_check(post_dated_check_id, loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepaymentWithPostDatedChecksApi->delete_post_dated_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_dated_check_id** | **int**| postDatedCheckId | 
 **loan_id** | **int**| loanId | 

### Return type

[**list[DeletePostDatedCheck]**](DeletePostDatedCheck.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_dated_check**
> list[GetPostDatedChecks] get_post_dated_check(installment_id, loan_id)

Get Post Dated Check

Get Post Dated Check

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
api_instance = fineract_client.RepaymentWithPostDatedChecksApi(fineract_client.ApiClient(configuration))
installment_id = 56 # int | installmentId
loan_id = 789 # int | loanId

try:
    # Get Post Dated Check
    api_response = api_instance.get_post_dated_check(installment_id, loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepaymentWithPostDatedChecksApi->get_post_dated_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installment_id** | **int**| installmentId | 
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetPostDatedChecks]**](GetPostDatedChecks.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_dated_checks**
> list[GetPostDatedChecks] get_post_dated_checks(loan_id)

Get All Post Dated Checks

Get All Post dated Checks

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
api_instance = fineract_client.RepaymentWithPostDatedChecksApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Get All Post Dated Checks
    api_response = api_instance.get_post_dated_checks(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepaymentWithPostDatedChecksApi->get_post_dated_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetPostDatedChecks]**](GetPostDatedChecks.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post_dated_checks**
> list[UpdatePostDatedCheckResponse] update_post_dated_checks(body, post_dated_check_id, loan_id, edit_type=edit_type)

Update Post Dated Check, Bounced Check

Update Post Dated Check, Bounced Check

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
api_instance = fineract_client.RepaymentWithPostDatedChecksApi(fineract_client.ApiClient(configuration))
body = fineract_client.UpdatePostDatedCheckRequest() # UpdatePostDatedCheckRequest | 
post_dated_check_id = 789 # int | postDatedCheckId
loan_id = 789 # int | loanId
edit_type = 'edit_type_example' # str | editType (optional)

try:
    # Update Post Dated Check, Bounced Check
    api_response = api_instance.update_post_dated_checks(body, post_dated_check_id, loan_id, edit_type=edit_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepaymentWithPostDatedChecksApi->update_post_dated_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePostDatedCheckRequest**](UpdatePostDatedCheckRequest.md)|  | 
 **post_dated_check_id** | **int**| postDatedCheckId | 
 **loan_id** | **int**| loanId | 
 **edit_type** | **str**| editType | [optional] 

### Return type

[**list[UpdatePostDatedCheckResponse]**](UpdatePostDatedCheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

