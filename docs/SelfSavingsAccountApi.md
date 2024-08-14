# fineract_client.SelfSavingsAccountApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_savings_account_application**](SelfSavingsAccountApi.md#modify_savings_account_application) | **PUT** /v1/self/savingsaccounts/{accountId} | 
[**retrieve_all_savings_account_charges1**](SelfSavingsAccountApi.md#retrieve_all_savings_account_charges1) | **GET** /v1/self/savingsaccounts/{accountId}/charges | List Savings Charges
[**retrieve_savings**](SelfSavingsAccountApi.md#retrieve_savings) | **GET** /v1/self/savingsaccounts/{accountId} | Retrieve a savings account
[**retrieve_savings_account_charge1**](SelfSavingsAccountApi.md#retrieve_savings_account_charge1) | **GET** /v1/self/savingsaccounts/{accountId}/charges/{savingsAccountChargeId} | Retrieve a Savings account Charge
[**retrieve_savings_transaction**](SelfSavingsAccountApi.md#retrieve_savings_transaction) | **GET** /v1/self/savingsaccounts/{accountId}/transactions/{transactionId} | Retrieve Savings Account Transaction
[**submit_savings_account_application**](SelfSavingsAccountApi.md#submit_savings_account_application) | **POST** /v1/self/savingsaccounts | 
[**template18**](SelfSavingsAccountApi.md#template18) | **GET** /v1/self/savingsaccounts/template | 

# **modify_savings_account_application**
> str modify_savings_account_application(account_id, body=body, command=command)



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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.modify_savings_account_application(account_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->modify_savings_account_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_savings_account_charges1**
> list[GetSelfSavingsAccountsAccountIdChargesResponse] retrieve_all_savings_account_charges1(account_id, charge_status=charge_status)

List Savings Charges

Lists Savings Charges  Example Requests:  self/savingsaccounts/1/charges  self/savingsaccounts/1/charges?chargeStatus=inactive  self/savingsaccounts/1/charges?fields=name,amountOrPercentage

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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
charge_status = 'all' # str | chargeStatus (optional) (default to all)

try:
    # List Savings Charges
    api_response = api_instance.retrieve_all_savings_account_charges1(account_id, charge_status=charge_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->retrieve_all_savings_account_charges1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to all]

### Return type

[**list[GetSelfSavingsAccountsAccountIdChargesResponse]**](GetSelfSavingsAccountsAccountIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_savings**
> GetSelfSavingsAccountsResponse retrieve_savings(account_id, charge_status=charge_status)

Retrieve a savings account

Retrieves a savings account  Example Requests :  self/savingsaccounts/1   self/savingsaccounts/1?associations=transactions

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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
charge_status = 'all' # str | chargeStatus (optional) (default to all)

try:
    # Retrieve a savings account
    api_response = api_instance.retrieve_savings(account_id, charge_status=charge_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->retrieve_savings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **charge_status** | **str**| chargeStatus | [optional] [default to all]

### Return type

[**GetSelfSavingsAccountsResponse**](GetSelfSavingsAccountsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_savings_account_charge1**
> GetSelfSavingsAccountsAccountIdChargesSavingsAccountChargeIdResponse retrieve_savings_account_charge1(account_id, savings_account_charge_id)

Retrieve a Savings account Charge

Retrieves a Savings account Charge  Example Requests:  self/savingsaccounts/1/charges/5   self/savingsaccounts/1/charges/5?fields=name,amountOrPercentage

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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
savings_account_charge_id = 789 # int | savingsAccountChargeId

try:
    # Retrieve a Savings account Charge
    api_response = api_instance.retrieve_savings_account_charge1(account_id, savings_account_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->retrieve_savings_account_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **savings_account_charge_id** | **int**| savingsAccountChargeId | 

### Return type

[**GetSelfSavingsAccountsAccountIdChargesSavingsAccountChargeIdResponse**](GetSelfSavingsAccountsAccountIdChargesSavingsAccountChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_savings_transaction**
> GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse retrieve_savings_transaction(account_id, transaction_id)

Retrieve Savings Account Transaction

Retrieves Savings Account Transaction  Example Requests:  self/savingsaccounts/1/transactions/1

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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
account_id = 789 # int | accountId
transaction_id = 789 # int | transactionId

try:
    # Retrieve Savings Account Transaction
    api_response = api_instance.retrieve_savings_transaction(account_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->retrieve_savings_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| accountId | 
 **transaction_id** | **int**| transactionId | 

### Return type

[**GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse**](GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_savings_account_application**
> str submit_savings_account_application(body=body, command=command)



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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.submit_savings_account_application(body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->submit_savings_account_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 
 **command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template18**
> str template18(client_id=client_id, product_id=product_id)



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
api_instance = fineract_client.SelfSavingsAccountApi(fineract_client.ApiClient(configuration))
client_id = 789 # int |  (optional)
product_id = 789 # int |  (optional)

try:
    api_response = api_instance.template18(client_id=client_id, product_id=product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfSavingsAccountApi->template18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | [optional] 
 **product_id** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

