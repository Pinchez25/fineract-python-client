# ExtensionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.extension_data import ExtensionData

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionData from a JSON string
extension_data_instance = ExtensionData.from_json(json)
# print the JSON string representation of the object
print(ExtensionData.to_json())

# convert the object into a dict
extension_data_dict = extension_data_instance.to_dict()
# create an instance of ExtensionData from a dict
extension_data_from_dict = ExtensionData.from_dict(extension_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


