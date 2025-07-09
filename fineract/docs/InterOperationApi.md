# fineract_client.InterOperationApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote**](InterOperationApi.md#create_quote) | **POST** /v1/interoperation/quotes | Calculate Interoperation Quote
[**create_transaction_request**](InterOperationApi.md#create_transaction_request) | **POST** /v1/interoperation/requests | Allow Interoperation Transaction Request
[**delete_account_identifier**](InterOperationApi.md#delete_account_identifier) | **DELETE** /v1/interoperation/parties/{idType}/{idValue} | Allow Interoperation Identifier registration
[**delete_account_identifier1**](InterOperationApi.md#delete_account_identifier1) | **DELETE** /v1/interoperation/parties/{idType}/{idValue}/{subIdOrType} | Allow Interoperation Identifier registration
[**disburse_loan**](InterOperationApi.md#disburse_loan) | **POST** /v1/interoperation/transactions/{accountId}/disburse | Disburse Loan by Account Id
[**get_account_by_identifier**](InterOperationApi.md#get_account_by_identifier) | **GET** /v1/interoperation/parties/{idType}/{idValue} | Query Interoperation Account by secondary identifier
[**get_account_by_identifier1**](InterOperationApi.md#get_account_by_identifier1) | **GET** /v1/interoperation/parties/{idType}/{idValue}/{subIdOrType} | Query Interoperation Account by secondary identifier
[**get_account_details**](InterOperationApi.md#get_account_details) | **GET** /v1/interoperation/accounts/{accountId} | Query Interoperation Account details
[**get_account_identifiers**](InterOperationApi.md#get_account_identifiers) | **GET** /v1/interoperation/accounts/{accountId}/identifiers | Query Interoperation secondary identifiers by Account Id
[**get_account_transactions**](InterOperationApi.md#get_account_transactions) | **GET** /v1/interoperation/accounts/{accountId}/transactions | Query transactions by Account Id
[**get_client_kyc**](InterOperationApi.md#get_client_kyc) | **GET** /v1/interoperation/accounts/{accountId}/kyc | Query KYC by Account Id
[**get_quote**](InterOperationApi.md#get_quote) | **GET** /v1/interoperation/transactions/{transactionCode}/quotes/{quoteCode} | Query Interoperation Quote
[**get_transaction_request**](InterOperationApi.md#get_transaction_request) | **GET** /v1/interoperation/transactions/{transactionCode}/requests/{requestCode} | Query Interoperation Transaction Request
[**get_transfer**](InterOperationApi.md#get_transfer) | **GET** /v1/interoperation/transactions/{transactionCode}/transfers/{transferCode} | Query Interoperation Transfer
[**health**](InterOperationApi.md#health) | **GET** /v1/interoperation/health | Query Interoperation Health Request
[**loan_repayment**](InterOperationApi.md#loan_repayment) | **POST** /v1/interoperation/transactions/{accountId}/loanrepayment | Disburse Loan by Account Id
[**perform_transfer**](InterOperationApi.md#perform_transfer) | **POST** /v1/interoperation/transfers | Prepare Interoperation Transfer
[**register_account_identifier**](InterOperationApi.md#register_account_identifier) | **POST** /v1/interoperation/parties/{idType}/{idValue} | Interoperation Identifier registration
[**register_account_identifier1**](InterOperationApi.md#register_account_identifier1) | **POST** /v1/interoperation/parties/{idType}/{idValue}/{subIdOrType} | Interoperation Identifier registration


# **create_quote**
> InteropQuoteResponseData create_quote(interop_quote_request_data)

Calculate Interoperation Quote

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_quote_request_data import InteropQuoteRequestData
from fineract_client.models.interop_quote_response_data import InteropQuoteResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    interop_quote_request_data = fineract_client.InteropQuoteRequestData() # InteropQuoteRequestData | 

    try:
        # Calculate Interoperation Quote
        api_response = api_instance.create_quote(interop_quote_request_data)
        print("The response of InterOperationApi->create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->create_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interop_quote_request_data** | [**InteropQuoteRequestData**](InteropQuoteRequestData.md)|  | 

### Return type

[**InteropQuoteResponseData**](InteropQuoteResponseData.md)

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

# **create_transaction_request**
> InteropTransactionRequestResponseData create_transaction_request(interop_transaction_request_data)

Allow Interoperation Transaction Request

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_transaction_request_data import InteropTransactionRequestData
from fineract_client.models.interop_transaction_request_response_data import InteropTransactionRequestResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    interop_transaction_request_data = fineract_client.InteropTransactionRequestData() # InteropTransactionRequestData | 

    try:
        # Allow Interoperation Transaction Request
        api_response = api_instance.create_transaction_request(interop_transaction_request_data)
        print("The response of InterOperationApi->create_transaction_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->create_transaction_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interop_transaction_request_data** | [**InteropTransactionRequestData**](InteropTransactionRequestData.md)|  | 

### Return type

[**InteropTransactionRequestResponseData**](InteropTransactionRequestResponseData.md)

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

# **delete_account_identifier**
> InteropIdentifierAccountResponseData delete_account_identifier(id_type, id_value, interop_identifier_request_data)

Allow Interoperation Identifier registration

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
from fineract_client.models.interop_identifier_request_data import InteropIdentifierRequestData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue
    interop_identifier_request_data = fineract_client.InteropIdentifierRequestData() # InteropIdentifierRequestData | 

    try:
        # Allow Interoperation Identifier registration
        api_response = api_instance.delete_account_identifier(id_type, id_value, interop_identifier_request_data)
        print("The response of InterOperationApi->delete_account_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->delete_account_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 
 **interop_identifier_request_data** | [**InteropIdentifierRequestData**](InteropIdentifierRequestData.md)|  | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

# **delete_account_identifier1**
> InteropIdentifierAccountResponseData delete_account_identifier1(id_type, id_value, sub_id_or_type, interop_identifier_request_data)

Allow Interoperation Identifier registration

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
from fineract_client.models.interop_identifier_request_data import InteropIdentifierRequestData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue
    sub_id_or_type = 'sub_id_or_type_example' # str | subIdOrType
    interop_identifier_request_data = fineract_client.InteropIdentifierRequestData() # InteropIdentifierRequestData | 

    try:
        # Allow Interoperation Identifier registration
        api_response = api_instance.delete_account_identifier1(id_type, id_value, sub_id_or_type, interop_identifier_request_data)
        print("The response of InterOperationApi->delete_account_identifier1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->delete_account_identifier1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 
 **sub_id_or_type** | **str**| subIdOrType | 
 **interop_identifier_request_data** | [**InteropIdentifierRequestData**](InteropIdentifierRequestData.md)|  | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

# **disburse_loan**
> str disburse_loan(account_id)

Disburse Loan by Account Id

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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId

    try:
        # Disburse Loan by Account Id
        api_response = api_instance.disburse_loan(account_id)
        print("The response of InterOperationApi->disburse_loan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->disburse_loan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_identifier**
> InteropIdentifierAccountResponseData get_account_by_identifier(id_type, id_value)

Query Interoperation Account by secondary identifier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue

    try:
        # Query Interoperation Account by secondary identifier
        api_response = api_instance.get_account_by_identifier(id_type, id_value)
        print("The response of InterOperationApi->get_account_by_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_account_by_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

# **get_account_by_identifier1**
> InteropIdentifierAccountResponseData get_account_by_identifier1(id_type, id_value, sub_id_or_type)

Query Interoperation Account by secondary identifier

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue
    sub_id_or_type = 'sub_id_or_type_example' # str | subIdOrType

    try:
        # Query Interoperation Account by secondary identifier
        api_response = api_instance.get_account_by_identifier1(id_type, id_value, sub_id_or_type)
        print("The response of InterOperationApi->get_account_by_identifier1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_account_by_identifier1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 
 **sub_id_or_type** | **str**| subIdOrType | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

# **get_account_details**
> InteropAccountData get_account_details(account_id)

Query Interoperation Account details

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_account_data import InteropAccountData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId

    try:
        # Query Interoperation Account details
        api_response = api_instance.get_account_details(account_id)
        print("The response of InterOperationApi->get_account_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_account_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

[**InteropAccountData**](InteropAccountData.md)

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

# **get_account_identifiers**
> InteropIdentifiersResponseData get_account_identifiers(account_id)

Query Interoperation secondary identifiers by Account Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifiers_response_data import InteropIdentifiersResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId

    try:
        # Query Interoperation secondary identifiers by Account Id
        api_response = api_instance.get_account_identifiers(account_id)
        print("The response of InterOperationApi->get_account_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_account_identifiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

[**InteropIdentifiersResponseData**](InteropIdentifiersResponseData.md)

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

# **get_account_transactions**
> InteropTransactionsData get_account_transactions(account_id, debit=debit, credit=credit, from_booking_date_time=from_booking_date_time, to_booking_date_time=to_booking_date_time)

Query transactions by Account Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_transactions_data import InteropTransactionsData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId
    debit = True # bool | debit (optional) (default to True)
    credit = False # bool | credit (optional) (default to False)
    from_booking_date_time = 'from_booking_date_time_example' # str | fromBookingDateTime (optional)
    to_booking_date_time = 'to_booking_date_time_example' # str | toBookingDateTime (optional)

    try:
        # Query transactions by Account Id
        api_response = api_instance.get_account_transactions(account_id, debit=debit, credit=credit, from_booking_date_time=from_booking_date_time, to_booking_date_time=to_booking_date_time)
        print("The response of InterOperationApi->get_account_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_account_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **debit** | **bool**| debit | [optional] [default to True]
 **credit** | **bool**| credit | [optional] [default to False]
 **from_booking_date_time** | **str**| fromBookingDateTime | [optional] 
 **to_booking_date_time** | **str**| toBookingDateTime | [optional] 

### Return type

[**InteropTransactionsData**](InteropTransactionsData.md)

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

# **get_client_kyc**
> InteropKycResponseData get_client_kyc(account_id)

Query KYC by Account Id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_kyc_response_data import InteropKycResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId

    try:
        # Query KYC by Account Id
        api_response = api_instance.get_client_kyc(account_id)
        print("The response of InterOperationApi->get_client_kyc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_client_kyc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

[**InteropKycResponseData**](InteropKycResponseData.md)

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

# **get_quote**
> InteropQuoteResponseData get_quote(transaction_code, quote_code)

Query Interoperation Quote

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_quote_response_data import InteropQuoteResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    transaction_code = 'transaction_code_example' # str | transactionCode
    quote_code = 'quote_code_example' # str | quoteCode

    try:
        # Query Interoperation Quote
        api_response = api_instance.get_quote(transaction_code, quote_code)
        print("The response of InterOperationApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_code** | **str**| transactionCode | 
 **quote_code** | **str**| quoteCode | 

### Return type

[**InteropQuoteResponseData**](InteropQuoteResponseData.md)

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

# **get_transaction_request**
> InteropTransactionRequestResponseData get_transaction_request(transaction_code, request_code)

Query Interoperation Transaction Request

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_transaction_request_response_data import InteropTransactionRequestResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    transaction_code = 'transaction_code_example' # str | transactionCode
    request_code = 'request_code_example' # str | requestCode

    try:
        # Query Interoperation Transaction Request
        api_response = api_instance.get_transaction_request(transaction_code, request_code)
        print("The response of InterOperationApi->get_transaction_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_transaction_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_code** | **str**| transactionCode | 
 **request_code** | **str**| requestCode | 

### Return type

[**InteropTransactionRequestResponseData**](InteropTransactionRequestResponseData.md)

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

# **get_transfer**
> InteropTransferResponseData get_transfer(transaction_code, transfer_code)

Query Interoperation Transfer

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_transfer_response_data import InteropTransferResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    transaction_code = 'transaction_code_example' # str | transactionCode
    transfer_code = 'transfer_code_example' # str | transferCode

    try:
        # Query Interoperation Transfer
        api_response = api_instance.get_transfer(transaction_code, transfer_code)
        print("The response of InterOperationApi->get_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->get_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_code** | **str**| transactionCode | 
 **transfer_code** | **str**| transferCode | 

### Return type

[**InteropTransferResponseData**](InteropTransferResponseData.md)

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

# **health**
> health()

Query Interoperation Health Request

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
    api_instance = fineract_client.InterOperationApi(api_client)

    try:
        # Query Interoperation Health Request
        api_instance.health()
    except Exception as e:
        print("Exception when calling InterOperationApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loan_repayment**
> str loan_repayment(account_id)

Disburse Loan by Account Id

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
    api_instance = fineract_client.InterOperationApi(api_client)
    account_id = 'account_id_example' # str | accountId

    try:
        # Disburse Loan by Account Id
        api_response = api_instance.loan_repayment(account_id)
        print("The response of InterOperationApi->loan_repayment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->loan_repayment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_transfer**
> InteropTransferResponseData perform_transfer(interop_transfer_request_data, action=action)

Prepare Interoperation Transfer

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_transfer_request_data import InteropTransferRequestData
from fineract_client.models.interop_transfer_response_data import InteropTransferResponseData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    interop_transfer_request_data = fineract_client.InteropTransferRequestData() # InteropTransferRequestData | 
    action = 'action_example' # str | action (optional)

    try:
        # Prepare Interoperation Transfer
        api_response = api_instance.perform_transfer(interop_transfer_request_data, action=action)
        print("The response of InterOperationApi->perform_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->perform_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interop_transfer_request_data** | [**InteropTransferRequestData**](InteropTransferRequestData.md)|  | 
 **action** | **str**| action | [optional] 

### Return type

[**InteropTransferResponseData**](InteropTransferResponseData.md)

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

# **register_account_identifier**
> InteropIdentifierAccountResponseData register_account_identifier(id_type, id_value, interop_identifier_request_data)

Interoperation Identifier registration

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
from fineract_client.models.interop_identifier_request_data import InteropIdentifierRequestData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue
    interop_identifier_request_data = fineract_client.InteropIdentifierRequestData() # InteropIdentifierRequestData | 

    try:
        # Interoperation Identifier registration
        api_response = api_instance.register_account_identifier(id_type, id_value, interop_identifier_request_data)
        print("The response of InterOperationApi->register_account_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->register_account_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 
 **interop_identifier_request_data** | [**InteropIdentifierRequestData**](InteropIdentifierRequestData.md)|  | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

# **register_account_identifier1**
> InteropIdentifierAccountResponseData register_account_identifier1(id_type, id_value, sub_id_or_type, interop_identifier_request_data)

Interoperation Identifier registration

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.interop_identifier_account_response_data import InteropIdentifierAccountResponseData
from fineract_client.models.interop_identifier_request_data import InteropIdentifierRequestData
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
    api_instance = fineract_client.InterOperationApi(api_client)
    id_type = 'id_type_example' # str | idType
    id_value = 'id_value_example' # str | idValue
    sub_id_or_type = 'sub_id_or_type_example' # str | subIdOrType
    interop_identifier_request_data = fineract_client.InteropIdentifierRequestData() # InteropIdentifierRequestData | 

    try:
        # Interoperation Identifier registration
        api_response = api_instance.register_account_identifier1(id_type, id_value, sub_id_or_type, interop_identifier_request_data)
        print("The response of InterOperationApi->register_account_identifier1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterOperationApi->register_account_identifier1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type** | **str**| idType | 
 **id_value** | **str**| idValue | 
 **sub_id_or_type** | **str**| subIdOrType | 
 **interop_identifier_request_data** | [**InteropIdentifierRequestData**](InteropIdentifierRequestData.md)|  | 

### Return type

[**InteropIdentifierAccountResponseData**](InteropIdentifierAccountResponseData.md)

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

