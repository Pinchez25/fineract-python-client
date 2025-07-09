# QuestionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_key** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**response_datas** | [**List[ResponseData]**](ResponseData.md) |  | [optional] 
**sequence_no** | **int** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.question_data import QuestionData

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionData from a JSON string
question_data_instance = QuestionData.from_json(json)
# print the JSON string representation of the object
print QuestionData.to_json()

# convert the object into a dict
question_data_dict = question_data_instance.to_dict()
# create an instance of QuestionData from a dict
question_data_form_dict = question_data.from_dict(question_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


