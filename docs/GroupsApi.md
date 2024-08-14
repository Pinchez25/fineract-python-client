# fineract_client.GroupsApi

All URIs are relative to */fineract-provider/api/v1*

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
> PostGroupsGroupIdResponse activate_or_generate_collection_sheet(body, group_id, command=command, role_id=role_id)

Activate a Group | Associate Clients | Disassociate Clients | Transfer Clients across groups | Generate Collection Sheet | Save Collection Sheet | Unassign a Staff | Assign a Staff | Close a Group | Unassign a Role | Update a Role

Activate a Group:  Groups can be created in a Pending state. This API exists to enable group activation.    If the group happens to be already active this API will result in an error.  Mandatory Fields: activationDate  Associate Clients:  This API allows to associate existing clients to a group.    The clients are listed from the office to which the group is associated.    If client(s) is already associated with group then API will result in an error.  Mandatory Fields: clientMembers  Disassociate Clients:  This API allows to disassociate clients from a group.    Disassociating a client with active joint liability group loans results in an error.  Mandatory Fields: clientMembers  Transfer Clients across groups:  This API allows to transfer clients from one group to another  Mandatory Fields: destinationGroupId and clients  Optional Fields: inheritDestinationGroupLoanOfficer (defaults to true) and transferActiveLoans (defaults to true)  Generate Collection Sheet:  This API retrieves repayment details of all jlg loans of all members of a group on a specified meeting date.  Mandatory Fields: calendarId and transactionDate  Save Collection Sheet:  This api allows the loan officer to perform bulk repayments of JLG loans for a group on its meeting date.  Mandatory Fields: calendarId, transactionDate, actualDisbursementDate  Optional Fields: clientsAttendance, bulkRepaymentTransaction, bulkDisbursementTransactions  Unassign a Staff:  Allows you to unassign the Staff.  Mandatory Fields: staffId  Assign a Staff:  Allows you to assign Staff to an existing Group.    The selected Staff should be belong to the same office (or an office higher up in the hierarchy) as this groupMandatory Fields: staffId  Optional Fields: inheritStaffForClientAccounts (Optional: Boolean if true all members of the group (i.e all clients with active loans and savings ) will inherit the staffId)  Close a Group:  This API exists to close a group. Groups can be closed if they don't have any non-closed clients/loans/savingsAccounts.    If the group has any active clients/loans/savingsAccount, this API will result in an error.Assign a Role:  Allows you to assign a Role to an existing member of a group.    We can define the different roles applicable to group members by adding code values to the pre-defined system code GROUPROLE. Example:Group leader etc.  Mandatory Fields: clientId, role  Unassign a Role:  Allows you to unassign Roles associated tp Group members.  Update a Role:  Allows you to update the member Role.  Mandatory Fields: role  Showing request/response for Transfer Clients across groups

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostGroupsGroupIdRequest() # PostGroupsGroupIdRequest | 
group_id = 789 # int | groupId
command = 'command_example' # str | command (optional)
role_id = 789 # int | roleId (optional)

try:
    # Activate a Group | Associate Clients | Disassociate Clients | Transfer Clients across groups | Generate Collection Sheet | Save Collection Sheet | Unassign a Staff | Assign a Staff | Close a Group | Unassign a Role | Update a Role
    api_response = api_instance.activate_or_generate_collection_sheet(body, group_id, command=command, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->activate_or_generate_collection_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGroupsGroupIdRequest**](PostGroupsGroupIdRequest.md)|  | 
 **group_id** | **int**| groupId | 
 **command** | **str**| command | [optional] 
 **role_id** | **int**| roleId | [optional] 

### Return type

