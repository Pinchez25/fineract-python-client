# fineract_client.WorkingDaysApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all17**](WorkingDaysApi.md#retrieve_all17) | **GET** /v1/workingdays | List Working days
[**template4**](WorkingDaysApi.md#template4) | **GET** /v1/workingdays/template | Working Days Template
[**update8**](WorkingDaysApi.md#update8) | **PUT** /v1/workingdays | Update a Working Day

# **retrieve_all17**
> list[GetWorkingDaysResponse] retrieve_all17()

List Working days

Example Requests:  workingdays

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
api_instance = fineract_client.WorkingDaysApi(fineract_client.ApiClient(configuration))

try:
    # List Working days
    api_response = api_instance.retrieve_all17()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingDaysApi->retrieve_all17: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetWorkingDaysResponse]**](GetWorkingDaysResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template4**
> GetWorkingDaysTemplateResponse template4()

Working Days Template

This is a convenience resource. It can be useful when building maintenance user interface screens for working days.  Example Request:  workingdays/template

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
api_instance = fineract_client.WorkingDaysApi(fineract_client.ApiClient(configuration))

try:
    # Working Days Template
    api_response = api_instance.template4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingDaysApi->template4: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetWorkingDaysTemplateResponse**](GetWorkingDaysTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update8**
> PutWorkingDaysResponse update8(body)

Update a Working Day

Mandatory Fields recurrence,repaymentRescheduleType,extendTermForDailyRepayments,locale

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
api_instance = fineract_client.WorkingDaysApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutWorkingDaysRequest() # PutWorkingDaysRequest | 

try:
    # Update a Working Day
    api_response = api_instance.update8(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingDaysApi->update8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutWorkingDaysRequest**](PutWorkingDaysRequest.md)|  | 

### Return type

[**PutWorkingDaysResponse**](PutWorkingDaysResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

