# fineract_client.SavingsProductApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create13**](SavingsProductApi.md#create13) | **POST** /v1/savingsproducts | Create a Savings Product
[**delete21**](SavingsProductApi.md#delete21) | **DELETE** /v1/savingsproducts/{productId} | Delete a Savings Product
[**retrieve_all34**](SavingsProductApi.md#retrieve_all34) | **GET** /v1/savingsproducts | List Savings Products
[**retrieve_one27**](SavingsProductApi.md#retrieve_one27) | **GET** /v1/savingsproducts/{productId} | Retrieve a Savings Product
[**retrieve_template20**](SavingsProductApi.md#retrieve_template20) | **GET** /v1/savingsproducts/template | Retrieve Savings Product Template
[**update22**](SavingsProductApi.md#update22) | **PUT** /v1/savingsproducts/{productId} | Update a Savings Product

# **create13**
> PostSavingsProductsResponse create13(body)

Create a Savings Product

Creates a Savings Product  Mandatory Fields: name, shortName, description, currencyCode, digitsAfterDecimal,inMultiplesOf, nominalAnnualInterestRate, interestCompoundingPeriodType, interestCalculationType, interestCalculationDaysInYearType,accountingRule  Mandatory Fields for Cash based accounting (accountingRule = 2): savingsReferenceAccountId, savingsControlAccountId, interestOnSavingsAccountId, incomeFromFeeAccountId, transfersInSuspenseAccountId, incomeFromPenaltyAccountId  Optional Fields: minRequiredOpeningBalance, lockinPeriodFrequency, lockinPeriodFrequencyType, withdrawalFeeForTransfers, paymentChannelToFundSourceMappings, feeToIncomeAccountMappings, penaltyToIncomeAccountMappings, charges, allowOverdraft, overdraftLimit, minBalanceForInterestCalculation,withHoldTax,taxGroupId,accountMapping, lienAllowed, maxAllowedLienLimit

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSavingsProductsRequest() # PostSavingsProductsRequest | 

try:
    # Create a Savings Product
    api_response = api_instance.create13(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->create13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSavingsProductsRequest**](PostSavingsProductsRequest.md)|  | 

### Return type

[**PostSavingsProductsResponse**](PostSavingsProductsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete21**
> DeleteSavingsProductsProductIdResponse delete21(product_id)

Delete a Savings Product

Deletes a Savings Product

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId

try:
    # Delete a Savings Product
    api_response = api_instance.delete21(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->delete21: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 

### Return type

[**DeleteSavingsProductsProductIdResponse**](DeleteSavingsProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all34**
> list[GetSavingsProductsResponse] retrieve_all34()

List Savings Products

Lists Savings Products  Example Requests:  savingsproducts  savingsproducts?fields=name

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))

try:
    # List Savings Products
    api_response = api_instance.retrieve_all34()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->retrieve_all34: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetSavingsProductsResponse]**](GetSavingsProductsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one27**
> GetSavingsProductsProductIdResponse retrieve_one27(product_id)

Retrieve a Savings Product

Retrieves a Savings Product  Example Requests:  savingsproducts/1  savingsproducts/1?template=true  savingsproducts/1?fields=name,description

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId

try:
    # Retrieve a Savings Product
    api_response = api_instance.retrieve_one27(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->retrieve_one27: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 

### Return type

[**GetSavingsProductsProductIdResponse**](GetSavingsProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template20**
> GetSavingsProductsTemplateResponse retrieve_template20()

Retrieve Savings Product Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request: Account Mapping:  savingsproducts/template

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve Savings Product Template
    api_response = api_instance.retrieve_template20()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->retrieve_template20: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSavingsProductsTemplateResponse**](GetSavingsProductsTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update22**
> PutSavingsProductsProductIdResponse update22(body, product_id)

Update a Savings Product

Updates a Savings Product

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
api_instance = fineract_client.SavingsProductApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutSavingsProductsProductIdRequest() # PutSavingsProductsProductIdRequest | 
product_id = 789 # int | productId

try:
    # Update a Savings Product
    api_response = api_instance.update22(body, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsProductApi->update22: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSavingsProductsProductIdRequest**](PutSavingsProductsProductIdRequest.md)|  | 
 **product_id** | **int**| productId | 

### Return type

[**PutSavingsProductsProductIdResponse**](PutSavingsProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

