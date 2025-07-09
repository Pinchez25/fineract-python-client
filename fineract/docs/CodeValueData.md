# CodeValueData


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
from fineract_client.models.code_value_data import CodeValueData

# TODO update the JSON string below
json = "{}"
# create an instance of CodeValueData from a JSON string
code_value_data_instance = CodeValueData.from_json(json)
# print the JSON string representation of the object
print CodeValueData.to_json()

# convert the object into a dict
code_value_data_dict = code_value_data_instance.to_dict()
# create an instance of CodeValueData from a dict
code_value_data_form_dict = code_value_data.from_dict(code_value_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


