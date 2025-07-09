# fineract_client.SCHEDULERJOBApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_job**](SCHEDULERJOBApi.md#execute_job) | **POST** /v1/jobs/{jobId} | Run a Job
[**retrieve_all8**](SCHEDULERJOBApi.md#retrieve_all8) | **GET** /v1/jobs | Retrieve Scheduler Jobs
[**retrieve_history**](SCHEDULERJOBApi.md#retrieve_history) | **GET** /v1/jobs/{jobId}/runhistory | Retrieve Job Run History
[**retrieve_one5**](SCHEDULERJOBApi.md#retrieve_one5) | **GET** /v1/jobs/{jobId} | Retrieve a Job
[**update_job_detail**](SCHEDULERJOBApi.md#update_job_detail) | **PUT** /v1/jobs/{jobId} | Update a Job


# **execute_job**
> execute_job(job_id, command=command, execute_job_request=execute_job_request)

Run a Job

Manually Execute Specific Job.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.execute_job_request import ExecuteJobRequest
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
    api_instance = fineract_client.SCHEDULERJOBApi(api_client)
    job_id = 56 # int | jobId
    command = 'command_example' # str | command (optional)
    execute_job_request = fineract_client.ExecuteJobRequest() # ExecuteJobRequest |  (optional)

    try:
        # Run a Job
        api_instance.execute_job(job_id, command=command, execute_job_request=execute_job_request)
    except Exception as e:
        print("Exception when calling SCHEDULERJOBApi->execute_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| jobId | 
 **command** | **str**| command | [optional] 
 **execute_job_request** | [**ExecuteJobRequest**](ExecuteJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POST: jobs/1?command&#x3D;executeJob |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all8**
> List[GetJobsResponse] retrieve_all8()

Retrieve Scheduler Jobs

Returns the list of jobs.  Example Requests:  jobs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_jobs_response import GetJobsResponse
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
    api_instance = fineract_client.SCHEDULERJOBApi(api_client)

    try:
        # Retrieve Scheduler Jobs
        api_response = api_instance.retrieve_all8()
        print("The response of SCHEDULERJOBApi->retrieve_all8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCHEDULERJOBApi->retrieve_all8: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetJobsResponse]**](GetJobsResponse.md)

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

# **retrieve_history**
> GetJobsJobIDJobRunHistoryResponse retrieve_history(job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Retrieve Job Run History

Example Requests:  jobs/5/runhistory?offset=0&limit=200

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_jobs_job_id_job_run_history_response import GetJobsJobIDJobRunHistoryResponse
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
    api_instance = fineract_client.SCHEDULERJOBApi(api_client)
    job_id = 56 # int | jobId
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # Retrieve Job Run History
        api_response = api_instance.retrieve_history(job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of SCHEDULERJOBApi->retrieve_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCHEDULERJOBApi->retrieve_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| jobId | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetJobsJobIDJobRunHistoryResponse**](GetJobsJobIDJobRunHistoryResponse.md)

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

# **retrieve_one5**
> GetJobsResponse retrieve_one5(job_id)

Retrieve a Job

Returns the details of a Job.  Example Requests:  jobs/5

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_jobs_response import GetJobsResponse
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
    api_instance = fineract_client.SCHEDULERJOBApi(api_client)
    job_id = 56 # int | jobId

    try:
        # Retrieve a Job
        api_response = api_instance.retrieve_one5(job_id)
        print("The response of SCHEDULERJOBApi->retrieve_one5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCHEDULERJOBApi->retrieve_one5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| jobId | 

### Return type

[**GetJobsResponse**](GetJobsResponse.md)

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

# **update_job_detail**
> update_job_detail(job_id, put_jobs_job_id_request)

Update a Job

Updates the details of a job.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_jobs_job_id_request import PutJobsJobIDRequest
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
    api_instance = fineract_client.SCHEDULERJOBApi(api_client)
    job_id = 56 # int | jobId
    put_jobs_job_id_request = fineract_client.PutJobsJobIDRequest() # PutJobsJobIDRequest | 

    try:
        # Update a Job
        api_instance.update_job_detail(job_id, put_jobs_job_id_request)
    except Exception as e:
        print("Exception when calling SCHEDULERJOBApi->update_job_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| jobId | 
 **put_jobs_job_id_request** | [**PutJobsJobIDRequest**](PutJobsJobIDRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

