# fineract_client.HolidaysApi

All URIs are relative to */fineract-provider/api/v1*

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
> PostHolidaysResponse create_new_holiday(body)

Create a Holiday

Mandatory Fields: name, description, fromDate, toDate, repaymentsRescheduledTo, offices

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostHolidaysRequest() # PostHolidaysRequest | 

try:
    # Create a Holiday
    api_response = api_instance.create_new_holiday(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidaysApi->create_new_holiday: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostHolidaysRequest**](PostHolidaysRequest.md)|  | 

### Return type

[**PostHolidaysResponse**](PostHolidaysResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete7**
> DeleteHolidaysHolidayIdResponse delete7(holiday_id)

Delete a Holiday

This API allows to delete a holiday. This is a soft delete the deleted holiday status is marked as deleted.

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
holiday_id = 789 # int | holidayId

try:
    # Delete a Holiday
    api_response = api_instance.delete7(holiday_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands1**
> PostHolidaysHolidayIdResponse handle_commands1(body, holiday_id, command=command)

Activate a Holiday

Always Holidays are created in pending state. This API allows to activate a holiday.  Only the active holidays are considered for rescheduling the loan repayment.

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostHolidaysHolidayIdRequest() # PostHolidaysHolidayIdRequest | 
holiday_id = 789 # int | holidayId
command = 'command_example' # str | command (optional)

try:
    # Activate a Holiday
    api_response = api_instance.handle_commands1(body, holiday_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidaysApi->handle_commands1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostHolidaysHolidayIdRequest**](PostHolidaysHolidayIdRequest.md)|  | 
 **holiday_id** | **int**| holidayId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostHolidaysHolidayIdResponse**](PostHolidaysHolidayIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_holidays**
> list[GetHolidaysResponse] retrieve_all_holidays(office_id=office_id, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)

List Holidays

Example Requests:  holidays?officeId=1

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)
from_date = fineract_client.DateParam() # DateParam | fromDate (optional)
to_date = fineract_client.DateParam() # DateParam | toDate (optional)
locale = 'locale_example' # str | locale (optional)
date_format = 'date_format_example' # str | dateFormat (optional)

try:
    # List Holidays
    api_response = api_instance.retrieve_all_holidays(office_id=office_id, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidaysApi->retrieve_all_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **from_date** | [**DateParam**](.md)| fromDate | [optional] 
 **to_date** | [**DateParam**](.md)| toDate | [optional] 
 **locale** | **str**| locale | [optional] 
 **date_format** | **str**| dateFormat | [optional] 

### Return type

[**list[GetHolidaysResponse]**](GetHolidaysResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one7**
> GetHolidaysResponse retrieve_one7(holiday_id)

Retrieve a Holiday

Example Requests:  holidays/1

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
holiday_id = 789 # int | holidayId

try:
    # Retrieve a Holiday
    api_response = api_instance.retrieve_one7(holiday_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_repayment_schedule_updation_tye_options**
> str retrieve_repayment_schedule_updation_tye_options()



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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_repayment_schedule_updation_tye_options()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update6**
> PutHolidaysHolidayIdResponse update6(body, holiday_id)

Update a Holiday

If a holiday is in pending state (created and not activated) then all fields are allowed to modify. Once holidays become active only name and descriptions are allowed to modify.

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
api_instance = fineract_client.HolidaysApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutHolidaysHolidayIdRequest() # PutHolidaysHolidayIdRequest | 
holiday_id = 789 # int | holidayId

try:
    # Update a Holiday
    api_response = api_instance.update6(body, holiday_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidaysApi->update6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutHolidaysHolidayIdRequest**](PutHolidaysHolidayIdRequest.md)|  | 
 **holiday_id** | **int**| holidayId | 

### Return type

[**PutHolidaysHolidayIdResponse**](PutHolidaysHolidayIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

