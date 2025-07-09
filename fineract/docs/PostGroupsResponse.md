# PostGroupsResponse

PostGroupsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_groups_response import PostGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupsResponse from a JSON string
post_groups_response_instance = PostGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(PostGroupsResponse.to_json())

# convert the object into a dict
post_groups_response_dict = post_groups_response_instance.to_dict()
# create an instance of PostGroupsResponse from a dict
post_groups_response_from_dict = PostGroupsResponse.from_dict(post_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


