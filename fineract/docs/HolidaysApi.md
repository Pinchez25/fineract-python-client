# fineract_client.HolidaysApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_holiday**](HolidaysApi.md#create_new_holiday) | **POST** /v1/holidays | Create a Holiday
[**delete7**](HolidaysApi.md#delete7) | **DELETE** /v1/holidays/{holidayId} | Delete a Holiday
[**handle_commands1**](HolidaysApi.md#handle_commands1) | **POST** /v1/holidays/{holidayId} | Activate a Holiday
[**retrieve_all_holidays**](HolidaysApi.md#retrieve_all_holidays) | **GET** /v1/holidays | List Holidays
[**retrieve_one7**](HolidaysApi.md#retrieve_one7) | **GET** /v1/holidays/{holidayId} | Retrieve a Holiday
[**retrieve_repayment_schedule_updation_tye_options**](HolidaysApi.md#retrieve_repayment_schedule_updation_tye_options) | **GET** /v1/holidays/template | 
[**update6**](HolidaysApi.md#update6) | **PUT** /v1/holidays/{holidayId} | Update a Holiday


# **create_new_holiday**
> PostHolidaysResponse create_new_holiday(post_holidays_request)

Create a Holiday

Mandatory Fields: name, description, fromDate, toDate, repaymentsRescheduledTo, offices

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_holidays_request import PostHolidaysRequest
from fineract_client.models.post_holidays_response import PostHolidaysResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    post_holidays_request = fineract_client.PostHolidaysRequest() # PostHolidaysRequest | 

    try:
        # Create a Holiday
        api_response = api_instance.create_new_holiday(post_holidays_request)
        print("The response of HolidaysApi->create_new_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->create_new_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_holidays_request** | [**PostHolidaysRequest**](PostHolidaysRequest.md)|  | 

### Return type

[**PostHolidaysResponse**](PostHolidaysResponse.md)

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

# **delete7**
> DeleteHolidaysHolidayIdResponse delete7(holiday_id)

Delete a Holiday

This API allows to delete a holiday. This is a soft delete the deleted holiday status is marked as deleted.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_holidays_holiday_id_response import DeleteHolidaysHolidayIdResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    holiday_id = 56 # int | holidayId

    try:
        # Delete a Holiday
        api_response = api_instance.delete7(holiday_id)
        print("The response of HolidaysApi->delete7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->delete7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_id** | **int**| holidayId | 

### Return type

[**DeleteHolidaysHolidayIdResponse**](DeleteHolidaysHolidayIdResponse.md)

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

# **handle_commands1**
> PostHolidaysHolidayIdResponse handle_commands1(holiday_id, body, command=command)

Activate a Holiday

Always Holidays are created in pending state. This API allows to activate a holiday.  Only the active holidays are considered for rescheduling the loan repayment.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_holidays_holiday_id_response import PostHolidaysHolidayIdResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    holiday_id = 56 # int | holidayId
    body = None # object | 
    command = 'command_example' # str | command (optional)

    try:
        # Activate a Holiday
        api_response = api_instance.handle_commands1(holiday_id, body, command=command)
        print("The response of HolidaysApi->handle_commands1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->handle_commands1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_id** | **int**| holidayId | 
 **body** | **object**|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostHolidaysHolidayIdResponse**](PostHolidaysHolidayIdResponse.md)

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

# **retrieve_all_holidays**
> List[GetHolidaysResponse] retrieve_all_holidays(office_id=office_id, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)

List Holidays

Example Requests:  holidays?officeId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_holidays_response import GetHolidaysResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    office_id = 56 # int | officeId (optional)
    from_date = None # object | fromDate (optional)
    to_date = None # object | toDate (optional)
    locale = 'locale_example' # str | locale (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)

    try:
        # List Holidays
        api_response = api_instance.retrieve_all_holidays(office_id=office_id, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)
        print("The response of HolidaysApi->retrieve_all_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->retrieve_all_holidays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **from_date** | [**object**](.md)| fromDate | [optional] 
 **to_date** | [**object**](.md)| toDate | [optional] 
 **locale** | **str**| locale | [optional] 
 **date_format** | **str**| dateFormat | [optional] 

### Return type

[**List[GetHolidaysResponse]**](GetHolidaysResponse.md)

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

# **retrieve_one7**
> GetHolidaysResponse retrieve_one7(holiday_id)

Retrieve a Holiday

Example Requests:  holidays/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_holidays_response import GetHolidaysResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    holiday_id = 56 # int | holidayId

    try:
        # Retrieve a Holiday
        api_response = api_instance.retrieve_one7(holiday_id)
        print("The response of HolidaysApi->retrieve_one7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->retrieve_one7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_id** | **int**| holidayId | 

### Return type

[**GetHolidaysResponse**](GetHolidaysResponse.md)

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

# **retrieve_repayment_schedule_updation_tye_options**
> str retrieve_repayment_schedule_updation_tye_options()



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
    api_instance = fineract_client.HolidaysApi(api_client)

    try:
        api_response = api_instance.retrieve_repayment_schedule_updation_tye_options()
        print("The response of HolidaysApi->retrieve_repayment_schedule_updation_tye_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->retrieve_repayment_schedule_updation_tye_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update6**
> PutHolidaysHolidayIdResponse update6(holiday_id, put_holidays_holiday_id_request)

Update a Holiday

If a holiday is in pending state (created and not activated) then all fields are allowed to modify. Once holidays become active only name and descriptions are allowed to modify.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_holidays_holiday_id_request import PutHolidaysHolidayIdRequest
from fineract_client.models.put_holidays_holiday_id_response import PutHolidaysHolidayIdResponse
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
    api_instance = fineract_client.HolidaysApi(api_client)
    holiday_id = 56 # int | holidayId
    put_holidays_holiday_id_request = fineract_client.PutHolidaysHolidayIdRequest() # PutHolidaysHolidayIdRequest | 

    try:
        # Update a Holiday
        api_response = api_instance.update6(holiday_id, put_holidays_holiday_id_request)
        print("The response of HolidaysApi->update6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->update6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_id** | **int**| holidayId | 
 **put_holidays_holiday_id_request** | [**PutHolidaysHolidayIdRequest**](PutHolidaysHolidayIdRequest.md)|  | 

### Return type

[**PutHolidaysHolidayIdResponse**](PutHolidaysHolidayIdResponse.md)

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

