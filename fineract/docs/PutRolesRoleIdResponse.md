# PutRolesRoleIdResponse

PutRolesRoleIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutRolesRoleIdResponseChanges**](PutRolesRoleIdResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_roles_role_id_response import PutRolesRoleIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRolesRoleIdResponse from a JSON string
put_roles_role_id_response_instance = PutRolesRoleIdResponse.from_json(json)
# print the JSON string representation of the object
print PutRolesRoleIdResponse.to_json()

# convert the object into a dict
put_roles_role_id_response_dict = put_roles_role_id_response_instance.to_dict()
# create an instance of PutRolesRoleIdResponse from a dict
put_roles_role_id_response_form_dict = put_roles_role_id_response.from_dict(put_roles_role_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


