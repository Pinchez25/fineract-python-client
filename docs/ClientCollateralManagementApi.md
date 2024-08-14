# fineract_client.ClientCollateralManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_collateral**](ClientCollateralManagementApi.md#add_collateral) | **POST** /v1/clients/{clientId}/collaterals | Add New Collateral For a Client
[**delete_collateral1**](ClientCollateralManagementApi.md#delete_collateral1) | **DELETE** /v1/clients/{clientId}/collaterals/{collateralId} | Delete Client Collateral
[**get_client_collateral**](ClientCollateralManagementApi.md#get_client_collateral) | **GET** /v1/clients/{clientId}/collaterals | Get Clients Collateral Products
[**get_client_collateral_data**](ClientCollateralManagementApi.md#get_client_collateral_data) | **GET** /v1/clients/{clientId}/collaterals/{clientCollateralId} | Get Client Collateral Data
[**get_client_collateral_template**](ClientCollateralManagementApi.md#get_client_collateral_template) | **GET** /v1/clients/{clientId}/collaterals/template | Get Client Collateral Template
[**update_collateral1**](ClientCollateralManagementApi.md#update_collateral1) | **PUT** /v1/clients/{clientId}/collaterals/{collateralId} | Update New Collateral of a Client

# **add_collateral**
> PostClientCollateralResponse add_collateral(body, client_id)

Add New Collateral For a Client

Add New Collateral For a Client

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostClientCollateralRequest() # PostClientCollateralRequest | 
client_id = 789 # int | clientId

try:
    # Add New Collateral For a Client
    api_response = api_instance.add_collateral(body, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->add_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostClientCollateralRequest**](PostClientCollateralRequest.md)|  | 
 **client_id** | **int**| clientId | 

### Return type

[**PostClientCollateralResponse**](PostClientCollateralResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collateral1**
> DeleteClientCollateralResponse delete_collateral1(client_id, collateral_id)

Delete Client Collateral

Delete Client Collateral

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
collateral_id = 789 # int | collateralId

try:
    # Delete Client Collateral
    api_response = api_instance.delete_collateral1(client_id, collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->delete_collateral1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**DeleteClientCollateralResponse**](DeleteClientCollateralResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_collateral**
> list[GetClientCollateralManagementsResponse] get_client_collateral(client_id, prod_id=prod_id)

Get Clients Collateral Products

Get Collateral Product of a Client

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
prod_id = 789 # int | prodId (optional)

try:
    # Get Clients Collateral Products
    api_response = api_instance.get_client_collateral(client_id, prod_id=prod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->get_client_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **prod_id** | **int**| prodId | [optional] 

### Return type

[**list[GetClientCollateralManagementsResponse]**](GetClientCollateralManagementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_collateral_data**
> GetClientCollateralManagementsResponse get_client_collateral_data(client_id, client_collateral_id)

Get Client Collateral Data

Get Client Collateral Data

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
client_collateral_id = 789 # int | clientCollateralId

try:
    # Get Client Collateral Data
    api_response = api_instance.get_client_collateral_data(client_id, client_collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->get_client_collateral_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **client_collateral_id** | **int**| clientCollateralId | 

### Return type

[**GetClientCollateralManagementsResponse**](GetClientCollateralManagementsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_collateral_template**
> list[GetLoanCollateralManagementTemplate] get_client_collateral_template(client_id)

Get Client Collateral Template

Get Client Collateral Template

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId

try:
    # Get Client Collateral Template
    api_response = api_instance.get_client_collateral_template(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->get_client_collateral_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

[**list[GetLoanCollateralManagementTemplate]**](GetLoanCollateralManagementTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collateral1**
> PutClientCollateralResponse update_collateral1(body, client_id, collateral_id)

Update New Collateral of a Client

Update New Collateral of a Client

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
api_instance = fineract_client.ClientCollateralManagementApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutClientCollateralRequest() # PutClientCollateralRequest | 
client_id = 789 # int | clientId
collateral_id = 789 # int | collateralId

try:
    # Update New Collateral of a Client
    api_response = api_instance.update_collateral1(body, client_id, collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientCollateralManagementApi->update_collateral1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutClientCollateralRequest**](PutClientCollateralRequest.md)|  | 
 **client_id** | **int**| clientId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**PutClientCollateralResponse**](PutClientCollateralResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