[**PostGroupsGroupIdResponse**](PostGroupsGroupIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create8**
> PostGroupsResponse create8(body)

Create a Group

Creates a Group  Mandatory Fields: name, officeId, active, activationDate (if active=true)  Optional Fields: externalId, staffId, clientMembers

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostGroupsRequest() # PostGroupsRequest | 

try:
    # Create a Group
    api_response = api_instance.create8(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGroupsRequest**](PostGroupsRequest.md)|  | 

### Return type

[**PostGroupsResponse**](PostGroupsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete12**
> DeleteGroupsGroupIdResponse delete12(group_id)

Delete a Group

A group can be deleted if it is in pending state and has no associations - clients, loans or savings

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
group_id = 789 # int | groupId

try:
    # Delete a Group
    api_response = api_instance.delete12(group_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_template**
> get_groups_template(office_id=office_id, staff_id=staff_id, date_format=date_format)



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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
office_id = 789 # int |  (optional)
staff_id = 789 # int |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_groups_template(office_id=office_id, staff_id=staff_id, date_format=date_format)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group_template**
> str post_group_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_group_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->post_group_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_accounts**
> GetGroupsGroupIdAccountsResponse retrieve_accounts(group_id)

Retrieve Group accounts overview

Retrieves details of all Loan and Savings accounts associated with this group.    Example Requests:    groups/1/accounts      groups/1/accounts?fields=loanAccounts,savingsAccounts,memberLoanAccounts,  memberSavingsAccounts

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
group_id = 789 # int | groupId

try:
    # Retrieve Group accounts overview
    api_response = api_instance.retrieve_accounts(group_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all24**
> GetGroupsResponse retrieve_all24(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)

List Groups

The default implementation of listing Groups returns 200 entries with support for pagination and sorting. Using the parameter limit with description -1 returns all entries.  Example Requests:    groups    groups?fields=name,officeName,joinedDate    groups?offset=10&limit=50    groups?orderBy=name&sortOrder=DESC

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)
staff_id = 789 # int | staffId (optional)
external_id = 'external_id_example' # str | externalId (optional)
name = 'name_example' # str | name (optional)
under_hierarchy = 'under_hierarchy_example' # str | underHierarchy (optional)
paged = true # bool | paged (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)
orphans_only = true # bool | orphansOnly (optional)

try:
    # List Groups
    api_response = api_instance.retrieve_all24(office_id=office_id, staff_id=staff_id, external_id=external_id, name=name, under_hierarchy=under_hierarchy, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, orphans_only=orphans_only)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_gsim_accounts**
> str retrieve_gsim_accounts(group_id, parent_gsim_account_no=parent_gsim_account_no, parent_gsimid=parent_gsimid)



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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
group_id = 789 # int | 
parent_gsim_account_no = 'parent_gsim_account_no_example' # str |  (optional)
parent_gsimid = 789 # int |  (optional)

try:
    api_response = api_instance.retrieve_gsim_accounts(group_id, parent_gsim_account_no=parent_gsim_account_no, parent_gsimid=parent_gsimid)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one15**
> GetGroupsGroupIdResponse retrieve_one15(group_id, staff_in_selected_office_only=staff_in_selected_office_only, role_id=role_id)

Retrieve a Group

Retrieve group information.  Example Requests:    groups/1    groups/1?associations=clientMembers

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
group_id = 789 # int | groupId
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)
role_id = 789 # int | roleId (optional)

try:
    # Retrieve a Group
    api_response = api_instance.retrieve_one15(group_id, staff_in_selected_office_only=staff_in_selected_office_only, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->retrieve_one15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId | 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]
 **role_id** | **int**| roleId | [optional] 

### Return type

[**GetGroupsGroupIdResponse**](GetGroupsGroupIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template7**
> GetGroupsTemplateResponse retrieve_template7(office_id=office_id, center=center, center_id=center_id, command=command, staff_in_selected_office_only=staff_in_selected_office_only)

Retrieve Group Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:    Field Defaults  Allowed Value Lists  Example Requests:    groups/template    groups/template?officeId=2    groups/template?centerId=1    groups/template?centerId=1&staffInSelectedOfficeOnly=true

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId (optional)
center = true # bool | center (optional)
center_id = 789 # int | centerId (optional)
command = 'command_example' # str | command (optional)
staff_in_selected_office_only = false # bool | staffInSelectedOfficeOnly (optional) (default to false)

try:
    # Retrieve Group Template
    api_response = api_instance.retrieve_template7(office_id=office_id, center=center, center_id=center_id, command=command, staff_in_selected_office_only=staff_in_selected_office_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->retrieve_template7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | [optional] 
 **center** | **bool**| center | [optional] 
 **center_id** | **int**| centerId | [optional] 
 **command** | **str**| command | [optional] 
 **staff_in_selected_office_only** | **bool**| staffInSelectedOfficeOnly | [optional] [default to false]

### Return type

[**GetGroupsTemplateResponse**](GetGroupsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveglim_accounts**
> str retrieveglim_accounts(group_id, parent_loan_account_no=parent_loan_account_no)



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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
group_id = 789 # int | 
parent_loan_account_no = 'parent_loan_account_no_example' # str |  (optional)

try:
    api_response = api_instance.retrieveglim_accounts(group_id, parent_loan_account_no=parent_loan_account_no)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_loan_officer**
> PostGroupsGroupIdCommandUnassignStaffResponse unassign_loan_officer(body, group_id)

Unassign a Staff

Allows you to unassign the Staff.  Mandatory Fields: staffId

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostGroupsGroupIdCommandUnassignStaffRequest() # PostGroupsGroupIdCommandUnassignStaffRequest | 
group_id = 789 # int | groupId

try:
    # Unassign a Staff
    api_response = api_instance.unassign_loan_officer(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->unassign_loan_officer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostGroupsGroupIdCommandUnassignStaffRequest**](PostGroupsGroupIdCommandUnassignStaffRequest.md)|  | 
 **group_id** | **int**| groupId | 

### Return type

[**PostGroupsGroupIdCommandUnassignStaffResponse**](PostGroupsGroupIdCommandUnassignStaffResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update13**
> PutGroupsGroupIdResponse update13(body, group_id)

Update a Group

Updates a Group

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
api_instance = fineract_client.GroupsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutGroupsGroupIdRequest() # PutGroupsGroupIdRequest | 
group_id = 789 # int | groupId

try:
    # Update a Group
    api_response = api_instance.update13(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutGroupsGroupIdRequest**](PutGroupsGroupIdRequest.md)|  | 
 **group_id** | **int**| groupId | 

### Return type

[**PutGroupsGroupIdResponse**](PutGroupsGroupIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

