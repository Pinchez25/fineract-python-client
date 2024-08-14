# fineract_client.OfficesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_office**](OfficesApi.md#create_office) | **POST** /v1/offices | Create an Office
[**get_office_template**](OfficesApi.md#get_office_template) | **GET** /v1/offices/downloadtemplate | 
[**post_office_template**](OfficesApi.md#post_office_template) | **POST** /v1/offices/uploadtemplate | 
[**retrieve_office**](OfficesApi.md#retrieve_office) | **GET** /v1/offices/{officeId} | Retrieve an Office
[**retrieve_office_by_external_id**](OfficesApi.md#retrieve_office_by_external_id) | **GET** /v1/offices/external-id/{externalId} | Retrieve an Office using external id
[**retrieve_office_template1**](OfficesApi.md#retrieve_office_template1) | **GET** /v1/offices/template | Retrieve Office Details Template
[**retrieve_offices**](OfficesApi.md#retrieve_offices) | **GET** /v1/offices | List Offices
[**update_office**](OfficesApi.md#update_office) | **PUT** /v1/offices/{officeId} | Update Office
[**update_office_with_external_id**](OfficesApi.md#update_office_with_external_id) | **PUT** /v1/offices/external-id/{externalId} | Update Office

# **create_office**
> PostOfficesResponse create_office(body)

Create an Office

Mandatory Fields name, openingDate, parentId

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostOfficesRequest() # PostOfficesRequest | 

try:
    # Create an Office
    api_response = api_instance.create_office(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->create_office: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostOfficesRequest**](PostOfficesRequest.md)|  | 

### Return type

[**PostOfficesResponse**](PostOfficesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_office_template**
> get_office_template(date_format=date_format)



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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)

try:
    api_instance.get_office_template(date_format=date_format)
except ApiException as e:
    print("Exception when calling OfficesApi->get_office_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_office_template**
> str post_office_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)



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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)

try:
    api_response = api_instance.post_office_template(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->post_office_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_office**
> GetOfficesResponse retrieve_office(office_id)

Retrieve an Office

Example Requests:  offices/1   offices/1?template=true   offices/1?fields=id,name,parentName

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
office_id = 789 # int | officeId

try:
    # Retrieve an Office
    api_response = api_instance.retrieve_office(office_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->retrieve_office: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **int**| officeId | 

### Return type

[**GetOfficesResponse**](GetOfficesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_office_by_external_id**
> GetOfficesResponse retrieve_office_by_external_id(external_id)

Retrieve an Office using external id

Example Requests:  offices/external-id/asd123   offices/external-id/asd123?template=true   offices/external-id/asd123?fields=id,name,parentName

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
external_id = 'external_id_example' # str | externalId

try:
    # Retrieve an Office using external id
    api_response = api_instance.retrieve_office_by_external_id(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->retrieve_office_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | 

### Return type

[**GetOfficesResponse**](GetOfficesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_office_template1**
> GetOfficesTemplateResponse retrieve_office_template1()

Retrieve Office Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  offices/template

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Office Details Template
    api_response = api_instance.retrieve_office_template1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->retrieve_office_template1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetOfficesTemplateResponse**](GetOfficesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_offices**
> list[GetOfficesResponse] retrieve_offices(include_all_offices=include_all_offices, order_by=order_by, sort_order=sort_order)

List Offices

Example Requests:  offices   offices?fields=id,name,openingDate

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
include_all_offices = false # bool | includeAllOffices (optional) (default to false)
order_by = 'order_by_example' # str | orderBy (optional)
sort_order = 'sort_order_example' # str | sortOrder (optional)

try:
    # List Offices
    api_response = api_instance.retrieve_offices(include_all_offices=include_all_offices, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->retrieve_offices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_all_offices** | **bool**| includeAllOffices | [optional] [default to false]
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**list[GetOfficesResponse]**](GetOfficesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_office**
> PutOfficesOfficeIdResponse update_office(body, office_id)

Update Office

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutOfficesOfficeIdRequest() # PutOfficesOfficeIdRequest | 
office_id = 789 # int | officeId

try:
    # Update Office
    api_response = api_instance.update_office(body, office_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->update_office: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutOfficesOfficeIdRequest**](PutOfficesOfficeIdRequest.md)|  | 
 **office_id** | **int**| officeId | 

### Return type

[**PutOfficesOfficeIdResponse**](PutOfficesOfficeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_office_with_external_id**
> PutOfficesOfficeIdResponse update_office_with_external_id(body, external_id)

Update Office

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
api_instance = fineract_client.OfficesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutOfficesOfficeIdRequest() # PutOfficesOfficeIdRequest | 
external_id = 'external_id_example' # str | externalId

try:
    # Update Office
    api_response = api_instance.update_office_with_external_id(body, external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficesApi->update_office_with_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutOfficesOfficeIdRequest**](PutOfficesOfficeIdRequest.md)|  | 
 **external_id** | **str**| externalId | 

### Return type

[**PutOfficesOfficeIdResponse**](PutOfficesOfficeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

