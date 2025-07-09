# RescheduleReasonsCodeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.reschedule_reasons_code_value import RescheduleReasonsCodeValue

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleReasonsCodeValue from a JSON string
reschedule_reasons_code_value_instance = RescheduleReasonsCodeValue.from_json(json)
# print the JSON string representation of the object
print(RescheduleReasonsCodeValue.to_json())

# convert the object into a dict
reschedule_reasons_code_value_dict = reschedule_reasons_code_value_instance.to_dict()
# create an instance of RescheduleReasonsCodeValue from a dict
reschedule_reasons_code_value_from_dict = RescheduleReasonsCodeValue.from_dict(reschedule_reasons_code_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


