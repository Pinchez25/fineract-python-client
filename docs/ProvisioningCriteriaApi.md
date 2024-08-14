# fineract_client.ProvisioningCriteriaApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provisioning_criteria**](ProvisioningCriteriaApi.md#create_provisioning_criteria) | **POST** /v1/provisioningcriteria | Create a new Provisioning Criteria
[**delete_provisioning_criteria**](ProvisioningCriteriaApi.md#delete_provisioning_criteria) | **DELETE** /v1/provisioningcriteria/{criteriaId} | Deletes Provisioning Criteria
[**retrieve_all_provisioning_criterias**](ProvisioningCriteriaApi.md#retrieve_all_provisioning_criterias) | **GET** /v1/provisioningcriteria | Retrieves all created Provisioning Criterias
[**retrieve_provisioning_criteria**](ProvisioningCriteriaApi.md#retrieve_provisioning_criteria) | **GET** /v1/provisioningcriteria/{criteriaId} | Retrieves a Provisioning Criteria
[**retrieve_template3**](ProvisioningCriteriaApi.md#retrieve_template3) | **GET** /v1/provisioningcriteria/template | 
[**update_provisioning_criteria**](ProvisioningCriteriaApi.md#update_provisioning_criteria) | **PUT** /v1/provisioningcriteria/{criteriaId} | Updates a new Provisioning Criteria

# **create_provisioning_criteria**
> PostProvisioningCriteriaResponse create_provisioning_criteria(body)

Create a new Provisioning Criteria

Creates a new Provisioning Criteria  Mandatory Fields:  criteriaName provisioningcriteria  Optional Fields:  loanProducts

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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostProvisioningCriteriaRequest() # PostProvisioningCriteriaRequest | 

try:
    # Create a new Provisioning Criteria
    api_response = api_instance.create_provisioning_criteria(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->create_provisioning_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostProvisioningCriteriaRequest**](PostProvisioningCriteriaRequest.md)|  | 

### Return type

[**PostProvisioningCriteriaResponse**](PostProvisioningCriteriaResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provisioning_criteria**
> DeleteProvisioningCriteriaResponse delete_provisioning_criteria(criteria_id)

Deletes Provisioning Criteria

Deletes Provisioning Criteria

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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))
criteria_id = 789 # int | criteriaId

try:
    # Deletes Provisioning Criteria
    api_response = api_instance.delete_provisioning_criteria(criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->delete_provisioning_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria_id** | **int**| criteriaId | 

### Return type

[**DeleteProvisioningCriteriaResponse**](DeleteProvisioningCriteriaResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_provisioning_criterias**
> list[GetProvisioningCriteriaResponse] retrieve_all_provisioning_criterias()

Retrieves all created Provisioning Criterias

Retrieves all created Provisioning Criterias

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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))

try:
    # Retrieves all created Provisioning Criterias
    api_response = api_instance.retrieve_all_provisioning_criterias()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->retrieve_all_provisioning_criterias: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetProvisioningCriteriaResponse]**](GetProvisioningCriteriaResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_provisioning_criteria**
> GetProvisioningCriteriaCriteriaIdResponse retrieve_provisioning_criteria(criteria_id)

Retrieves a Provisioning Criteria

Retrieves a Provisioning Criteria

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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))
criteria_id = 789 # int | criteriaId

try:
    # Retrieves a Provisioning Criteria
    api_response = api_instance.retrieve_provisioning_criteria(criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->retrieve_provisioning_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria_id** | **int**| criteriaId | 

### Return type

[**GetProvisioningCriteriaCriteriaIdResponse**](GetProvisioningCriteriaCriteriaIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template3**
> str retrieve_template3()



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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_template3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->retrieve_template3: %s\n" % e)
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

# **update_provisioning_criteria**
> PutProvisioningCriteriaResponse update_provisioning_criteria(body, criteria_id)

Updates a new Provisioning Criteria

Updates a new Provisioning Criteria  Optional Fields criteriaName, loanProducts, provisioningcriteria

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
api_instance = fineract_client.ProvisioningCriteriaApi(fineract_client.ApiClient(configuration))
body = fineract_client.PutProvisioningCriteriaRequest() # PutProvisioningCriteriaRequest | 
criteria_id = 789 # int | criteriaId

try:
    # Updates a new Provisioning Criteria
    api_response = api_instance.update_provisioning_criteria(body, criteria_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningCriteriaApi->update_provisioning_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutProvisioningCriteriaRequest**](PutProvisioningCriteriaRequest.md)|  | 
 **criteria_id** | **int**| criteriaId | 

### Return type

[**PutProvisioningCriteriaResponse**](PutProvisioningCriteriaResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

