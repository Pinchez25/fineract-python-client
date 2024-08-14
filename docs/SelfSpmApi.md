# fineract_client.SelfSpmApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_all_surveys**](SelfSpmApi.md#fetch_all_surveys) | **GET** /v1/self/surveys | 

# **fetch_all_surveys**
> list[SurveyData] fetch_all_surveys()



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
api_instance = fineract_client.SelfSpmApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.fetch_all_surveys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSpmApi->fetch_all_surveys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SurveyData]**](SurveyData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

