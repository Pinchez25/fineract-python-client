# fineract_client.EntityFieldConfigurationApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses**](EntityFieldConfigurationApi.md#get_addresses) | **GET** /v1/fieldconfiguration/{entity} | Retrieves the Entity Field Configuration


# **get_addresses**
> List[GetFieldConfigurationEntityResponse] get_addresses(entity)

Retrieves the Entity Field Configuration

It retrieves all the Entity Field Configuration

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_field_configuration_entity_response import GetFieldConfigurationEntityResponse
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
    api_instance = fineract_client.EntityFieldConfigurationApi(api_client)
    entity = 'entity_example' # str | entity

    try:
        # Retrieves the Entity Field Configuration
        api_response = api_instance.get_addresses(entity)
        print("The response of EntityFieldConfigurationApi->get_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityFieldConfigurationApi->get_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| entity | 

### Return type

[**List[GetFieldConfigurationEntityResponse]**](GetFieldConfigurationEntityResponse.md)

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

