# Question


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_key** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**responses** | [**List[Response]**](Response.md) |  | [optional] 
**sequence_no** | **int** |  | [optional] 
**survey** | [**Survey**](Survey.md) |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.question import Question

# TODO update the JSON string below
json = "{}"
# create an instance of Question from a JSON string
question_instance = Question.from_json(json)
# print the JSON string representation of the object
print(Question.to_json())

# convert the object into a dict
question_dict = question_instance.to_dict()
# create an instance of Question from a dict
question_from_dict = Question.from_dict(question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


