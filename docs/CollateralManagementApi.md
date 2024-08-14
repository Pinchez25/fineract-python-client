# fineract_client.CollateralManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collateral1**](CollateralManagementApi.md#create_collateral1) | **POST** /v1/collateral-management | Create a new collateral
[**delete_collateral2**](CollateralManagementApi.md#delete_collateral2) | **DELETE** /v1/collateral-management/{collateralId} | Delete a Collateral
[**get_all_collaterals**](CollateralManagementApi.md#get_all_collaterals) | **GET** /v1/collateral-management | Get All Collaterals
[**get_collateral**](CollateralManagementApi.md#get_collateral) | **GET** /v1/collateral-management/{collateralId} | Get Collateral
[**get_collateral_template**](CollateralManagementApi.md#get_collateral_template) | **GET** /v1/collateral-management/template | Get Collateral Template
[**update_collateral2**](CollateralManagementApi.md#update_collateral2) | **PUT** /v1/collateral-management/{collateralId} | Update Collateral

# **create_collateral1**
> PostCollateralManagementProductResponse create_collateral1(body)

Create a new collateral

Collateral Creation

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostCollateralManagementProductRequest() # PostCollateralManagementProductRequest | 

try:
    # Create a new collateral
    api_response = api_instance.create_collateral1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->create_collateral1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCollateralManagementProductRequest**](PostCollateralManagementProductRequest.md)|  | 

### Return type

[**PostCollateralManagementProductResponse**](PostCollateralManagementProductResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collateral2**
> DeleteCollateralProductResponse delete_collateral2(collateral_id)

Delete a Collateral

Delete Collateral

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))
collateral_id = 789 # int | collateralId

try:
    # Delete a Collateral
    api_response = api_instance.delete_collateral2(collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->delete_collateral2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 

### Return type

[**DeleteCollateralProductResponse**](DeleteCollateralProductResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_collaterals**
> list[GetCollateralManagementsResponse] get_all_collaterals()

Get All Collaterals

Fetch all Collateral Products

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))

try:
    # Get All Collaterals
    api_response = api_instance.get_all_collaterals()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->get_all_collaterals: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetCollateralManagementsResponse]**](GetCollateralManagementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collateral**
> GetCollateralManagementsResponse get_collateral(collateral_id)

Get Collateral

Fetch Collateral

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))
collateral_id = 789 # int | collateralId

try:
    # Get Collateral
    api_response = api_instance.get_collateral(collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->get_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 

### Return type

[**GetCollateralManagementsResponse**](GetCollateralManagementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collateral_template**
> list[GetCollateralProductTemplate] get_collateral_template()

Get Collateral Template

Get Collateral Template

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))

try:
    # Get Collateral Template
    api_response = api_instance.get_collateral_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->get_collateral_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetCollateralProductTemplate]**](GetCollateralProductTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collateral2**
> PutCollateralProductResponse update_collateral2(body, collateral_id)

Update Collateral

Update Collateral

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
api_instance = fineract_client.CollateralManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutCollateralProductRequest() # PutCollateralProductRequest | 
collateral_id = 789 # int | collateralId

try:
    # Update Collateral
    api_response = api_instance.update_collateral2(body, collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollateralManagementApi->update_collateral2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCollateralProductRequest**](PutCollateralProductRequest.md)|  | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**PutCollateralProductResponse**](PutCollateralProductResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

