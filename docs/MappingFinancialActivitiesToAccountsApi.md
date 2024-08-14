# fineract_client.MappingFinancialActivitiesToAccountsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gl_account**](MappingFinancialActivitiesToAccountsApi.md#create_gl_account) | **POST** /v1/financialactivityaccounts | Create a new Financial Activity to Accounts Mapping
[**delete_gl_account**](MappingFinancialActivitiesToAccountsApi.md#delete_gl_account) | **DELETE** /v1/financialactivityaccounts/{mappingId} | Delete a Financial Activity to Account Mapping
[**retreive**](MappingFinancialActivitiesToAccountsApi.md#retreive) | **GET** /v1/financialactivityaccounts/{mappingId} | Retrieve a Financial Activity to Account Mapping 
[**retrieve_all**](MappingFinancialActivitiesToAccountsApi.md#retrieve_all) | **GET** /v1/financialactivityaccounts | List Financial Activities to Accounts Mappings
[**retrieve_template**](MappingFinancialActivitiesToAccountsApi.md#retrieve_template) | **GET** /v1/financialactivityaccounts/template | 
[**update_gl_account**](MappingFinancialActivitiesToAccountsApi.md#update_gl_account) | **PUT** /v1/financialactivityaccounts/{mappingId} | Update a Financial Activity to Account Mapping

# **create_gl_account**
> PostFinancialActivityAccountsResponse create_gl_account(body=body)

Create a new Financial Activity to Accounts Mapping

Mandatory Fields financialActivityId, glAccountId

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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostFinancialActivityAccountsRequest() # PostFinancialActivityAccountsRequest |  (optional)

try:
    # Create a new Financial Activity to Accounts Mapping
    api_response = api_instance.create_gl_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->create_gl_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostFinancialActivityAccountsRequest**](PostFinancialActivityAccountsRequest.md)|  | [optional] 

### Return type

[**PostFinancialActivityAccountsResponse**](PostFinancialActivityAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gl_account**
> DeleteFinancialActivityAccountsResponse delete_gl_account(mapping_id)

Delete a Financial Activity to Account Mapping

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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))
mapping_id = 789 # int | mappingId

try:
    # Delete a Financial Activity to Account Mapping
    api_response = api_instance.delete_gl_account(mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->delete_gl_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 

### Return type

[**DeleteFinancialActivityAccountsResponse**](DeleteFinancialActivityAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retreive**
> GetFinancialActivityAccountsResponse retreive(mapping_id)

Retrieve a Financial Activity to Account Mapping 

Example Requests:  financialactivityaccounts/1

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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))
mapping_id = 789 # int | mappingId

try:
    # Retrieve a Financial Activity to Account Mapping 
    api_response = api_instance.retreive(mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->retreive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 

### Return type

[**GetFinancialActivityAccountsResponse**](GetFinancialActivityAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all**
> list[GetFinancialActivityAccountsResponse] retrieve_all()

List Financial Activities to Accounts Mappings

Example Requests:  financialactivityaccounts

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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))

try:
    # List Financial Activities to Accounts Mappings
    api_response = api_instance.retrieve_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->retrieve_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetFinancialActivityAccountsResponse]**](GetFinancialActivityAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template**
> str retrieve_template()



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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->retrieve_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gl_account**
> PutFinancialActivityAccountsResponse update_gl_account(mapping_id, body=body)

Update a Financial Activity to Account Mapping

the API updates the Ledger account linked to a Financial Activity  

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
api_instance = fineract_client.MappingFinancialActivitiesToAccountsApi(fineract_client.ApiClient(configuration))
mapping_id = 789 # int | mappingId
body = fineract_client.PostFinancialActivityAccountsRequest() # PostFinancialActivityAccountsRequest |  (optional)

try:
    # Update a Financial Activity to Account Mapping
    api_response = api_instance.update_gl_account(mapping_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingFinancialActivitiesToAccountsApi->update_gl_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| mappingId | 
 **body** | [**PostFinancialActivityAccountsRequest**](PostFinancialActivityAccountsRequest.md)|  | [optional] 

### Return type

[**PutFinancialActivityAccountsResponse**](PutFinancialActivityAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

