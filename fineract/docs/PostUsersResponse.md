# PostUsersResponse

PostUsersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_users_response import PostUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUsersResponse from a JSON string
post_users_response_instance = PostUsersResponse.from_json(json)
# print the JSON string representation of the object
print(PostUsersResponse.to_json())

# convert the object into a dict
post_users_response_dict = post_users_response_instance.to_dict()
# create an instance of PostUsersResponse from a dict
post_users_response_from_dict = PostUsersResponse.from_dict(post_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


