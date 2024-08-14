# fineract_client.MeetingsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meeting**](MeetingsApi.md#create_meeting) | **POST** /v1/{entityType}/{entityId}/meetings | 
[**delete_meeting**](MeetingsApi.md#delete_meeting) | **DELETE** /v1/{entityType}/{entityId}/meetings/{meetingId} | 
[**perform_meeting_commands**](MeetingsApi.md#perform_meeting_commands) | **POST** /v1/{entityType}/{entityId}/meetings/{meetingId} | 
[**retrieve_meeting**](MeetingsApi.md#retrieve_meeting) | **GET** /v1/{entityType}/{entityId}/meetings/{meetingId} | 
[**retrieve_meetings**](MeetingsApi.md#retrieve_meetings) | **GET** /v1/{entityType}/{entityId}/meetings | 
[**template11**](MeetingsApi.md#template11) | **GET** /v1/{entityType}/{entityId}/meetings/template | 
[**update_meeting**](MeetingsApi.md#update_meeting) | **PUT** /v1/{entityType}/{entityId}/meetings/{meetingId} | 

# **create_meeting**
> str create_meeting(entity_type, entity_id, body=body)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_meeting(entity_type, entity_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->create_meeting: %s\n" % e)
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

# **delete_meeting**
> str delete_meeting(entity_type, entity_id, meeting_id)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
meeting_id = 789 # int | 

try:
    api_response = api_instance.delete_meeting(entity_type, entity_id, meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->delete_meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **meeting_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_meeting_commands**
> str perform_meeting_commands(entity_type, entity_id, meeting_id, body=body, command=command)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
meeting_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.perform_meeting_commands(entity_type, entity_id, meeting_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->perform_meeting_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **meeting_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_meeting**
> str retrieve_meeting(meeting_id, entity_type, entity_id)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
meeting_id = 789 # int | 
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 

try:
    api_response = api_instance.retrieve_meeting(meeting_id, entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->retrieve_meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **int**|  | 
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

# **retrieve_meetings**
> str retrieve_meetings(entity_type, entity_id, limit=limit)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
limit = 56 # int |  (optional)

try:
    api_response = api_instance.retrieve_meetings(entity_type, entity_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->retrieve_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **limit** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template11**
> str template11(entity_type, entity_id, calendar_id=calendar_id)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
calendar_id = 789 # int |  (optional)

try:
    api_response = api_instance.template11(entity_type, entity_id, calendar_id=calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->template11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **calendar_id** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meeting**
> str update_meeting(entity_type, entity_id, meeting_id, body=body)



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
api_instance = fineract_client.MeetingsApi(fineract_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 789 # int | 
meeting_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_meeting(entity_type, entity_id, meeting_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeetingsApi->update_meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **int**|  | 
 **meeting_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

