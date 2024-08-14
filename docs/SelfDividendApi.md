# fineract_client.SelfDividendApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dividend_detail**](SelfDividendApi.md#create_dividend_detail) | **POST** /v1/shareproduct/{productId}/dividend | 
[**delete_dividend_detail**](SelfDividendApi.md#delete_dividend_detail) | **DELETE** /v1/shareproduct/{productId}/dividend/{dividendId} | 
[**retrieve_all39**](SelfDividendApi.md#retrieve_all39) | **GET** /v1/shareproduct/{productId}/dividend | 
[**retrieve_dividend_details**](SelfDividendApi.md#retrieve_dividend_details) | **GET** /v1/shareproduct/{productId}/dividend/{dividendId} | 
[**update_dividend_detail**](SelfDividendApi.md#update_dividend_detail) | **PUT** /v1/shareproduct/{productId}/dividend/{dividendId} | 

# **create_dividend_detail**
> str create_dividend_detail(product_id, body=body)



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
api_instance = fineract_client.SelfDividendApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_dividend_detail(product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfDividendApi->create_dividend_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dividend_detail**
> str delete_dividend_detail(product_id, dividend_id)



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
api_instance = fineract_client.SelfDividendApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | 
dividend_id = 789 # int | 

try:
    api_response = api_instance.delete_dividend_detail(product_id, dividend_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfDividendApi->delete_dividend_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **dividend_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all39**
> str retrieve_all39(product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, status=status)



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
api_instance = fineract_client.SelfDividendApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
status = 56 # int |  (optional)

try:
    api_response = api_instance.retrieve_all39(product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfDividendApi->retrieve_all39: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **status** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dividend_details**
> str retrieve_dividend_details(dividend_id, product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no)



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
api_instance = fineract_client.SelfDividendApi(fineract_client.ApiClient(configuration))
dividend_id = 789 # int | 
product_id = 789 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
account_no = 'account_no_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_dividend_details(dividend_id, product_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, account_no=account_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfDividendApi->retrieve_dividend_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dividend_id** | **int**|  | 
 **product_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **account_no** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dividend_detail**
> str update_dividend_detail(product_id, dividend_id, body=body, command=command)



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
api_instance = fineract_client.SelfDividendApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | 
dividend_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.update_dividend_detail(product_id, dividend_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfDividendApi->update_dividend_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **dividend_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

