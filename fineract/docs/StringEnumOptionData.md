# StringEnumOptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.string_enum_option_data import StringEnumOptionData

# TODO update the JSON string below
json = "{}"
# create an instance of StringEnumOptionData from a JSON string
string_enum_option_data_instance = StringEnumOptionData.from_json(json)
# print the JSON string representation of the object
print StringEnumOptionData.to_json()

# convert the object into a dict
string_enum_option_data_dict = string_enum_option_data_instance.to_dict()
# create an instance of StringEnumOptionData from a dict
string_enum_option_data_form_dict = string_enum_option_data.from_dict(string_enum_option_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


