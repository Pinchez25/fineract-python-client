# fineract_client.ClientChargesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_client_charge**](ClientChargesApi.md#apply_client_charge) | **POST** /v1/clients/{clientId}/charges | Add Client Charge
[**delete_client_charge**](ClientChargesApi.md#delete_client_charge) | **DELETE** /v1/clients/{clientId}/charges/{chargeId} | Delete a Client Charge
[**pay_or_waive_client_charge**](ClientChargesApi.md#pay_or_waive_client_charge) | **POST** /v1/clients/{clientId}/charges/{chargeId} | Pay a Client Charge | Waive a Client Charge
[**retrieve_all_client_charges**](ClientChargesApi.md#retrieve_all_client_charges) | **GET** /v1/clients/{clientId}/charges | List Client Charges
[**retrieve_client_charge**](ClientChargesApi.md#retrieve_client_charge) | **GET** /v1/clients/{clientId}/charges/{chargeId} | Retrieve a Client Charge
[**retrieve_template4**](ClientChargesApi.md#retrieve_template4) | **GET** /v1/clients/{clientId}/charges/template | 

# **apply_client_charge**
> PostClientsClientIdChargesResponse apply_client_charge(body, client_id)

Add Client Charge

 This API associates a Client charge with an implicit Client account Mandatory Fields :  chargeId and dueDate   Optional Fields :  amount

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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostClientsClientIdChargesRequest() # PostClientsClientIdChargesRequest | 
client_id = 789 # int | clientId

try:
    # Add Client Charge
    api_response = api_instance.apply_client_charge(body, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->apply_client_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostClientsClientIdChargesRequest**](PostClientsClientIdChargesRequest.md)|  | 
 **client_id** | **int**| clientId | 

### Return type

[**PostClientsClientIdChargesResponse**](PostClientsClientIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_charge**
> DeleteClientsClientIdChargesChargeIdResponse delete_client_charge(client_id, charge_id)

Delete a Client Charge

Deletes a Client Charge on which no transactions have taken place (either payments or waivers).

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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
charge_id = 789 # int | chargeId

try:
    # Delete a Client Charge
    api_response = api_instance.delete_client_charge(client_id, charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->delete_client_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_id** | **int**| chargeId | 

### Return type

[**DeleteClientsClientIdChargesChargeIdResponse**](DeleteClientsClientIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_or_waive_client_charge**
> PostClientsClientIdChargesChargeIdResponse pay_or_waive_client_charge(body, client_id, charge_id, command=command)

Pay a Client Charge | Waive a Client Charge

Pay a Client Charge:  Mandatory Fields:transactionDate and amount \"Pay either a part of or the entire due amount for a charge.(command=paycharge)  Waive a Client Charge:   This API provides the facility of waiving off the remaining amount on a client charge (command=waive)  Showing request/response for 'Pay a Client Charge'

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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostClientsClientIdChargesChargeIdRequest() # PostClientsClientIdChargesChargeIdRequest | 
client_id = 789 # int | clientId
charge_id = 789 # int | chargeId
command = 'command_example' # str | command (optional)

try:
    # Pay a Client Charge | Waive a Client Charge
    api_response = api_instance.pay_or_waive_client_charge(body, client_id, charge_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->pay_or_waive_client_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostClientsClientIdChargesChargeIdRequest**](PostClientsClientIdChargesChargeIdRequest.md)|  | 
 **client_id** | **int**| clientId | 
 **charge_id** | **int**| chargeId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdChargesChargeIdResponse**](PostClientsClientIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_client_charges**
> GetClientsClientIdChargesResponse retrieve_all_client_charges(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)

List Client Charges

The list capability of client charges supports pagination.Example Requests: clients/1/charges  clients/1/charges?offset=0&limit=5

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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
charge_status = 'all' # str | chargeStatus (optional) (default to all)
pending_payment = true # bool | pendingPayment (optional)
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

try:
    # List Client Charges
    api_response = api_instance.retrieve_all_client_charges(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->retrieve_all_client_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to all]
 **pending_payment** | **bool**| pendingPayment | [optional] 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**GetClientsClientIdChargesResponse**](GetClientsClientIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_client_charge**
> GetClientsChargesPageItems retrieve_client_charge(client_id, charge_id)

Retrieve a Client Charge

Example Requests: clients/1/charges/1   clients/1/charges/1?fields=name,id

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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId
charge_id = 789 # int | chargeId

try:
    # Retrieve a Client Charge
    api_response = api_instance.retrieve_client_charge(client_id, charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->retrieve_client_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_id** | **int**| chargeId | 

### Return type

[**GetClientsChargesPageItems**](GetClientsChargesPageItems.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template4**
> str retrieve_template4(client_id)



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
api_instance = fineract_client.ClientChargesApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | clientId

try:
    api_response = api_instance.retrieve_template4(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientChargesApi->retrieve_template4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

