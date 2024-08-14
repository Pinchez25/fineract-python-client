# fineract_client.AccountNumberFormatApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AccountNumberFormatApi.md#create) | **POST** /v1/accountnumberformats | Create an Account number format
[**delete**](AccountNumberFormatApi.md#delete) | **DELETE** /v1/accountnumberformats/{accountNumberFormatId} | Delete an Account number format
[**retrieve_all3**](AccountNumberFormatApi.md#retrieve_all3) | **GET** /v1/accountnumberformats | List Account number formats
[**retrieve_one**](AccountNumberFormatApi.md#retrieve_one) | **GET** /v1/accountnumberformats/{accountNumberFormatId} | Retrieve an Account number format
[**retrieve_template2**](AccountNumberFormatApi.md#retrieve_template2) | **GET** /v1/accountnumberformats/template | Retrieve Account number format Template
[**update1**](AccountNumberFormatApi.md#update1) | **PUT** /v1/accountnumberformats/{accountNumberFormatId} | Update an Account number format

# **create**
> PostAccountNumberFormatsResponse create(body=body)

Create an Account number format

Note: You may associate a single Account number format for a given account type Mandatory Fields for Account number formats accountType

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostAccountNumberFormatsRequest() # PostAccountNumberFormatsRequest |  (optional)

try:
    # Create an Account number format
    api_response = api_instance.create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountNumberFormatApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountNumberFormatsRequest**](PostAccountNumberFormatsRequest.md)|  | [optional] 

### Return type

[**PostAccountNumberFormatsResponse**](PostAccountNumberFormatsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteAccountNumberFormatsResponse delete(account_number_format_id)

Delete an Account number format

Note: Account numbers created while this format was active would remain unchanged.

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))
account_number_format_id = 789 # int | accountNumberFormatId

try:
    # Delete an Account number format
    api_response = api_instance.delete(account_number_format_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all3**
> list[GetAccountNumberFormatsIdResponse] retrieve_all3()

List Account number formats

Example Requests:  accountnumberformats   accountnumberformats?fields=accountType,prefixType

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))

try:
    # List Account number formats
    api_response = api_instance.retrieve_all3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountNumberFormatApi->retrieve_all3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetAccountNumberFormatsIdResponse]**](GetAccountNumberFormatsIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one**
> GetAccountNumberFormatsIdResponse retrieve_one(account_number_format_id)

Retrieve an Account number format

Example Requests:  accountnumberformats/1   accountnumberformats/1?template=true   accountnumberformats/1?fields=accountType,prefixType

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))
account_number_format_id = 789 # int | accountNumberFormatId

try:
    # Retrieve an Account number format
    api_response = api_instance.retrieve_one(account_number_format_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template2**
> GetAccountNumberFormatsResponseTemplate retrieve_template2()

Retrieve Account number format Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists  Example Request:  accountnumberformats/template

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Account number format Template
    api_response = api_instance.retrieve_template2()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> PutAccountNumberFormatsResponse update1(body, account_number_format_id)

Update an Account number format

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
api_instance = fineract_client.AccountNumberFormatApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutAccountNumberFormatsRequest() # PutAccountNumberFormatsRequest | 
account_number_format_id = 789 # int | accountNumberFormatId

try:
    # Update an Account number format
    api_response = api_instance.update1(body, account_number_format_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountNumberFormatApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutAccountNumberFormatsRequest**](PutAccountNumberFormatsRequest.md)|  | 
 **account_number_format_id** | **int**| accountNumberFormatId | 

### Return type

[**PutAccountNumberFormatsResponse**](PutAccountNumberFormatsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

