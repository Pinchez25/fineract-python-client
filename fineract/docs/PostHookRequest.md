# PostHookRequest

PostHookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[Field]**](Field.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_hook_request import PostHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostHookRequest from a JSON string
post_hook_request_instance = PostHookRequest.from_json(json)
# print the JSON string representation of the object
print PostHookRequest.to_json()

# convert the object into a dict
post_hook_request_dict = post_hook_request_instance.to_dict()
# create an instance of PostHookRequest from a dict
post_hook_request_form_dict = post_hook_request.from_dict(post_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


