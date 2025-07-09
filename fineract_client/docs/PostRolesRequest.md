# PostRolesRequest

PostRolesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_roles_request import PostRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRolesRequest from a JSON string
post_roles_request_instance = PostRolesRequest.from_json(json)
# print the JSON string representation of the object
print(PostRolesRequest.to_json())

# convert the object into a dict
post_roles_request_dict = post_roles_request_instance.to_dict()
# create an instance of PostRolesRequest from a dict
post_roles_request_from_dict = PostRolesRequest.from_dict(post_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


