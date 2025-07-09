# fineract_client.SavingsChargesApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_savings_account_charge**](SavingsChargesApi.md#add_savings_account_charge) | **POST** /v1/savingsaccounts/{savingsAccountId}/charges | Create a Savings account Charge
[**delete_savings_account_charge**](SavingsChargesApi.md#delete_savings_account_charge) | **DELETE** /v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId} | Delete a Savings account Charge
[**pay_or_waive_savings_account_charge**](SavingsChargesApi.md#pay_or_waive_savings_account_charge) | **POST** /v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId} | Pay a Savings account Charge | Waive off a Savings account Charge | Inactivate a Savings account Charge
[**retrieve_all_savings_account_charges**](SavingsChargesApi.md#retrieve_all_savings_account_charges) | **GET** /v1/savingsaccounts/{savingsAccountId}/charges | List Savings Charges
[**retrieve_savings_account_charge**](SavingsChargesApi.md#retrieve_savings_account_charge) | **GET** /v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId} | Retrieve a Savings account Charge
[**retrieve_template18**](SavingsChargesApi.md#retrieve_template18) | **GET** /v1/savingsaccounts/{savingsAccountId}/charges/template | Retrieve Savings Charges Template
[**update_savings_account_charge**](SavingsChargesApi.md#update_savings_account_charge) | **PUT** /v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId} | Update a Savings account Charge


# **add_savings_account_charge**
> PostSavingsAccountsSavingsAccountIdChargesResponse add_savings_account_charge(savings_account_id, post_savings_accounts_savings_account_id_charges_request)

Create a Savings account Charge

Creates a Savings account Charge  Mandatory Fields for Savings account Charges: chargeId, amount  chargeId, amount, dueDate, dateFormat, locale  chargeId, amount, feeOnMonthDay, monthDayFormat, locale

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_accounts_savings_account_id_charges_request import PostSavingsAccountsSavingsAccountIdChargesRequest
from fineract_client.models.post_savings_accounts_savings_account_id_charges_response import PostSavingsAccountsSavingsAccountIdChargesResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    post_savings_accounts_savings_account_id_charges_request = fineract_client.PostSavingsAccountsSavingsAccountIdChargesRequest() # PostSavingsAccountsSavingsAccountIdChargesRequest | 

    try:
        # Create a Savings account Charge
        api_response = api_instance.add_savings_account_charge(savings_account_id, post_savings_accounts_savings_account_id_charges_request)
        print("The response of SavingsChargesApi->add_savings_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->add_savings_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **post_savings_accounts_savings_account_id_charges_request** | [**PostSavingsAccountsSavingsAccountIdChargesRequest**](PostSavingsAccountsSavingsAccountIdChargesRequest.md)|  | 

### Return type

[**PostSavingsAccountsSavingsAccountIdChargesResponse**](PostSavingsAccountsSavingsAccountIdChargesResponse.md)

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

# **delete_savings_account_charge**
> DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse delete_savings_account_charge(savings_account_id, savings_account_charge_id)

Delete a Savings account Charge

Note: Currently, A Savings account Charge may only be removed from Savings that are not yet approved.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    savings_account_charge_id = 56 # int | savingsAccountChargeId

    try:
        # Delete a Savings account Charge
        api_response = api_instance.delete_savings_account_charge(savings_account_id, savings_account_charge_id)
        print("The response of SavingsChargesApi->delete_savings_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->delete_savings_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **savings_account_charge_id** | **int**| savingsAccountChargeId | 

### Return type

[**DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse**](DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.md)

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

# **pay_or_waive_savings_account_charge**
> PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse pay_or_waive_savings_account_charge(savings_account_id, savings_account_charge_id, post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request, command=command)

Pay a Savings account Charge | Waive off a Savings account Charge | Inactivate a Savings account Charge

Pay a Savings account Charge:  An active charge will be paid when savings account is active and having sufficient balance.  Waive off a Savings account Charge:  Outstanding charge amount will be waived off.  Inactivate a Savings account Charge:  A charge will be allowed to inactivate when savings account is active and not having any dues as of today. If charge is overpaid, corresponding charge payment transactions will be reversed.  Showing request/response for 'Pay a Savings account Charge'

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request import PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest
from fineract_client.models.post_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    savings_account_charge_id = 56 # int | savingsAccountChargeId
    post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request = fineract_client.PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest() # PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest | 
    command = 'command_example' # str | command (optional)

    try:
        # Pay a Savings account Charge | Waive off a Savings account Charge | Inactivate a Savings account Charge
        api_response = api_instance.pay_or_waive_savings_account_charge(savings_account_id, savings_account_charge_id, post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request, command=command)
        print("The response of SavingsChargesApi->pay_or_waive_savings_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->pay_or_waive_savings_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **savings_account_charge_id** | **int**| savingsAccountChargeId | 
 **post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request** | [**PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest**](PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.md)|  | 
 **command** | **str**| command | [optional] 

### Return type

[**PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse**](PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.md)

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

# **retrieve_all_savings_account_charges**
> List[GetSavingsAccountsSavingsAccountIdChargesResponse] retrieve_all_savings_account_charges(savings_account_id, charge_status=charge_status)

List Savings Charges

Lists Savings Charges  Example Requests:  savingsaccounts/1/charges  savingsaccounts/1/charges?chargeStatus=all  savingsaccounts/1/charges?chargeStatus=inactive  savingsaccounts/1/charges?chargeStatus=active  savingsaccounts/1/charges?fields=name,amountOrPercentage

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_savings_account_id_charges_response import GetSavingsAccountsSavingsAccountIdChargesResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    charge_status = 'all' # str | chargeStatus (optional) (default to 'all')

    try:
        # List Savings Charges
        api_response = api_instance.retrieve_all_savings_account_charges(savings_account_id, charge_status=charge_status)
        print("The response of SavingsChargesApi->retrieve_all_savings_account_charges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->retrieve_all_savings_account_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to &#39;all&#39;]

### Return type

[**List[GetSavingsAccountsSavingsAccountIdChargesResponse]**](GetSavingsAccountsSavingsAccountIdChargesResponse.md)

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

# **retrieve_savings_account_charge**
> GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse retrieve_savings_account_charge(savings_account_id, savings_account_charge_id)

Retrieve a Savings account Charge

Retrieves a Savings account Charge  Example Requests:  /savingsaccounts/1/charges/5   /savingsaccounts/1/charges/5?fields=name,amountOrPercentage

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    savings_account_charge_id = 56 # int | savingsAccountChargeId

    try:
        # Retrieve a Savings account Charge
        api_response = api_instance.retrieve_savings_account_charge(savings_account_id, savings_account_charge_id)
        print("The response of SavingsChargesApi->retrieve_savings_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->retrieve_savings_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **savings_account_charge_id** | **int**| savingsAccountChargeId | 

### Return type

[**GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse**](GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.md)

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

# **retrieve_template18**
> GetSavingsAccountsSavingsAccountIdChargesTemplateResponse retrieve_template18(savings_account_id)

Retrieve Savings Charges Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  savingsaccounts/1/charges/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_savings_accounts_savings_account_id_charges_template_response import GetSavingsAccountsSavingsAccountIdChargesTemplateResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId

    try:
        # Retrieve Savings Charges Template
        api_response = api_instance.retrieve_template18(savings_account_id)
        print("The response of SavingsChargesApi->retrieve_template18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->retrieve_template18: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 

### Return type

[**GetSavingsAccountsSavingsAccountIdChargesTemplateResponse**](GetSavingsAccountsSavingsAccountIdChargesTemplateResponse.md)

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

# **update_savings_account_charge**
> PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse update_savings_account_charge(savings_account_id, savings_account_charge_id, put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request)

Update a Savings account Charge

Currently Savings account Charges may be updated only if the Savings account is not yet approved.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request import PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest
from fineract_client.models.put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
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
    api_instance = fineract_client.SavingsChargesApi(api_client)
    savings_account_id = 56 # int | savingsAccountId
    savings_account_charge_id = 56 # int | savingsAccountChargeId
    put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request = fineract_client.PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest() # PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest | 

    try:
        # Update a Savings account Charge
        api_response = api_instance.update_savings_account_charge(savings_account_id, savings_account_charge_id, put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request)
        print("The response of SavingsChargesApi->update_savings_account_charge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavingsChargesApi->update_savings_account_charge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **savings_account_id** | **int**| savingsAccountId | 
 **savings_account_charge_id** | **int**| savingsAccountChargeId | 
 **put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request** | [**PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest**](PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.md)|  | 

### Return type

[**PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse**](PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.md)

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

