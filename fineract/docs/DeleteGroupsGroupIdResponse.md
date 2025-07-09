# DeleteGroupsGroupIdResponse

DeleteGroupsGroupIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_groups_group_id_response import DeleteGroupsGroupIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGroupsGroupIdResponse from a JSON string
delete_groups_group_id_response_instance = DeleteGroupsGroupIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteGroupsGroupIdResponse.to_json()

# convert the object into a dict
delete_groups_group_id_response_dict = delete_groups_group_id_response_instance.to_dict()
# create an instance of DeleteGroupsGroupIdResponse from a dict
delete_groups_group_id_response_form_dict = delete_groups_group_id_response.from_dict(delete_groups_group_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


