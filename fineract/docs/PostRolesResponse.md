# PostRolesResponse

PostRolesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_roles_response import PostRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRolesResponse from a JSON string
post_roles_response_instance = PostRolesResponse.from_json(json)
# print the JSON string representation of the object
print(PostRolesResponse.to_json())

# convert the object into a dict
post_roles_response_dict = post_roles_response_instance.to_dict()
# create an instance of PostRolesResponse from a dict
post_roles_response_from_dict = PostRolesResponse.from_dict(post_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


