# GetSelfUserDetailsRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_user_details_roles import GetSelfUserDetailsRoles

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfUserDetailsRoles from a JSON string
get_self_user_details_roles_instance = GetSelfUserDetailsRoles.from_json(json)
# print the JSON string representation of the object
print GetSelfUserDetailsRoles.to_json()

# convert the object into a dict
get_self_user_details_roles_dict = get_self_user_details_roles_instance.to_dict()
# create an instance of GetSelfUserDetailsRoles from a dict
get_self_user_details_roles_form_dict = get_self_user_details_roles.from_dict(get_self_user_details_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


