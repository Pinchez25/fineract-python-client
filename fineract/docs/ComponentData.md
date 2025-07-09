# ComponentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**sequence_no** | **int** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.component_data import ComponentData

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentData from a JSON string
component_data_instance = ComponentData.from_json(json)
# print the JSON string representation of the object
print(ComponentData.to_json())

# convert the object into a dict
component_data_dict = component_data_instance.to_dict()
# create an instance of ComponentData from a dict
component_data_from_dict = ComponentData.from_dict(component_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


