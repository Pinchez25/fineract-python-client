# fineract_client.CreditBureauConfigurationApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organisation_credit_bureau**](CreditBureauConfigurationApi.md#add_organisation_credit_bureau) | **POST** /v1/CreditBureauConfiguration/organisationCreditBureau/{organisationCreditBureauId} | 
[**create_credit_bureau_configuration**](CreditBureauConfigurationApi.md#create_credit_bureau_configuration) | **POST** /v1/CreditBureauConfiguration/configuration/{creditBureauId} | 
[**create_credit_bureau_loan_product_mapping**](CreditBureauConfigurationApi.md#create_credit_bureau_loan_product_mapping) | **POST** /v1/CreditBureauConfiguration/mappings/{organisationCreditBureauId} | 
[**fetch_loan_products**](CreditBureauConfigurationApi.md#fetch_loan_products) | **GET** /v1/CreditBureauConfiguration/loanProduct | 
[**fetch_mapping_by_loan_product_id**](CreditBureauConfigurationApi.md#fetch_mapping_by_loan_product_id) | **GET** /v1/CreditBureauConfiguration/loanProduct/{loanProductId} | 
[**get_configuration**](CreditBureauConfigurationApi.md#get_configuration) | **GET** /v1/CreditBureauConfiguration/config/{organisationCreditBureauId} | 
[**get_credit_bureau**](CreditBureauConfigurationApi.md#get_credit_bureau) | **GET** /v1/CreditBureauConfiguration | 
[**get_credit_bureau_loan_product_mapping**](CreditBureauConfigurationApi.md#get_credit_bureau_loan_product_mapping) | **GET** /v1/CreditBureauConfiguration/mappings | 
[**get_organisation_credit_bureau**](CreditBureauConfigurationApi.md#get_organisation_credit_bureau) | **GET** /v1/CreditBureauConfiguration/organisationCreditBureau | 
[**update_credit_bureau**](CreditBureauConfigurationApi.md#update_credit_bureau) | **PUT** /v1/CreditBureauConfiguration/organisationCreditBureau | 
[**update_credit_bureau_configuration**](CreditBureauConfigurationApi.md#update_credit_bureau_configuration) | **PUT** /v1/CreditBureauConfiguration/configuration/{configurationId} | 
[**update_credit_bureau_loan_product_mapping**](CreditBureauConfigurationApi.md#update_credit_bureau_loan_product_mapping) | **PUT** /v1/CreditBureauConfiguration/mappings | 

# **add_organisation_credit_bureau**
> str add_organisation_credit_bureau(organisation_credit_bureau_id, body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
organisation_credit_bureau_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.add_organisation_credit_bureau(organisation_credit_bureau_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->add_organisation_credit_bureau: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_credit_bureau_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_bureau_configuration**
> str create_credit_bureau_configuration(credit_bureau_id, body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
credit_bureau_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_credit_bureau_configuration(credit_bureau_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->create_credit_bureau_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bureau_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_bureau_loan_product_mapping**
> str create_credit_bureau_loan_product_mapping(organisation_credit_bureau_id, body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
organisation_credit_bureau_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_credit_bureau_loan_product_mapping(organisation_credit_bureau_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->create_credit_bureau_loan_product_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_credit_bureau_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_loan_products**
> str fetch_loan_products()



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.fetch_loan_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->fetch_loan_products: %s\n" % e)
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

# **fetch_mapping_by_loan_product_id**
> str fetch_mapping_by_loan_product_id(loan_product_id)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
loan_product_id = 789 # int | 

try:
    api_response = api_instance.fetch_mapping_by_loan_product_id(loan_product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->fetch_mapping_by_loan_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_product_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> str get_configuration(organisation_credit_bureau_id)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
organisation_credit_bureau_id = 789 # int | 

try:
    api_response = api_instance.get_configuration(organisation_credit_bureau_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_credit_bureau_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_bureau**
> str get_credit_bureau()



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.get_credit_bureau()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->get_credit_bureau: %s\n" % e)
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

# **get_credit_bureau_loan_product_mapping**
> str get_credit_bureau_loan_product_mapping()



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.get_credit_bureau_loan_product_mapping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->get_credit_bureau_loan_product_mapping: %s\n" % e)
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

# **get_organisation_credit_bureau**
> str get_organisation_credit_bureau()



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.get_organisation_credit_bureau()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->get_organisation_credit_bureau: %s\n" % e)
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

# **update_credit_bureau**
> str update_credit_bureau(body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_credit_bureau(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->update_credit_bureau: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_bureau_configuration**
> str update_credit_bureau_configuration(configuration_id, body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
configuration_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_credit_bureau_configuration(configuration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->update_credit_bureau_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_bureau_loan_product_mapping**
> str update_credit_bureau_loan_product_mapping(body=body)



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
api_instance = fineract_client.CreditBureauConfigurationApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_credit_bureau_loan_product_mapping(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditBureauConfigurationApi->update_credit_bureau_loan_product_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

