# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 

## Example

```python
from fineract_client.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


