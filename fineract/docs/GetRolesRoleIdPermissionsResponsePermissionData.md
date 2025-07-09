# GetRolesRoleIdPermissionsResponsePermissionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**grouping** | **str** |  | [optional] 
**selected** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_roles_role_id_permissions_response_permission_data import GetRolesRoleIdPermissionsResponsePermissionData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRolesRoleIdPermissionsResponsePermissionData from a JSON string
get_roles_role_id_permissions_response_permission_data_instance = GetRolesRoleIdPermissionsResponsePermissionData.from_json(json)
# print the JSON string representation of the object
print GetRolesRoleIdPermissionsResponsePermissionData.to_json()

# convert the object into a dict
get_roles_role_id_permissions_response_permission_data_dict = get_roles_role_id_permissions_response_permission_data_instance.to_dict()
# create an instance of GetRolesRoleIdPermissionsResponsePermissionData from a dict
get_roles_role_id_permissions_response_permission_data_form_dict = get_roles_role_id_permissions_response_permission_data.from_dict(get_roles_role_id_permissions_response_permission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


