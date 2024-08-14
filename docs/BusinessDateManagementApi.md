# fineract_client.BusinessDateManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_date**](BusinessDateManagementApi.md#get_business_date) | **GET** /v1/businessdate/{type} | Retrieve a specific Business date
[**get_business_dates**](BusinessDateManagementApi.md#get_business_dates) | **GET** /v1/businessdate | List all business dates
[**update_business_date**](BusinessDateManagementApi.md#update_business_date) | **POST** /v1/businessdate | Update Business Date

# **get_business_date**
> BusinessDateResponse get_business_date(type)

Retrieve a specific Business date

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
api_instance = fineract_client.BusinessDateManagementApi(fineract_client.ApiClient(configuration))
type = 'type_example' # str | type

try:
    # Retrieve a specific Business date
    api_response = api_instance.get_business_date(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessDateManagementApi->get_business_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

[**BusinessDateResponse**](BusinessDateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_dates**
> list[BusinessDateResponse] get_business_dates()

List all business dates

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
api_instance = fineract_client.BusinessDateManagementApi(fineract_client.ApiClient(configuration))

try:
    # List all business dates
    api_response = api_instance.get_business_dates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessDateManagementApi->get_business_dates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BusinessDateResponse]**](BusinessDateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_date**
> BusinessDateResponse update_business_date(body)

Update Business Date

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
api_instance = fineract_client.BusinessDateManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.BusinessDateRequest() # BusinessDateRequest | 

try:
    # Update Business Date
    api_response = api_instance.update_business_date(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessDateManagementApi->update_business_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BusinessDateRequest**](BusinessDateRequest.md)|  | 

### Return type

[**BusinessDateResponse**](BusinessDateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

