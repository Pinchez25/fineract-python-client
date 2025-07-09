# EnumOptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.enum_option_data import EnumOptionData

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOptionData from a JSON string
enum_option_data_instance = EnumOptionData.from_json(json)
# print the JSON string representation of the object
print(EnumOptionData.to_json())

# convert the object into a dict
enum_option_data_dict = enum_option_data_instance.to_dict()
# create an instance of EnumOptionData from a dict
enum_option_data_from_dict = EnumOptionData.from_dict(enum_option_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


