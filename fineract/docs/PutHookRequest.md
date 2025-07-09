# PutHookRequest

PutHookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[ModelField]**](ModelField.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_hook_request import PutHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutHookRequest from a JSON string
put_hook_request_instance = PutHookRequest.from_json(json)
# print the JSON string representation of the object
print(PutHookRequest.to_json())

# convert the object into a dict
put_hook_request_dict = put_hook_request_instance.to_dict()
# create an instance of PutHookRequest from a dict
put_hook_request_from_dict = PutHookRequest.from_dict(put_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


