# PutHookResponseChangesSwagger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[Field]**](Field.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_hook_response_changes_swagger import PutHookResponseChangesSwagger

# TODO update the JSON string below
json = "{}"
# create an instance of PutHookResponseChangesSwagger from a JSON string
put_hook_response_changes_swagger_instance = PutHookResponseChangesSwagger.from_json(json)
# print the JSON string representation of the object
print PutHookResponseChangesSwagger.to_json()

# convert the object into a dict
put_hook_response_changes_swagger_dict = put_hook_response_changes_swagger_instance.to_dict()
# create an instance of PutHookResponseChangesSwagger from a dict
put_hook_response_changes_swagger_form_dict = put_hook_response_changes_swagger.from_dict(put_hook_response_changes_swagger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


