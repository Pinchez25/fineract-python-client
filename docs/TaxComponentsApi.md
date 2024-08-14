# fineract_client.TaxComponentsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_compoent**](TaxComponentsApi.md#create_tax_compoent) | **POST** /v1/taxes/component | Create a new Tax Component
[**retrieve_all_tax_components**](TaxComponentsApi.md#retrieve_all_tax_components) | **GET** /v1/taxes/component | List Tax Components
[**retrieve_tax_component**](TaxComponentsApi.md#retrieve_tax_component) | **GET** /v1/taxes/component/{taxComponentId} | Retrieve Tax Component
[**retrieve_template21**](TaxComponentsApi.md#retrieve_template21) | **GET** /v1/taxes/component/template | 
[**update_tax_compoent**](TaxComponentsApi.md#update_tax_compoent) | **PUT** /v1/taxes/component/{taxComponentId} | Update Tax Component

# **create_tax_compoent**
> PostTaxesComponentsResponse create_tax_compoent(body)

Create a new Tax Component

Creates a new Tax Component  Mandatory Fields: name, percentage  Optional Fields: debitAccountType, debitAcountId, creditAccountType, creditAcountId, startDate

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
api_instance = fineract_client.TaxComponentsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTaxesComponentsRequest() # PostTaxesComponentsRequest | 

try:
    # Create a new Tax Component
    api_response = api_instance.create_tax_compoent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxComponentsApi->create_tax_compoent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTaxesComponentsRequest**](PostTaxesComponentsRequest.md)|  | 

### Return type

[**PostTaxesComponentsResponse**](PostTaxesComponentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_tax_components**
> list[GetTaxesComponentsResponse] retrieve_all_tax_components()

List Tax Components

List Tax Components

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
api_instance = fineract_client.TaxComponentsApi(fineract_client.ApiClient(configuration))

try:
    # List Tax Components
    api_response = api_instance.retrieve_all_tax_components()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxComponentsApi->retrieve_all_tax_components: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetTaxesComponentsResponse]**](GetTaxesComponentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_tax_component**
> GetTaxesComponentsResponse retrieve_tax_component(tax_component_id)

Retrieve Tax Component

Retrieve Tax Component

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
api_instance = fineract_client.TaxComponentsApi(fineract_client.ApiClient(configuration))
tax_component_id = 789 # int | taxComponentId

try:
    # Retrieve Tax Component
    api_response = api_instance.retrieve_tax_component(tax_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxComponentsApi->retrieve_tax_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_component_id** | **int**| taxComponentId | 

### Return type

[**GetTaxesComponentsResponse**](GetTaxesComponentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template21**
> str retrieve_template21()



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
api_instance = fineract_client.TaxComponentsApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_template21()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxComponentsApi->retrieve_template21: %s\n" % e)
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

# **update_tax_compoent**
> PutTaxesComponentsTaxComponentIdResponse update_tax_compoent(body, tax_component_id)

Update Tax Component

Updates Tax component. Debit and credit account details cannot be modified. All the future tax components would be replaced with the new percentage.

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
api_instance = fineract_client.TaxComponentsApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutTaxesComponentsTaxComponentIdRequest() # PutTaxesComponentsTaxComponentIdRequest | 
tax_component_id = 789 # int | taxComponentId

try:
    # Update Tax Component
    api_response = api_instance.update_tax_compoent(body, tax_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxComponentsApi->update_tax_compoent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutTaxesComponentsTaxComponentIdRequest**](PutTaxesComponentsTaxComponentIdRequest.md)|  | 
 **tax_component_id** | **int**| taxComponentId | 

### Return type

[**PutTaxesComponentsTaxComponentIdResponse**](PutTaxesComponentsTaxComponentIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

