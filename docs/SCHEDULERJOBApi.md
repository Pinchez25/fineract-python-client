# fineract_client.SCHEDULERJOBApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_job**](SCHEDULERJOBApi.md#execute_job) | **POST** /v1/jobs/{jobId} | Run a Job
[**retrieve_all8**](SCHEDULERJOBApi.md#retrieve_all8) | **GET** /v1/jobs | Retrieve Scheduler Jobs
[**retrieve_history**](SCHEDULERJOBApi.md#retrieve_history) | **GET** /v1/jobs/{jobId}/runhistory | Retrieve Job Run History
[**retrieve_one5**](SCHEDULERJOBApi.md#retrieve_one5) | **GET** /v1/jobs/{jobId} | Retrieve a Job
[**update_job_detail**](SCHEDULERJOBApi.md#update_job_detail) | **PUT** /v1/jobs/{jobId} | Update a Job

# **execute_job**
> execute_job(job_id, body=body, command=command)

Run a Job

Manually Execute Specific Job.

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
api_instance = fineract_client.SCHEDULERJOBApi(fineract_client.ApiClient(configuration))
job_id = 789 # int | jobId
body = fineract_client.ExecuteJobRequest() # ExecuteJobRequest |  (optional)
command = 'command_example' # str | command (optional)

try:
    # Run a Job
    api_instance.execute_job(job_id, body=body, command=command)
except ApiException as e:
    print("Exception when calling SCHEDULERJOBApi->execute_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| jobId | 
 **body** | [**ExecuteJobRequest**](ExecuteJobRequest.md)|  | [optional] 
 **command** | **str**| command | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all8**
> list[GetJobsResponse] retrieve_all8()

Retrieve Scheduler Jobs

Returns the list of jobs.  Example Requests:  jobs

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
api_instance = fineract_client.SCHEDULERJOBApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Scheduler Jobs
    api_response = api_instance.retrieve_all8()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCHEDULERJOBApi->retrieve_all8: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetJobsResponse]**](GetJobsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_history**
> GetJobsJobIDJobRunHistoryResponse retrieve_history(job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Retrieve Job Run History

Example Requests:  jobs/5/runhistory?offset=0&limit=200

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
api_instance = fineract_client.SCHEDULERJOBApi(fineract_client.ApiClient(configuration))
job_id = 789 # int | jobId
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # Retrieve Job Run History
    api_response = api_instance.retrieve_history(job_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one5**
> GetJobsResponse retrieve_one5(job_id)

Retrieve a Job

Returns the details of a Job.  Example Requests:  jobs/5

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
api_instance = fineract_client.SCHEDULERJOBApi(fineract_client.ApiClient(configuration))
job_id = 789 # int | jobId

try:
    # Retrieve a Job
    api_response = api_instance.retrieve_one5(job_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_detail**
> update_job_detail(body, job_id)

Update a Job

Updates the details of a job.

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
api_instance = fineract_client.SCHEDULERJOBApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutJobsJobIDRequest() # PutJobsJobIDRequest | 
job_id = 789 # int | jobId

try:
    # Update a Job
    api_instance.update_job_detail(body, job_id)
except ApiException as e:
    print("Exception when calling SCHEDULERJOBApi->update_job_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutJobsJobIDRequest**](PutJobsJobIDRequest.md)|  | 
 **job_id** | **int**| jobId | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

