# GetResourceTypeResourceIdNotesResponse

GetResourceTypeResourceIdNotesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**created_by_id** | **int** |  | [optional] 
**created_by_username** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**note_type** | [**GetNotesNoteType**](GetNotesNoteType.md) |  | [optional] 
**updated_by_id** | **int** |  | [optional] 
**updated_by_username** | **str** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 

## Example

```python
from fineract_client.models.get_resource_type_resource_id_notes_response import GetResourceTypeResourceIdNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceTypeResourceIdNotesResponse from a JSON string
get_resource_type_resource_id_notes_response_instance = GetResourceTypeResourceIdNotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceTypeResourceIdNotesResponse.to_json())

# convert the object into a dict
get_resource_type_resource_id_notes_response_dict = get_resource_type_resource_id_notes_response_instance.to_dict()
# create an instance of GetResourceTypeResourceIdNotesResponse from a dict
get_resource_type_resource_id_notes_response_from_dict = GetResourceTypeResourceIdNotesResponse.from_dict(get_resource_type_resource_id_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


