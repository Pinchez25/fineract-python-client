# PutHookResponse

PutHookResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutHookResponseChangesSwagger**](PutHookResponseChangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_hook_response import PutHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutHookResponse from a JSON string
put_hook_response_instance = PutHookResponse.from_json(json)
# print the JSON string representation of the object
print PutHookResponse.to_json()

# convert the object into a dict
put_hook_response_dict = put_hook_response_instance.to_dict()
# create an instance of PutHookResponse from a dict
put_hook_response_form_dict = put_hook_response.from_dict(put_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


