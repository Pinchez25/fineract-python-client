# fineract_client.ProvisioningEntriesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_entries**](ProvisioningEntriesApi.md#create_provisioning_entries) | **POST** /v1/provisioningentries | Create new Provisioning Entries
[**modify_provisioning_entry**](ProvisioningEntriesApi.md#modify_provisioning_entry) | **POST** /v1/provisioningentries/{entryId} | Recreates Provisioning Entry
[**retrieve_all_provisioning_entries**](ProvisioningEntriesApi.md#retrieve_all_provisioning_entries) | **GET** /v1/provisioningentries | List all Provisioning Entries
[**retrieve_proviioning_entries**](ProvisioningEntriesApi.md#retrieve_proviioning_entries) | **GET** /v1/provisioningentries/entries | 
[**retrieve_provisioning_entry**](ProvisioningEntriesApi.md#retrieve_provisioning_entry) | **GET** /v1/provisioningentries/{entryId} | Retrieves a Provisioning Entry

# **create_provisioning_entries**
> PostProvisioningEntriesResponse create_provisioning_entries(body=body)

Create new Provisioning Entries

Creates a new Provisioning Entries  Mandatory Fields date dateFormat locale Optional Fields createjournalentries

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
api_instance = fineract_client.ProvisioningEntriesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostProvisioningEntriesRequest() # PostProvisioningEntriesRequest |  (optional)

try:
    # Create new Provisioning Entries
    api_response = api_instance.create_provisioning_entries(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningEntriesApi->create_provisioning_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostProvisioningEntriesRequest**](PostProvisioningEntriesRequest.md)|  | [optional] 

### Return type

[**PostProvisioningEntriesResponse**](PostProvisioningEntriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_provisioning_entry**
> PutProvisioningEntriesResponse modify_provisioning_entry(entry_id, body=body, command=command)

Recreates Provisioning Entry

Recreates Provisioning Entry | createjournalentry.

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
api_instance = fineract_client.ProvisioningEntriesApi(fineract_client.ApiClient(configuration))
entry_id = 789 # int | entryId
body = fineract_client.PutProvisioningEntriesRequest() # PutProvisioningEntriesRequest |  (optional)
command = 'command_example' # str | command=createjournalentry command=recreateprovisioningentry (optional)

try:
    # Recreates Provisioning Entry
    api_response = api_instance.modify_provisioning_entry(entry_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningEntriesApi->modify_provisioning_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| entryId | 
 **body** | [**PutProvisioningEntriesRequest**](PutProvisioningEntriesRequest.md)|  | [optional] 
 **command** | **str**| command&#x3D;createjournalentry command&#x3D;recreateprovisioningentry | [optional] 

### Return type

[**PutProvisioningEntriesResponse**](PutProvisioningEntriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_provisioning_entries**
> list[ProvisioningEntryData] retrieve_all_provisioning_entries(offset=offset, limit=limit)

List all Provisioning Entries

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
api_instance = fineract_client.ProvisioningEntriesApi(fineract_client.ApiClient(configuration))
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try:
    # List all Provisioning Entries
    api_response = api_instance.retrieve_all_provisioning_entries(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningEntriesApi->retrieve_all_provisioning_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**list[ProvisioningEntryData]**](ProvisioningEntryData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_proviioning_entries**
> LoanProductProvisioningEntryData retrieve_proviioning_entries(entry_id=entry_id, offset=offset, limit=limit, office_id=office_id, product_id=product_id, category_id=category_id)



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
api_instance = fineract_client.ProvisioningEntriesApi(fineract_client.ApiClient(configuration))
entry_id = 789 # int |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
office_id = 789 # int |  (optional)
product_id = 789 # int |  (optional)
category_id = 789 # int |  (optional)

try:
    api_response = api_instance.retrieve_proviioning_entries(entry_id=entry_id, offset=offset, limit=limit, office_id=office_id, product_id=product_id, category_id=category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningEntriesApi->retrieve_proviioning_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **office_id** | **int**|  | [optional] 
 **product_id** | **int**|  | [optional] 
 **category_id** | **int**|  | [optional] 

### Return type

[**LoanProductProvisioningEntryData**](LoanProductProvisioningEntryData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_provisioning_entry**
> ProvisioningEntryData retrieve_provisioning_entry(entry_id)

Retrieves a Provisioning Entry

Returns the details of a generated Provisioning Entry.

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
api_instance = fineract_client.ProvisioningEntriesApi(fineract_client.ApiClient(configuration))
entry_id = 789 # int | entryId

try:
    # Retrieves a Provisioning Entry
    api_response = api_instance.retrieve_provisioning_entry(entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningEntriesApi->retrieve_provisioning_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| entryId | 

### Return type

[**ProvisioningEntryData**](ProvisioningEntryData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

