# fineract_client.BatchAPIApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_batch_requests**](BatchAPIApi.md#handle_batch_requests) | **POST** /v1/batches | Batch requests in a single transaction

# **handle_batch_requests**
> list[BatchResponse] handle_batch_requests(body, enclosing_transaction=enclosing_transaction)

Batch requests in a single transaction

The Apache Fineract Batch API is also capable of executing all the requests in a single transaction, by setting a Query Parameter, \"enclosingTransaction=true\". So, if one or more of the requests in a batch returns an erroneous response all of the Data base transactions made by other successful requests will be rolled back.  If there has been a rollback in a transaction then a single response will be provided, with a '400' status code and a body consisting of the error details of the first failed request.

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
api_instance = fineract_client.BatchAPIApi(fineract_client.ApiClient(configuration))
body = [fineract_client.BatchRequest()] # list[BatchRequest] | 
enclosing_transaction = false # bool | enclosingTransaction (optional) (default to false)

try:
    # Batch requests in a single transaction
    api_response = api_instance.handle_batch_requests(body, enclosing_transaction=enclosing_transaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchAPIApi->handle_batch_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BatchRequest]**](BatchRequest.md)|  | 
 **enclosing_transaction** | **bool**| enclosingTransaction | [optional] [default to false]

### Return type

[**list[BatchResponse]**](BatchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

