# PutRolesRoleIdPermissionsResponse

PutRolesRoleIdPermissionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutRolesRoleIdPermissionsResponsePermissionsChanges**](PutRolesRoleIdPermissionsResponsePermissionsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_roles_role_id_permissions_response import PutRolesRoleIdPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRolesRoleIdPermissionsResponse from a JSON string
put_roles_role_id_permissions_response_instance = PutRolesRoleIdPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(PutRolesRoleIdPermissionsResponse.to_json())

# convert the object into a dict
put_roles_role_id_permissions_response_dict = put_roles_role_id_permissions_response_instance.to_dict()
# create an instance of PutRolesRoleIdPermissionsResponse from a dict
put_roles_role_id_permissions_response_from_dict = PutRolesRoleIdPermissionsResponse.from_dict(put_roles_role_id_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


