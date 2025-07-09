# PostGroupsRequest

PostGroupsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_groups_request import PostGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupsRequest from a JSON string
post_groups_request_instance = PostGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(PostGroupsRequest.to_json())

# convert the object into a dict
post_groups_request_dict = post_groups_request_instance.to_dict()
# create an instance of PostGroupsRequest from a dict
post_groups_request_from_dict = PostGroupsRequest.from_dict(post_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


