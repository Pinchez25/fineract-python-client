# GetRolesRoleIdResponse

GetRolesRoleIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_roles_role_id_response import GetRolesRoleIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRolesRoleIdResponse from a JSON string
get_roles_role_id_response_instance = GetRolesRoleIdResponse.from_json(json)
# print the JSON string representation of the object
print GetRolesRoleIdResponse.to_json()

# convert the object into a dict
get_roles_role_id_response_dict = get_roles_role_id_response_instance.to_dict()
# create an instance of GetRolesRoleIdResponse from a dict
get_roles_role_id_response_form_dict = get_roles_role_id_response.from_dict(get_roles_role_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


