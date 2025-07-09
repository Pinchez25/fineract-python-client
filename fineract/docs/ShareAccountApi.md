# fineract_client.ShareAccountApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](ShareAccountApi.md#create_account) | **POST** /v1/accounts/{type} | Submit new share application
[**get_shared_accounts_template**](ShareAccountApi.md#get_shared_accounts_template) | **GET** /v1/accounts/{type}/downloadtemplate | 
[**handle_commands2**](ShareAccountApi.md#handle_commands2) | **POST** /v1/accounts/{type}/{accountId} | Approve share application | Undo approval share application | Reject share application | Activate a share account | Close a share account | Apply additional shares on a share account | Approve additional shares request on a share account | Reject additional shares request on a share account | Redeem shares on a share account
[**post_shared_accounts_template**](ShareAccountApi.md#post_shared_accounts_template) | **POST** /v1/accounts/{type}/uploadtemplate | 
[**retrieve_account**](ShareAccountApi.md#retrieve_account) | **GET** /v1/accounts/{type}/{accountId} | Retrieve a share application/account
[**retrieve_all_accounts1**](ShareAccountApi.md#retrieve_all_accounts1) | **GET** /v1/accounts/{type} | List share applications/accounts
[**template7**](ShareAccountApi.md#template7) | **GET** /v1/accounts/{type}/template | Retrieve Share Account Template
[**update_account**](ShareAccountApi.md#update_account) | **PUT** /v1/accounts/{type}/{accountId} | Modify a share application


# **create_account**
> PostAccountsTypeResponse create_account(type, post_accounts_type_request)

Submit new share application

Submits new share application

Mandatory Fields: clientId, productId, submittedDate, savingsAccountId, requestedShares, applicationDate

Optional Fields: accountNo, externalId

Inherited from Product (if not provided): minimumActivePeriod, minimumActivePeriodFrequencyType, lockinPeriodFrequency, lockinPeriodFrequencyType

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_accounts_type_request import PostAccountsTypeRequest
from fineract_client.models.post_accounts_type_response import PostAccountsTypeResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    post_accounts_type_request = fineract_client.PostAccountsTypeRequest() # PostAccountsTypeRequest | 

    try:
        # Submit new share application
        api_response = api_instance.create_account(type, post_accounts_type_request)
        print("The response of ShareAccountApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **post_accounts_type_request** | [**PostAccountsTypeRequest**](PostAccountsTypeRequest.md)|  | 

### Return type

[**PostAccountsTypeResponse**](PostAccountsTypeResponse.md)

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

# **get_shared_accounts_template**
> get_shared_accounts_template(type, office_id=office_id, date_format=date_format)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    office_id = 56 # int |  (optional)
    date_format = 'date_format_example' # str |  (optional)

    try:
        api_instance.get_shared_accounts_template(type, office_id=office_id, date_format=date_format)
    except Exception as e:
        print("Exception when calling ShareAccountApi->get_shared_accounts_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **office_id** | **int**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands2**
> PostAccountsTypeAccountIdResponse handle_commands2(type, account_id, post_accounts_type_account_id_request, command=command)

Approve share application | Undo approval share application | Reject share application | Activate a share account | Close a share account | Apply additional shares on a share account | Approve additional shares request on a share account | Reject additional shares request on a share account | Redeem shares on a share account

Approve share application:

Approves share application so long as its in 'Submitted and pending approval' state.

Undo approval share application:

Will move 'approved' share application back to 'Submitted and pending approval' state.

Reject share application:

Rejects share application so long as its in 'Submitted and pending approval' state.

Activate a share account:

Results in an approved share application being converted into an 'active' share account.

Close a share account:

Results in an Activated share application being converted into an 'closed' share account.

closedDate is closure date of share account

Mandatory Fields: dateFormat,locale,closedDate

Apply additional shares on a share account:

requestedDate is requsted date of share purchase

requestedShares is number of shares to be purchase

Mandatory Fields: dateFormat,locale,requestedDate, requestedShares

Approve additional shares request on a share account

requestedShares is Share purchase transaction ids

Mandatory Fields: requestedShares

Reject additional shares request on a share account:

requestedShares is Share purchase transaction ids

Mandatory Fields: requestedShares

Redeem shares on a share account:

Results redeem some/all shares from share account.

requestedDate is requsted date of shares redeem

requestedShares is number of shares to be redeemed

Mandatory Fields: dateFormat,locale,requestedDate,requestedShares

Showing request/response for 'Reject additional shares request on a share account'

For more info visit this link - https://fineract.apache.org/legacy-docs/apiLive.htm#shareaccounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_accounts_type_account_id_request import PostAccountsTypeAccountIdRequest
from fineract_client.models.post_accounts_type_account_id_response import PostAccountsTypeAccountIdResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    account_id = 56 # int | accountId
    post_accounts_type_account_id_request = fineract_client.PostAccountsTypeAccountIdRequest() # PostAccountsTypeAccountIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Approve share application | Undo approval share application | Reject share application | Activate a share account | Close a share account | Apply additional shares on a share account | Approve additional shares request on a share account | Reject additional shares request on a share account | Redeem shares on a share account
        api_response = api_instance.handle_commands2(type, account_id, post_accounts_type_account_id_request, command=command)
        print("The response of ShareAccountApi->handle_commands2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->handle_commands2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **account_id** | **int**| accountId | 
 **post_accounts_type_account_id_request** | [**PostAccountsTypeAccountIdRequest**](PostAccountsTypeAccountIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostAccountsTypeAccountIdResponse**](PostAccountsTypeAccountIdResponse.md)

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

# **post_shared_accounts_template**
> str post_shared_accounts_template(type, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    date_format = 'date_format_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)
    uploaded_input_stream = None # bytearray |  (optional)

    try:
        api_response = api_instance.post_shared_accounts_template(type, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream)
        print("The response of ShareAccountApi->post_shared_accounts_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->post_shared_accounts_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account**
> GetAccountsTypeAccountIdResponse retrieve_account(account_id, type)

Retrieve a share application/account

Retrieves a share application/account

Example Requests :

shareaccount/1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_accounts_type_account_id_response import GetAccountsTypeAccountIdResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    account_id = 56 # int | accountId
    type = 'type_example' # str | type

    try:
        # Retrieve a share application/account
        api_response = api_instance.retrieve_account(account_id, type)
        print("The response of ShareAccountApi->retrieve_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->retrieve_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **type** | **str**| type | 

### Return type

[**GetAccountsTypeAccountIdResponse**](GetAccountsTypeAccountIdResponse.md)

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

# **retrieve_all_accounts1**
> GetAccountsTypeResponse retrieve_all_accounts1(type, offset=offset, limit=limit)

List share applications/accounts

Lists share applications/accounts

Example Requests:

shareaccount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_accounts_type_response import GetAccountsTypeResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    offset = 56 # int | offset (optional)
    limit = 56 # int | limit (optional)

    try:
        # List share applications/accounts
        api_response = api_instance.retrieve_all_accounts1(type, offset=offset, limit=limit)
        print("The response of ShareAccountApi->retrieve_all_accounts1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->retrieve_all_accounts1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**GetAccountsTypeResponse**](GetAccountsTypeResponse.md)

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

# **template7**
> GetAccountsTypeTemplateResponse template7(type, client_id=client_id, product_id=product_id)

Retrieve Share Account Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists

Example Requests:

accounts/share/template?clientId=1


accounts/share/template?clientId=1&productId=1

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_accounts_type_template_response import GetAccountsTypeTemplateResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    client_id = 56 # int | clientId (optional)
    product_id = 56 # int | productId (optional)

    try:
        # Retrieve Share Account Template
        api_response = api_instance.template7(type, client_id=client_id, product_id=product_id)
        print("The response of ShareAccountApi->template7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->template7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **client_id** | **int**| clientId | [optional] 
 **product_id** | **int**| productId | [optional] 

### Return type

[**GetAccountsTypeTemplateResponse**](GetAccountsTypeTemplateResponse.md)

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

# **update_account**
> PutAccountsTypeAccountIdResponse update_account(type, account_id, put_accounts_type_account_id_request)

Modify a share application

Share application can only be modified when in 'Submitted and pending approval' state. Once the application is approved, the details cannot be changed using this method. Specific api endpoints will be created to allow change of interest detail such as rate, compounding period, posting period etc

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_accounts_type_account_id_request import PutAccountsTypeAccountIdRequest
from fineract_client.models.put_accounts_type_account_id_response import PutAccountsTypeAccountIdResponse
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
    api_instance = fineract_client.ShareAccountApi(api_client)
    type = 'type_example' # str | type
    account_id = 56 # int | accountId
    put_accounts_type_account_id_request = fineract_client.PutAccountsTypeAccountIdRequest() # PutAccountsTypeAccountIdRequest | 

    try:
        # Modify a share application
        api_response = api_instance.update_account(type, account_id, put_accounts_type_account_id_request)
        print("The response of ShareAccountApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShareAccountApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 
 **account_id** | **int**| accountId | 
 **put_accounts_type_account_id_request** | [**PutAccountsTypeAccountIdRequest**](PutAccountsTypeAccountIdRequest.md)|  | 

### Return type

[**PutAccountsTypeAccountIdResponse**](PutAccountsTypeAccountIdResponse.md)

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

