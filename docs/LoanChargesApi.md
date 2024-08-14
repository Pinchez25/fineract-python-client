# fineract_client.LoanChargesApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_loan_charge**](LoanChargesApi.md#delete_loan_charge) | **DELETE** /v1/loans/{loanId}/charges/{loanChargeId} | Delete a Loan Charge
[**delete_loan_charge1**](LoanChargesApi.md#delete_loan_charge1) | **DELETE** /v1/loans/{loanId}/charges/external-id/{loanChargeExternalId} | Delete a Loan Charge
[**delete_loan_charge2**](LoanChargesApi.md#delete_loan_charge2) | **DELETE** /v1/loans/external-id/{loanExternalId}/charges/{loanChargeId} | Delete a Loan Charge
[**delete_loan_charge3**](LoanChargesApi.md#delete_loan_charge3) | **DELETE** /v1/loans/external-id/{loanExternalId}/charges/external-id/{loanChargeExternalId} | Delete a Loan Charge
[**execute_loan_charge**](LoanChargesApi.md#execute_loan_charge) | **POST** /v1/loans/{loanId}/charges | Create a Loan Charge (no command provided) or Pay a charge (command&#x3D;pay)
[**execute_loan_charge1**](LoanChargesApi.md#execute_loan_charge1) | **POST** /v1/loans/external-id/{loanExternalId}/charges | Create a Loan Charge (no command provided) or Pay a charge (command&#x3D;pay)
[**execute_loan_charge2**](LoanChargesApi.md#execute_loan_charge2) | **POST** /v1/loans/{loanId}/charges/{loanChargeId} | Pay / Waive / Adjustment for Loan Charge
[**execute_loan_charge3**](LoanChargesApi.md#execute_loan_charge3) | **POST** /v1/loans/{loanId}/charges/external-id/{loanChargeExternalId} | Pay / Waive / Adjustment for Loan Charge
[**execute_loan_charge4**](LoanChargesApi.md#execute_loan_charge4) | **POST** /v1/loans/external-id/{loanExternalId}/charges/{loanChargeId} | Pay / Waive / Adjustment for Loan Charge
[**execute_loan_charge5**](LoanChargesApi.md#execute_loan_charge5) | **POST** /v1/loans/external-id/{loanExternalId}/charges/external-id/{loanChargeExternalId} | Pay / Waive / Adjustment for Loan Charge
[**retrieve_all_loan_charges**](LoanChargesApi.md#retrieve_all_loan_charges) | **GET** /v1/loans/{loanId}/charges | List Loan Charges
[**retrieve_all_loan_charges1**](LoanChargesApi.md#retrieve_all_loan_charges1) | **GET** /v1/loans/external-id/{loanExternalId}/charges | List Loan Charges
[**retrieve_loan_charge**](LoanChargesApi.md#retrieve_loan_charge) | **GET** /v1/loans/{loanId}/charges/{loanChargeId} | Retrieve a Loan Charge
[**retrieve_loan_charge1**](LoanChargesApi.md#retrieve_loan_charge1) | **GET** /v1/loans/{loanId}/charges/external-id/{loanChargeExternalId} | Retrieve a Loan Charge
[**retrieve_loan_charge2**](LoanChargesApi.md#retrieve_loan_charge2) | **GET** /v1/loans/external-id/{loanExternalId}/charges/{loanChargeId} | Retrieve a Loan Charge
[**retrieve_loan_charge3**](LoanChargesApi.md#retrieve_loan_charge3) | **GET** /v1/loans/external-id/{loanExternalId}/charges/external-id/{loanChargeExternalId} | Retrieve a Loan Charge
[**retrieve_template8**](LoanChargesApi.md#retrieve_template8) | **GET** /v1/loans/{loanId}/charges/template | Retrieve Loan Charges Template
[**retrieve_template9**](LoanChargesApi.md#retrieve_template9) | **GET** /v1/loans/external-id/{loanExternalId}/charges/template | Retrieve Loan Charges Template
[**update_loan_charge**](LoanChargesApi.md#update_loan_charge) | **PUT** /v1/loans/{loanId}/charges/{loanChargeId} | Update a Loan Charge
[**update_loan_charge1**](LoanChargesApi.md#update_loan_charge1) | **PUT** /v1/loans/{loanId}/charges/external-id/{loanChargeExternalId} | Update a Loan Charge
[**update_loan_charge2**](LoanChargesApi.md#update_loan_charge2) | **PUT** /v1/loans/external-id/{loanExternalId}/charges/{loanChargeId} | Update a Loan Charge
[**update_loan_charge3**](LoanChargesApi.md#update_loan_charge3) | **PUT** /v1/loans/external-id/{loanExternalId}/charges/external-id/{loanChargeExternalId} | Update a Loan Charge

# **delete_loan_charge**
> DeleteLoansLoanIdChargesChargeIdResponse delete_loan_charge(loan_id, loan_charge_id)

Delete a Loan Charge

Note: Currently, A Loan Charge may only be removed from Loans that are not yet approved.

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
loan_charge_id = 789 # int | loanChargeId

try:
    # Delete a Loan Charge
    api_response = api_instance.delete_loan_charge(loan_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->delete_loan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**DeleteLoansLoanIdChargesChargeIdResponse**](DeleteLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_charge1**
> DeleteLoansLoanIdChargesChargeIdResponse delete_loan_charge1(loan_id, loan_charge_external_id)

Delete a Loan Charge

Note: Currently, A Loan Charge may only be removed from Loans that are not yet approved.

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Delete a Loan Charge
    api_response = api_instance.delete_loan_charge1(loan_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->delete_loan_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**DeleteLoansLoanIdChargesChargeIdResponse**](DeleteLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_charge2**
> DeleteLoansLoanIdChargesChargeIdResponse delete_loan_charge2(loan_external_id, loan_charge_id)

Delete a Loan Charge

Note: Currently, A Loan Charge may only be removed from Loans that are not yet approved.

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_id = 789 # int | loanChargeId

try:
    # Delete a Loan Charge
    api_response = api_instance.delete_loan_charge2(loan_external_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->delete_loan_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**DeleteLoansLoanIdChargesChargeIdResponse**](DeleteLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loan_charge3**
> DeleteLoansLoanIdChargesChargeIdResponse delete_loan_charge3(loan_external_id, loan_charge_external_id)

Delete a Loan Charge

Note: Currently, A Loan Charge may only be removed from Loans that are not yet approved.

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Delete a Loan Charge
    api_response = api_instance.delete_loan_charge3(loan_external_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->delete_loan_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**DeleteLoansLoanIdChargesChargeIdResponse**](DeleteLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge**
> PostLoansLoanIdChargesResponse execute_loan_charge(body, loan_id, command=command)

Create a Loan Charge (no command provided) or Pay a charge (command=pay)

Creates a Loan Charge | Pay a Loan Charge

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesRequest() # PostLoansLoanIdChargesRequest | 
loan_id = 789 # int | loanId
command = 'command_example' # str | command (optional)

try:
    # Create a Loan Charge (no command provided) or Pay a charge (command=pay)
    api_response = api_instance.execute_loan_charge(body, loan_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesRequest**](PostLoansLoanIdChargesRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesResponse**](PostLoansLoanIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge1**
> PostLoansLoanIdChargesResponse execute_loan_charge1(body, loan_external_id, command=command)

Create a Loan Charge (no command provided) or Pay a charge (command=pay)

Creates a Loan Charge | Pay a Loan Charge

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesRequest() # PostLoansLoanIdChargesRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
command = 'command_example' # str | command (optional)

try:
    # Create a Loan Charge (no command provided) or Pay a charge (command=pay)
    api_response = api_instance.execute_loan_charge1(body, loan_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesRequest**](PostLoansLoanIdChargesRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesResponse**](PostLoansLoanIdChargesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge2**
> PostLoansLoanIdChargesChargeIdResponse execute_loan_charge2(body, loan_id, loan_charge_id, command=command)

Pay / Waive / Adjustment for Loan Charge

Loan Charge will be paid if the loan is linked with a savings account | Waive Loan Charge | Add Charge Adjustment

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesChargeIdRequest() # PostLoansLoanIdChargesChargeIdRequest | 
loan_id = 789 # int | loanId
loan_charge_id = 789 # int | loanChargeId
command = 'command_example' # str | command (optional)

try:
    # Pay / Waive / Adjustment for Loan Charge
    api_response = api_instance.execute_loan_charge2(body, loan_id, loan_charge_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesChargeIdRequest**](PostLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **loan_charge_id** | **int**| loanChargeId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesChargeIdResponse**](PostLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge3**
> PostLoansLoanIdChargesChargeIdResponse execute_loan_charge3(body, loan_id, loan_charge_external_id, command=command)

Pay / Waive / Adjustment for Loan Charge

Loan Charge will be paid if the loan is linked with a savings account | Waive Loan Charge | Add Charge Adjustment

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesChargeIdRequest() # PostLoansLoanIdChargesChargeIdRequest | 
loan_id = 789 # int | loanId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId
command = 'command_example' # str | command (optional)

try:
    # Pay / Waive / Adjustment for Loan Charge
    api_response = api_instance.execute_loan_charge3(body, loan_id, loan_charge_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesChargeIdRequest**](PostLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesChargeIdResponse**](PostLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge4**
> PostLoansLoanIdChargesChargeIdResponse execute_loan_charge4(body, loan_external_id, loan_charge_id, command=command)

Pay / Waive / Adjustment for Loan Charge

Loan Charge will be paid if the loan is linked with a savings account | Waive Loan Charge | Add Charge Adjustment

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesChargeIdRequest() # PostLoansLoanIdChargesChargeIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_id = 789 # int | loanChargeId
command = 'command_example' # str | command (optional)

try:
    # Pay / Waive / Adjustment for Loan Charge
    api_response = api_instance.execute_loan_charge4(body, loan_external_id, loan_charge_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesChargeIdRequest**](PostLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_id** | **int**| loanChargeId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesChargeIdResponse**](PostLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_loan_charge5**
> PostLoansLoanIdChargesChargeIdResponse execute_loan_charge5(body, loan_external_id, loan_charge_external_id, command=command)

Pay / Waive / Adjustment for Loan Charge

Loan Charge will be paid if the loan is linked with a savings account | Waive Loan Charge | Add Charge Adjustment

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostLoansLoanIdChargesChargeIdRequest() # PostLoansLoanIdChargesChargeIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId
command = 'command_example' # str | command (optional)

try:
    # Pay / Waive / Adjustment for Loan Charge
    api_response = api_instance.execute_loan_charge5(body, loan_external_id, loan_charge_external_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->execute_loan_charge5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostLoansLoanIdChargesChargeIdRequest**](PostLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 
 **command** | **str**| command | [optional] 

### Return type

[**PostLoansLoanIdChargesChargeIdResponse**](PostLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_loan_charges**
> list[GetLoansLoanIdChargesChargeIdResponse] retrieve_all_loan_charges(loan_id)

List Loan Charges

It lists all the Loan Charges specific to a Loan   Example Requests:  loans/1/charges   loans/1/charges?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # List Loan Charges
    api_response = api_instance.retrieve_all_loan_charges(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_all_loan_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**list[GetLoansLoanIdChargesChargeIdResponse]**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_loan_charges1**
> list[GetLoansLoanIdChargesChargeIdResponse] retrieve_all_loan_charges1(loan_external_id)

List Loan Charges

It lists all the Loan Charges specific to a Loan   Example Requests:  loans/1/charges   loans/1/charges?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # List Loan Charges
    api_response = api_instance.retrieve_all_loan_charges1(loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_all_loan_charges1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**list[GetLoansLoanIdChargesChargeIdResponse]**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan_charge**
> GetLoansLoanIdChargesChargeIdResponse retrieve_loan_charge(loan_id, loan_charge_id)

Retrieve a Loan Charge

Retrieves Loan Charge according to the Loan ID and Loan Charge IDExample Requests:  /loans/1/charges/1   /loans/1/charges/1?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
loan_charge_id = 789 # int | loanChargeId

try:
    # Retrieve a Loan Charge
    api_response = api_instance.retrieve_loan_charge(loan_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_loan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**GetLoansLoanIdChargesChargeIdResponse**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan_charge1**
> GetLoansLoanIdChargesChargeIdResponse retrieve_loan_charge1(loan_id, loan_charge_external_id)

Retrieve a Loan Charge

Retrieves Loan Charge according to the Loan ID and Loan Charge External IDExample Requests:  /loans/1/charges/1   /loans/1/charges/external-id/1?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Retrieve a Loan Charge
    api_response = api_instance.retrieve_loan_charge1(loan_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_loan_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**GetLoansLoanIdChargesChargeIdResponse**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan_charge2**
> GetLoansLoanIdChargesChargeIdResponse retrieve_loan_charge2(loan_external_id, loan_charge_id)

Retrieve a Loan Charge

Retrieves Loan Charge according to the Loan external ID and Loan Charge IDExample Requests:  /loans/1/charges/1   /loans/1/charges/1?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_id = 789 # int | loanChargeId

try:
    # Retrieve a Loan Charge
    api_response = api_instance.retrieve_loan_charge2(loan_external_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_loan_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**GetLoansLoanIdChargesChargeIdResponse**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_loan_charge3**
> GetLoansLoanIdChargesChargeIdResponse retrieve_loan_charge3(loan_external_id, loan_charge_external_id)

Retrieve a Loan Charge

Retrieves Loan Charge according to the Loan External ID and Loan Charge External IDExample Requests:  /loans/1/charges/1   /loans/1/charges/1?fields=name,amountOrPercentage

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Retrieve a Loan Charge
    api_response = api_instance.retrieve_loan_charge3(loan_external_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_loan_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**GetLoansLoanIdChargesChargeIdResponse**](GetLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template8**
> GetLoansLoanIdChargesTemplateResponse retrieve_template8(loan_id)

Retrieve Loan Charges Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  loans/1/charges/template  

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | loanId

try:
    # Retrieve Loan Charges Template
    api_response = api_instance.retrieve_template8(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_template8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**| loanId | 

### Return type

[**GetLoansLoanIdChargesTemplateResponse**](GetLoansLoanIdChargesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template9**
> GetLoansLoanIdChargesTemplateResponse retrieve_template9(loan_external_id)

Retrieve Loan Charges Template

This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  loans/1/charges/template  

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
loan_external_id = 'loan_external_id_example' # str | loanExternalId

try:
    # Retrieve Loan Charges Template
    api_response = api_instance.retrieve_template9(loan_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->retrieve_template9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_external_id** | **str**| loanExternalId | 

### Return type

[**GetLoansLoanIdChargesTemplateResponse**](GetLoansLoanIdChargesTemplateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_charge**
> PutLoansLoanIdChargesChargeIdResponse update_loan_charge(body, loan_id, loan_charge_id)

Update a Loan Charge

Currently Loan Charges may be updated only if the Loan is not yet approved

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdChargesChargeIdRequest() # PutLoansLoanIdChargesChargeIdRequest | 
loan_id = 789 # int | loanId
loan_charge_id = 789 # int | loanChargeId

try:
    # Update a Loan Charge
    api_response = api_instance.update_loan_charge(body, loan_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->update_loan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdChargesChargeIdRequest**](PutLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**PutLoansLoanIdChargesChargeIdResponse**](PutLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_charge1**
> PutLoansLoanIdChargesChargeIdResponse update_loan_charge1(body, loan_id, loan_charge_external_id)

Update a Loan Charge

Currently Loan Charges may be updated only if the Loan is not yet approved

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdChargesChargeIdRequest() # PutLoansLoanIdChargesChargeIdRequest | 
loan_id = 789 # int | loanId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Update a Loan Charge
    api_response = api_instance.update_loan_charge1(body, loan_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->update_loan_charge1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdChargesChargeIdRequest**](PutLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_id** | **int**| loanId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**PutLoansLoanIdChargesChargeIdResponse**](PutLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_charge2**
> PutLoansLoanIdChargesChargeIdResponse update_loan_charge2(body, loan_external_id, loan_charge_id)

Update a Loan Charge

Currently Loan Charges may be updated only if the Loan is not yet approved

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdChargesChargeIdRequest() # PutLoansLoanIdChargesChargeIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_id = 789 # int | loanChargeId

try:
    # Update a Loan Charge
    api_response = api_instance.update_loan_charge2(body, loan_external_id, loan_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->update_loan_charge2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdChargesChargeIdRequest**](PutLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_id** | **int**| loanChargeId | 

### Return type

[**PutLoansLoanIdChargesChargeIdResponse**](PutLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_charge3**
> PutLoansLoanIdChargesChargeIdResponse update_loan_charge3(body, loan_external_id, loan_charge_external_id)

Update a Loan Charge

Currently Loan Charges may be updated only if the Loan is not yet approved

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
api_instance = fineract_client.LoanChargesApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutLoansLoanIdChargesChargeIdRequest() # PutLoansLoanIdChargesChargeIdRequest | 
loan_external_id = 'loan_external_id_example' # str | loanExternalId
loan_charge_external_id = 'loan_charge_external_id_example' # str | loanChargeExternalId

try:
    # Update a Loan Charge
    api_response = api_instance.update_loan_charge3(body, loan_external_id, loan_charge_external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanChargesApi->update_loan_charge3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutLoansLoanIdChargesChargeIdRequest**](PutLoansLoanIdChargesChargeIdRequest.md)|  | 
 **loan_external_id** | **str**| loanExternalId | 
 **loan_charge_external_id** | **str**| loanChargeExternalId | 

### Return type

[**PutLoansLoanIdChargesChargeIdResponse**](PutLoansLoanIdChargesChargeIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

