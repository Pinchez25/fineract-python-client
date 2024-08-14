# fineract_client.FixedDepositProductApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create11**](FixedDepositProductApi.md#create11) | **POST** /v1/fixeddepositproducts | Create a Fixed Deposit Product
[**delete16**](FixedDepositProductApi.md#delete16) | **DELETE** /v1/fixeddepositproducts/{productId} | Delete a Fixed Deposit Product
[**retrieve_all30**](FixedDepositProductApi.md#retrieve_all30) | **GET** /v1/fixeddepositproducts | List Fixed Deposit Products
[**retrieve_one20**](FixedDepositProductApi.md#retrieve_one20) | **GET** /v1/fixeddepositproducts/{productId} | Retrieve a Fixed Deposit Product
[**retrieve_template15**](FixedDepositProductApi.md#retrieve_template15) | **GET** /v1/fixeddepositproducts/template | 
[**update17**](FixedDepositProductApi.md#update17) | **PUT** /v1/fixeddepositproducts/{productId} | Update a Fixed Deposit Product

# **create11**
> PostFixedDepositProductsResponse create11(body)

Create a Fixed Deposit Product

Creates a Fixed Deposit Product  Mandatory Fields: name, shortName, description, currencyCode, digitsAfterDecimal,inMultiplesOf, interestCompoundingPeriodType, interestCalculationType, interestCalculationDaysInYearType, minDepositTerm, minDepositTermTypeId, accountingRule  Optional Fields: lockinPeriodFrequency, lockinPeriodFrequencyType, maxDepositTerm, maxDepositTermTypeId, inMultiplesOfDepositTerm, inMultiplesOfDepositTermTypeId, preClosurePenalApplicable, preClosurePenalInterest, preClosurePenalInterestOnTypeId, feeToIncomeAccountMappings, penaltyToIncomeAccountMappings, charges, charts, , withHoldTax, taxGroupId   Mandatory Fields for Cash based accounting (accountingRule = 2): savingsReferenceAccountId, savingsControlAccountId, interestOnSavingsAccountId, incomeFromFeeAccountId, transfersInSuspenseAccountId, incomeFromPenaltyAccountId

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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostFixedDepositProductsRequest() # PostFixedDepositProductsRequest | 

try:
    # Create a Fixed Deposit Product
    api_response = api_instance.create11(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->create11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostFixedDepositProductsRequest**](PostFixedDepositProductsRequest.md)|  | 

### Return type

[**PostFixedDepositProductsResponse**](PostFixedDepositProductsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete16**
> DeleteFixedDepositProductsProductIdResponse delete16(product_id)

Delete a Fixed Deposit Product

Deletes a Fixed Deposit Product

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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId

try:
    # Delete a Fixed Deposit Product
    api_response = api_instance.delete16(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->delete16: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 

### Return type

[**DeleteFixedDepositProductsProductIdResponse**](DeleteFixedDepositProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all30**
> list[GetFixedDepositProductsResponse] retrieve_all30()

List Fixed Deposit Products

Lists Fixed Deposit Products  Example Requests:  fixeddepositproducts   fixeddepositproducts?fields=name

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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))

try:
    # List Fixed Deposit Products
    api_response = api_instance.retrieve_all30()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->retrieve_all30: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetFixedDepositProductsResponse]**](GetFixedDepositProductsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one20**
> GetFixedDepositProductsProductIdResponse retrieve_one20(product_id)

Retrieve a Fixed Deposit Product

Retrieves a Fixed Deposit Product  Example Requests:  fixeddepositproducts/1   fixeddepositproducts/1?template=true   fixeddepositproducts/1?fields=name,description

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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))
product_id = 789 # int | productId

try:
    # Retrieve a Fixed Deposit Product
    api_response = api_instance.retrieve_one20(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->retrieve_one20: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 

### Return type

[**GetFixedDepositProductsProductIdResponse**](GetFixedDepositProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template15**
> str retrieve_template15()



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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_template15()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->retrieve_template15: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update17**
> PutFixedDepositProductsProductIdResponse update17(body, product_id)

Update a Fixed Deposit Product

Updates a Fixed Deposit Product

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
api_instance = fineract_client.FixedDepositProductApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutFixedDepositProductsProductIdRequest() # PutFixedDepositProductsProductIdRequest | 
product_id = 789 # int | productId

try:
    # Update a Fixed Deposit Product
    api_response = api_instance.update17(body, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FixedDepositProductApi->update17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutFixedDepositProductsProductIdRequest**](PutFixedDepositProductsProductIdRequest.md)|  | 
 **product_id** | **int**| productId | 

### Return type

[**PutFixedDepositProductsProductIdResponse**](PutFixedDepositProductsProductIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

