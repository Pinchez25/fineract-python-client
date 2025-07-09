# ScorecardValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [optional] 
**question_id** | **int** |  | [optional] 
**response_id** | **int** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.scorecard_value import ScorecardValue

# TODO update the JSON string below
json = "{}"
# create an instance of ScorecardValue from a JSON string
scorecard_value_instance = ScorecardValue.from_json(json)
# print the JSON string representation of the object
print(ScorecardValue.to_json())

# convert the object into a dict
scorecard_value_dict = scorecard_value_instance.to_dict()
# create an instance of ScorecardValue from a dict
scorecard_value_from_dict = ScorecardValue.from_dict(scorecard_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


