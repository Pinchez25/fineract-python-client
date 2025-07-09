# fineract_client.GroupsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_or_generate_collection_sheet**](GroupsApi.md#activate_or_generate_collection_sheet) | **POST** /v1/groups/{groupId} | Activate a Group | Associate Clients | Disassociate Clients | Transfer Clients across groups | Generate Collection Sheet | Save Collection Sheet | Unassign a Staff | Assign a Staff | Close a Group | Unassign a Role | Update a Role
[**create8**](GroupsApi.md#create8) | **POST** /v1/groups | Create a Group
[**delete12**](GroupsApi.md#delete12) | **DELETE** /v1/groups/{groupId} | Delete a Group
[**get_groups_template**](GroupsApi.md#get_groups_template) | **GET** /v1/groups/downloadtemplate | 
[**post_group_template**](GroupsApi.md#post_group_template) | **POST** /v1/groups/uploadtemplate | 
[**retrieve_accounts**](GroupsApi.md#retrieve_accounts) | **GET** /v1/groups/{groupId}/accounts | Retrieve Group accounts overview
[**retrieve_all24**](GroupsApi.md#retrieve_all24) | **GET** /v1/groups | List Groups
[**retrieve_gsim_accounts**](GroupsApi.md#retrieve_gsim_accounts) | **GET** /v1/groups/{groupId}/gsimaccounts | 
[**retrieve_one15**](GroupsApi.md#retrieve_one15) | **GET** /v1/groups/{groupId} | Retrieve a Group
[**retrieve_template7**](GroupsApi.md#retrieve_template7) | **GET** /v1/groups/template | Retrieve Group Template
[**retrieveglim_accounts**](GroupsApi.md#retrieveglim_accounts) | **GET** /v1/groups/{groupId}/glimaccounts | 
[**unassign_loan_officer**](GroupsApi.md#unassign_loan_officer) | **POST** /v1/groups/{groupId}/command/unassign_staff | Unassign a Staff
[**update13**](GroupsApi.md#update13) | **PUT** /v1/groups/{groupId} | Update a Group


# **activate_or_generate_collection_sheet**
> PostGroupsGroupIdResponse activate_or_generate_collection_sheet(group_id, post_groups_group_id_request, command=command, role_id=role_id)

Activate a Group | Associate Clients | Disassociate Clients | Transfer Clients across groups | Generate Collection Sheet | Save Collection Sheet | Unassign a Staff | Assign a Staff | Close a Group | Unassign a Role | Update a Role

Activate a Group:  Groups can be created in a Pending state. This API exists to enable group activation.    If the group happens to be already active this API will result in an error.  Mandatory Fields: activationDate  Associate Clients:  This API allows to associate existing clients to a group.    The clients are listed from the office to which the group is associated.    If client(s) is already associated with group then API will result in an error.  Mandatory Fields: clientMembers  Disassociate Clients:  This API allows to disassociate clients from a group.    Disassociating a client with active joint liability group loans results in an error.  Mandatory Fields: clientMembers  Transfer Clients across groups:  This API allows to transfer clients from one group to another  Mandatory Fields: destinationGroupId and clients  Optional Fields: inheritDestinationGroupLoanOfficer (defaults to true) and transferActiveLoans (defaults to true)  Generate Collection Sheet:  This API retrieves repayment details of all jlg loans of all members of a group on a specified meeting date.  Mandatory Fields: calendarId and transactionDate  Save Collection Sheet:  This api allows the loan officer to perform bulk repayments of JLG loans for a group on its meeting date.  Mandatory Fields: calendarId, transactionDate, actualDisbursementDate  Optional Fields: clientsAttendance, bulkRepaymentTransaction, bulkDisbursementTransactions  Unassign a Staff:  Allows you to unassign the Staff.  Mandatory Fields: staffId  Assign a Staff:  Allows you to assign Staff to an existing Group.    The selected Staff should be belong to the same office (or an office higher up in the hierarchy) as this groupMandatory Fields: staffId  Optional Fields: inheritStaffForClientAccounts (Optional: Boolean if true all members of the group (i.e all clients with active loans and savings ) will inherit the staffId)  Close a Group:  This API exists to close a group. Groups can be closed if they don't have any non-closed clients/loans/savingsAccounts.    If the group has any active clients/loans/savingsAccount, this API will result in an error.Assign a Role:  Allows you to assign a Role to an existing member of a group.    We can define the different roles applicable to group members by adding code values to the pre-defined system code GROUPROLE. Example:Group leader etc.  Mandatory Fields: clientId, role  Unassign a Role:  Allows you to unassign Roles associated tp Group members.  Update a Role:  Allows you to update the member Role.  Mandatory Fields: role  Showing request/response for Transfer Clients across groups

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_groups_group_id_request import PostGroupsGroupIdRequest
from fineract_client.models.post_groups_group_id_response import PostGroupsGroupIdResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId
    post_groups_group_id_request = fineract_client.PostGroupsGroupIdRequest() # PostGroupsGroupIdRequest | 
    command = 'command_example' # str | command (optional)
    role_id = 56 # int | roleId (optional)

    try:
        # Activate a Group | Associate Clients | Disassociate Clients | Transfer Clients across groups | Generate Collection Sheet | Save Collection Sheet | Unassign a Staff | Assign a Staff | Close a Group | Unassign a Role | Update a Role
        api_response = api_instance.activate_or_generate_collection_sheet(group_id, post_groups_group_id_request, command=command, role_id=role_id)
        print("The response of GroupsApi->activate_or_generate_collection_sheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->activate_or_generate_collection_sheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **post_groups_group_id_request** | [**PostGroupsGroupIdRequest**](PostGroupsGroupIdRequest.md)|  | 
 **command** | **str**| command | [optional] 
 **role_id** | **int**| roleId | [optional] 

### Return type

[**PostGroupsGroupIdResponse**](PostGroupsGroupIdResponse.md)

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

# **create8**
> PostGroupsResponse create8(post_groups_request)

Create a Group

Creates a Group  Mandatory Fields: name, officeId, active, activationDate (if active=true)  Optional Fields: externalId, staffId, clientMembers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_groups_request import PostGroupsRequest
from fineract_client.models.post_groups_response import PostGroupsResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    post_groups_request = fineract_client.PostGroupsRequest() # PostGroupsRequest | 

    try:
        # Create a Group
        api_response = api_instance.create8(post_groups_request)
        print("The response of GroupsApi->create8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_groups_request** | [**PostGroupsRequest**](PostGroupsRequest.md)|  | 

### Return type

[**PostGroupsResponse**](PostGroupsResponse.md)

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

# **delete12**
> DeleteGroupsGroupIdResponse delete12(group_id)

Delete a Group

A group can be deleted if it is in pending state and has no associations - clients, loans or savings

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_groups_group_id_response import DeleteGroupsGroupIdResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId

    try:
        # Delete a Group
        api_response = api_instance.delete12(group_id)
        print("The response of GroupsApi->delete12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 

### Return type

[**DeleteGroupsGroupIdResponse**](DeleteGroupsGroupIdResponse.md)

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

# **get_groups_template**
> get_groups_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
    api_instance = fineract_client.GroupsApi(api_client)
    office_id = 56 # int |  (optional)
    staff_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_groups_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups_template: %s\n" % e)
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

# **post_group_template**
> str post_group_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
    api_instance = fineract_client.GroupsApi(api_client)
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_group_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of GroupsApi->post_group_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->post_group_template: %s\n" % e)
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

# **retrieve_accounts**
> GetGroupsGroupIdAccountsResponse retrieve_accounts(group_id)

Retrieve Group accounts overview

Retrieves details of all Loan and Savings accounts associated with this group.    Example Requests:    groups/1/accounts      groups/1/accounts?fields=loanAccounts,savingsAccounts,memberLoanAccounts,  memberSavingsAccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_groups_group_id_accounts_response import GetGroupsGroupIdAccountsResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId

    try:
        # Retrieve Group accounts overview
        api_response = api_instance.retrieve_accounts(group_id)
        print("The response of GroupsApi->retrieve_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieve_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 

### Return type

[**GetGroupsGroupIdAccountsResponse**](GetGroupsGroupIdAccountsResponse.md)

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

# **retrieve_all24**
> GetGroupsResponse retrieve_all24(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)

List Groups

The default implementation of listing Groups returns 200 entries with support for pagination and sorting. Using the parameter limit with description -1 returns all entries.  Example Requests:    groups    groups?fields=name,officeName,joinedDate    groups?offset=10&limit=50    groups?orderBy=name&sortOrder=DESC

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_groups_response import GetGroupsResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
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
    orphans_only = True # bool | orphansOnly (optional)

    try:
        # List Groups
        api_response = api_instance.retrieve_all24(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)
        print("The response of GroupsApi->retrieve_all24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieve_all24: %s\n" % e)
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
 **orphans_only** | **bool**| orphansOnly | [optional] 

### Return type

[**GetGroupsResponse**](GetGroupsResponse.md)

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

# **retrieve_gsim_accounts**
> str retrieve_gsim_accounts(group_id, parent_gsim_account_no=parent_gsim_account_no, parent_gsimid=parent_gsimid)



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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | 
    parent_gsim_account_no = 'parent_gsim_account_no_example' # str |  (optional)
    parent_gsimid = 56 # int |  (optional)

    try:
        api_response = api_instance.retrieve_gsim_accounts(group_id, parent_gsim_account_no=parent_gsim_account_no, parent_gsimid=parent_gsimid)
        print("The response of GroupsApi->retrieve_gsim_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieve_gsim_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **parent_gsim_account_no** | **str**|  | [optional] 
 **parent_gsimid** | **int**|  | [optional] 

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

# **retrieve_one15**
> GetGroupsGroupIdResponse retrieve_one15(group_id, staff_in_selected_office_only=staff_in_selected_office_only, role_id=role_id)

Retrieve a Group

Retrieve group information.  Example Requests:    groups/1    groups/1?associations=clientMembers

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_groups_group_id_response import GetGroupsGroupIdResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)
    role_id = 56 # int | roleId (optional)

    try:
        # Retrieve a Group
        api_response = api_instance.retrieve_one15(group_id, staff_in_selected_office_only=staff_in_selected_office_only, role_id=role_id)
        print("The response of GroupsApi->retrieve_one15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieve_one15: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]
 **role_id** | **int**| roleId | [optional] 

### Return type

[**GetGroupsGroupIdResponse**](GetGroupsGroupIdResponse.md)

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

# **retrieve_template7**
> GetGroupsTemplateResponse retrieve_template7(office_id=office_id, center=center, center_id=center_id, command=command, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve Group Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:    Field Defaults  Allowed Value Lists  Example Requests:    groups/template    groups/template?officeId=2    groups/template?centerId=1    groups/template?centerId=1&staffInSelectedOfficeOnly=true

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_groups_template_response import GetGroupsTemplateResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    office_id = 56 # int | officeId (optional)
    center = True # bool | center (optional)
    center_id = 56 # int | centerId (optional)
    command = 'command_example' # str | command (optional)
    staff_in_selected_office_only = False # bool | staffInSelectedOfficeOnly (optional) (default to False)

    try:
        # Retrieve Group Template
        api_response = api_instance.retrieve_template7(office_id=office_id, center=center, center_id=center_id, command=command, staff_in_selected_office_only=staff_in_selected_office_only)
        print("The response of GroupsApi->retrieve_template7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieve_template7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **center** | **bool**| center | [optional] 
 **center_id** | **int**| centerId | [optional] 
 **command** | **str**| command | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to False]

### Return type

[**GetGroupsTemplateResponse**](GetGroupsTemplateResponse.md)

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

# **retrieveglim_accounts**
> str retrieveglim_accounts(group_id, parent_loan_account_no=parent_loan_account_no)



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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | 
    parent_loan_account_no = 'parent_loan_account_no_example' # str |  (optional)

    try:
        api_response = api_instance.retrieveglim_accounts(group_id, parent_loan_account_no=parent_loan_account_no)
        print("The response of GroupsApi->retrieveglim_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->retrieveglim_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 
 **parent_loan_account_no** | **str**|  | [optional] 

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

# **unassign_loan_officer**
> PostGroupsGroupIdCommandUnassignStaffResponse unassign_loan_officer(group_id, post_groups_group_id_command_unassign_staff_request)

Unassign a Staff

Allows you to unassign the Staff.  Mandatory Fields: staffId

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_groups_group_id_command_unassign_staff_request import PostGroupsGroupIdCommandUnassignStaffRequest
from fineract_client.models.post_groups_group_id_command_unassign_staff_response import PostGroupsGroupIdCommandUnassignStaffResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId
    post_groups_group_id_command_unassign_staff_request = fineract_client.PostGroupsGroupIdCommandUnassignStaffRequest() # PostGroupsGroupIdCommandUnassignStaffRequest | 

    try:
        # Unassign a Staff
        api_response = api_instance.unassign_loan_officer(group_id, post_groups_group_id_command_unassign_staff_request)
        print("The response of GroupsApi->unassign_loan_officer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->unassign_loan_officer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **post_groups_group_id_command_unassign_staff_request** | [**PostGroupsGroupIdCommandUnassignStaffRequest**](PostGroupsGroupIdCommandUnassignStaffRequest.md)|  | 

### Return type

[**PostGroupsGroupIdCommandUnassignStaffResponse**](PostGroupsGroupIdCommandUnassignStaffResponse.md)

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

# **update13**
> PutGroupsGroupIdResponse update13(group_id, put_groups_group_id_request)

Update a Group

Updates a Group

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_groups_group_id_request import PutGroupsGroupIdRequest
from fineract_client.models.put_groups_group_id_response import PutGroupsGroupIdResponse
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
    api_instance = fineract_client.GroupsApi(api_client)
    group_id = 56 # int | groupId
    put_groups_group_id_request = fineract_client.PutGroupsGroupIdRequest() # PutGroupsGroupIdRequest | 

    try:
        # Update a Group
        api_response = api_instance.update13(group_id, put_groups_group_id_request)
        print("The response of GroupsApi->update13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update13: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **put_groups_group_id_request** | [**PutGroupsGroupIdRequest**](PutGroupsGroupIdRequest.md)|  | 

### Return type

[**PutGroupsGroupIdResponse**](PutGroupsGroupIdResponse.md)

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

