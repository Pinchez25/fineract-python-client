# ScorecardData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**scorecard_values** | [**List[ScorecardValue]**](ScorecardValue.md) |  | [optional] 
**survey_id** | **int** |  | [optional] 
**survey_name** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.scorecard_data import ScorecardData

# TODO update the JSON string below
json = "{}"
# create an instance of ScorecardData from a JSON string
scorecard_data_instance = ScorecardData.from_json(json)
# print the JSON string representation of the object
print ScorecardData.to_json()

# convert the object into a dict
scorecard_data_dict = scorecard_data_instance.to_dict()
# create an instance of ScorecardData from a dict
scorecard_data_form_dict = scorecard_data.from_dict(scorecard_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


