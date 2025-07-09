# PostGroupsGroupIdRequest

PostGroupsGroupIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**List[PostGroupsGroupIdClients]**](PostGroupsGroupIdClients.md) |  | [optional] 
**destination_group_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_groups_group_id_request import PostGroupsGroupIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupsGroupIdRequest from a JSON string
post_groups_group_id_request_instance = PostGroupsGroupIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostGroupsGroupIdRequest.to_json())

# convert the object into a dict
post_groups_group_id_request_dict = post_groups_group_id_request_instance.to_dict()
# create an instance of PostGroupsGroupIdRequest from a dict
post_groups_group_id_request_from_dict = PostGroupsGroupIdRequest.from_dict(post_groups_group_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


