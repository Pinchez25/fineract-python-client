# SurveyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_datas** | [**List[ComponentData]**](ComponentData.md) |  | [optional] 
**country_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**question_datas** | [**List[QuestionData]**](QuestionData.md) |  | [optional] 
**valid_from** | **date** |  | [optional] 
**valid_to** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.survey_data import SurveyData

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyData from a JSON string
survey_data_instance = SurveyData.from_json(json)
# print the JSON string representation of the object
print SurveyData.to_json()

# convert the object into a dict
survey_data_dict = survey_data_instance.to_dict()
# create an instance of SurveyData from a dict
survey_data_form_dict = survey_data.from_dict(survey_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


