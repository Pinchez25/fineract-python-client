# fineract_client.LoanCollateralApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collateral**](LoanCollateralApi.md#create_collateral) | **POST** /v1/loans/{loanId}/collaterals | Create a Collateral
[**delete_collateral**](LoanCollateralApi.md#delete_collateral) | **DELETE** /v1/loans/{loanId}/collaterals/{collateralId} | Remove a Collateral
[**new_collateral_template**](LoanCollateralApi.md#new_collateral_template) | **GET** /v1/loans/{loanId}/collaterals/template | Retrieve Collateral Details Template
[**retrieve_collateral_details**](LoanCollateralApi.md#retrieve_collateral_details) | **GET** /v1/loans/{loanId}/collaterals | List Loan Collaterals
[**retrieve_collateral_details1**](LoanCollateralApi.md#retrieve_collateral_details1) | **GET** /v1/loans/{loanId}/collaterals/{collateralId} | Retrieve a Collateral
[**update_collateral**](LoanCollateralApi.md#update_collateral) | **PUT** /v1/loans/{loanId}/collaterals/{collateralId} | Update a Collateral


# **create_collateral**
> PostLoansLoanIdCollateralsResponse create_collateral(loan_id, post_loans_loan_id_collaterals_request)

Create a Collateral

Note: Currently, Collaterals may be added only before a Loan is approved

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_loans_loan_id_collaterals_request import PostLoansLoanIdCollateralsRequest
from fineract_client.models.post_loans_loan_id_collaterals_response import PostLoansLoanIdCollateralsResponse
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId
    post_loans_loan_id_collaterals_request = fineract_client.PostLoansLoanIdCollateralsRequest() # PostLoansLoanIdCollateralsRequest | 

    try:
        # Create a Collateral
        api_response = api_instance.create_collateral(loan_id, post_loans_loan_id_collaterals_request)
        print("The response of LoanCollateralApi->create_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->create_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **post_loans_loan_id_collaterals_request** | [**PostLoansLoanIdCollateralsRequest**](PostLoansLoanIdCollateralsRequest.md)|  | 

### Return type

[**PostLoansLoanIdCollateralsResponse**](PostLoansLoanIdCollateralsResponse.md)

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

# **delete_collateral**
> DeleteLoansLoanIdCollateralsCollateralIdResponse delete_collateral(loan_id, collateral_id)

Remove a Collateral

Note: A collateral can only be removed from Loans that are not yet approved.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.delete_loans_loan_id_collaterals_collateral_id_response import DeleteLoansLoanIdCollateralsCollateralIdResponse
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId
    collateral_id = 56 # int | collateralId

    try:
        # Remove a Collateral
        api_response = api_instance.delete_collateral(loan_id, collateral_id)
        print("The response of LoanCollateralApi->delete_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->delete_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**DeleteLoansLoanIdCollateralsCollateralIdResponse**](DeleteLoansLoanIdCollateralsCollateralIdResponse.md)

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

# **new_collateral_template**
> GetLoansLoanIdCollateralsTemplateResponse new_collateral_template(loan_id)

Retrieve Collateral Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:

Field Defaults
Allowed Value Lists
Example Request:

loans/1/collaterals/template

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_collaterals_template_response import GetLoansLoanIdCollateralsTemplateResponse
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId

    try:
        # Retrieve Collateral Details Template
        api_response = api_instance.new_collateral_template(loan_id)
        print("The response of LoanCollateralApi->new_collateral_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->new_collateral_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**GetLoansLoanIdCollateralsTemplateResponse**](GetLoansLoanIdCollateralsTemplateResponse.md)

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

# **retrieve_collateral_details**
> List[GetLoansLoanIdCollateralsResponse] retrieve_collateral_details(loan_id)

List Loan Collaterals

Example Requests:

loans/1/collaterals


loans/1/collaterals?fields=value,description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_collaterals_response import GetLoansLoanIdCollateralsResponse
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId

    try:
        # List Loan Collaterals
        api_response = api_instance.retrieve_collateral_details(loan_id)
        print("The response of LoanCollateralApi->retrieve_collateral_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->retrieve_collateral_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**List[GetLoansLoanIdCollateralsResponse]**](GetLoansLoanIdCollateralsResponse.md)

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

# **retrieve_collateral_details1**
> GetLoansLoanIdCollateralsResponse retrieve_collateral_details1(loan_id, collateral_id)

Retrieve a Collateral

Example Requests:

/loans/1/collaterals/1


/loans/1/collaterals/1?fields=description,description

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_loans_loan_id_collaterals_response import GetLoansLoanIdCollateralsResponse
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId
    collateral_id = 56 # int | collateralId

    try:
        # Retrieve a Collateral
        api_response = api_instance.retrieve_collateral_details1(loan_id, collateral_id)
        print("The response of LoanCollateralApi->retrieve_collateral_details1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->retrieve_collateral_details1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**GetLoansLoanIdCollateralsResponse**](GetLoansLoanIdCollateralsResponse.md)

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

# **update_collateral**
> PutLoansLoanIdCollateralsCollateralIdResponse update_collateral(loan_id, collateral_id, put_loans_loand_id_collaterals_collateral_id_request)

Update a Collateral

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.put_loans_loan_id_collaterals_collateral_id_response import PutLoansLoanIdCollateralsCollateralIdResponse
from fineract_client.models.put_loans_loand_id_collaterals_collateral_id_request import PutLoansLoandIdCollateralsCollateralIdRequest
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
    api_instance = fineract_client.LoanCollateralApi(api_client)
    loan_id = 56 # int | loanId
    collateral_id = 56 # int | collateralId
    put_loans_loand_id_collaterals_collateral_id_request = fineract_client.PutLoansLoandIdCollateralsCollateralIdRequest() # PutLoansLoandIdCollateralsCollateralIdRequest | 

    try:
        # Update a Collateral
        api_response = api_instance.update_collateral(loan_id, collateral_id, put_loans_loand_id_collaterals_collateral_id_request)
        print("The response of LoanCollateralApi->update_collateral:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoanCollateralApi->update_collateral: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **collateral_id** | **int**| collateralId | 
 **put_loans_loand_id_collaterals_collateral_id_request** | [**PutLoansLoandIdCollateralsCollateralIdRequest**](PutLoansLoandIdCollateralsCollateralIdRequest.md)|  | 

### Return type

[**PutLoansLoanIdCollateralsCollateralIdResponse**](PutLoansLoanIdCollateralsCollateralIdResponse.md)

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

