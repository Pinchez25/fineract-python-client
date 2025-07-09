# fineract_client.AccountNumberFormatApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AccountNumberFormatApi.md#create) | **POST** /v1/accountnumberformats | Create an Account number format
[**delete**](AccountNumberFormatApi.md#delete) | **DELETE** /v1/accountnumberformats/{accountNumberFormatId} | Delete an Account number format
[**retrieve_all3**](AccountNumberFormatApi.md#retrieve_all3) | **GET** /v1/accountnumberformats | List Account number formats
[**retrieve_one**](AccountNumberFormatApi.md#retrieve_one) | **GET** /v1/accountnumberformats/{accountNumberFormatId} | Retrieve an Account number format
[**retrieve_template2**](AccountNumberFormatApi.md#retrieve_template2) | **GET** /v1/accountnumberformats/template | Retrieve Account number format Template
[**update1**](AccountNumberFormatApi.md#update1) | **PUT** /v1/accountnumberformats/{accountNumberFormatId} | Update an Account number format


# **create**
> PostAccountNumberFormatsResponse create(post_account_number_formats_request=post_account_number_formats_request)

Create an Account number format

Note: You may associate a single Account number format for a given account type
Mandatory Fields for Account number formats
accountType

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_account_number_formats_request import PostAccountNumberFormatsRequest
from fineract_client.models.post_account_number_formats_response import PostAccountNumberFormatsResponse
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)
    post_account_number_formats_request = fineract_client.PostAccountNumberFormatsRequest() # PostAccountNumberFormatsRequest |  (optional)

    try:
        # Create an Account number format
        api_response = api_instance.create(post_account_number_formats_request=post_account_number_formats_request)
        print("The response of AccountNumberFormatApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_account_number_formats_request** | [**PostAccountNumberFormatsRequest**](PostAccountNumberFormatsRequest.md)|  | [optional] 

### Return type

[**PostAccountNumberFormatsResponse**](PostAccountNumberFormatsResponse.md)

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

# **delete**
> DeleteAccountNumberFormatsResponse delete(account_number_format_id)

Delete an Account number format

Note: Account numbers created while this format was active would remain unchanged.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_account_number_formats_response import DeleteAccountNumberFormatsResponse
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)
    account_number_format_id = 56 # int | accountNumberFormatId

    try:
        # Delete an Account number format
        api_response = api_instance.delete(account_number_format_id)
        print("The response of AccountNumberFormatApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number_format_id** | **int**| accountNumberFormatId | 

### Return type

[**DeleteAccountNumberFormatsResponse**](DeleteAccountNumberFormatsResponse.md)

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

# **retrieve_all3**
> List[GetAccountNumberFormatsIdResponse] retrieve_all3()

List Account number formats

Example Requests:

accountnumberformats


accountnumberformats?fields=accountType,prefixType

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_number_formats_id_response import GetAccountNumberFormatsIdResponse
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)

    try:
        # List Account number formats
        api_response = api_instance.retrieve_all3()
        print("The response of AccountNumberFormatApi->retrieve_all3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->retrieve_all3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetAccountNumberFormatsIdResponse]**](GetAccountNumberFormatsIdResponse.md)

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

# **retrieve_one**
> GetAccountNumberFormatsIdResponse retrieve_one(account_number_format_id)

Retrieve an Account number format

Example Requests:

accountnumberformats/1


accountnumberformats/1?template=true


accountnumberformats/1?fields=accountType,prefixType

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_number_formats_id_response import GetAccountNumberFormatsIdResponse
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)
    account_number_format_id = 56 # int | accountNumberFormatId

    try:
        # Retrieve an Account number format
        api_response = api_instance.retrieve_one(account_number_format_id)
        print("The response of AccountNumberFormatApi->retrieve_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->retrieve_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number_format_id** | **int**| accountNumberFormatId | 

### Return type

[**GetAccountNumberFormatsIdResponse**](GetAccountNumberFormatsIdResponse.md)

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

# **retrieve_template2**
> GetAccountNumberFormatsResponseTemplate retrieve_template2()

Retrieve Account number format Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists

Example Request:

accountnumberformats/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_account_number_formats_response_template import GetAccountNumberFormatsResponseTemplate
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)

    try:
        # Retrieve Account number format Template
        api_response = api_instance.retrieve_template2()
        print("The response of AccountNumberFormatApi->retrieve_template2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->retrieve_template2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccountNumberFormatsResponseTemplate**](GetAccountNumberFormatsResponseTemplate.md)

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

# **update1**
> PutAccountNumberFormatsResponse update1(account_number_format_id, put_account_number_formats_request)

Update an Account number format

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_account_number_formats_request import PutAccountNumberFormatsRequest
from fineract_client.models.put_account_number_formats_response import PutAccountNumberFormatsResponse
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
    api_instance = fineract_client.AccountNumberFormatApi(api_client)
    account_number_format_id = 56 # int | accountNumberFormatId
    put_account_number_formats_request = fineract_client.PutAccountNumberFormatsRequest() # PutAccountNumberFormatsRequest | 

    try:
        # Update an Account number format
        api_response = api_instance.update1(account_number_format_id, put_account_number_formats_request)
        print("The response of AccountNumberFormatApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountNumberFormatApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number_format_id** | **int**| accountNumberFormatId | 
 **put_account_number_formats_request** | [**PutAccountNumberFormatsRequest**](PutAccountNumberFormatsRequest.md)|  | 

### Return type

[**PutAccountNumberFormatsResponse**](PutAccountNumberFormatsResponse.md)

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

