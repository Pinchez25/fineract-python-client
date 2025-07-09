# GetGlAccountMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_gl_account_mapping import GetGlAccountMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlAccountMapping from a JSON string
get_gl_account_mapping_instance = GetGlAccountMapping.from_json(json)
# print the JSON string representation of the object
print(GetGlAccountMapping.to_json())

# convert the object into a dict
get_gl_account_mapping_dict = get_gl_account_mapping_instance.to_dict()
# create an instance of GetGlAccountMapping from a dict
get_gl_account_mapping_from_dict = GetGlAccountMapping.from_dict(get_gl_account_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


