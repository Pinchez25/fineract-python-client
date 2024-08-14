# fineract_client.EntityFieldConfigurationApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses**](EntityFieldConfigurationApi.md#get_addresses) | **GET** /v1/fieldconfiguration/{entity} | Retrieves the Entity Field Configuration

# **get_addresses**
> list[GetFieldConfigurationEntityResponse] get_addresses(entity)

Retrieves the Entity Field Configuration

It retrieves all the Entity Field Configuration

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
api_instance = fineract_client.EntityFieldConfigurationApi(fineract_client.ApiClient(configuration))
entity = 'entity_example' # str | entity

try:
    # Retrieves the Entity Field Configuration
    api_response = api_instance.get_addresses(entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityFieldConfigurationApi->get_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| entity | 

### Return type

[**list[GetFieldConfigurationEntityResponse]**](GetFieldConfigurationEntityResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

