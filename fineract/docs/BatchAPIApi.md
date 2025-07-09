# fineract_client.BatchAPIApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_batch_requests**](BatchAPIApi.md#handle_batch_requests) | **POST** /v1/batches | Batch requests in a single transaction


# **handle_batch_requests**
> List[BatchResponse] handle_batch_requests(batch_request, enclosing_transaction=enclosing_transaction)

Batch requests in a single transaction

The Apache Fineract Batch API is also capable of executing all the requests in a single transaction, by setting a Query Parameter, "enclosingTransaction=true". So, if one or more of the requests in a batch returns an erroneous response all of the Data base transactions made by other successful requests will be rolled back.

If there has been a rollback in a transaction then a single response will be provided, with a '400' status code and a body consisting of the error details of the first failed request.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.batch_request import BatchRequest
from fineract_client.models.batch_response import BatchResponse
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
    api_instance = fineract_client.BatchAPIApi(api_client)
    batch_request = [fineract_client.BatchRequest()] # List[BatchRequest] | 
    enclosing_transaction = False # bool | enclosingTransaction (optional) (default to False)

    try:
        # Batch requests in a single transaction
        api_response = api_instance.handle_batch_requests(batch_request, enclosing_transaction=enclosing_transaction)
        print("The response of BatchAPIApi->handle_batch_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchAPIApi->handle_batch_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request** | [**List[BatchRequest]**](BatchRequest.md)|  | 
 **enclosing_transaction** | **bool**| enclosingTransaction | [optional] [default to False]

### Return type

[**List[BatchResponse]**](BatchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

