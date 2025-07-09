# fineract_client.StandingInstructionsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create5**](StandingInstructionsApi.md#create5) | **POST** /v1/standinginstructions | Create new Standing Instruction
[**retrieve_all19**](StandingInstructionsApi.md#retrieve_all19) | **GET** /v1/standinginstructions | List Standing Instructions
[**retrieve_one10**](StandingInstructionsApi.md#retrieve_one10) | **GET** /v1/standinginstructions/{standingInstructionId} | Retrieve Standing Instruction
[**template6**](StandingInstructionsApi.md#template6) | **GET** /v1/standinginstructions/template | Retrieve Standing Instruction Template
[**update9**](StandingInstructionsApi.md#update9) | **PUT** /v1/standinginstructions/{standingInstructionId} | Update Standing Instruction | Delete Standing Instruction


# **create5**
> PostStandingInstructionsResponse create5(post_standing_instructions_request)

Create new Standing Instruction

Ability to create new instruction for transfer of monetary funds from one account to another

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_standing_instructions_request import PostStandingInstructionsRequest
from fineract_client.models.post_standing_instructions_response import PostStandingInstructionsResponse
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
    api_instance = fineract_client.StandingInstructionsApi(api_client)
    post_standing_instructions_request = fineract_client.PostStandingInstructionsRequest() # PostStandingInstructionsRequest | 

    try:
        # Create new Standing Instruction
        api_response = api_instance.create5(post_standing_instructions_request)
        print("The response of StandingInstructionsApi->create5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsApi->create5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_standing_instructions_request** | [**PostStandingInstructionsRequest**](PostStandingInstructionsRequest.md)|  | 

### Return type

[**PostStandingInstructionsResponse**](PostStandingInstructionsResponse.md)

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

# **retrieve_all19**
> GetStandingInstructionsResponse retrieve_all19(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type)

List Standing Instructions

Example Requests:

standinginstructions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_standing_instructions_response import GetStandingInstructionsResponse
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
    api_instance = fineract_client.StandingInstructionsApi(api_client)
    external_id = 'external_id_example' # str | externalId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)
    transfer_type = 56 # int | transferType (optional)
    client_name = 'client_name_example' # str | clientName (optional)
    client_id = 56 # int | clientId (optional)
    from_account_id = 56 # int | fromAccountId (optional)
    from_account_type = 56 # int | fromAccountType (optional)

    try:
        # List Standing Instructions
        api_response = api_instance.retrieve_all19(external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order, transfer_type=transfer_type, client_name=client_name, client_id=client_id, from_account_id=from_account_id, from_account_type=from_account_type)
        print("The response of StandingInstructionsApi->retrieve_all19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsApi->retrieve_all19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 
 **transfer_type** | **int**| transferType | [optional] 
 **client_name** | **str**| clientName | [optional] 
 **client_id** | **int**| clientId | [optional] 
 **from_account_id** | **int**| fromAccountId | [optional] 
 **from_account_type** | **int**| fromAccountType | [optional] 

### Return type

[**GetStandingInstructionsResponse**](GetStandingInstructionsResponse.md)

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

# **retrieve_one10**
> GetStandingInstructionsStandingInstructionIdResponse retrieve_one10(standing_instruction_id, external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

Retrieve Standing Instruction

Example Requests :

standinginstructions/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_standing_instructions_standing_instruction_id_response import GetStandingInstructionsStandingInstructionIdResponse
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
    api_instance = fineract_client.StandingInstructionsApi(api_client)
    standing_instruction_id = 56 # int | standingInstructionId
    external_id = 'external_id_example' # str | externalId (optional)
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)
    order_by = 'order_by_example' # str | orderBy (optional)
    sort_order = 'sort_order_example' # str | sortOrder (optional)

    try:
        # Retrieve Standing Instruction
        api_response = api_instance.retrieve_one10(standing_instruction_id, external_id=external_id, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
        print("The response of StandingInstructionsApi->retrieve_one10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsApi->retrieve_one10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standing_instruction_id** | **int**| standingInstructionId | 
 **external_id** | **str**| externalId | [optional] 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **order_by** | **str**| orderBy | [optional] 
 **sort_order** | **str**| sortOrder | [optional] 

### Return type

[**GetStandingInstructionsStandingInstructionIdResponse**](GetStandingInstructionsStandingInstructionIdResponse.md)

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

# **template6**
> GetStandingInstructionsTemplateResponse template6(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type, transfer_type=transfer_type)

Retrieve Standing Instruction Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists
Example Requests:

standinginstructions/template?fromAccountType=2&fromOfficeId=1

standinginstructions/template?fromAccountType=2&fromOfficeId=1&fromClientId=1&transferType=1

standinginstructions/template?fromClientId=1&fromAccountType=2&fromAccountId=1&transferType=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_standing_instructions_template_response import GetStandingInstructionsTemplateResponse
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
    api_instance = fineract_client.StandingInstructionsApi(api_client)
    from_office_id = 56 # int | fromOfficeId (optional)
    from_client_id = 56 # int | fromClientId (optional)
    from_account_id = 56 # int | fromAccountId (optional)
    from_account_type = 56 # int | fromAccountType (optional)
    to_office_id = 56 # int | toOfficeId (optional)
    to_client_id = 56 # int | toClientId (optional)
    to_account_id = 56 # int | toAccountId (optional)
    to_account_type = 56 # int | toAccountType (optional)
    transfer_type = 56 # int | transferType (optional)

    try:
        # Retrieve Standing Instruction Template
        api_response = api_instance.template6(from_office_id=from_office_id, from_client_id=from_client_id, from_account_id=from_account_id, from_account_type=from_account_type, to_office_id=to_office_id, to_client_id=to_client_id, to_account_id=to_account_id, to_account_type=to_account_type, transfer_type=transfer_type)
        print("The response of StandingInstructionsApi->template6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsApi->template6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_office_id** | **int**| fromOfficeId | [optional] 
 **from_client_id** | **int**| fromClientId | [optional] 
 **from_account_id** | **int**| fromAccountId | [optional] 
 **from_account_type** | **int**| fromAccountType | [optional] 
 **to_office_id** | **int**| toOfficeId | [optional] 
 **to_client_id** | **int**| toClientId | [optional] 
 **to_account_id** | **int**| toAccountId | [optional] 
 **to_account_type** | **int**| toAccountType | [optional] 
 **transfer_type** | **int**| transferType | [optional] 

### Return type

[**GetStandingInstructionsTemplateResponse**](GetStandingInstructionsTemplateResponse.md)

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

# **update9**
> PutStandingInstructionsStandingInstructionIdResponse update9(standing_instruction_id, command=command, put_standing_instructions_standing_instruction_id_request=put_standing_instructions_standing_instruction_id_request)

Update Standing Instruction | Delete Standing Instruction

Ability to modify existing instruction for transfer of monetary funds from one account to another.

PUT https://DomainName/api/v1/standinginstructions/1?command=update


Ability to modify existing instruction for transfer of monetary funds from one account to another.

PUT https://DomainName/api/v1/standinginstructions/1?command=delete

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_standing_instructions_standing_instruction_id_request import PutStandingInstructionsStandingInstructionIdRequest
from fineract_client.models.put_standing_instructions_standing_instruction_id_response import PutStandingInstructionsStandingInstructionIdResponse
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
    api_instance = fineract_client.StandingInstructionsApi(api_client)
    standing_instruction_id = 56 # int | standingInstructionId
    command = 'command_example' # str | command (optional)
    put_standing_instructions_standing_instruction_id_request = fineract_client.PutStandingInstructionsStandingInstructionIdRequest() # PutStandingInstructionsStandingInstructionIdRequest |  (optional)

    try:
        # Update Standing Instruction | Delete Standing Instruction
        api_response = api_instance.update9(standing_instruction_id, command=command, put_standing_instructions_standing_instruction_id_request=put_standing_instructions_standing_instruction_id_request)
        print("The response of StandingInstructionsApi->update9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingInstructionsApi->update9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standing_instruction_id** | **int**| standingInstructionId | 
 **command** | **str**| command | [optional] 
 **put_standing_instructions_standing_instruction_id_request** | [**PutStandingInstructionsStandingInstructionIdRequest**](PutStandingInstructionsStandingInstructionIdRequest.md)|  | [optional] 

### Return type

[**PutStandingInstructionsStandingInstructionIdResponse**](PutStandingInstructionsStandingInstructionIdResponse.md)

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

