# fineract_client.PocketApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_commands8**](PocketApi.md#handle_commands8) | **POST** /v1/self/pockets | Link/delink accounts to/from pocket
[**retrieve_all37**](PocketApi.md#retrieve_all37) | **GET** /v1/self/pockets | Retrieve accounts linked to pocket


# **handle_commands8**
> PostLinkDelinkAccountsToFromPocketResponse handle_commands8(command=command, body=body)

Link/delink accounts to/from pocket

Pockets behave as favourites. An user can link his/her Loan, Savings and Share accounts to pocket for faster access. In a similar way linked accounts can be delinked from the pocket.  Example Requests:  self/pockets?command=linkAccounts  self/pockets?command=delinkAccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_link_delink_accounts_to_from_pocket_response import PostLinkDelinkAccountsToFromPocketResponse
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
    api_instance = fineract_client.PocketApi(api_client)
    command = 'command_example' # str | command (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Link/delink accounts to/from pocket
        api_response = api_instance.handle_commands8(command=command, body=body)
        print("The response of PocketApi->handle_commands8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PocketApi->handle_commands8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| command | [optional] 
 **body** | **str**|  | [optional] 

### Return type

[**PostLinkDelinkAccountsToFromPocketResponse**](PostLinkDelinkAccountsToFromPocketResponse.md)

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

# **retrieve_all37**
> GetAccountsLinkedToPocketResponse retrieve_all37()

Retrieve accounts linked to pocket

All linked loan  Example Requests:   self/pockets

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_accounts_linked_to_pocket_response import GetAccountsLinkedToPocketResponse
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
    api_instance = fineract_client.PocketApi(api_client)

    try:
        # Retrieve accounts linked to pocket
        api_response = api_instance.retrieve_all37()
        print("The response of PocketApi->retrieve_all37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PocketApi->retrieve_all37: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccountsLinkedToPocketResponse**](GetAccountsLinkedToPocketResponse.md)

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

