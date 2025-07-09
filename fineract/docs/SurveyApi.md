# fineract_client.SurveyApi

All URIs are relative to *http://localhost/fineract-provider/api/v1*

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
> PostSurveySurveyNameApptableIdResponse create_datatable_entry1(survey_name, apptable_id, post_survey_survey_name_apptable_id_request)

Create an entry in the survey table

Insert and entry in a survey table (full fill the survey).  Refer Link for sample Body:  [ https://fineract.apache.org/legacy-docs/apiLive.htm#survey_create ]

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.post_survey_survey_name_apptable_id_request import PostSurveySurveyNameApptableIdRequest
from fineract_client.models.post_survey_survey_name_apptable_id_response import PostSurveySurveyNameApptableIdResponse
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | surveyName
    apptable_id = 56 # int | apptableId
    post_survey_survey_name_apptable_id_request = fineract_client.PostSurveySurveyNameApptableIdRequest() # PostSurveySurveyNameApptableIdRequest | 

    try:
        # Create an entry in the survey table
        api_response = api_instance.create_datatable_entry1(survey_name, apptable_id, post_survey_survey_name_apptable_id_request)
        print("The response of SurveyApi->create_datatable_entry1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyApi->create_datatable_entry1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**| surveyName | 
 **apptable_id** | **int**| apptableId | 
 **post_survey_survey_name_apptable_id_request** | [**PostSurveySurveyNameApptableIdRequest**](PostSurveySurveyNameApptableIdRequest.md)|  | 

### Return type

[**PostSurveySurveyNameApptableIdResponse**](PostSurveySurveyNameApptableIdResponse.md)

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

# **delete_datatable_entries1**
> str delete_datatable_entries1(survey_name, client_id, fulfilled_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | 
    client_id = 56 # int | 
    fulfilled_id = 56 # int | 

    try:
        api_response = api_instance.delete_datatable_entries1(survey_name, client_id, fulfilled_id)
        print("The response of SurveyApi->delete_datatable_entries1:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_survey_overview**
> str get_client_survey_overview(survey_name, client_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | 
    client_id = 56 # int | 

    try:
        api_response = api_instance.get_client_survey_overview(survey_name, client_id)
        print("The response of SurveyApi->get_client_survey_overview:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_survey_entry**
> str get_survey_entry(survey_name, client_id, entry_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | 
    client_id = 56 # int | 
    entry_id = 56 # int | 

    try:
        api_response = api_instance.get_survey_entry(survey_name, client_id, entry_id)
        print("The response of SurveyApi->get_survey_entry:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> str register(survey_name, apptable, body=body)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | 
    apptable = 'apptable_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.register(survey_name, apptable, body=body)
        print("The response of SurveyApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_name** | **str**|  | 
 **apptable** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_survey**
> GetSurveyResponse retrieve_survey(survey_name)

Retrieve survey

Lists a registered survey table details and the Apache Fineract Core application table they are registered to.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_survey_response import GetSurveyResponse
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
    api_instance = fineract_client.SurveyApi(api_client)
    survey_name = 'survey_name_example' # str | surveyName

    try:
        # Retrieve survey
        api_response = api_instance.retrieve_survey(survey_name)
        print("The response of SurveyApi->retrieve_survey:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_surveys**
> List[GetSurveyResponse] retrieve_surveys()

Retrieve surveys

Retrieve surveys. This allows to retrieve the list of survey tables registered .

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tenantid):

```python
import fineract_client
from fineract_client.models.get_survey_response import GetSurveyResponse
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
    api_instance = fineract_client.SurveyApi(api_client)

    try:
        # Retrieve surveys
        api_response = api_instance.retrieve_surveys()
        print("The response of SurveyApi->retrieve_surveys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyApi->retrieve_surveys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetSurveyResponse]**](GetSurveyResponse.md)

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

