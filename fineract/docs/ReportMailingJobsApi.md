# fineract_client.ReportMailingJobsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_mailing_job**](ReportMailingJobsApi.md#create_report_mailing_job) | **POST** /v1/reportmailingjobs | Create a Report Mailing Job
[**delete_report_mailing_job**](ReportMailingJobsApi.md#delete_report_mailing_job) | **DELETE** /v1/reportmailingjobs/{entityId} | Delete a Report Mailing Job
[**retrieve_all_report_mailing_jobs**](ReportMailingJobsApi.md#retrieve_all_report_mailing_jobs) | **GET** /v1/reportmailingjobs | List Report Mailing Jobs
[**retrieve_report_mailing_job**](ReportMailingJobsApi.md#retrieve_report_mailing_job) | **GET** /v1/reportmailingjobs/{entityId} | Retrieve a Report Mailing Job
[**retrieve_report_mailing_job_template**](ReportMailingJobsApi.md#retrieve_report_mailing_job_template) | **GET** /v1/reportmailingjobs/template | Retrieve Report Mailing Job Details Template
[**update_report_mailing_job**](ReportMailingJobsApi.md#update_report_mailing_job) | **PUT** /v1/reportmailingjobs/{entityId} | Update a Report Mailing Job 


# **create_report_mailing_job**
> PostReportMailingJobsResponse create_report_mailing_job(post_report_mailing_jobs_request)

Create a Report Mailing Job

Mandatory Fields: name, startDateTime, stretchyReportId, emailRecipients, emailSubject, emailMessage, emailAttachmentFileFormatId, recurrence, isActive  Optional Fields: description, stretchyReportParamMap

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_report_mailing_jobs_request import PostReportMailingJobsRequest
from fineract_client.models.post_report_mailing_jobs_response import PostReportMailingJobsResponse
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)
    post_report_mailing_jobs_request = fineract_client.PostReportMailingJobsRequest() # PostReportMailingJobsRequest | 

    try:
        # Create a Report Mailing Job
        api_response = api_instance.create_report_mailing_job(post_report_mailing_jobs_request)
        print("The response of ReportMailingJobsApi->create_report_mailing_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportMailingJobsApi->create_report_mailing_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_report_mailing_jobs_request** | [**PostReportMailingJobsRequest**](PostReportMailingJobsRequest.md)|  | 

### Return type

[**PostReportMailingJobsResponse**](PostReportMailingJobsResponse.md)

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

# **delete_report_mailing_job**
> DeleteReportMailingJobsResponse delete_report_mailing_job(entity_id, body)

Delete a Report Mailing Job

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_report_mailing_jobs_response import DeleteReportMailingJobsResponse
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)
    entity_id = 56 # int | entityId
    body = None # object | 

    try:
        # Delete a Report Mailing Job
        api_response = api_instance.delete_report_mailing_job(entity_id, body)
        print("The response of ReportMailingJobsApi->delete_report_mailing_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportMailingJobsApi->delete_report_mailing_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **int**| entityId | 
 **body** | **object**|  | 

### Return type

[**DeleteReportMailingJobsResponse**](DeleteReportMailingJobsResponse.md)

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

# **retrieve_all_report_mailing_jobs**
> List[GetReportMailingJobsResponse] retrieve_all_report_mailing_jobs(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List Report Mailing Jobs

Example Requests:  reportmailingjobs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_report_mailing_jobs_response import GetReportMailingJobsResponse
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # List Report Mailing Jobs
        api_response = api_instance.retrieve_all_report_mailing_jobs(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of ReportMailingJobsApi->retrieve_all_report_mailing_jobs:\n")
        pprint(api_response)
    except Exception as e:
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

[**List[GetReportMailingJobsResponse]**](GetReportMailingJobsResponse.md)

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

# **retrieve_report_mailing_job**
> GetReportMailingJobsResponse retrieve_report_mailing_job(entity_id)

Retrieve a Report Mailing Job

Example Requests:  reportmailingjobs/1   reportmailingjobs/1?template=true

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_report_mailing_jobs_response import GetReportMailingJobsResponse
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)
    entity_id = 56 # int | entityId

    try:
        # Retrieve a Report Mailing Job
        api_response = api_instance.retrieve_report_mailing_job(entity_id)
        print("The response of ReportMailingJobsApi->retrieve_report_mailing_job:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_report_mailing_job_template**
> GetReportMailingJobsTemplate retrieve_report_mailing_job_template()

Retrieve Report Mailing Job Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for report mailing job applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  reportmailingjobs/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_report_mailing_jobs_template import GetReportMailingJobsTemplate
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)

    try:
        # Retrieve Report Mailing Job Details Template
        api_response = api_instance.retrieve_report_mailing_job_template()
        print("The response of ReportMailingJobsApi->retrieve_report_mailing_job_template:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_mailing_job**
> PutReportMailingJobsResponse update_report_mailing_job(entity_id, put_report_mailing_jobs_request)

Update a Report Mailing Job 

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_report_mailing_jobs_request import PutReportMailingJobsRequest
from fineract_client.models.put_report_mailing_jobs_response import PutReportMailingJobsResponse
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
    api_instance = fineract_client.ReportMailingJobsApi(api_client)
    entity_id = 56 # int | entityId
    put_report_mailing_jobs_request = fineract_client.PutReportMailingJobsRequest() # PutReportMailingJobsRequest | 

    try:
        # Update a Report Mailing Job 
        api_response = api_instance.update_report_mailing_job(entity_id, put_report_mailing_jobs_request)
        print("The response of ReportMailingJobsApi->update_report_mailing_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportMailingJobsApi->update_report_mailing_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **int**| entityId | 
 **put_report_mailing_jobs_request** | [**PutReportMailingJobsRequest**](PutReportMailingJobsRequest.md)|  | 

### Return type

[**PutReportMailingJobsResponse**](PutReportMailingJobsResponse.md)

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

