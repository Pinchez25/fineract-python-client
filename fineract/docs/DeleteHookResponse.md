# DeleteHookResponse

DeleteHookResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_hook_response import DeleteHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHookResponse from a JSON string
delete_hook_response_instance = DeleteHookResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteHookResponse.to_json())

# convert the object into a dict
delete_hook_response_dict = delete_hook_response_instance.to_dict()
# create an instance of DeleteHookResponse from a dict
delete_hook_response_from_dict = DeleteHookResponse.from_dict(delete_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


