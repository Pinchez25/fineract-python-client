# PutRolesRoleIdPermissionsRequest

PutRolesRoleIdPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from fineract_client.models.put_roles_role_id_permissions_request import PutRolesRoleIdPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutRolesRoleIdPermissionsRequest from a JSON string
put_roles_role_id_permissions_request_instance = PutRolesRoleIdPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print PutRolesRoleIdPermissionsRequest.to_json()

# convert the object into a dict
put_roles_role_id_permissions_request_dict = put_roles_role_id_permissions_request_instance.to_dict()
# create an instance of PutRolesRoleIdPermissionsRequest from a dict
put_roles_role_id_permissions_request_form_dict = put_roles_role_id_permissions_request.from_dict(put_roles_role_id_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


