# fineract_client.ClientChargesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_client_charge**](ClientChargesApi.md#apply_client_charge) | **POST** /v1/clients/{clientId}/charges | Add Client Charge
[**delete_client_charge**](ClientChargesApi.md#delete_client_charge) | **DELETE** /v1/clients/{clientId}/charges/{chargeId} | Delete a Client Charge
[**pay_or_waive_client_charge**](ClientChargesApi.md#pay_or_waive_client_charge) | **POST** /v1/clients/{clientId}/charges/{chargeId} | Pay a Client Charge | Waive a Client Charge
[**retrieve_all_client_charges**](ClientChargesApi.md#retrieve_all_client_charges) | **GET** /v1/clients/{clientId}/charges | List Client Charges
[**retrieve_client_charge**](ClientChargesApi.md#retrieve_client_charge) | **GET** /v1/clients/{clientId}/charges/{chargeId} | Retrieve a Client Charge
[**retrieve_template4**](ClientChargesApi.md#retrieve_template4) | **GET** /v1/clients/{clientId}/charges/template | 


# **apply_client_charge**
> PostClientsClientIdChargesResponse apply_client_charge(client_id, post_clients_client_id_charges_request)

Add Client Charge

 This API associates a Client charge with an implicit Client account
Mandatory Fields : 
chargeId and dueDate  
Optional Fields : 
amount

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_charges_request import PostClientsClientIdChargesRequest
from fineract_client.models.post_clients_client_id_charges_response import PostClientsClientIdChargesResponse
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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId
    post_clients_client_id_charges_request = fineract_client.PostClientsClientIdChargesRequest() # PostClientsClientIdChargesRequest | 

    try:
        # Add Client Charge
        api_response = api_instance.apply_client_charge(client_id, post_clients_client_id_charges_request)
        print("The response of ClientChargesApi->apply_client_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientChargesApi->apply_client_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **post_clients_client_id_charges_request** | [**PostClientsClientIdChargesRequest**](PostClientsClientIdChargesRequest.md)|  | 

### Return type

[**PostClientsClientIdChargesResponse**](PostClientsClientIdChargesResponse.md)

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

# **delete_client_charge**
> DeleteClientsClientIdChargesChargeIdResponse delete_client_charge(client_id, charge_id)

Delete a Client Charge

Deletes a Client Charge on which no transactions have taken place (either payments or waivers).

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_clients_client_id_charges_charge_id_response import DeleteClientsClientIdChargesChargeIdResponse
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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId
    charge_id = 56 # int | chargeId

    try:
        # Delete a Client Charge
        api_response = api_instance.delete_client_charge(client_id, charge_id)
        print("The response of ClientChargesApi->delete_client_charge:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_or_waive_client_charge**
> PostClientsClientIdChargesChargeIdResponse pay_or_waive_client_charge(client_id, charge_id, post_clients_client_id_charges_charge_id_request, command=command)

Pay a Client Charge | Waive a Client Charge

Pay a Client Charge:

Mandatory Fields:transactionDate and amount "Pay either a part of or the entire due amount for a charge.(command=paycharge)

Waive a Client Charge:


This API provides the facility of waiving off the remaining amount on a client charge (command=waive)

Showing request/response for 'Pay a Client Charge'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_clients_client_id_charges_charge_id_request import PostClientsClientIdChargesChargeIdRequest
from fineract_client.models.post_clients_client_id_charges_charge_id_response import PostClientsClientIdChargesChargeIdResponse
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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId
    charge_id = 56 # int | chargeId
    post_clients_client_id_charges_charge_id_request = fineract_client.PostClientsClientIdChargesChargeIdRequest() # PostClientsClientIdChargesChargeIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Pay a Client Charge | Waive a Client Charge
        api_response = api_instance.pay_or_waive_client_charge(client_id, charge_id, post_clients_client_id_charges_charge_id_request, command=command)
        print("The response of ClientChargesApi->pay_or_waive_client_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientChargesApi->pay_or_waive_client_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_id** | **int**| chargeId | 
 **post_clients_client_id_charges_charge_id_request** | [**PostClientsClientIdChargesChargeIdRequest**](PostClientsClientIdChargesChargeIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostClientsClientIdChargesChargeIdResponse**](PostClientsClientIdChargesChargeIdResponse.md)

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

# **retrieve_all_client_charges**
> GetClientsClientIdChargesResponse retrieve_all_client_charges(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)

List Client Charges

The list capability of client charges supports pagination.Example Requests:
clients/1/charges

clients/1/charges?offset=0&limit=5

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_client_id_charges_response import GetClientsClientIdChargesResponse
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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')
    pending_payment = True # bool | pendingPayment (optional)
    limit = 56 # int | limit (optional)
    offset = 56 # int | offset (optional)

    try:
        # List Client Charges
        api_response = api_instance.retrieve_all_client_charges(client_id, charge_status=charge_status, pending_payment=pending_payment, limit=limit, offset=offset)
        print("The response of ClientChargesApi->retrieve_all_client_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientChargesApi->retrieve_all_client_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_client_charge**
> GetClientsChargesPageItems retrieve_client_charge(client_id, charge_id)

Retrieve a Client Charge

Example Requests:
clients/1/charges/1


clients/1/charges/1?fields=name,id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_clients_charges_page_items import GetClientsChargesPageItems
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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId
    charge_id = 56 # int | chargeId

    try:
        # Retrieve a Client Charge
        api_response = api_instance.retrieve_client_charge(client_id, charge_id)
        print("The response of ClientChargesApi->retrieve_client_charge:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template4**
> str retrieve_template4(client_id)

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
    api_instance = fineract_client.ClientChargesApi(api_client)
    client_id = 56 # int | clientId

    try:
        api_response = api_instance.retrieve_template4(client_id)
        print("The response of ClientChargesApi->retrieve_template4:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

