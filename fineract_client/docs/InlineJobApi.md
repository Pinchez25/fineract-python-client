# fineract_client.InlineJobApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_inline_job**](InlineJobApi.md#execute_inline_job) | **POST** /v1/jobs/{jobName}/inline | Starts an inline Job


# **execute_inline_job**
> InlineJobResponse execute_inline_job(job_name, inline_job_request=inline_job_request)

Starts an inline Job

Starts an inline Job

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.inline_job_request import InlineJobRequest
from fineract_client.models.inline_job_response import InlineJobResponse
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
    api_instance = fineract_client.InlineJobApi(api_client)
    job_name = 'job_name_example' # str | jobName
    inline_job_request = fineract_client.InlineJobRequest() # InlineJobRequest |  (optional)

    try:
        # Starts an inline Job
        api_response = api_instance.execute_inline_job(job_name, inline_job_request=inline_job_request)
        print("The response of InlineJobApi->execute_inline_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineJobApi->execute_inline_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| jobName | 
 **inline_job_request** | [**InlineJobRequest**](InlineJobRequest.md)|  | [optional] 

### Return type

[**InlineJobResponse**](InlineJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Request body item size validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

