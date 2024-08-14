# fineract_client.AccountingRulesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_accounting_rule**](AccountingRulesApi.md#create_accounting_rule) | **POST** /v1/accountingrules | Create/Define a Accounting rule
[**delete_accounting_rule**](AccountingRulesApi.md#delete_accounting_rule) | **DELETE** /v1/accountingrules/{accountingRuleId} | Delete a Accounting Rule
[**retreive_accounting_rule**](AccountingRulesApi.md#retreive_accounting_rule) | **GET** /v1/accountingrules/{accountingRuleId} | Retrieve a Accounting rule
[**retrieve_all_accounting_rules**](AccountingRulesApi.md#retrieve_all_accounting_rules) | **GET** /v1/accountingrules | Retrieve Accounting Rules
[**retrieve_template1**](AccountingRulesApi.md#retrieve_template1) | **GET** /v1/accountingrules/template | Retrieve Accounting Rule Details Template
[**update_accounting_rule**](AccountingRulesApi.md#update_accounting_rule) | **PUT** /v1/accountingrules/{accountingRuleId} | Update a Accounting Rule

# **create_accounting_rule**
> PostAccountingRulesResponse create_accounting_rule(body=body)

Create/Define a Accounting rule

Define a new Accounting rule.  Mandatory Fields name, officeId, accountToDebit OR debitTags, accountToCredit OR creditTags.  Optional Fields description

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostAccountingRulesRequest() # PostAccountingRulesRequest |  (optional)

try:
    # Create/Define a Accounting rule
    api_response = api_instance.create_accounting_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->create_accounting_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountingRulesRequest**](PostAccountingRulesRequest.md)|  | [optional] 

### Return type

[**PostAccountingRulesResponse**](PostAccountingRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounting_rule**
> DeleteAccountingRulesResponse delete_accounting_rule(accounting_rule_id)

Delete a Accounting Rule

Deletes a Accounting rule.

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))
accounting_rule_id = 789 # int | accountingRuleId

try:
    # Delete a Accounting Rule
    api_response = api_instance.delete_accounting_rule(accounting_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->delete_accounting_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_rule_id** | **int**| accountingRuleId | 

### Return type

[**DeleteAccountingRulesResponse**](DeleteAccountingRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retreive_accounting_rule**
> AccountingRuleData retreive_accounting_rule(accounting_rule_id)

Retrieve a Accounting rule

Returns the details of a defined Accounting rule.  Example Requests:  accountingrules/1

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))
accounting_rule_id = 789 # int | accountingRuleId

try:
    # Retrieve a Accounting rule
    api_response = api_instance.retreive_accounting_rule(accounting_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->retreive_accounting_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_rule_id** | **int**| accountingRuleId | 

### Return type

[**AccountingRuleData**](AccountingRuleData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_accounting_rules**
> list[GetAccountRulesResponse] retrieve_all_accounting_rules()

Retrieve Accounting Rules

Returns the list of defined accounting rules.  Example Requests:  accountingrules

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Accounting Rules
    api_response = api_instance.retrieve_all_accounting_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->retrieve_all_accounting_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetAccountRulesResponse]**](GetAccountRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template1**
> GetAccountRulesTemplateResponse retrieve_template1()

Retrieve Accounting Rule Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  accountingrules/template

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Accounting Rule Details Template
    api_response = api_instance.retrieve_template1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->retrieve_template1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAccountRulesTemplateResponse**](GetAccountRulesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accounting_rule**
> PutAccountingRulesResponse update_accounting_rule(accounting_rule_id, body=body)

Update a Accounting Rule

Updates the details of a Accounting rule.

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
api_instance = fineract_client.AccountingRulesApi(fineract_client.ApiClient(configuration))
accounting_rule_id = 789 # int | accountingRuleId
body = fineract_client.PutAccountingRulesRequest() # PutAccountingRulesRequest |  (optional)

try:
    # Update a Accounting Rule
    api_response = api_instance.update_accounting_rule(accounting_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingRulesApi->update_accounting_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_rule_id** | **int**| accountingRuleId | 
 **body** | [**PutAccountingRulesRequest**](PutAccountingRulesRequest.md)|  | [optional] 

### Return type

[**PutAccountingRulesResponse**](PutAccountingRulesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

