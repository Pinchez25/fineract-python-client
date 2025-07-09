# GetSelfUserDetailsOrganisationalRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_user_details_organisational_role import GetSelfUserDetailsOrganisationalRole

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfUserDetailsOrganisationalRole from a JSON string
get_self_user_details_organisational_role_instance = GetSelfUserDetailsOrganisationalRole.from_json(json)
# print the JSON string representation of the object
print(GetSelfUserDetailsOrganisationalRole.to_json())

# convert the object into a dict
get_self_user_details_organisational_role_dict = get_self_user_details_organisational_role_instance.to_dict()
# create an instance of GetSelfUserDetailsOrganisationalRole from a dict
get_self_user_details_organisational_role_from_dict = GetSelfUserDetailsOrganisationalRole.from_dict(get_self_user_details_organisational_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


