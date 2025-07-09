# EnumOptionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.enum_option_type import EnumOptionType

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOptionType from a JSON string
enum_option_type_instance = EnumOptionType.from_json(json)
# print the JSON string representation of the object
print(EnumOptionType.to_json())

# convert the object into a dict
enum_option_type_dict = enum_option_type_instance.to_dict()
# create an instance of EnumOptionType from a dict
enum_option_type_from_dict = EnumOptionType.from_dict(enum_option_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


