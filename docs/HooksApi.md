# fineract_client.HooksApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hook**](HooksApi.md#create_hook) | **POST** /v1/hooks | Create a Hook
[**delete_hook**](HooksApi.md#delete_hook) | **DELETE** /v1/hooks/{hookId} | Delete a Hook
[**retrieve_hook**](HooksApi.md#retrieve_hook) | **GET** /v1/hooks/{hookId} | Retrieve a Hook
[**retrieve_hooks**](HooksApi.md#retrieve_hooks) | **GET** /v1/hooks | Retrieve Hooks
[**template3**](HooksApi.md#template3) | **GET** /v1/hooks/template | Retrieve Hooks Template
[**update_hook**](HooksApi.md#update_hook) | **PUT** /v1/hooks/{hookId} | Update a Hook

# **create_hook**
> PostHookResponse create_hook(body)

Create a Hook

The following parameters can be passed for the creation of a hook :-  name - string - Required. The name of the template that is being called. (See /hooks/template for the list of valid hook names.)  isActive - boolean - Determines whether the hook is actually triggered.  events - array - Determines what events the hook is triggered for.  config - hash - Required. Key/value pairs to provide settings for this hook. These settings vary between the templates.  templateId - Optional. The UGD template ID associated with the same entity (client or loan).

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostHookRequest() # PostHookRequest | 

try:
    # Create a Hook
    api_response = api_instance.create_hook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->create_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostHookRequest**](PostHookRequest.md)|  | 

### Return type

[**PostHookResponse**](PostHookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hook**
> DeleteHookResponse delete_hook(hook_id)

Delete a Hook

Deletes a hook.

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))
hook_id = 789 # int | hookId

try:
    # Delete a Hook
    api_response = api_instance.delete_hook(hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->delete_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **int**| hookId | 

### Return type

[**DeleteHookResponse**](DeleteHookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_hook**
> GetHookResponse retrieve_hook(hook_id)

Retrieve a Hook

Returns the details of a Hook.  Example Requests:  hooks/1

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))
hook_id = 789 # int | hookId

try:
    # Retrieve a Hook
    api_response = api_instance.retrieve_hook(hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->retrieve_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **int**| hookId | 

### Return type

[**GetHookResponse**](GetHookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_hooks**
> list[GetHookResponse] retrieve_hooks()

Retrieve Hooks

Returns the list of hooks.  Example Requests:  hooks

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Hooks
    api_response = api_instance.retrieve_hooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->retrieve_hooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetHookResponse]**](GetHookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template3**
> GetHookTemplateResponse template3()

Retrieve Hooks Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  hooks/template

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Hooks Template
    api_response = api_instance.template3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->template3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetHookTemplateResponse**](GetHookTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hook**
> PutHookResponse update_hook(body, hook_id)

Update a Hook

Updates the details of a hook.

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
api_instance = fineract_client.HooksApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutHookRequest() # PutHookRequest | 
hook_id = 789 # int | hookId

try:
    # Update a Hook
    api_response = api_instance.update_hook(body, hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HooksApi->update_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutHookRequest**](PutHookRequest.md)|  | 
 **hook_id** | **int**| hookId | 

### Return type

[**PutHookResponse**](PutHookResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

