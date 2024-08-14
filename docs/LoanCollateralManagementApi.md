# fineract_client.LoanCollateralManagementApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_loan_collateral**](LoanCollateralManagementApi.md#delete_loan_collateral) | **DELETE** /v1/loan-collateral-management/{id} | Delete Loan Collateral
[**get_loan_collateral**](LoanCollateralManagementApi.md#get_loan_collateral) | **GET** /v1/loan-collateral-management/{collateralId} | Get Loan Collateral Details

# **delete_loan_collateral**
> str delete_loan_collateral(loan_id, id)

Delete Loan Collateral

Delete Loan Collateral

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
api_instance = fineract_client.LoanCollateralManagementApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
id = 789 # int | loan collateral id

try:
    # Delete Loan Collateral
    api_response = api_instance.delete_loan_collateral(loan_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanCollateralManagementApi->delete_loan_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **id** | **int**| loan collateral id | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_collateral**
> str get_loan_collateral(collateral_id)

Get Loan Collateral Details

Get Loan Collateral Details

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
api_instance = fineract_client.LoanCollateralManagementApi(fineract_client.ApiClient(configuration))
collateral_id = 789 # int | collateralId

try:
    # Get Loan Collateral Details
    api_response = api_instance.get_loan_collateral(collateral_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanCollateralManagementApi->get_loan_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_id** | **int**| collateralId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

