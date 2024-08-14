# fineract_client.ScoreCardApi

All URIs are relative to */fineract-provider/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scorecard1**](ScoreCardApi.md#create_scorecard1) | **POST** /v1/surveys/scorecards/{surveyId} | Create a Scorecard entry
[**find_by_client1**](ScoreCardApi.md#find_by_client1) | **GET** /v1/surveys/scorecards/clients/{clientId} | 
[**find_by_survey**](ScoreCardApi.md#find_by_survey) | **GET** /v1/surveys/scorecards/{surveyId} | List all Scorecard entries
[**find_by_survey_and_client**](ScoreCardApi.md#find_by_survey_and_client) | **GET** /v1/surveys/scorecards/{surveyId}/clients/{clientId} | 

# **create_scorecard1**
> create_scorecard1(survey_id, body=body)

Create a Scorecard entry

Add a new entry to a survey.  Mandatory Fields clientId, createdOn, questionId, responseId, staffId

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
api_instance = fineract_client.ScoreCardApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId
body = fineract_client.ScorecardData() # ScorecardData | scorecardData (optional)

try:
    # Create a Scorecard entry
    api_instance.create_scorecard1(survey_id, body=body)
except ApiException as e:
    print("Exception when calling ScoreCardApi->create_scorecard1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 
 **body** | [**ScorecardData**](ScorecardData.md)| scorecardData | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_client1**
> list[ScorecardData] find_by_client1(client_id)



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
api_instance = fineract_client.ScoreCardApi(fineract_client.ApiClient(configuration))
client_id = 789 # int | 

try:
    api_response = api_instance.find_by_client1(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreCardApi->find_by_client1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

[**list[ScorecardData]**](ScorecardData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_survey**
> list[Scorecard] find_by_survey(survey_id)

List all Scorecard entries

List all Scorecard entries for a survey.

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
api_instance = fineract_client.ScoreCardApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId

try:
    # List all Scorecard entries
    api_response = api_instance.find_by_survey(survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreCardApi->find_by_survey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 

### Return type

[**list[Scorecard]**](Scorecard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_survey_and_client**
> list[ScorecardData] find_by_survey_and_client(survey_id, client_id)



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
api_instance = fineract_client.ScoreCardApi(fineract_client.ApiClient(configuration))
survey_id = 789 # int | Enter surveyId
client_id = 789 # int | Enter clientId

try:
    api_response = api_instance.find_by_survey_and_client(survey_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreCardApi->find_by_survey_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| Enter surveyId | 
 **client_id** | **int**| Enter clientId | 

### Return type

[**list[ScorecardData]**](ScorecardData.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tenantid](../README.md#tenantid)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

