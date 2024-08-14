# fineract_client.ReportMailingJobsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_mailing_job**](ReportMailingJobsApi.md#create_report_mailing_job) | **POST** /v1/reportmailingjobs | Create a Report Mailing Job
[**delete_report_mailing_job**](ReportMailingJobsApi.md#delete_report_mailing_job) | **DELETE** /v1/reportmailingjobs/{entityId} | Delete a Report Mailing Job
[**retrieve_all_report_mailing_jobs**](ReportMailingJobsApi.md#retrieve_all_report_mailing_jobs) | **GET** /v1/reportmailingjobs | List Report Mailing Jobs
[**retrieve_report_mailing_job**](ReportMailingJobsApi.md#retrieve_report_mailing_job) | **GET** /v1/reportmailingjobs/{entityId} | Retrieve a Report Mailing Job
[**retrieve_report_mailing_job_template**](ReportMailingJobsApi.md#retrieve_report_mailing_job_template) | **GET** /v1/reportmailingjobs/template | Retrieve Report Mailing Job Details Template
[**update_report_mailing_job**](ReportMailingJobsApi.md#update_report_mailing_job) | **PUT** /v1/reportmailingjobs/{entityId} | Update a Report Mailing Job 

# **create_report_mailing_job**
> PostReportMailingJobsResponse create_report_mailing_job(body)

Create a Report Mailing Job

Mandatory Fields: name, startDateTime, stretchyReportId, emailRecipients, emailSubject, emailMessage, emailAttachmentFileFormatId, recurrence, isActive  Optional Fields: description, stretchyReportParamMap

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostReportMailingJobsRequest() # PostReportMailingJobsRequest | 

try:
    # Create a Report Mailing Job
    api_response = api_instance.create_report_mailing_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->create_report_mailing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostReportMailingJobsRequest**](PostReportMailingJobsRequest.md)|  | 

### Return type

[**PostReportMailingJobsResponse**](PostReportMailingJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_mailing_job**
> DeleteReportMailingJobsResponse delete_report_mailing_job(body, entity_id)

Delete a Report Mailing Job

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))
body = fineract_client.DeleteReportMailingJobsRequest() # DeleteReportMailingJobsRequest | 
entity_id = 789 # int | entityId

try:
    # Delete a Report Mailing Job
    api_response = api_instance.delete_report_mailing_job(body, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->delete_report_mailing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteReportMailingJobsRequest**](DeleteReportMailingJobsRequest.md)|  | 
 **entity_id** | **int**| entityId | 

### Return type

[**DeleteReportMailingJobsResponse**](DeleteReportMailingJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_report_mailing_jobs**
> list[GetReportMailingJobsResponse] retrieve_all_report_mailing_jobs(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Report Mailing Jobs

Example Requests:  reportmailingjobs

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # List Report Mailing Jobs
    api_response = api_instance.retrieve_all_report_mailing_jobs(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->retrieve_all_report_mailing_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**list[GetReportMailingJobsResponse]**](GetReportMailingJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_report_mailing_job**
> GetReportMailingJobsResponse retrieve_report_mailing_job(entity_id)

Retrieve a Report Mailing Job

Example Requests:  reportmailingjobs/1   reportmailingjobs/1?template=true

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))
entity_id = 789 # int | entityId

try:
    # Retrieve a Report Mailing Job
    api_response = api_instance.retrieve_report_mailing_job(entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->retrieve_report_mailing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **int**| entityId | 

### Return type

[**GetReportMailingJobsResponse**](GetReportMailingJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_report_mailing_job_template**
> GetReportMailingJobsTemplate retrieve_report_mailing_job_template()

Retrieve Report Mailing Job Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for report mailing job applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  reportmailingjobs/template

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Report Mailing Job Details Template
    api_response = api_instance.retrieve_report_mailing_job_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->retrieve_report_mailing_job_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetReportMailingJobsTemplate**](GetReportMailingJobsTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_mailing_job**
> PutReportMailingJobsResponse update_report_mailing_job(body, entity_id)

Update a Report Mailing Job 

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
api_instance = fineract_client.ReportMailingJobsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutReportMailingJobsRequest() # PutReportMailingJobsRequest | 
entity_id = 789 # int | entityId

try:
    # Update a Report Mailing Job 
    api_response = api_instance.update_report_mailing_job(body, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportMailingJobsApi->update_report_mailing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutReportMailingJobsRequest**](PutReportMailingJobsRequest.md)|  | 
 **entity_id** | **int**| entityId | 

### Return type

[**PutReportMailingJobsResponse**](PutReportMailingJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

