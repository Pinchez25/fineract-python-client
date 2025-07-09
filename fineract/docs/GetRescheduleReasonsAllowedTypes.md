# GetRescheduleReasonsAllowedTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_reschedule_reasons_allowed_types import GetRescheduleReasonsAllowedTypes

# TODO update the JSON string below
json = "{}"
# create an instance of GetRescheduleReasonsAllowedTypes from a JSON string
get_reschedule_reasons_allowed_types_instance = GetRescheduleReasonsAllowedTypes.from_json(json)
# print the JSON string representation of the object
print GetRescheduleReasonsAllowedTypes.to_json()

# convert the object into a dict
get_reschedule_reasons_allowed_types_dict = get_reschedule_reasons_allowed_types_instance.to_dict()
# create an instance of GetRescheduleReasonsAllowedTypes from a dict
get_reschedule_reasons_allowed_types_form_dict = get_reschedule_reasons_allowed_types.from_dict(get_reschedule_reasons_allowed_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


