# fineract_client.ProductsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /v1/products/{type} | Create a Share Product
[**handle_commands3**](ProductsApi.md#handle_commands3) | **POST** /v1/products/{type}/{productId} | 
[**retrieve_all_products**](ProductsApi.md#retrieve_all_products) | **GET** /v1/products/{type} | List Share Products
[**retrieve_product**](ProductsApi.md#retrieve_product) | **GET** /v1/products/{type}/{productId} | Retrieve a Share Product
[**retrieve_template13**](ProductsApi.md#retrieve_template13) | **GET** /v1/products/{type}/template | 
[**update_product**](ProductsApi.md#update_product) | **PUT** /v1/products/{type}/{productId} | Update a Share Product

# **create_product**
> PostProductsTypeResponse create_product(body, type)

Create a Share Product

Creates a Share Product  Mandatory Fields: name, shortName, description, currencyCode, digitsAfterDecimal,inMultiplesOf, locale, totalShares, unitPrice, nominalShares,allowDividendCalculationForInactiveClients,accountingRule  Mandatory Fields for Cash based accounting (accountingRule = 2): shareReferenceId, shareSuspenseId, shareEquityId, incomeFromFeeAccountId  Optional Fields: sharesIssued, minimumShares, maximumShares, minimumActivePeriodForDividends, minimumactiveperiodFrequencyType, lockinPeriodFrequency, lockinPeriodFrequencyType, marketPricePeriods, chargesSelected

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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostProductsTypeRequest() # PostProductsTypeRequest | 
type = 'type_example' # str | type

try:
    # Create a Share Product
    api_response = api_instance.create_product(body, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostProductsTypeRequest**](PostProductsTypeRequest.md)|  | 
 **type** | **str**| type | 

### Return type

[**PostProductsTypeResponse**](PostProductsTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands3**
> str handle_commands3(type, product_id, command=command)



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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
type = 'type_example' # str | type
product_id = 789 # int | productId
command = 'command_example' # str | command (optional)

try:
    api_response = api_instance.handle_commands3(type, product_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->handle_commands3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **product_id** | **int**| productId | 
 **command** | **str**| command | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_products**
> GetProductsTypeResponse retrieve_all_products(type, offset=offset, limit=limit)

List Share Products

Lists Share Products  Mandatory Fields: limit, offset  Example Requests:  shareproducts

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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
type = 'type_example' # str | type
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # List Share Products
    api_response = api_instance.retrieve_all_products(type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retrieve_all_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**GetProductsTypeResponse**](GetProductsTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_product**
> GetProductsTypeProductIdResponse retrieve_product(product_id, type)

Retrieve a Share Product

Retrieves a Share Product  Example Requests:  products/share/1   products/share/1?template=true

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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId
type = 'type_example' # str | type

try:
    # Retrieve a Share Product
    api_response = api_instance.retrieve_product(product_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retrieve_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 
 **type** | **str**| type | 

### Return type

[**GetProductsTypeProductIdResponse**](GetProductsTypeProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template13**
> str retrieve_template13(type)



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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
type = 'type_example' # str | type

try:
    api_response = api_instance.retrieve_template13(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retrieve_template13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> PutProductsTypeProductIdResponse update_product(body, type, product_id)

Update a Share Product

Updates a Share Product

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
api_instance = fineract_client.ProductsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutProductsTypeProductIdRequest() # PutProductsTypeProductIdRequest | 
type = 'type_example' # str | type
product_id = 789 # int | productId

try:
    # Update a Share Product
    api_response = api_instance.update_product(body, type, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutProductsTypeProductIdRequest**](PutProductsTypeProductIdRequest.md)|  | 
 **type** | **str**| type | 
 **product_id** | **int**| productId | 

### Return type

[**PutProductsTypeProductIdResponse**](PutProductsTypeProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

