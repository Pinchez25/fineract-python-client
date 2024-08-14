# fineract_client.SelfShareProductsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_products1**](SelfShareProductsApi.md#retrieve_all_products1) | **GET** /v1/self/products/share | 
[**retrieve_product1**](SelfShareProductsApi.md#retrieve_product1) | **GET** /v1/self/products/share/{productId} | 

# **retrieve_all_products1**
> str retrieve_all_products1(client_id=client_id, offset=offset, limit=limit)



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
api_instance = fineract_client.SelfShareProductsApi(fineract_client.ApiClient(configuration))
client_id = 789 # int |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    api_response = api_instance.retrieve_all_products1(client_id=client_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfShareProductsApi->retrieve_all_products1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_product1**
> str retrieve_product1(product_id, type, client_id=client_id)



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
api_instance = fineract_client.SelfShareProductsApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | 
type = 'type_example' # str | 
client_id = 789 # int |  (optional)

try:
    api_response = api_instance.retrieve_product1(product_id, type, client_id=client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfShareProductsApi->retrieve_product1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **type** | **str**|  | 
 **client_id** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

