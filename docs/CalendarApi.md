# fineract_client.CalendarApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_calendar**](CalendarApi.md#create_calendar) | **POST** /v1/{entityType}/{entityId}/calendars | 
[**delete_calendar**](CalendarApi.md#delete_calendar) | **DELETE** /v1/{entityType}/{entityId}/calendars/{calendarId} | 
[**retrieve_calendar**](CalendarApi.md#retrieve_calendar) | **GET** /v1/{entityType}/{entityId}/calendars/{calendarId} | 
[**retrieve_calendars_by_entity**](CalendarApi.md#retrieve_calendars_by_entity) | **GET** /v1/{entityType}/{entityId}/calendars | 
[**retrieve_new_calendar_details**](CalendarApi.md#retrieve_new_calendar_details) | **GET** /v1/{entityType}/{entityId}/calendars/template | 
[**update_calendar**](CalendarApi.md#update_calendar) | **PUT** /v1/{entityType}/{entityId}/calendars/{calendarId} | 

# **create_calendar**
> str create_calendar(entity_type, entity_id, body=body)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_calendar(entity_type, entity_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->create_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calendar**
> str delete_calendar(entity_type, entity_id, calendar_id)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
calendar_id = 789 # int | 

try:
    api_response = api_instance.delete_calendar(entity_type, entity_id, calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->delete_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **calendar_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_calendar**
> str retrieve_calendar(calendar_id, entity_type, entity_id)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
calendar_id = 789 # int | 
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 

try:
    api_response = api_instance.retrieve_calendar(calendar_id, entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->retrieve_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_id** | **int**|  | 
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_calendars_by_entity**
> str retrieve_calendars_by_entity(entity_type, entity_id, calendar_type=calendar_type)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
calendar_type = 'all' # str |  (optional) (default to all)

try:
    api_response = api_instance.retrieve_calendars_by_entity(entity_type, entity_id, calendar_type=calendar_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->retrieve_calendars_by_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **calendar_type** | **str**|  | [optional] [default to all]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_new_calendar_details**
> str retrieve_new_calendar_details(entity_type, entity_id)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 

try:
    api_response = api_instance.retrieve_new_calendar_details(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->retrieve_new_calendar_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_calendar**
> str update_calendar(entity_type, entity_id, calendar_id, body=body)



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
api_instance = fineract_client.CalendarApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
calendar_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_calendar(entity_type, entity_id, calendar_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarApi->update_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **calendar_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

