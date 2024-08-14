# fineract_client.BusinessStepConfigurationApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_available_business_step**](BusinessStepConfigurationApi.md#retrieve_all_available_business_step) | **GET** /v1/jobs/{jobName}/available-steps | List Business Step Configurations for a Job
[**retrieve_all_configured_business_jobs**](BusinessStepConfigurationApi.md#retrieve_all_configured_business_jobs) | **GET** /v1/jobs/names | List Business Jobs
[**retrieve_all_configured_business_step**](BusinessStepConfigurationApi.md#retrieve_all_configured_business_step) | **GET** /v1/jobs/{jobName}/steps | List Business Step Configurations for a Job
[**update_job_business_step_config**](BusinessStepConfigurationApi.md#update_job_business_step_config) | **PUT** /v1/jobs/{jobName}/steps | List Business Step Configurations for a Job

# **retrieve_all_available_business_step**
> GetBusinessStepConfigResponse retrieve_all_available_business_step(job_name)

List Business Step Configurations for a Job

Returns the available Business Steps for a job

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
api_instance = fineract_client.BusinessStepConfigurationApi(fineract_client.ApiClient(configuration))
job_name = 'job_name_example' # str | jobName

try:
    # List Business Step Configurations for a Job
    api_response = api_instance.retrieve_all_available_business_step(job_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessStepConfigurationApi->retrieve_all_available_business_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| jobName | 

### Return type

[**GetBusinessStepConfigResponse**](GetBusinessStepConfigResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_configured_business_jobs**
> GetBusinessJobConfigResponse retrieve_all_configured_business_jobs()

List Business Jobs

Returns the configured Business Jobs

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
api_instance = fineract_client.BusinessStepConfigurationApi(fineract_client.ApiClient(configuration))

try:
    # List Business Jobs
    api_response = api_instance.retrieve_all_configured_business_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessStepConfigurationApi->retrieve_all_configured_business_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBusinessJobConfigResponse**](GetBusinessJobConfigResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_configured_business_step**
> GetBusinessStepConfigResponse retrieve_all_configured_business_step(job_name)

List Business Step Configurations for a Job

Returns the configured Business Steps for a job

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
api_instance = fineract_client.BusinessStepConfigurationApi(fineract_client.ApiClient(configuration))
job_name = 'job_name_example' # str | jobName

try:
    # List Business Step Configurations for a Job
    api_response = api_instance.retrieve_all_configured_business_step(job_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessStepConfigurationApi->retrieve_all_configured_business_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| jobName | 

### Return type

[**GetBusinessStepConfigResponse**](GetBusinessStepConfigResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_business_step_config**
> update_job_business_step_config(job_name, body=body)

List Business Step Configurations for a Job

Updates the Business steps execution order for a job

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
api_instance = fineract_client.BusinessStepConfigurationApi(fineract_client.ApiClient(configuration))
job_name = 'job_name_example' # str | jobName
body = fineract_client.UpdateBusinessStepConfigRequest() # UpdateBusinessStepConfigRequest |  (optional)

try:
    # List Business Step Configurations for a Job
    api_instance.update_job_business_step_config(job_name, body=body)
except ApiException as e:
    print("Exception when calling BusinessStepConfigurationApi->update_job_business_step_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| jobName | 
 **body** | [**UpdateBusinessStepConfigRequest**](UpdateBusinessStepConfigRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

