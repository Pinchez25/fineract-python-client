# fineract_client.CentersApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate2**](CentersApi.md#activate2) | **POST** /v1/centers/{centerId} | Activate a Center | Generate Collection Sheet | Save Collection Sheet | Close a Center | Associate Groups | Disassociate Groups
[**create7**](CentersApi.md#create7) | **POST** /v1/centers | Create a Center
[**delete11**](CentersApi.md#delete11) | **DELETE** /v1/centers/{centerId} | Delete a Center
[**get_centers_template**](CentersApi.md#get_centers_template) | **GET** /v1/centers/downloadtemplate | 
[**post_centers_template**](CentersApi.md#post_centers_template) | **POST** /v1/centers/uploadtemplate | 
[**retrieve_all23**](CentersApi.md#retrieve_all23) | **GET** /v1/centers | List Centers
[**retrieve_group_account**](CentersApi.md#retrieve_group_account) | **GET** /v1/centers/{centerId}/accounts | Retrieve Center accounts overview
[**retrieve_one14**](CentersApi.md#retrieve_one14) | **GET** /v1/centers/{centerId} | Retrieve a Center
[**retrieve_template6**](CentersApi.md#retrieve_template6) | **GET** /v1/centers/template | Retrieve a Center Template
[**update12**](CentersApi.md#update12) | **PUT** /v1/centers/{centerId} | Update a Center


# **activate2**
> PostCentersCenterIdResponse activate2(center_id, post_centers_center_id_request, command=command)

Activate a Center | Generate Collection Sheet | Save Collection Sheet | Close a Center | Associate Groups | Disassociate Groups

Activate a Center:  Centers can be created in a Pending state. This API exists to enable center activation. If the center happens to be already active, this API will result in an error.  Close a Center:  Centers can be closed if they don't have any non-closed groups or saving accounts. If the Center has any active groups or savings accounts, this API will result in an error.  Associate Groups:  This API allows associating existing groups to a center. The groups are listed from the office to which the center is associated. If group(s) is already associated with a center, this API will result in an error.  Disassociate Groups:  This API allows to disassociate groups from a center.  Generate Collection Sheet:  This Api retrieves repayment details of all jlg loans under a center as on a specified meeting date.  Save Collection Sheet:  This Api allows the loan officer to perform bulk repayments of JLG loans for a center on a given meeting date.  Showing Request/Response for Close a Center

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_centers_center_id_request import PostCentersCenterIdRequest
from fineract_client.models.post_centers_center_id_response import PostCentersCenterIdResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    center_id = 56 # int | centerId
    post_centers_center_id_request = fineract_client.PostCentersCenterIdRequest() # PostCentersCenterIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Activate a Center | Generate Collection Sheet | Save Collection Sheet | Close a Center | Associate Groups | Disassociate Groups
        api_response = api_instance.activate2(center_id, post_centers_center_id_request, command=command)
        print("The response of CentersApi->activate2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->activate2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **center_id** | **int**| centerId | 
 **post_centers_center_id_request** | [**PostCentersCenterIdRequest**](PostCentersCenterIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostCentersCenterIdResponse**](PostCentersCenterIdResponse.md)

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

# **create7**
> PostCentersResponse create7(post_centers_request)

Create a Center

Creates a Center  Mandatory Fields: name, officeId, active, activationDate (if active=true)  Optional Fields: externalId, staffId, groupMembers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_centers_request import PostCentersRequest
from fineract_client.models.post_centers_response import PostCentersResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    post_centers_request = fineract_client.PostCentersRequest() # PostCentersRequest | 

    try:
        # Create a Center
        api_response = api_instance.create7(post_centers_request)
        print("The response of CentersApi->create7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->create7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_centers_request** | [**PostCentersRequest**](PostCentersRequest.md)|  | 

### Return type

[**PostCentersResponse**](PostCentersResponse.md)

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

# **delete11**
> DeleteCentersCenterIdResponse delete11(center_id)

Delete a Center

A Center can be deleted if it is in pending state and has no association - groups, loans or savings

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_centers_center_id_response import DeleteCentersCenterIdResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    center_id = 56 # int | centerId

    try:
        # Delete a Center
        api_response = api_instance.delete11(center_id)
        print("The response of CentersApi->delete11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->delete11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **center_id** | **int**| centerId | 

### Return type

[**DeleteCentersCenterIdResponse**](DeleteCentersCenterIdResponse.md)

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

# **get_centers_template**
> get_centers_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
    api_instance = fineract_client.CentersApi(api_client)
    office_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_centers_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling CentersApi->get_centers_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**|  | [optional] 
 **staff_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_centers_template**
> str post_centers_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
    api_instance = fineract_client.CentersApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_centers_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of CentersApi->post_centers_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->post_centers_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all23**
> GetCentersResponse retrieve_all23(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, meeting_date=meeting_date, date_format=date_format, locale=locale)

List Centers

The default implementation supports pagination and sorting with the default pagination size set to 200 records. The parameter limit with description -1 will return all entries.  Example Requests:    centers    centers?fields=name,officeName,joinedDate    centers?offset=10&limit=50    centers?orderBy=name&sortOrder=DESC

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_centers_response import GetCentersResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    office_id = 56 # int | officeId (optional)
    staff_id = 56 # int | staffId (optional)
    external_id = 'external_id_example' # str | externalId (optional)
    name = 'name_example' # str | name (optional)
    under_hierarchy = 'under_hierarchy_example' # str | underHierarchy (optional)
    paged = True # bool | paged (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    meeting_date = None # object | meetingDate (optional)
    date_format = 'date_format_example' # str | dateFormat (optional)
    locale = 'locale_example' # str | locale (optional)

    try:
        # List Centers
        api_response = api_instance.retrieve_all23(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, meeting_date=meeting_date, date_format=date_format, locale=locale)
        print("The response of CentersApi->retrieve_all23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->retrieve_all23: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **staff_id** | **int**| staffId | [optional] 
 **external_id** | **str**| externalId | [optional] 
 **name** | **str**| name | [optional] 
 **under_hierarchy** | **str**| underHierarchy | [optional] 
 **paged** | **bool**| paged | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **meeting_date** | [**object**](.md)| meetingDate | [optional] 
 **date_format** | **str**| dateFormat | [optional] 
 **locale** | **str**| locale | [optional] 

### Return type

[**GetCentersResponse**](GetCentersResponse.md)

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

# **retrieve_group_account**
> GetCentersCenterIdAccountsResponse retrieve_group_account(center_id)

Retrieve Center accounts overview

An example of how a savings summary for a Center can be provided. This is requested in a specific use case of the reference application.  It is quite reasonable to add resources like this to simplify User Interface development.    Example Requests:    centers/9/accounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_centers_center_id_accounts_response import GetCentersCenterIdAccountsResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    center_id = 56 # int | centerId

    try:
        # Retrieve Center accounts overview
        api_response = api_instance.retrieve_group_account(center_id)
        print("The response of CentersApi->retrieve_group_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->retrieve_group_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **center_id** | **int**| centerId | 

### Return type

[**GetCentersCenterIdAccountsResponse**](GetCentersCenterIdAccountsResponse.md)

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

# **retrieve_one14**
> GetCentersCenterIdResponse retrieve_one14(center_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve a Center

Retrieves a Center  Example Requests:    centers/1    centers/1?associations=groupMembers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_centers_center_id_response import GetCentersCenterIdResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    center_id = 56 # int | centerId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve a Center
        api_response = api_instance.retrieve_one14(center_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of CentersApi->retrieve_one14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->retrieve_one14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **center_id** | **int**| centerId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetCentersCenterIdResponse**](GetCentersCenterIdResponse.md)

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

# **retrieve_template6**
> GetCentersTemplateResponse retrieve_template6(command=command, office_id=office_id, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve a Center Template

Retrieves a Center Template  Example Requests:    centers/template    centers/template?officeId=2

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_centers_template_response import GetCentersTemplateResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    command = 'command_example' # str | command (optional)
    office_id = 56 # int | officeId (optional)
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve a Center Template
        api_response = api_instance.retrieve_template6(command=command, office_id=office_id, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of CentersApi->retrieve_template6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->retrieve_template6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| command | [optional] 
 **office_id** | **int**| officeId | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetCentersTemplateResponse**](GetCentersTemplateResponse.md)

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

# **update12**
> PutCentersCenterIdResponse update12(center_id, put_centers_center_id_request)

Update a Center

Updates a Center

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_centers_center_id_request import PutCentersCenterIdRequest
from fineract_client.models.put_centers_center_id_response import PutCentersCenterIdResponse
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
    api_instance = fineract_client.CentersApi(api_client)
    center_id = 56 # int | centerId
    put_centers_center_id_request = fineract_client.PutCentersCenterIdRequest() # PutCentersCenterIdRequest | 

    try:
        # Update a Center
        api_response = api_instance.update12(center_id, put_centers_center_id_request)
        print("The response of CentersApi->update12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CentersApi->update12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **center_id** | **int**| centerId | 
 **put_centers_center_id_request** | [**PutCentersCenterIdRequest**](PutCentersCenterIdRequest.md)|  | 

### Return type

[**PutCentersCenterIdResponse**](PutCentersCenterIdResponse.md)

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

