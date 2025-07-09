# ParameterizedHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **Dict[str, str]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.parameterized_header import ParameterizedHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterizedHeader from a JSON string
parameterized_header_instance = ParameterizedHeader.from_json(json)
# print the JSON string representation of the object
print(ParameterizedHeader.to_json())

# convert the object into a dict
parameterized_header_dict = parameterized_header_instance.to_dict()
# create an instance of ParameterizedHeader from a dict
parameterized_header_from_dict = ParameterizedHeader.from_dict(parameterized_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


