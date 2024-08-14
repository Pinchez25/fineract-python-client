# fineract_client.NotificationApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_notifications**](NotificationApi.md#get_all_notifications) | **GET** /v1/notifications | 
[**update5**](NotificationApi.md#update5) | **PUT** /v1/notifications | 

# **get_all_notifications**
> GetNotificationsResponse get_all_notifications(order_by=order_by, limit=limit, offset=offset, sort_order=sort_order, is_read=is_read)



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
api_instance = fineract_client.NotificationApi(fineract_client.ApiClient(configuration))
order_by = 'order_by_example' # str | orderBy (optional)
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
is_read = true # bool | isRead (optional)

try:
    api_response = api_instance.get_all_notifications(order_by=order_by, limit=limit, offset=offset, sort_order=sort_order, is_read=is_read)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_all_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| orderBy | [optional] 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **is_read** | **bool**| isRead | [optional] 

### Return type

[**GetNotificationsResponse**](GetNotificationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update5**
> update5()



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
api_instance = fineract_client.NotificationApi(fineract_client.ApiClient(configuration))

try:
    api_instance.update5()
except ApiException as e:
    print("Exception when calling NotificationApi->update5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

