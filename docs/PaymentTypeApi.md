# fineract_client.PaymentTypeApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_type**](PaymentTypeApi.md#create_payment_type) | **POST** /v1/paymenttypes | Create a Payment Type
[**delete_code1**](PaymentTypeApi.md#delete_code1) | **DELETE** /v1/paymenttypes/{paymentTypeId} | Delete a Payment Type
[**get_all_payment_types**](PaymentTypeApi.md#get_all_payment_types) | **GET** /v1/paymenttypes | Retrieve all Payment Types
[**retrieve_one_payment_type**](PaymentTypeApi.md#retrieve_one_payment_type) | **GET** /v1/paymenttypes/{paymentTypeId} | Retrieve a Payment Type
[**update_payment_type**](PaymentTypeApi.md#update_payment_type) | **PUT** /v1/paymenttypes/{paymentTypeId} | Update a Payment Type

# **create_payment_type**
> PostPaymentTypesResponse create_payment_type(body)

Create a Payment Type

Creates a new Payment type  Mandatory Fields: name  Optional Fields: Description, isCashPayment,Position

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
api_instance = fineract_client.PaymentTypeApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostPaymentTypesRequest() # PostPaymentTypesRequest | 

try:
    # Create a Payment Type
    api_response = api_instance.create_payment_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTypeApi->create_payment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPaymentTypesRequest**](PostPaymentTypesRequest.md)|  | 

### Return type

[**PostPaymentTypesResponse**](PostPaymentTypesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_code1**
> DeletePaymentTypesPaymentTypeIdResponse delete_code1(payment_type_id)

Delete a Payment Type

Deletes payment type

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
api_instance = fineract_client.PaymentTypeApi(fineract_client.ApiClient(configuration))
payment_type_id = 789 # int | paymentTypeId

try:
    # Delete a Payment Type
    api_response = api_instance.delete_code1(payment_type_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_types**
> list[GetPaymentTypesResponse] get_all_payment_types(only_with_code=only_with_code)

Retrieve all Payment Types

Retrieve list of payment types

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
api_instance = fineract_client.PaymentTypeApi(fineract_client.ApiClient(configuration))
only_with_code = true # bool | onlyWithCode (optional)

try:
    # Retrieve all Payment Types
    api_response = api_instance.get_all_payment_types(only_with_code=only_with_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTypeApi->get_all_payment_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_with_code** | **bool**| onlyWithCode | [optional] 

### Return type

[**list[GetPaymentTypesResponse]**](GetPaymentTypesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one_payment_type**
> GetPaymentTypesPaymentTypeIdResponse retrieve_one_payment_type(payment_type_id)

Retrieve a Payment Type

Retrieves a payment type

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
api_instance = fineract_client.PaymentTypeApi(fineract_client.ApiClient(configuration))
payment_type_id = 789 # int | paymentTypeId

try:
    # Retrieve a Payment Type
    api_response = api_instance.retrieve_one_payment_type(payment_type_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_type**
> PutPaymentTypesPaymentTypeIdResponse update_payment_type(body, payment_type_id)

Update a Payment Type

Updates a Payment Type

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
api_instance = fineract_client.PaymentTypeApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutPaymentTypesPaymentTypeIdRequest() # PutPaymentTypesPaymentTypeIdRequest | 
payment_type_id = 789 # int | paymentTypeId

try:
    # Update a Payment Type
    api_response = api_instance.update_payment_type(body, payment_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentTypeApi->update_payment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPaymentTypesPaymentTypeIdRequest**](PutPaymentTypesPaymentTypeIdRequest.md)|  | 
 **payment_type_id** | **int**| paymentTypeId | 

### Return type

[**PutPaymentTypesPaymentTypeIdResponse**](PutPaymentTypesPaymentTypeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

