# fineract_client.InlineJobApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_inline_job**](InlineJobApi.md#execute_inline_job) | **POST** /v1/jobs/{jobName}/inline | Starts an inline Job

# **execute_inline_job**
> InlineJobResponse execute_inline_job(job_name, body=body)

Starts an inline Job

Starts an inline Job

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
api_instance = fineract_client.InlineJobApi(fineract_client.ApiClient(configuration))
job_name = 'job_name_example' # str | jobName
body = fineract_client.InlineJobRequest() # InlineJobRequest |  (optional)

try:
    # Starts an inline Job
    api_response = api_instance.execute_inline_job(job_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineJobApi->execute_inline_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| jobName | 
 **body** | [**InlineJobRequest**](InlineJobRequest.md)|  | [optional] 

### Return type

[**InlineJobResponse**](InlineJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

