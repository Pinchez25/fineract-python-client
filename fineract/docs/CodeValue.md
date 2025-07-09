# CodeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**code** | [**Code**](Code.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**new** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.code_value import CodeValue

# TODO update the JSON string below
json = "{}"
# create an instance of CodeValue from a JSON string
code_value_instance = CodeValue.from_json(json)
# print the JSON string representation of the object
print(CodeValue.to_json())

# convert the object into a dict
code_value_dict = code_value_instance.to_dict()
# create an instance of CodeValue from a dict
code_value_from_dict = CodeValue.from_dict(code_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


