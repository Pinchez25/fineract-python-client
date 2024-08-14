# fineract_client.EntityDataTableApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_datatable_check**](EntityDataTableApi.md#create_entity_datatable_check) | **POST** /v1/entityDatatableChecks | Create Entity-Datatable Checks
[**delete_datatable1**](EntityDataTableApi.md#delete_datatable1) | **DELETE** /v1/entityDatatableChecks/{entityDatatableCheckId} | Delete Entity-Datatable Checks
[**get_template**](EntityDataTableApi.md#get_template) | **GET** /v1/entityDatatableChecks/template | Retrieve Entity-Datatable Checks Template
[**retrieve_all6**](EntityDataTableApi.md#retrieve_all6) | **GET** /v1/entityDatatableChecks | List Entity-Datatable Checks

# **create_entity_datatable_check**
> PostEntityDatatableChecksTemplateResponse create_entity_datatable_check(body)

Create Entity-Datatable Checks

Mandatory Fields :  entity, status, datatableName  Non-Mandatory Fields :  productId

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
api_instance = fineract_client.EntityDataTableApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostEntityDatatableChecksTemplateRequest() # PostEntityDatatableChecksTemplateRequest | 

try:
    # Create Entity-Datatable Checks
    api_response = api_instance.create_entity_datatable_check(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityDataTableApi->create_entity_datatable_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostEntityDatatableChecksTemplateRequest**](PostEntityDatatableChecksTemplateRequest.md)|  | 

### Return type

[**PostEntityDatatableChecksTemplateResponse**](PostEntityDatatableChecksTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datatable1**
> DeleteEntityDatatableChecksTemplateResponse delete_datatable1(entity_datatable_check_id, body=body)

Delete Entity-Datatable Checks

Deletes an existing Entity-Datatable Check

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
api_instance = fineract_client.EntityDataTableApi(fineract_client.ApiClient(configuration))
entity_datatable_check_id = 789 # int | entityDatatableCheckId
body = 'body_example' # str |  (optional)

try:
    # Delete Entity-Datatable Checks
    api_response = api_instance.delete_datatable1(entity_datatable_check_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityDataTableApi->delete_datatable1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_datatable_check_id** | **int**| entityDatatableCheckId | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

[**DeleteEntityDatatableChecksTemplateResponse**](DeleteEntityDatatableChecksTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> GetEntityDatatableChecksTemplateResponse get_template()

Retrieve Entity-Datatable Checks Template

This is a convenience resource useful for building maintenance user interface screens for Entity-Datatable Checks applications. The template data returned consists of:  Allowed description Lists Example Request:  entityDatatableChecks/template

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
api_instance = fineract_client.EntityDataTableApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Entity-Datatable Checks Template
    api_response = api_instance.get_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityDataTableApi->get_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEntityDatatableChecksTemplateResponse**](GetEntityDatatableChecksTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all6**
> list[GetEntityDatatableChecksResponse] retrieve_all6(status=status, entity=entity, product_id=product_id, offset=offset, limit=limit)

List Entity-Datatable Checks

The list capability of Entity-Datatable Checks can support pagination.  OPTIONAL ARGUMENTS offset Integer optional, defaults to 0 Indicates the result from which pagination startslimit Integer optional, defaults to 200 Restricts the size of results returned. To override the default and return all entries you must explicitly pass a non-positive integer value for limit e.g. limit=0, or limit=-1 Example Request:  entityDatatableChecks?offset=0&limit=15

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
api_instance = fineract_client.EntityDataTableApi(fineract_client.ApiClient(configuration))
status = 56 # int | status (optional)
entity = 'entity_example' # str | entity (optional)
product_id = 789 # int | productId (optional)
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # List Entity-Datatable Checks
    api_response = api_instance.retrieve_all6(status=status, entity=entity, product_id=product_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityDataTableApi->retrieve_all6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| status | [optional] 
 **entity** | **str**| entity | [optional] 
 **product_id** | **int**| productId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**list[GetEntityDatatableChecksResponse]**](GetEntityDatatableChecksResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

