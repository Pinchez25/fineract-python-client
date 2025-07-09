# fineract_client.ProvisioningEntriesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_entries**](ProvisioningEntriesApi.md#create_provisioning_entries) | **POST** /v1/provisioningentries | Create new Provisioning Entries
[**modify_provisioning_entry**](ProvisioningEntriesApi.md#modify_provisioning_entry) | **POST** /v1/provisioningentries/{entryId} | Recreates Provisioning Entry
[**retrieve_all_provisioning_entries**](ProvisioningEntriesApi.md#retrieve_all_provisioning_entries) | **GET** /v1/provisioningentries | List all Provisioning Entries
[**retrieve_proviioning_entries**](ProvisioningEntriesApi.md#retrieve_proviioning_entries) | **GET** /v1/provisioningentries/entries | 
[**retrieve_provisioning_entry**](ProvisioningEntriesApi.md#retrieve_provisioning_entry) | **GET** /v1/provisioningentries/{entryId} | Retrieves a Provisioning Entry


# **create_provisioning_entries**
> PostProvisioningEntriesResponse create_provisioning_entries(post_provisioning_entries_request=post_provisioning_entries_request)

Create new Provisioning Entries

Creates a new Provisioning Entries  Mandatory Fields date dateFormat locale Optional Fields createjournalentries

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_provisioning_entries_request import PostProvisioningEntriesRequest
from fineract_client.models.post_provisioning_entries_response import PostProvisioningEntriesResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.ProvisioningEntriesApi(api_client)
    post_provisioning_entries_request = fineract_client.PostProvisioningEntriesRequest() # PostProvisioningEntriesRequest |  (optional)

    try:
        # Create new Provisioning Entries
        api_response = api_instance.create_provisioning_entries(post_provisioning_entries_request=post_provisioning_entries_request)
        print("The response of ProvisioningEntriesApi->create_provisioning_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningEntriesApi->create_provisioning_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_provisioning_entries_request** | [**PostProvisioningEntriesRequest**](PostProvisioningEntriesRequest.md)|  | [optional] 

### Return type

[**PostProvisioningEntriesResponse**](PostProvisioningEntriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_provisioning_entry**
> PutProvisioningEntriesResponse modify_provisioning_entry(entry_id, command=command, put_provisioning_entries_request=put_provisioning_entries_request)

Recreates Provisioning Entry

Recreates Provisioning Entry | createjournalentry.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_provisioning_entries_request import PutProvisioningEntriesRequest
from fineract_client.models.put_provisioning_entries_response import PutProvisioningEntriesResponse
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.ProvisioningEntriesApi(api_client)
    entry_id = 56 # int | entryId
    command = 'command_example' # str | command=createjournalentry command=recreateprovisioningentry (optional)
    put_provisioning_entries_request = fineract_client.PutProvisioningEntriesRequest() # PutProvisioningEntriesRequest |  (optional)

    try:
        # Recreates Provisioning Entry
        api_response = api_instance.modify_provisioning_entry(entry_id, command=command, put_provisioning_entries_request=put_provisioning_entries_request)
        print("The response of ProvisioningEntriesApi->modify_provisioning_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningEntriesApi->modify_provisioning_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| entryId | 
 **command** | **str**| command&#x3D;createjournalentry command&#x3D;recreateprovisioningentry | [optional] 
 **put_provisioning_entries_request** | [**PutProvisioningEntriesRequest**](PutProvisioningEntriesRequest.md)|  | [optional] 

### Return type

[**PutProvisioningEntriesResponse**](PutProvisioningEntriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_provisioning_entries**
> List[ProvisioningEntryData] retrieve_all_provisioning_entries(offset=offset, limit=limit)

List all Provisioning Entries

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.provisioning_entry_data import ProvisioningEntryData
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.ProvisioningEntriesApi(api_client)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List all Provisioning Entries
        api_response = api_instance.retrieve_all_provisioning_entries(offset=offset, limit=limit)
        print("The response of ProvisioningEntriesApi->retrieve_all_provisioning_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningEntriesApi->retrieve_all_provisioning_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**List[ProvisioningEntryData]**](ProvisioningEntryData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_proviioning_entries**
> LoanProductProvisioningEntryData retrieve_proviioning_entries(entry_id=entry_id, offset=offset, limit=limit, office_id=office_id, product_id=product_id, category_id=category_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.loan_product_provisioning_entry_data import LoanProductProvisioningEntryData
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.ProvisioningEntriesApi(api_client)
    entry_id = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    office_id = 56 # int |  (optional)
    product_id = 56 # int |  (optional)
    category_id = 56 # int |  (optional)

    try:
        api_response = api_instance.retrieve_proviioning_entries(entry_id=entry_id, offset=offset, limit=limit, office_id=office_id, product_id=product_id, category_id=category_id)
        print("The response of ProvisioningEntriesApi->retrieve_proviioning_entries:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_provisioning_entry**
> ProvisioningEntryData retrieve_provisioning_entry(entry_id)

Retrieves a Provisioning Entry

Returns the details of a generated Provisioning Entry.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.provisioning_entry_data import ProvisioningEntryData
from fineract_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/fineract-provider/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fineract_client.Configuration(
    host = "http://localhost/fineract-provider/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = fineract_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tenantid
configuration.api_key['tenantid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tenantid'] = 'Bearer'

# Enter a context with an instance of the API client
with fineract_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fineract_client.ProvisioningEntriesApi(api_client)
    entry_id = 56 # int | entryId

    try:
        # Retrieves a Provisioning Entry
        api_response = api_instance.retrieve_provisioning_entry(entry_id)
        print("The response of ProvisioningEntriesApi->retrieve_provisioning_entry:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

