# PutRolesRoleIdRequest

PutRolesRoleIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_roles_role_id_request import PutRolesRoleIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutRolesRoleIdRequest from a JSON string
put_roles_role_id_request_instance = PutRolesRoleIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutRolesRoleIdRequest.to_json())

# convert the object into a dict
put_roles_role_id_request_dict = put_roles_role_id_request_instance.to_dict()
# create an instance of PutRolesRoleIdRequest from a dict
put_roles_role_id_request_from_dict = PutRolesRoleIdRequest.from_dict(put_roles_role_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


