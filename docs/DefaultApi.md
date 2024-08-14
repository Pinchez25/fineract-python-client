# fineract_client.DefaultApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](DefaultApi.md#activate) | **POST** /v1/email/campaign/{resourceId} | 
[**add_credit_report**](DefaultApi.md#add_credit_report) | **POST** /v1/creditBureauIntegration/addCreditReport | 
[**add_new_client_image1**](DefaultApi.md#add_new_client_image1) | **POST** /v1/{entity}/{entityId}/images | 
[**create1**](DefaultApi.md#create1) | **POST** /v1/email | 
[**create_campaign**](DefaultApi.md#create_campaign) | **POST** /v1/email/campaign | 
[**create_campaign1**](DefaultApi.md#create_campaign1) | **POST** /v1/smscampaigns | Create a SMS Campaign
[**delete1**](DefaultApi.md#delete1) | **DELETE** /v1/email/{resourceId} | 
[**delete2**](DefaultApi.md#delete2) | **DELETE** /v1/email/campaign/{resourceId} | 
[**delete3**](DefaultApi.md#delete3) | **DELETE** /v1/smscampaigns/{campaignId} | Delete a SMS Campaign
[**delete8**](DefaultApi.md#delete8) | **DELETE** /v1/officetransactions/{transactionId} | 
[**delete_all_external_events**](DefaultApi.md#delete_all_external_events) | **DELETE** /v1/internal/externalevents | 
[**delete_client_image**](DefaultApi.md#delete_client_image) | **DELETE** /v1/{entity}/{entityId}/images | 
[**delete_credit_report**](DefaultApi.md#delete_credit_report) | **DELETE** /v1/creditBureauIntegration/deleteCreditReport/{creditBureauId} | 
[**fetch_credit_report**](DefaultApi.md#fetch_credit_report) | **POST** /v1/creditBureauIntegration/creditReport | 
[**get**](DefaultApi.md#get) | **GET** /v1/echo | 
[**get_advanced_payment_allocation_rules_of_loan**](DefaultApi.md#get_advanced_payment_allocation_rules_of_loan) | **GET** /v1/internal/loan/{loanId}/advanced-payment-allocation-rules | 
[**get_all_external_events**](DefaultApi.md#get_all_external_events) | **GET** /v1/internal/externalevents | 
[**get_client_audit_fields**](DefaultApi.md#get_client_audit_fields) | **GET** /v1/internal/client/{clientId}/audit | 
[**get_cob_partitions**](DefaultApi.md#get_cob_partitions) | **GET** /v1/internal/cob/partitions/{partitionSize} | 
[**get_external_grammar**](DefaultApi.md#get_external_grammar) | **GET** /application.wadl/{path} | 
[**get_loan_audit_fields**](DefaultApi.md#get_loan_audit_fields) | **GET** /v1/internal/loan/{loanId}/audit | 
[**get_loan_transaction_audit_fields**](DefaultApi.md#get_loan_transaction_audit_fields) | **GET** /v1/internal/loan/{loanId}/transaction/{transactionId}/audit | 
[**get_loans_by_status**](DefaultApi.md#get_loans_by_status) | **GET** /v1/internal/loan/status/{statusId} | 
[**get_saved_credit_report**](DefaultApi.md#get_saved_credit_report) | **GET** /v1/creditBureauIntegration/creditReport/{creditBureauId} | 
[**get_wadl**](DefaultApi.md#get_wadl) | **GET** /application.wadl | 
[**handle_commands**](DefaultApi.md#handle_commands) | **POST** /v1/smscampaigns/{campaignId} | SMS Campaign
[**new_office_transaction_details**](DefaultApi.md#new_office_transaction_details) | **GET** /v1/officetransactions/template | 
[**place_lock_on_loan_account**](DefaultApi.md#place_lock_on_loan_account) | **POST** /v1/internal/loans/{loanId}/place-lock/{lockOwner} | 
[**preview**](DefaultApi.md#preview) | **POST** /v1/email/campaign/preview | 
[**preview1**](DefaultApi.md#preview1) | **POST** /v1/smscampaigns/preview | 
[**retrieve_all5**](DefaultApi.md#retrieve_all5) | **GET** /v1/email/configuration | 
[**retrieve_all9**](DefaultApi.md#retrieve_all9) | **GET** /v1/twofactor/configure | 
[**retrieve_all_campaign**](DefaultApi.md#retrieve_all_campaign) | **GET** /v1/email/campaign | 
[**retrieve_all_email_by_status**](DefaultApi.md#retrieve_all_email_by_status) | **GET** /v1/email/messageByStatus | 
[**retrieve_all_emails**](DefaultApi.md#retrieve_all_emails) | **GET** /v1/email | 
[**retrieve_all_emails1**](DefaultApi.md#retrieve_all_emails1) | **GET** /v1/smscampaigns | List SMS Campaigns
[**retrieve_campaign**](DefaultApi.md#retrieve_campaign) | **GET** /v1/smscampaigns/{resourceId} | Retrieve a SMS Campaign
[**retrieve_failed_email**](DefaultApi.md#retrieve_failed_email) | **GET** /v1/email/failedEmail | 
[**retrieve_image**](DefaultApi.md#retrieve_image) | **GET** /v1/{entity}/{entityId}/images | 
[**retrieve_office_transactions**](DefaultApi.md#retrieve_office_transactions) | **GET** /v1/officetransactions | 
[**retrieve_one1**](DefaultApi.md#retrieve_one1) | **GET** /v1/email/{resourceId} | 
[**retrieve_one_campaign**](DefaultApi.md#retrieve_one_campaign) | **GET** /v1/email/campaign/{resourceId} | 
[**retrieve_one_template**](DefaultApi.md#retrieve_one_template) | **GET** /v1/email/campaign/template/{resourceId} | 
[**retrieve_pending_email**](DefaultApi.md#retrieve_pending_email) | **GET** /v1/email/pendingEmail | 
[**retrieve_sent_email**](DefaultApi.md#retrieve_sent_email) | **GET** /v1/email/sentEmail | 
[**save_credit_report**](DefaultApi.md#save_credit_report) | **POST** /v1/creditBureauIntegration/saveCreditReport | 
[**template1**](DefaultApi.md#template1) | **GET** /v1/email/campaign/template | 
[**template2**](DefaultApi.md#template2) | **GET** /v1/smscampaigns/template | Retrieve a SMS Campaign
[**transfer_money_from**](DefaultApi.md#transfer_money_from) | **POST** /v1/officetransactions | 
[**update2**](DefaultApi.md#update2) | **PUT** /v1/email/{resourceId} | 
[**update_campaign**](DefaultApi.md#update_campaign) | **PUT** /v1/email/campaign/{resourceId} | 
[**update_campaign1**](DefaultApi.md#update_campaign1) | **PUT** /v1/smscampaigns/{campaignId} | Update a Campaign
[**update_client_image1**](DefaultApi.md#update_client_image1) | **PUT** /v1/{entity}/{entityId}/images | 
[**update_configuration**](DefaultApi.md#update_configuration) | **PUT** /v1/email/configuration | 
[**update_configuration3**](DefaultApi.md#update_configuration3) | **PUT** /v1/twofactor/configure | 
[**update_global_configuration**](DefaultApi.md#update_global_configuration) | **POST** /v1/internal/configurations/{configId}/value/{configValue} | 
[**update_loan_cob_last_date**](DefaultApi.md#update_loan_cob_last_date) | **POST** /v1/internal/cob/fast-forward-cob-date-of-loan/{loanId} | 

# **activate**
> str activate(resource_id, body=body, command=command)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 
body = 'body_example' # str |  (optional)
command = 'command_example' # str |  (optional)

try:
    api_response = api_instance.activate(resource_id, body=body, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **command** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credit_report**
> str add_credit_report(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, credit_bureau_id=credit_bureau_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)
credit_bureau_id = 789 # int | creditBureauId (optional)

try:
    api_response = api_instance.add_credit_report(date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, credit_bureau_id=credit_bureau_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 
 **credit_bureau_id** | **int**| creditBureauId | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_client_image1**
> str add_new_client_image1(entity, entity_id, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, content_length=content_length)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
entity = 'entity_example' # str | 
entity_id = 789 # int | 
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)
content_length = 789 # int |  (optional)

try:
    api_response = api_instance.add_new_client_image1(entity, entity_id, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, content_length=content_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_new_client_image1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 
 **entity_id** | **int**|  | 
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 
 **content_length** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create1**
> str create1(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create1: %s\n" % e)
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

# **create_campaign**
> str create_campaign(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.create_campaign(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_campaign: %s\n" % e)
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

# **create_campaign1**
> CommandProcessingResult create_campaign1(body)

Create a SMS Campaign

Mandatory Fields campaignName, campaignType, triggerType, providerId, runReportId, message  Mandatory Fields for Cash based on selected report id paramValue in json format

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = fineract_client.CommandWrapper() # CommandWrapper | 

try:
    # Create a SMS Campaign
    api_response = api_instance.create_campaign1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_campaign1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommandWrapper**](CommandWrapper.md)|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> str delete1(resource_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    api_response = api_instance.delete1(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete2**
> str delete2(resource_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    api_response = api_instance.delete2(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete3**
> CommandProcessingResult delete3(campaign_id)

Delete a SMS Campaign

Note: Only closed SMS Campaigns can be deleted

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
campaign_id = 789 # int | 

try:
    # Delete a SMS Campaign
    api_response = api_instance.delete3(campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete8**
> str delete8(transaction_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
transaction_id = 789 # int | 

try:
    api_response = api_instance.delete8(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_external_events**
> delete_all_external_events()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_instance.delete_all_external_events()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_all_external_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_image**
> str delete_client_image(entity, entity_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
entity = 'entity_example' # str | 
entity_id = 789 # int | 

try:
    api_response = api_instance.delete_client_image(entity, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_client_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 
 **entity_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credit_report**
> str delete_credit_report(credit_bureau_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
credit_bureau_id = 789 # int | creditBureauId

try:
    api_response = api_instance.delete_credit_report(credit_bureau_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bureau_id** | **int**| creditBureauId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_credit_report**
> str fetch_credit_report(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = NULL # object | Fetch credit report (optional)

try:
    api_response = api_instance.fetch_credit_report(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fetch_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Fetch credit report | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> str get()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_payment_allocation_rules_of_loan**
> list[AdvancedPaymentData] get_advanced_payment_allocation_rules_of_loan(loan_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 

try:
    api_response = api_instance.get_advanced_payment_allocation_rules_of_loan(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_advanced_payment_allocation_rules_of_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 

### Return type

[**list[AdvancedPaymentData]**](AdvancedPaymentData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_external_events**
> str get_all_external_events(idempotency_key=idempotency_key, type=type, category=category, aggregate_root_id=aggregate_root_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
idempotency_key = 'idempotency_key_example' # str |  (optional)
type = 'type_example' # str |  (optional)
category = 'category_example' # str |  (optional)
aggregate_root_id = 789 # int |  (optional)

try:
    api_response = api_instance.get_all_external_events(idempotency_key=idempotency_key, type=type, category=category, aggregate_root_id=aggregate_root_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_external_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **aggregate_root_id** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_audit_fields**
> str get_client_audit_fields(client_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | 

try:
    api_response = api_instance.get_client_audit_fields(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_client_audit_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cob_partitions**
> str get_cob_partitions(partition_size)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
partition_size = 56 # int | 

try:
    api_response = api_instance.get_cob_partitions(partition_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cob_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_size** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_grammar**
> get_external_grammar(path)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
path = 'path_example' # str | 

try:
    api_instance.get_external_grammar(path)
except ApiException as e:
    print("Exception when calling DefaultApi->get_external_grammar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_audit_fields**
> str get_loan_audit_fields(loan_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 

try:
    api_response = api_instance.get_loan_audit_fields(loan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_loan_audit_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_transaction_audit_fields**
> str get_loan_transaction_audit_fields(loan_id, transaction_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
transaction_id = 789 # int | 

try:
    api_response = api_instance.get_loan_transaction_audit_fields(loan_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_loan_transaction_audit_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **transaction_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loans_by_status**
> str get_loans_by_status(status_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
status_id = 56 # int | 

try:
    api_response = api_instance.get_loans_by_status(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_loans_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_credit_report**
> str get_saved_credit_report(credit_bureau_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
credit_bureau_id = 789 # int | creditBureauId

try:
    api_response = api_instance.get_saved_credit_report(credit_bureau_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_saved_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bureau_id** | **int**| creditBureauId | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wadl**
> get_wadl()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_instance.get_wadl()
except ApiException as e:
    print("Exception when calling DefaultApi->get_wadl: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.sun.wadl+xml, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_commands**
> CommandProcessingResult handle_commands(campaign_id, command=command)

SMS Campaign

Activates | Deactivates | Reactivates

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
campaign_id = 789 # int | 
command = 'command_example' # str |  (optional)

try:
    # SMS Campaign
    api_response = api_instance.handle_commands(campaign_id, command=command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->handle_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **command** | **str**|  | [optional] 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_office_transaction_details**
> str new_office_transaction_details()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.new_office_transaction_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->new_office_transaction_details: %s\n" % e)
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

# **place_lock_on_loan_account**
> place_lock_on_loan_account(loan_id, lock_owner, body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
lock_owner = 'lock_owner_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.place_lock_on_loan_account(loan_id, lock_owner, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->place_lock_on_loan_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **lock_owner** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview**
> str preview(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.preview(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->preview: %s\n" % e)
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

# **preview1**
> str preview1(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.preview1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->preview1: %s\n" % e)
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

# **retrieve_all5**
> str retrieve_all5()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_all5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all5: %s\n" % e)
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

# **retrieve_all9**
> str retrieve_all9()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_all9()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all9: %s\n" % e)
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

# **retrieve_all_campaign**
> str retrieve_all_campaign()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_all_campaign()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all_campaign: %s\n" % e)
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

# **retrieve_all_email_by_status**
> str retrieve_all_email_by_status(sql_search=sql_search, offset=offset, limit=limit, status=status, order_by=order_by, sort_order=sort_order, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
sql_search = 'sql_search_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
status = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
from_date = fineract_client.DateParam() # DateParam |  (optional)
to_date = fineract_client.DateParam() # DateParam |  (optional)
locale = 'locale_example' # str |  (optional)
date_format = 'date_format_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_all_email_by_status(sql_search=sql_search, offset=offset, limit=limit, status=status, order_by=order_by, sort_order=sort_order, from_date=from_date, to_date=to_date, locale=locale, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all_email_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_search** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **status** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **from_date** | [**DateParam**](.md)|  | [optional] 
 **to_date** | [**DateParam**](.md)|  | [optional] 
 **locale** | **str**|  | [optional] 
 **date_format** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_emails**
> str retrieve_all_emails()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_all_emails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all_emails: %s\n" % e)
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

# **retrieve_all_emails1**
> SmsCampaignData retrieve_all_emails1(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)

List SMS Campaigns

Example Requests:  smscampaigns

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    # List SMS Campaigns
    api_response = api_instance.retrieve_all_emails1(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_all_emails1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

[**SmsCampaignData**](SmsCampaignData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_campaign**
> SmsCampaignData retrieve_campaign(resource_id)

Retrieve a SMS Campaign

Example Requests:  smscampaigns/1 

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    # Retrieve a SMS Campaign
    api_response = api_instance.retrieve_campaign(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

[**SmsCampaignData**](SmsCampaignData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_failed_email**
> str retrieve_failed_email(sql_search=sql_search, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
sql_search = 'sql_search_example' # str |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_failed_email(sql_search=sql_search, offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_failed_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_search** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_image**
> retrieve_image(entity, entity_id, max_width=max_width, max_height=max_height, output=output, accept=accept)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
entity = 'entity_example' # str | 
entity_id = 789 # int | 
max_width = 56 # int |  (optional)
max_height = 56 # int |  (optional)
output = 'output_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)

try:
    api_instance.retrieve_image(entity, entity_id, max_width=max_width, max_height=max_height, output=output, accept=accept)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 
 **entity_id** | **int**|  | 
 **max_width** | **int**|  | [optional] 
 **max_height** | **int**|  | [optional] 
 **output** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_office_transactions**
> str retrieve_office_transactions()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_office_transactions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_office_transactions: %s\n" % e)
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

# **retrieve_one1**
> str retrieve_one1(resource_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    api_response = api_instance.retrieve_one1(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_one1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one_campaign**
> str retrieve_one_campaign(resource_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    api_response = api_instance.retrieve_one_campaign(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_one_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_one_template**
> str retrieve_one_template(resource_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 

try:
    api_response = api_instance.retrieve_one_template(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_one_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_pending_email**
> str retrieve_pending_email(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_pending_email(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_pending_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sent_email**
> str retrieve_sent_email(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order_by = 'order_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    api_response = api_instance.retrieve_sent_email(offset=offset, limit=limit, order_by=order_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_sent_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_credit_report**
> str save_credit_report(credit_bureau_id=credit_bureau_id, national_id=national_id)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
credit_bureau_id = 789 # int | creditBureauId (optional)
national_id = 'national_id_example' # str | nationalId (optional)

try:
    api_response = api_instance.save_credit_report(credit_bureau_id=credit_bureau_id, national_id=national_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_bureau_id** | **int**| creditBureauId | [optional] 
 **national_id** | **str**| nationalId | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template1**
> str template1()



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    api_response = api_instance.template1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->template1: %s\n" % e)
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

# **template2**
> SmsCampaignData template2()

Retrieve a SMS Campaign

Example Requests:  smscampaigns/1   smscampaigns/1?template=true   smscampaigns/template

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve a SMS Campaign
    api_response = api_instance.template2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->template2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmsCampaignData**](SmsCampaignData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_money_from**
> str transfer_money_from(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.transfer_money_from(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transfer_money_from: %s\n" % e)
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

# **update2**
> str update2(resource_id, body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update2(resource_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> str update_campaign(resource_id, body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
resource_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_campaign(resource_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign1**
> CommandProcessingResult update_campaign1(body, campaign_id)

Update a Campaign

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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = fineract_client.CommandWrapper() # CommandWrapper | 
campaign_id = 789 # int | 

try:
    # Update a Campaign
    api_response = api_instance.update_campaign1(body, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_campaign1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommandWrapper**](CommandWrapper.md)|  | 
 **campaign_id** | **int**|  | 

### Return type

[**CommandProcessingResult**](CommandProcessingResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_image1**
> str update_client_image1(entity, entity_id, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, content_length=content_length)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
entity = 'entity_example' # str | 
entity_id = 789 # int | 
date_format = 'date_format_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
uploaded_input_stream = 'uploaded_input_stream_example' # str |  (optional)
content_length = 789 # int |  (optional)

try:
    api_response = api_instance.update_client_image1(entity, entity_id, date_format=date_format, locale=locale, uploaded_input_stream=uploaded_input_stream, content_length=content_length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_client_image1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 
 **entity_id** | **int**|  | 
 **date_format** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **uploaded_input_stream** | **str**|  | [optional] 
 **content_length** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> str update_configuration(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_configuration: %s\n" % e)
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

# **update_configuration3**
> str update_configuration3(body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_configuration3(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_configuration3: %s\n" % e)
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

# **update_global_configuration**
> update_global_configuration(config_id, config_value, body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
config_id = 789 # int | 
config_value = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_instance.update_global_configuration(config_id, config_value, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->update_global_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**|  | 
 **config_value** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_cob_last_date**
> update_loan_cob_last_date(loan_id, body=body)



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
api_instance = fineract_client.DefaultApi(fineract_client.ApiClient(configuration))
loan_id = 789 # int | 
body = 'body_example' # str |  (optional)

try:
    api_instance.update_loan_cob_last_date(loan_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->update_loan_cob_last_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

