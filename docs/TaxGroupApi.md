# fineract_client.TaxGroupApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_group**](TaxGroupApi.md#create_tax_group) | **POST** /v1/taxes/group | Create a new Tax Group
[**retrieve_all_tax_groups**](TaxGroupApi.md#retrieve_all_tax_groups) | **GET** /v1/taxes/group | List Tax Group
[**retrieve_tax_group**](TaxGroupApi.md#retrieve_tax_group) | **GET** /v1/taxes/group/{taxGroupId} | Retrieve Tax Group
[**retrieve_template22**](TaxGroupApi.md#retrieve_template22) | **GET** /v1/taxes/group/template | 
[**update_tax_group**](TaxGroupApi.md#update_tax_group) | **PUT** /v1/taxes/group/{taxGroupId} | Update Tax Group

# **create_tax_group**
> PostTaxesGroupResponse create_tax_group(body)

Create a new Tax Group

Create a new Tax Group Mandatory Fields: name and taxComponents Mandatory Fields in taxComponents: taxComponentId Optional Fields in taxComponents: id, startDate and endDate

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
api_instance = fineract_client.TaxGroupApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostTaxesGroupRequest() # PostTaxesGroupRequest | 

try:
    # Create a new Tax Group
    api_response = api_instance.create_tax_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxGroupApi->create_tax_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTaxesGroupRequest**](PostTaxesGroupRequest.md)|  | 

### Return type

[**PostTaxesGroupResponse**](PostTaxesGroupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_tax_groups**
> list[GetTaxesGroupResponse] retrieve_all_tax_groups()

List Tax Group

List Tax Group

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
api_instance = fineract_client.TaxGroupApi(fineract_client.ApiClient(configuration))

try:
    # List Tax Group
    api_response = api_instance.retrieve_all_tax_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxGroupApi->retrieve_all_tax_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetTaxesGroupResponse]**](GetTaxesGroupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_tax_group**
> GetTaxesGroupResponse retrieve_tax_group(tax_group_id)

Retrieve Tax Group

Retrieve Tax Group

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
api_instance = fineract_client.TaxGroupApi(fineract_client.ApiClient(configuration))
tax_group_id = 789 # int | taxGroupId

try:
    # Retrieve Tax Group
    api_response = api_instance.retrieve_tax_group(tax_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxGroupApi->retrieve_tax_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_group_id** | **int**| taxGroupId | 

### Return type

[**GetTaxesGroupResponse**](GetTaxesGroupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template22**
> str retrieve_template22()



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
api_instance = fineract_client.TaxGroupApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_template22()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxGroupApi->retrieve_template22: %s\n" % e)
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

# **update_tax_group**
> PutTaxesGroupTaxGroupIdResponse update_tax_group(body, tax_group_id)

Update Tax Group

Updates Tax Group. Only end date can be up-datable and can insert new tax components.

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
api_instance = fineract_client.TaxGroupApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutTaxesGroupTaxGroupIdRequest() # PutTaxesGroupTaxGroupIdRequest | 
tax_group_id = 789 # int | taxGroupId

try:
    # Update Tax Group
    api_response = api_instance.update_tax_group(body, tax_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxGroupApi->update_tax_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutTaxesGroupTaxGroupIdRequest**](PutTaxesGroupTaxGroupIdRequest.md)|  | 
 **tax_group_id** | **int**| taxGroupId | 

### Return type

[**PutTaxesGroupTaxGroupIdResponse**](PutTaxesGroupTaxGroupIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

