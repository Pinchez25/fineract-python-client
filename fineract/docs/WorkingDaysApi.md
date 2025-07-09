# fineract_client.WorkingDaysApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all17**](WorkingDaysApi.md#retrieve_all17) | **GET** /v1/workingdays | List Working days
[**template4**](WorkingDaysApi.md#template4) | **GET** /v1/workingdays/template | Working Days Template
[**update8**](WorkingDaysApi.md#update8) | **PUT** /v1/workingdays | Update a Working Day


# **retrieve_all17**
> List[GetWorkingDaysResponse] retrieve_all17()

List Working days

Example Requests:  workingdays

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_working_days_response import GetWorkingDaysResponse
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
    api_instance = fineract_client.WorkingDaysApi(api_client)

    try:
        # List Working days
        api_response = api_instance.retrieve_all17()
        print("The response of WorkingDaysApi->retrieve_all17:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingDaysApi->retrieve_all17: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetWorkingDaysResponse]**](GetWorkingDaysResponse.md)

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

# **template4**
> GetWorkingDaysTemplateResponse template4()

Working Days Template

This is a convenience resource. It can be useful when building maintenance user interface screens for working days.  Example Request:  workingdays/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_working_days_template_response import GetWorkingDaysTemplateResponse
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
    api_instance = fineract_client.WorkingDaysApi(api_client)

    try:
        # Working Days Template
        api_response = api_instance.template4()
        print("The response of WorkingDaysApi->template4:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update8**
> PutWorkingDaysResponse update8(put_working_days_request)

Update a Working Day

Mandatory Fields recurrence,repaymentRescheduleType,extendTermForDailyRepayments,locale

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_working_days_request import PutWorkingDaysRequest
from fineract_client.models.put_working_days_response import PutWorkingDaysResponse
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
    api_instance = fineract_client.WorkingDaysApi(api_client)
    put_working_days_request = fineract_client.PutWorkingDaysRequest() # PutWorkingDaysRequest | 

    try:
        # Update a Working Day
        api_response = api_instance.update8(put_working_days_request)
        print("The response of WorkingDaysApi->update8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingDaysApi->update8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_working_days_request** | [**PutWorkingDaysRequest**](PutWorkingDaysRequest.md)|  | 

### Return type

[**PutWorkingDaysResponse**](PutWorkingDaysResponse.md)

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

