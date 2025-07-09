# PostNewShareApplicationResponse

PostNewShareApplicationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_new_share_application_response import PostNewShareApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewShareApplicationResponse from a JSON string
post_new_share_application_response_instance = PostNewShareApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(PostNewShareApplicationResponse.to_json())

# convert the object into a dict
post_new_share_application_response_dict = post_new_share_application_response_instance.to_dict()
# create an instance of PostNewShareApplicationResponse from a dict
post_new_share_application_response_from_dict = PostNewShareApplicationResponse.from_dict(post_new_share_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


