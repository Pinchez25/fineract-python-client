# fineract_client.RolesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_on_roles**](RolesApi.md#actions_on_roles) | **POST** /v1/roles/{roleId} | Enable Role | Disable Role
[**create_role**](RolesApi.md#create_role) | **POST** /v1/roles | Create a New Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete a Role
[**retrieve_all_roles**](RolesApi.md#retrieve_all_roles) | **GET** /v1/roles | List Roles
[**retrieve_role**](RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleId} | Retrieve a Role
[**retrieve_role_permissions**](RolesApi.md#retrieve_role_permissions) | **GET** /v1/roles/{roleId}/permissions | Retrieve a Role&#39;s Permissions
[**update_role**](RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update a Role
[**update_role_permissions**](RolesApi.md#update_role_permissions) | **PUT** /v1/roles/{roleId}/permissions | Update a Role&#39;s Permissions


# **actions_on_roles**
> PostRolesRoleIdResponse actions_on_roles(role_id, command=command)

Enable Role | Disable Role

Description : Enable role in case role is disabled. | Disable the role in case role is not associated with any users.





Example Request:   https://DomainName/api/v1/roles/{roleId}?command=enable





https://DomainName/api/v1/roles/{roleId}?command=disable

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_roles_role_id_response import PostRolesRoleIdResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId
    command = 'command_example' # str | command (optional)

    try:
        # Enable Role | Disable Role
        api_response = api_instance.actions_on_roles(role_id, command=command)
        print("The response of RolesApi->actions_on_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->actions_on_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostRolesRoleIdResponse**](PostRolesRoleIdResponse.md)

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

# **create_role**
> PostRolesResponse create_role(post_roles_request)

Create a New Role

Mandatory Fields
name, description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_roles_request import PostRolesRequest
from fineract_client.models.post_roles_response import PostRolesResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    post_roles_request = fineract_client.PostRolesRequest() # PostRolesRequest | 

    try:
        # Create a New Role
        api_response = api_instance.create_role(post_roles_request)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_roles_request** | [**PostRolesRequest**](PostRolesRequest.md)|  | 

### Return type

[**PostRolesResponse**](PostRolesResponse.md)

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

# **delete_role**
> DeleteRolesRoleIdResponse delete_role(role_id)

Delete a Role

Description : Delete the role in case role is not associated with any users.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_roles_role_id_response import DeleteRolesRoleIdResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId

    try:
        # Delete a Role
        api_response = api_instance.delete_role(role_id)
        print("The response of RolesApi->delete_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 

### Return type

[**DeleteRolesRoleIdResponse**](DeleteRolesRoleIdResponse.md)

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

# **retrieve_all_roles**
> List[GetRolesResponse] retrieve_all_roles()

List Roles

Example Requests:

roles


roles?fields=name

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_roles_response import GetRolesResponse
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
    api_instance = fineract_client.RolesApi(api_client)

    try:
        # List Roles
        api_response = api_instance.retrieve_all_roles()
        print("The response of RolesApi->retrieve_all_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->retrieve_all_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetRolesResponse]**](GetRolesResponse.md)

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

# **retrieve_role**
> GetRolesRoleIdResponse retrieve_role(role_id)

Retrieve a Role

Example Requests:

roles/1


roles/1?fields=name

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_roles_role_id_response import GetRolesRoleIdResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId

    try:
        # Retrieve a Role
        api_response = api_instance.retrieve_role(role_id)
        print("The response of RolesApi->retrieve_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->retrieve_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 

### Return type

[**GetRolesRoleIdResponse**](GetRolesRoleIdResponse.md)

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

# **retrieve_role_permissions**
> GetRolesRoleIdPermissionsResponse retrieve_role_permissions(role_id)

Retrieve a Role's Permissions

Example Requests:

roles/1/permissions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_roles_role_id_permissions_response import GetRolesRoleIdPermissionsResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId

    try:
        # Retrieve a Role's Permissions
        api_response = api_instance.retrieve_role_permissions(role_id)
        print("The response of RolesApi->retrieve_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->retrieve_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 

### Return type

[**GetRolesRoleIdPermissionsResponse**](GetRolesRoleIdPermissionsResponse.md)

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

# **update_role**
> PutRolesRoleIdResponse update_role(role_id, put_roles_role_id_request)

Update a Role

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_roles_role_id_request import PutRolesRoleIdRequest
from fineract_client.models.put_roles_role_id_response import PutRolesRoleIdResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId
    put_roles_role_id_request = fineract_client.PutRolesRoleIdRequest() # PutRolesRoleIdRequest | 

    try:
        # Update a Role
        api_response = api_instance.update_role(role_id, put_roles_role_id_request)
        print("The response of RolesApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 
 **put_roles_role_id_request** | [**PutRolesRoleIdRequest**](PutRolesRoleIdRequest.md)|  | 

### Return type

[**PutRolesRoleIdResponse**](PutRolesRoleIdResponse.md)

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

# **update_role_permissions**
> PutRolesRoleIdPermissionsResponse update_role_permissions(role_id, put_roles_role_id_permissions_request)

Update a Role's Permissions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_roles_role_id_permissions_request import PutRolesRoleIdPermissionsRequest
from fineract_client.models.put_roles_role_id_permissions_response import PutRolesRoleIdPermissionsResponse
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
    api_instance = fineract_client.RolesApi(api_client)
    role_id = 56 # int | roleId
    put_roles_role_id_permissions_request = fineract_client.PutRolesRoleIdPermissionsRequest() # PutRolesRoleIdPermissionsRequest | 

    try:
        # Update a Role's Permissions
        api_response = api_instance.update_role_permissions(role_id, put_roles_role_id_permissions_request)
        print("The response of RolesApi->update_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| roleId | 
 **put_roles_role_id_permissions_request** | [**PutRolesRoleIdPermissionsRequest**](PutRolesRoleIdPermissionsRequest.md)|  | 

### Return type

[**PutRolesRoleIdPermissionsResponse**](PutRolesRoleIdPermissionsResponse.md)

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

