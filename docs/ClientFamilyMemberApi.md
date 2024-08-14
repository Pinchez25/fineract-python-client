# fineract_client.ClientFamilyMemberApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_family_members**](ClientFamilyMemberApi.md#add_client_family_members) | **POST** /v1/clients/{clientId}/familymembers | 
[**delete_client_family_members**](ClientFamilyMemberApi.md#delete_client_family_members) | **DELETE** /v1/clients/{clientId}/familymembers/{familyMemberId} | 
[**get_family_member**](ClientFamilyMemberApi.md#get_family_member) | **GET** /v1/clients/{clientId}/familymembers/{familyMemberId} | 
[**get_family_members**](ClientFamilyMemberApi.md#get_family_members) | **GET** /v1/clients/{clientId}/familymembers | 
[**get_template2**](ClientFamilyMemberApi.md#get_template2) | **GET** /v1/clients/{clientId}/familymembers/template | 
[**update_client_family_members**](ClientFamilyMemberApi.md#update_client_family_members) | **PUT** /v1/clients/{clientId}/familymembers/{familyMemberId} | 

# **add_client_family_members**
> str add_client_family_members(client_id, body=body)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.add_client_family_members(client_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->add_client_family_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_family_members**
> str delete_client_family_members(family_member_id, client_id, body=body)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
family_member_id = 789 # int | 
client_id = 789 # int | clientId
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.delete_client_family_members(family_member_id, client_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->delete_client_family_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_member_id** | **int**|  | 
 **client_id** | **int**| clientId | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_family_member**
> str get_family_member(family_member_id, client_id)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
family_member_id = 789 # int | 
client_id = 789 # int | clientId

try:
    api_response = api_instance.get_family_member(family_member_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->get_family_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_member_id** | **int**|  | 
 **client_id** | **int**| clientId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_family_members**
> str get_family_members(client_id)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | 

try:
    api_response = api_instance.get_family_members(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->get_family_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template2**
> str get_template2(client_id)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | 

try:
    api_response = api_instance.get_template2(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->get_template2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_family_members**
> str update_client_family_members(family_member_id, client_id, body=body)



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
api_instance = fineract_client.ClientFamilyMemberApi(fineract_client.ApiClient(configuration))
family_member_id = 789 # int | 
client_id = 789 # int | clientId
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_client_family_members(family_member_id, client_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientFamilyMemberApi->update_client_family_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_member_id** | **int**|  | 
 **client_id** | **int**| clientId | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

