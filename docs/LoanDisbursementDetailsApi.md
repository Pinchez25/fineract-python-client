# fineract_client.LoanDisbursementDetailsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_and_delete_disbursement_detail**](LoanDisbursementDetailsApi.md#add_and_delete_disbursement_detail) | **PUT** /v1/loans/{loanId}/disbursements/editDisbursements | 
[**retrive_detail**](LoanDisbursementDetailsApi.md#retrive_detail) | **GET** /v1/loans/{loanId}/disbursements/{disbursementId} | 
[**update_disbursement_date**](LoanDisbursementDetailsApi.md#update_disbursement_date) | **PUT** /v1/loans/{loanId}/disbursements/{disbursementId} | 

# **add_and_delete_disbursement_detail**
> str add_and_delete_disbursement_detail(loan_id, body=body)



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
api_instance = fineract_client.LoanDisbursementDetailsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.add_and_delete_disbursement_detail(loan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanDisbursementDetailsApi->add_and_delete_disbursement_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrive_detail**
> str retrive_detail(loan_id, disbursement_id)



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
api_instance = fineract_client.LoanDisbursementDetailsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
disbursement_id = 789 # int | 

try:
    api_response = api_instance.retrive_detail(loan_id, disbursement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanDisbursementDetailsApi->retrive_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **disbursement_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disbursement_date**
> str update_disbursement_date(loan_id, disbursement_id, body=body)



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
api_instance = fineract_client.LoanDisbursementDetailsApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
disbursement_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_disbursement_date(loan_id, disbursement_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanDisbursementDetailsApi->update_disbursement_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **disbursement_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

