# PostGroupsGroupIdCommandUnassignStaffResponse

PostGroupsGroupIdCommandUnassignStaffResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_groups_group_id_command_unassign_staff_response import PostGroupsGroupIdCommandUnassignStaffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupsGroupIdCommandUnassignStaffResponse from a JSON string
post_groups_group_id_command_unassign_staff_response_instance = PostGroupsGroupIdCommandUnassignStaffResponse.from_json(json)
# print the JSON string representation of the object
print(PostGroupsGroupIdCommandUnassignStaffResponse.to_json())

# convert the object into a dict
post_groups_group_id_command_unassign_staff_response_dict = post_groups_group_id_command_unassign_staff_response_instance.to_dict()
# create an instance of PostGroupsGroupIdCommandUnassignStaffResponse from a dict
post_groups_group_id_command_unassign_staff_response_from_dict = PostGroupsGroupIdCommandUnassignStaffResponse.from_dict(post_groups_group_id_command_unassign_staff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


