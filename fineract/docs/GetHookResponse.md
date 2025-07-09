# GetHookResponse

GetHookResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[ModelField]**](ModelField.md) |  | [optional] 
**created_at** | **date** |  | [optional] 
**display_name** | **str** |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**template_name** | **str** |  | [optional] 
**updated_at** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_hook_response import GetHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHookResponse from a JSON string
get_hook_response_instance = GetHookResponse.from_json(json)
# print the JSON string representation of the object
print(GetHookResponse.to_json())

# convert the object into a dict
get_hook_response_dict = get_hook_response_instance.to_dict()
# create an instance of GetHookResponse from a dict
get_hook_response_from_dict = GetHookResponse.from_dict(get_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


