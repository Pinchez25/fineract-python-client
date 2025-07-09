# fineract_client.PaymentTypeApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_type**](PaymentTypeApi.md#create_payment_type) | **POST** /v1/paymenttypes | Create a Payment Type
[**delete_code1**](PaymentTypeApi.md#delete_code1) | **DELETE** /v1/paymenttypes/{paymentTypeId} | Delete a Payment Type
[**get_all_payment_types**](PaymentTypeApi.md#get_all_payment_types) | **GET** /v1/paymenttypes | Retrieve all Payment Types
[**retrieve_one_payment_type**](PaymentTypeApi.md#retrieve_one_payment_type) | **GET** /v1/paymenttypes/{paymentTypeId} | Retrieve a Payment Type
[**update_payment_type**](PaymentTypeApi.md#update_payment_type) | **PUT** /v1/paymenttypes/{paymentTypeId} | Update a Payment Type


# **create_payment_type**
> PostPaymentTypesResponse create_payment_type(post_payment_types_request)

Create a Payment Type

Creates a new Payment type

Mandatory Fields: name

Optional Fields: Description, isCashPayment,Position

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_payment_types_request import PostPaymentTypesRequest
from fineract_client.models.post_payment_types_response import PostPaymentTypesResponse
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
    api_instance = fineract_client.PaymentTypeApi(api_client)
    post_payment_types_request = fineract_client.PostPaymentTypesRequest() # PostPaymentTypesRequest | 

    try:
        # Create a Payment Type
        api_response = api_instance.create_payment_type(post_payment_types_request)
        print("The response of PaymentTypeApi->create_payment_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTypeApi->create_payment_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_payment_types_request** | [**PostPaymentTypesRequest**](PostPaymentTypesRequest.md)|  | 

### Return type

[**PostPaymentTypesResponse**](PostPaymentTypesResponse.md)

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

# **delete_code1**
> DeletePaymentTypesPaymentTypeIdResponse delete_code1(payment_type_id)

Delete a Payment Type

Deletes payment type

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_payment_types_payment_type_id_response import DeletePaymentTypesPaymentTypeIdResponse
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
    api_instance = fineract_client.PaymentTypeApi(api_client)
    payment_type_id = 56 # int | paymentTypeId

    try:
        # Delete a Payment Type
        api_response = api_instance.delete_code1(payment_type_id)
        print("The response of PaymentTypeApi->delete_code1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTypeApi->delete_code1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_type_id** | **int**| paymentTypeId | 

### Return type

[**DeletePaymentTypesPaymentTypeIdResponse**](DeletePaymentTypesPaymentTypeIdResponse.md)

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

# **get_all_payment_types**
> List[GetPaymentTypesResponse] get_all_payment_types(only_with_code=only_with_code)

Retrieve all Payment Types

Retrieve list of payment types

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_payment_types_response import GetPaymentTypesResponse
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
    api_instance = fineract_client.PaymentTypeApi(api_client)
    only_with_code = True # bool | onlyWithCode (optional)

    try:
        # Retrieve all Payment Types
        api_response = api_instance.get_all_payment_types(only_with_code=only_with_code)
        print("The response of PaymentTypeApi->get_all_payment_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTypeApi->get_all_payment_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_with_code** | **bool**| onlyWithCode | [optional] 

### Return type

[**List[GetPaymentTypesResponse]**](GetPaymentTypesResponse.md)

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

# **retrieve_one_payment_type**
> GetPaymentTypesPaymentTypeIdResponse retrieve_one_payment_type(payment_type_id)

Retrieve a Payment Type

Retrieves a payment type

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_payment_types_payment_type_id_response import GetPaymentTypesPaymentTypeIdResponse
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
    api_instance = fineract_client.PaymentTypeApi(api_client)
    payment_type_id = 56 # int | paymentTypeId

    try:
        # Retrieve a Payment Type
        api_response = api_instance.retrieve_one_payment_type(payment_type_id)
        print("The response of PaymentTypeApi->retrieve_one_payment_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTypeApi->retrieve_one_payment_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_type_id** | **int**| paymentTypeId | 

### Return type

[**GetPaymentTypesPaymentTypeIdResponse**](GetPaymentTypesPaymentTypeIdResponse.md)

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

# **update_payment_type**
> PutPaymentTypesPaymentTypeIdResponse update_payment_type(payment_type_id, put_payment_types_payment_type_id_request)

Update a Payment Type

Updates a Payment Type

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_payment_types_payment_type_id_request import PutPaymentTypesPaymentTypeIdRequest
from fineract_client.models.put_payment_types_payment_type_id_response import PutPaymentTypesPaymentTypeIdResponse
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
    api_instance = fineract_client.PaymentTypeApi(api_client)
    payment_type_id = 56 # int | paymentTypeId
    put_payment_types_payment_type_id_request = fineract_client.PutPaymentTypesPaymentTypeIdRequest() # PutPaymentTypesPaymentTypeIdRequest | 

    try:
        # Update a Payment Type
        api_response = api_instance.update_payment_type(payment_type_id, put_payment_types_payment_type_id_request)
        print("The response of PaymentTypeApi->update_payment_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTypeApi->update_payment_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_type_id** | **int**| paymentTypeId | 
 **put_payment_types_payment_type_id_request** | [**PutPaymentTypesPaymentTypeIdRequest**](PutPaymentTypesPaymentTypeIdRequest.md)|  | 

### Return type

[**PutPaymentTypesPaymentTypeIdResponse**](PutPaymentTypesPaymentTypeIdResponse.md)

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

