# PostHookResponse

PostHookResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_hook_response import PostHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostHookResponse from a JSON string
post_hook_response_instance = PostHookResponse.from_json(json)
# print the JSON string representation of the object
print PostHookResponse.to_json()

# convert the object into a dict
post_hook_response_dict = post_hook_response_instance.to_dict()
# create an instance of PostHookResponse from a dict
post_hook_response_form_dict = post_hook_response.from_dict(post_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


