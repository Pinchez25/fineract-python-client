# fineract_client.LoanProductsApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan_product**](LoanProductsApi.md#create_loan_product) | **POST** /v1/loanproducts | Create a Loan Product
[**retrieve_all_loan_products**](LoanProductsApi.md#retrieve_all_loan_products) | **GET** /v1/loanproducts | List Loan Products
[**retrieve_loan_product_details**](LoanProductsApi.md#retrieve_loan_product_details) | **GET** /v1/loanproducts/{productId} | Retrieve a Loan Product
[**retrieve_loan_product_details1**](LoanProductsApi.md#retrieve_loan_product_details1) | **GET** /v1/loanproducts/external-id/{externalProductId} | Retrieve a Loan Product
[**retrieve_template11**](LoanProductsApi.md#retrieve_template11) | **GET** /v1/loanproducts/template | Retrieve Loan Product Details Template
[**update_loan_product**](LoanProductsApi.md#update_loan_product) | **PUT** /v1/loanproducts/{productId} | Update a Loan Product
[**update_loan_product1**](LoanProductsApi.md#update_loan_product1) | **PUT** /v1/loanproducts/external-id/{externalProductId} | Update a Loan Product


# **create_loan_product**
> PostLoanProductsResponse create_loan_product(post_loan_products_request)

Create a Loan Product

Depending of the Accounting Rule (accountingRule) selected, additional fields with details of the appropriate Ledger Account identifiers would need to be passed in.  Refer MifosX Accounting Specs Draft for more details regarding the significance of the selected accounting rule  Mandatory Fields: name, shortName, currencyCode, digitsAfterDecimal, inMultiplesOf, principal, numberOfRepayments, repaymentEvery, repaymentFrequencyType, interestRatePerPeriod, interestRateFrequencyType, amortizationType, interestType, interestCalculationPeriodType, transactionProcessingStrategyCode, accountingRule, isInterestRecalculationEnabled, daysInYearType, daysInMonthType  Optional Fields: inArrearsTolerance, graceOnPrincipalPayment, graceOnInterestPayment, graceOnInterestCharged, graceOnArrearsAgeing, charges, paymentChannelToFundSourceMappings, feeToIncomeAccountMappings, penaltyToIncomeAccountMappings, includeInBorrowerCycle, useBorrowerCycle,principalVariationsForBorrowerCycle, numberOfRepaymentVariationsForBorrowerCycle, interestRateVariationsForBorrowerCycle, multiDisburseLoan,maxTrancheCount, outstandingLoanBalance,overdueDaysForNPA,holdGuaranteeFunds, principalThresholdForLastInstalment, accountMovesOutOfNPAOnlyOnArrearsCompletion, canDefineInstallmentAmount, installmentAmountInMultiplesOf, allowAttributeOverrides, allowPartialPeriodInterestCalcualtion,dueDaysForRepaymentEvent,overDueDaysForRepaymentEvent,enableDownPayment,disbursedAmountPercentageDownPayment,enableAutoRepaymentForDownPayment,repaymentStartDateType  Additional Mandatory Fields for Cash(2) based accounting: fundSourceAccountId, loanPortfolioAccountId, interestOnLoanAccountId, incomeFromFeeAccountId, incomeFromPenaltyAccountId, writeOffAccountId, transfersInSuspenseAccountId, overpaymentLiabilityAccountId  Additional Mandatory Fields for periodic (3) and upfront (4)accrual accounting: fundSourceAccountId, loanPortfolioAccountId, interestOnLoanAccountId, incomeFromFeeAccountId, incomeFromPenaltyAccountId, writeOffAccountId, receivableInterestAccountId, receivableFeeAccountId, receivablePenaltyAccountId, transfersInSuspenseAccountId, overpaymentLiabilityAccountId  Additional Mandatory Fields if interest recalculation is enabled(true): interestRecalculationCompoundingMethod, rescheduleStrategyMethod, recalculationRestFrequencyType  Additional Optional Fields if interest recalculation is enabled(true): isArrearsBasedOnOriginalSchedule, preClosureInterestCalculationStrategy  Additional Optional Fields if interest recalculation is enabled(true) and recalculationRestFrequencyType is not same as repayment period: recalculationRestFrequencyInterval, recalculationRestFrequencyDate  Additional Optional Fields if interest recalculation is enabled(true) and interestRecalculationCompoundingMethod is enabled: recalculationCompoundingFrequencyType  Additional Optional Fields if interest recalculation is enabled(true) and interestRecalculationCompoundingMethod is enabled and recalculationCompoundingFrequencyType is not same as repayment period: recalculationCompoundingFrequencyInterval, recalculationCompoundingFrequencyDate  Additional Mandatory Fields if Hold Guarantee funds is enabled(true): mandatoryGuarantee  Additional Optional Fields if Hold Guarantee funds is enabled(true): minimumGuaranteeFromOwnFunds,minimumGuaranteeFromGuarantor

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loan_products_request import PostLoanProductsRequest
from fineract_client.models.post_loan_products_response import PostLoanProductsResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    post_loan_products_request = fineract_client.PostLoanProductsRequest() # PostLoanProductsRequest | 

    try:
        # Create a Loan Product
        api_response = api_instance.create_loan_product(post_loan_products_request)
        print("The response of LoanProductsApi->create_loan_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->create_loan_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_loan_products_request** | [**PostLoanProductsRequest**](PostLoanProductsRequest.md)|  | 

### Return type

[**PostLoanProductsResponse**](PostLoanProductsResponse.md)

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

# **retrieve_all_loan_products**
> List[GetLoanProductsResponse] retrieve_all_loan_products()

List Loan Products

Lists Loan Products  Example Requests:  loanproducts   loanproducts?fields=name,description,interestRateFrequencyType,amortizationType

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_products_response import GetLoanProductsResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)

    try:
        # List Loan Products
        api_response = api_instance.retrieve_all_loan_products()
        print("The response of LoanProductsApi->retrieve_all_loan_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->retrieve_all_loan_products: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetLoanProductsResponse]**](GetLoanProductsResponse.md)

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

# **retrieve_loan_product_details**
> GetLoanProductsProductIdResponse retrieve_loan_product_details(product_id)

Retrieve a Loan Product

Retrieves a Loan Product  Example Requests:  loanproducts/1   loanproducts/1?template=true   loanproducts/1?fields=name,description,numberOfRepayments

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_products_product_id_response import GetLoanProductsProductIdResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    product_id = 56 # int | productId

    try:
        # Retrieve a Loan Product
        api_response = api_instance.retrieve_loan_product_details(product_id)
        print("The response of LoanProductsApi->retrieve_loan_product_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->retrieve_loan_product_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 

### Return type

[**GetLoanProductsProductIdResponse**](GetLoanProductsProductIdResponse.md)

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

# **retrieve_loan_product_details1**
> GetLoanProductsProductIdResponse retrieve_loan_product_details1(external_product_id)

Retrieve a Loan Product

Retrieves a Loan Product  Example Requests:  loanproducts/external-id/2075e308-d4a8-44d9-8203-f5a947b8c2f4   loanproducts/external-id/2075e308-d4a8-44d9-8203-f5a947b8c2f4?template=true   loanproducts/external-id/2075e308-d4a8-44d9-8203-f5a947b8c2f4?fields=name,description,numberOfRepayments

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_products_product_id_response import GetLoanProductsProductIdResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    external_product_id = 'external_product_id_example' # str | externalProductId

    try:
        # Retrieve a Loan Product
        api_response = api_instance.retrieve_loan_product_details1(external_product_id)
        print("The response of LoanProductsApi->retrieve_loan_product_details1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->retrieve_loan_product_details1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_product_id** | **str**| externalProductId | 

### Return type

[**GetLoanProductsProductIdResponse**](GetLoanProductsProductIdResponse.md)

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

# **retrieve_template11**
> GetLoanProductsTemplateResponse retrieve_template11(is_product_mix_template=is_product_mix_template)

Retrieve Loan Product Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  loanproducts/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loan_products_template_response import GetLoanProductsTemplateResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    is_product_mix_template = True # bool | isProductMixTemplate (optional)

    try:
        # Retrieve Loan Product Details Template
        api_response = api_instance.retrieve_template11(is_product_mix_template=is_product_mix_template)
        print("The response of LoanProductsApi->retrieve_template11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->retrieve_template11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_product_mix_template** | **bool**| isProductMixTemplate | [optional] 

### Return type

[**GetLoanProductsTemplateResponse**](GetLoanProductsTemplateResponse.md)

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

# **update_loan_product**
> PutLoanProductsProductIdResponse update_loan_product(product_id, put_loan_products_product_id_request)

Update a Loan Product

Updates a Loan Product

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_loan_products_product_id_request import PutLoanProductsProductIdRequest
from fineract_client.models.put_loan_products_product_id_response import PutLoanProductsProductIdResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    product_id = 56 # int | productId
    put_loan_products_product_id_request = fineract_client.PutLoanProductsProductIdRequest() # PutLoanProductsProductIdRequest | 

    try:
        # Update a Loan Product
        api_response = api_instance.update_loan_product(product_id, put_loan_products_product_id_request)
        print("The response of LoanProductsApi->update_loan_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->update_loan_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| productId | 
 **put_loan_products_product_id_request** | [**PutLoanProductsProductIdRequest**](PutLoanProductsProductIdRequest.md)|  | 

### Return type

[**PutLoanProductsProductIdResponse**](PutLoanProductsProductIdResponse.md)

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

# **update_loan_product1**
> PutLoanProductsProductIdResponse update_loan_product1(external_product_id, put_loan_products_product_id_request)

Update a Loan Product

Updates a Loan Product

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_loan_products_product_id_request import PutLoanProductsProductIdRequest
from fineract_client.models.put_loan_products_product_id_response import PutLoanProductsProductIdResponse
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
    api_instance = fineract_client.LoanProductsApi(api_client)
    external_product_id = 'external_product_id_example' # str | externalProductId
    put_loan_products_product_id_request = fineract_client.PutLoanProductsProductIdRequest() # PutLoanProductsProductIdRequest | 

    try:
        # Update a Loan Product
        api_response = api_instance.update_loan_product1(external_product_id, put_loan_products_product_id_request)
        print("The response of LoanProductsApi->update_loan_product1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanProductsApi->update_loan_product1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_product_id** | **str**| externalProductId | 
 **put_loan_products_product_id_request** | [**PutLoanProductsProductIdRequest**](PutLoanProductsProductIdRequest.md)|  | 

### Return type

[**PutLoanProductsProductIdResponse**](PutLoanProductsProductIdResponse.md)

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

