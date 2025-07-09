# GetSurveyResponse

GetSurveyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatable_data** | [**GetSurveyResponseDatatableData**](GetSurveyResponseDatatableData.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_survey_response import GetSurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSurveyResponse from a JSON string
get_survey_response_instance = GetSurveyResponse.from_json(json)
# print the JSON string representation of the object
print GetSurveyResponse.to_json()

# convert the object into a dict
get_survey_response_dict = get_survey_response_instance.to_dict()
# create an instance of GetSurveyResponse from a dict
get_survey_response_form_dict = get_survey_response.from_dict(get_survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


