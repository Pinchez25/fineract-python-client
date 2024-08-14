# fineract_client.LoanCollateralApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collateral**](LoanCollateralApi.md#create_collateral) | **POST** /v1/loans/{loanId}/collaterals | Create a Collateral
[**delete_collateral**](LoanCollateralApi.md#delete_collateral) | **DELETE** /v1/loans/{loanId}/collaterals/{collateralId} | Remove a Collateral
[**new_collateral_template**](LoanCollateralApi.md#new_collateral_template) | **GET** /v1/loans/{loanId}/collaterals/template | Retrieve Collateral Details Template
[**retrieve_collateral_details**](LoanCollateralApi.md#retrieve_collateral_details) | **GET** /v1/loans/{loanId}/collaterals | List Loan Collaterals
[**retrieve_collateral_details1**](LoanCollateralApi.md#retrieve_collateral_details1) | **GET** /v1/loans/{loanId}/collaterals/{collateralId} | Retrieve a Collateral
[**update_collateral**](LoanCollateralApi.md#update_collateral) | **PUT** /v1/loans/{loanId}/collaterals/{collateralId} | Update a Collateral

# **create_collateral**
> PostLoansLoanIdCollateralsResponse create_collateral(body, loan_id)

Create a Collateral

Note: Currently, Collaterals may be added only before a Loan is approved

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdCollateralsRequest() # PostLoansLoanIdCollateralsRequest | 
loan_id = 789 # int | loanId

try:
    # Create a Collateral
    api_response = api_instance.create_collateral(body, loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanCollateralApi->create_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdCollateralsRequest**](PostLoansLoanIdCollateralsRequest.md)|  | 
 **loan_id** | **int**| loanId | 

### Return type

[**PostLoansLoanIdCollateralsResponse**](PostLoansLoanIdCollateralsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collateral**
> DeleteLoansLoanIdCollateralsCollateralIdResponse delete_collateral(loan_id, collateral_id)

Remove a Collateral

Note: A collateral can only be removed from Loans that are not yet approved.

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
collateral_id = 789 # int | collateralId

try:
    # Remove a Collateral
    api_response = api_instance.delete_collateral(loan_id, collateral_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_collateral_template**
> GetLoansLoanIdCollateralsTemplateResponse new_collateral_template(loan_id)

Retrieve Collateral Details Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  loans/1/collaterals/template

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Retrieve Collateral Details Template
    api_response = api_instance.new_collateral_template(loan_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_collateral_details**
> list[GetLoansLoanIdCollateralsResponse] retrieve_collateral_details(loan_id)

List Loan Collaterals

Example Requests:  loans/1/collaterals   loans/1/collaterals?fields=value,description

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # List Loan Collaterals
    api_response = api_instance.retrieve_collateral_details(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanCollateralApi->retrieve_collateral_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetLoansLoanIdCollateralsResponse]**](GetLoansLoanIdCollateralsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_collateral_details1**
> GetLoansLoanIdCollateralsResponse retrieve_collateral_details1(loan_id, collateral_id)

Retrieve a Collateral

Example Requests:  /loans/1/collaterals/1   /loans/1/collaterals/1?fields=description,description

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
collateral_id = 789 # int | collateralId

try:
    # Retrieve a Collateral
    api_response = api_instance.retrieve_collateral_details1(loan_id, collateral_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collateral**
> PutLoansLoanIdCollateralsCollateralIdResponse update_collateral(body, loan_id, collateral_id)

Update a Collateral

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
api_instance = fineract_client.LoanCollateralApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoandIdCollateralsCollateralIdRequest() # PutLoansLoandIdCollateralsCollateralIdRequest | 
loan_id = 789 # int | loanId
collateral_id = 789 # int | collateralId

try:
    # Update a Collateral
    api_response = api_instance.update_collateral(body, loan_id, collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanCollateralApi->update_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoandIdCollateralsCollateralIdRequest**](PutLoansLoandIdCollateralsCollateralIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **collateral_id** | **int**| collateralId | 

### Return type

[**PutLoansLoanIdCollateralsCollateralIdResponse**](PutLoansLoanIdCollateralsCollateralIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

