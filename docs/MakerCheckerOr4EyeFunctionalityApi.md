# fineract_client.MakerCheckerOr4EyeFunctionalityApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_maker_checker_entry**](MakerCheckerOr4EyeFunctionalityApi.md#approve_maker_checker_entry) | **POST** /v1/makercheckers/{auditId} | Approve Maker Checker Entry | Reject Maker Checker Entry
[**delete_maker_checker_entry**](MakerCheckerOr4EyeFunctionalityApi.md#delete_maker_checker_entry) | **DELETE** /v1/makercheckers/{auditId} | Delete Maker Checker Entry
[**retrieve_audit_search_template1**](MakerCheckerOr4EyeFunctionalityApi.md#retrieve_audit_search_template1) | **GET** /v1/makercheckers/searchtemplate | Maker Checker Search Template
[**retrieve_commands**](MakerCheckerOr4EyeFunctionalityApi.md#retrieve_commands) | **GET** /v1/makercheckers | List Maker Checker Entries

# **approve_maker_checker_entry**
> PostMakerCheckersResponse approve_maker_checker_entry(audit_id, command=command)

Approve Maker Checker Entry | Reject Maker Checker Entry

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
api_instance = fineract_client.MakerCheckerOr4EyeFunctionalityApi(fineract_client.ApiClient(configuration))
audit_id = 789 # int | auditId
command = 'command_example' # str | command (optional)

try:
    # Approve Maker Checker Entry | Reject Maker Checker Entry
    api_response = api_instance.approve_maker_checker_entry(audit_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakerCheckerOr4EyeFunctionalityApi->approve_maker_checker_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **int**| auditId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostMakerCheckersResponse**](PostMakerCheckersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_maker_checker_entry**
> PostMakerCheckersResponse delete_maker_checker_entry(audit_id)

Delete Maker Checker Entry

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
api_instance = fineract_client.MakerCheckerOr4EyeFunctionalityApi(fineract_client.ApiClient(configuration))
audit_id = 789 # int | auditId

try:
    # Delete Maker Checker Entry
    api_response = api_instance.delete_maker_checker_entry(audit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakerCheckerOr4EyeFunctionalityApi->delete_maker_checker_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **int**| auditId | 

### Return type

[**PostMakerCheckersResponse**](PostMakerCheckersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_audit_search_template1**
> GetMakerCheckersSearchTemplateResponse retrieve_audit_search_template1()

Maker Checker Search Template

This is a convenience resource. It can be useful when building a Checker Inbox UI. \"appUsers\" are data scoped to the office/branch the requestor is associated with. \"actionNames\" and \"entityNames\" returned are those that the requestor has Checker approval permissions for.  Example Requests:  makercheckers/searchtemplate makercheckers/searchtemplate?fields=entityNames

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
api_instance = fineract_client.MakerCheckerOr4EyeFunctionalityApi(fineract_client.ApiClient(configuration))

try:
    # Maker Checker Search Template
    api_response = api_instance.retrieve_audit_search_template1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakerCheckerOr4EyeFunctionalityApi->retrieve_audit_search_template1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMakerCheckersSearchTemplateResponse**](GetMakerCheckersSearchTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_commands**
> list[GetMakerCheckerResponse] retrieve_commands(action_name=action_name, entity_name=entity_name, resource_id=resource_id, maker_id=maker_id, maker_date_time_from=maker_date_time_from, maker_date_time_to=maker_date_time_to, office_id=office_id, group_id=group_id, client_id=client_id, loanid=loanid, savings_account_id=savings_account_id)

List Maker Checker Entries

Get a list of entries that can be checked by the requestor that match the criteria supplied.  Example Requests:  makercheckers  makercheckers?fields=madeOnDate,maker,processingResult  makercheckers?makerDateTimeFrom=2013-03-25 08:00:00&makerDateTimeTo=2013-04-04 18:00:00  makercheckers?officeId=1  makercheckers?officeId=1&includeJson=true

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
api_instance = fineract_client.MakerCheckerOr4EyeFunctionalityApi(fineract_client.ApiClient(configuration))
action_name = 'action_name_example' # str | actionName (optional)
entity_name = 'entity_name_example' # str | entityName (optional)
resource_id = 789 # int | resourceId (optional)
maker_id = 789 # int | makerId (optional)
maker_date_time_from = 'maker_date_time_from_example' # str | makerDateTimeFrom (optional)
maker_date_time_to = 'maker_date_time_to_example' # str | makerDateTimeTo (optional)
office_id = 56 # int | officeId (optional)
group_id = 56 # int | groupId (optional)
client_id = 56 # int | clientId (optional)
loanid = 56 # int | loanid (optional)
savings_account_id = 56 # int | savingsAccountId (optional)

try:
    # List Maker Checker Entries
    api_response = api_instance.retrieve_commands(action_name=action_name, entity_name=entity_name, resource_id=resource_id, maker_id=maker_id, maker_date_time_from=maker_date_time_from, maker_date_time_to=maker_date_time_to, office_id=office_id, group_id=group_id, client_id=client_id, loanid=loanid, savings_account_id=savings_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakerCheckerOr4EyeFunctionalityApi->retrieve_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_name** | **str**| actionName | [optional] 
 **entity_name** | **str**| entityName | [optional] 
 **resource_id** | **int**| resourceId | [optional] 
 **maker_id** | **int**| makerId | [optional] 
 **maker_date_time_from** | **str**| makerDateTimeFrom | [optional] 
 **maker_date_time_to** | **str**| makerDateTimeTo | [optional] 
 **office_id** | **int**| officeId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **client_id** | **int**| clientId | [optional] 
 **loanid** | **int**| loanid | [optional] 
 **savings_account_id** | **int**| savingsAccountId | [optional] 

### Return type

[**list[GetMakerCheckerResponse]**](GetMakerCheckerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

