# fineract_client.AuditsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_audit_entries**](AuditsApi.md#retrieve_audit_entries) | **GET** /v1/audits | List Audits
[**retrieve_audit_entry**](AuditsApi.md#retrieve_audit_entry) | **GET** /v1/audits/{auditId} | Retrieve an Audit Entry
[**retrieve_audit_search_template**](AuditsApi.md#retrieve_audit_search_template) | **GET** /v1/audits/searchtemplate | Audit Search Template

# **retrieve_audit_entries**
> list[GetMakerCheckerResponse] retrieve_audit_entries(action_name=action_name, entity_name=entity_name, resource_id=resource_id, maker_id=maker_id, maker_date_time_from=maker_date_time_from, maker_date_time_to=maker_date_time_to, checker_id=checker_id, checker_date_time_from=checker_date_time_from, checker_date_time_to=checker_date_time_to, processing_result=processing_result, office_id=office_id, group_id=group_id, client_id=client_id, loanid=loanid, savings_account_id=savings_account_id, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Audits

Get a 200 list of audits that match the criteria supplied and sorted by audit id in descending order, and are within the requestors' data scope. Also it supports pagination and sorting  Example Requests:  audits  audits?fields=madeOnDate,maker,processingResult  audits?makerDateTimeFrom=2013-03-25 08:00:00&makerDateTimeTo=2013-04-04 18:00:00  audits?officeId=1  audits?officeId=1&includeJson=true

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
api_instance = fineract_client.AuditsApi(fineract_client.ApiClient(configuration))
action_name = 'action_name_example' # str | actionName (optional)
entity_name = 'entity_name_example' # str | entityName (optional)
resource_id = 789 # int | resourceId (optional)
maker_id = 789 # int | makerId (optional)
maker_date_time_from = 'maker_date_time_from_example' # str | makerDateTimeFrom (optional)
maker_date_time_to = 'maker_date_time_to_example' # str | makerDateTimeTo (optional)
checker_id = 789 # int | checkerId (optional)
checker_date_time_from = 'checker_date_time_from_example' # str | checkerDateTimeFrom (optional)
checker_date_time_to = 'checker_date_time_to_example' # str | checkerDateTimeTo (optional)
processing_result = 56 # int | processingResult (optional)
office_id = 56 # int | officeId (optional)
group_id = 56 # int | groupId (optional)
client_id = 56 # int | clientId (optional)
loanid = 56 # int | loanid (optional)
savings_account_id = 56 # int | savingsAccountId (optional)
paged = true # bool | paged (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # List Audits
    api_response = api_instance.retrieve_audit_entries(action_name=action_name, entity_name=entity_name, resource_id=resource_id, maker_id=maker_id, maker_date_time_from=maker_date_time_from, maker_date_time_to=maker_date_time_to, checker_id=checker_id, checker_date_time_from=checker_date_time_from, checker_date_time_to=checker_date_time_to, processing_result=processing_result, office_id=office_id, group_id=group_id, client_id=client_id, loanid=loanid, savings_account_id=savings_account_id, paged=paged, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsApi->retrieve_audit_entries: %s\n" % e)
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
 **checker_id** | **int**| checkerId | [optional] 
 **checker_date_time_from** | **str**| checkerDateTimeFrom | [optional] 
 **checker_date_time_to** | **str**| checkerDateTimeTo | [optional] 
 **processing_result** | **int**| processingResult | [optional] 
 **office_id** | **int**| officeId | [optional] 
 **group_id** | **int**| groupId | [optional] 
 **client_id** | **int**| clientId | [optional] 
 **loanid** | **int**| loanid | [optional] 
 **savings_account_id** | **int**| savingsAccountId | [optional] 
 **paged** | **bool**| paged | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**list[GetMakerCheckerResponse]**](GetMakerCheckerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_audit_entry**
> GetMakerCheckerResponse retrieve_audit_entry(audit_id)

Retrieve an Audit Entry

Example Requests:  audits/20 audits/20?fields=madeOnDate,maker,processingResult

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
api_instance = fineract_client.AuditsApi(fineract_client.ApiClient(configuration))
audit_id = 789 # int | auditId

try:
    # Retrieve an Audit Entry
    api_response = api_instance.retrieve_audit_entry(audit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsApi->retrieve_audit_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **int**| auditId | 

### Return type

[**GetMakerCheckerResponse**](GetMakerCheckerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_audit_search_template**
> GetMakerCheckersSearchTemplateResponse retrieve_audit_search_template()

Audit Search Template

This is a convenience resource. It can be useful when building an Audit Search UI. \"appUsers\" are data scoped to the office/branch the requestor is associated with.  Example Requests:  audits/searchtemplate audits/searchtemplate?fields=actionNames

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
api_instance = fineract_client.AuditsApi(fineract_client.ApiClient(configuration))

try:
    # Audit Search Template
    api_response = api_instance.retrieve_audit_search_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsApi->retrieve_audit_search_template: %s\n" % e)
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

