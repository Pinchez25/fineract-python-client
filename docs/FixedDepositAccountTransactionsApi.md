# fineract_client.FixedDepositAccountTransactionsApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_transaction**](FixedDepositAccountTransactionsApi.md#adjust_transaction) | **POST** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/{transactionId} | 
[**retrieve_one18**](FixedDepositAccountTransactionsApi.md#retrieve_one18) | **GET** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/{transactionId} | 
[**retrieve_template14**](FixedDepositAccountTransactionsApi.md#retrieve_template14) | **GET** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions/template | 
[**transaction**](FixedDepositAccountTransactionsApi.md#transaction) | **POST** /v1/fixeddepositaccounts/{fixedDepositAccountId}/transactions | 

# **adjust_transaction**
> str adjust_transaction(fixed_deposit_account_id, transaction_id, body=body, command=command)



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
api_instance = fineract_client.FixedDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
fixed_deposit_account_id = 789 # int | 
transaction_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.adjust_transaction(fixed_deposit_account_id, transaction_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositAccountTransactionsApi->adjust_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 
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

# **retrieve_one18**
> str retrieve_one18(fixed_deposit_account_id, transaction_id)



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
api_instance = fineract_client.FixedDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
fixed_deposit_account_id = 789 # int | 
transaction_id = 789 # int | 

try:
    api_response = api_instance.retrieve_one18(fixed_deposit_account_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositAccountTransactionsApi->retrieve_one18: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template14**
> str retrieve_template14(fixed_deposit_account_id)



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
api_instance = fineract_client.FixedDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
fixed_deposit_account_id = 789 # int | 

try:
    api_response = api_instance.retrieve_template14(fixed_deposit_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositAccountTransactionsApi->retrieve_template14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction**
> str transaction(fixed_deposit_account_id, body=body, command=command)



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
api_instance = fineract_client.FixedDepositAccountTransactionsApi(fineract_client.ApiClient(configuration))
fixed_deposit_account_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.transaction(fixed_deposit_account_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositAccountTransactionsApi->transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_deposit_account_id** | **int**|  | 
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

