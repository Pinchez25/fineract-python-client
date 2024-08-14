# fineract_client.ChargesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_charge**](ChargesApi.md#create_charge) | **POST** /v1/charges | Create/Define a Charge
[**delete_charge**](ChargesApi.md#delete_charge) | **DELETE** /v1/charges/{chargeId} | Delete a Charge
[**retrieve_all_charges**](ChargesApi.md#retrieve_all_charges) | **GET** /v1/charges | Retrieve Charges
[**retrieve_charge**](ChargesApi.md#retrieve_charge) | **GET** /v1/charges/{chargeId} | Retrieve a Charge
[**retrieve_new_charge_details**](ChargesApi.md#retrieve_new_charge_details) | **GET** /v1/charges/template | Retrieve Charge Template
[**update_charge**](ChargesApi.md#update_charge) | **PUT** /v1/charges/{chargeId} | Update a Charge

# **create_charge**
> PostChargesResponse create_charge(body)

Create/Define a Charge

Define a new charge that can later be associated with loans and savings through their respective product definitions or directly on each account instance.

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostChargesRequest() # PostChargesRequest | 

try:
    # Create/Define a Charge
    api_response = api_instance.create_charge(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->create_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostChargesRequest**](PostChargesRequest.md)|  | 

### Return type

[**PostChargesResponse**](PostChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_charge**
> DeleteChargesChargeIdResponse delete_charge(charge_id)

Delete a Charge

Deletes a Charge.

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))
charge_id = 789 # int | chargeId

try:
    # Delete a Charge
    api_response = api_instance.delete_charge(charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->delete_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **int**| chargeId | 

### Return type

[**DeleteChargesChargeIdResponse**](DeleteChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_charges**
> list[GetChargesResponse] retrieve_all_charges()

Retrieve Charges

Returns the list of defined charges.  Example Requests:  charges

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Charges
    api_response = api_instance.retrieve_all_charges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->retrieve_all_charges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetChargesResponse]**](GetChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_charge**
> GetChargesResponse retrieve_charge(charge_id)

Retrieve a Charge

Returns the details of a defined Charge.  Example Requests:  charges/1

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))
charge_id = 789 # int | chargeId

try:
    # Retrieve a Charge
    api_response = api_instance.retrieve_charge(charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->retrieve_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **int**| chargeId | 

### Return type

[**GetChargesResponse**](GetChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_new_charge_details**
> GetChargesTemplateResponse retrieve_new_charge_details()

Retrieve Charge Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  charges/template 

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Charge Template
    api_response = api_instance.retrieve_new_charge_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->retrieve_new_charge_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetChargesTemplateResponse**](GetChargesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_charge**
> PutChargesChargeIdResponse update_charge(body, charge_id)

Update a Charge

Updates the details of a Charge.

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
api_instance = fineract_client.ChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutChargesChargeIdRequest() # PutChargesChargeIdRequest | 
charge_id = 789 # int | chargeId

try:
    # Update a Charge
    api_response = api_instance.update_charge(body, charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->update_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutChargesChargeIdRequest**](PutChargesChargeIdRequest.md)|  | 
 **charge_id** | **int**| chargeId | 

### Return type

[**PutChargesChargeIdResponse**](PutChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

