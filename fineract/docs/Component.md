# Component


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**sequence_no** | **int** |  | [optional] 
**survey** | [**Survey**](Survey.md) |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.component import Component

# TODO update the JSON string below
json = "{}"
# create an instance of Component from a JSON string
component_instance = Component.from_json(json)
# print the JSON string representation of the object
print Component.to_json()

# convert the object into a dict
component_dict = component_instance.to_dict()
# create an instance of Component from a dict
component_form_dict = component.from_dict(component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


