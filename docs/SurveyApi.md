# fineract_client.SurveyApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_datatable_entry1**](SurveyApi.md#create_datatable_entry1) | **POST** /v1/survey/{surveyName}/{apptableId} | Create an entry in the survey table
[**delete_datatable_entries1**](SurveyApi.md#delete_datatable_entries1) | **DELETE** /v1/survey/{surveyName}/{clientId}/{fulfilledId} | 
[**get_client_survey_overview**](SurveyApi.md#get_client_survey_overview) | **GET** /v1/survey/{surveyName}/{clientId} | 
[**get_survey_entry**](SurveyApi.md#get_survey_entry) | **GET** /v1/survey/{surveyName}/{clientId}/{entryId} | 
[**register**](SurveyApi.md#register) | **PUT** /v1/survey/register/{surveyName}/{apptable} | 
[**retrieve_survey**](SurveyApi.md#retrieve_survey) | **GET** /v1/survey/{surveyName} | Retrieve survey
[**retrieve_surveys**](SurveyApi.md#retrieve_surveys) | **GET** /v1/survey | Retrieve surveys

# **create_datatable_entry1**
> PostSurveySurveyNameApptableIdResponse create_datatable_entry1(body, survey_name, apptable_id)

Create an entry in the survey table

Insert and entry in a survey table (full fill the survey).  Refer Link for sample Body:  [ https://fineract.apache.org/legacy-docs/apiLive.htm#survey_create ]

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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
body = fineract_client.PostSurveySurveyNameApptableIdRequest() # PostSurveySurveyNameApptableIdRequest | 
survey_name = 'survey_name_example' # str | surveyName
apptable_id = 789 # int | apptableId

try:
    # Create an entry in the survey table
    api_response = api_instance.create_datatable_entry1(body, survey_name, apptable_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->create_datatable_entry1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSurveySurveyNameApptableIdRequest**](PostSurveySurveyNameApptableIdRequest.md)|  | 
 **survey_name** | **str**| surveyName | 
 **apptable_id** | **int**| apptableId | 

### Return type

[**PostSurveySurveyNameApptableIdResponse**](PostSurveySurveyNameApptableIdResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datatable_entries1**
> str delete_datatable_entries1(survey_name, client_id, fulfilled_id)



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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
survey_name = 'survey_name_example' # str | 
client_id = 789 # int | 
fulfilled_id = 789 # int | 

try:
    api_response = api_instance.delete_datatable_entries1(survey_name, client_id, fulfilled_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->delete_datatable_entries1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**|  | 
 **client_id** | **int**|  | 
 **fulfilled_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_survey_overview**
> str get_client_survey_overview(survey_name, client_id)



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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
survey_name = 'survey_name_example' # str | 
client_id = 789 # int | 

try:
    api_response = api_instance.get_client_survey_overview(survey_name, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->get_client_survey_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**|  | 
 **client_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_entry**
> str get_survey_entry(survey_name, client_id, entry_id)



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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
survey_name = 'survey_name_example' # str | 
client_id = 789 # int | 
entry_id = 789 # int | 

try:
    api_response = api_instance.get_survey_entry(survey_name, client_id, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->get_survey_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**|  | 
 **client_id** | **int**|  | 
 **entry_id** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> str register(survey_name, apptable, body=body)



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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
survey_name = 'survey_name_example' # str | 
apptable = 'apptable_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.register(survey_name, apptable, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**|  | 
 **apptable** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_survey**
> GetSurveyResponse retrieve_survey(survey_name)

Retrieve survey

Lists a registered survey table details and the Apache Fineract Core application table they are registered to.

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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))
survey_name = 'survey_name_example' # str | surveyName

try:
    # Retrieve survey
    api_response = api_instance.retrieve_survey(survey_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->retrieve_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**| surveyName | 

### Return type

[**GetSurveyResponse**](GetSurveyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_surveys**
> list[GetSurveyResponse] retrieve_surveys()

Retrieve surveys

Retrieve surveys. This allows to retrieve the list of survey tables registered .

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
api_instance = fineract_client.SurveyApi(fineract_client.ApiClient(configuration))

try:
    # Retrieve surveys
    api_response = api_instance.retrieve_surveys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SurveyApi->retrieve_surveys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetSurveyResponse]**](GetSurveyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

