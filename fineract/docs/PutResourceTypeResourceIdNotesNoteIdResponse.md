# PutResourceTypeResourceIdNotesNoteIdResponse

PutResourceTypeResourceIdNotesNoteIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutNotesChanges**](PutNotesChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_resource_type_resource_id_notes_note_id_response import PutResourceTypeResourceIdNotesNoteIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutResourceTypeResourceIdNotesNoteIdResponse from a JSON string
put_resource_type_resource_id_notes_note_id_response_instance = PutResourceTypeResourceIdNotesNoteIdResponse.from_json(json)
# print the JSON string representation of the object
print PutResourceTypeResourceIdNotesNoteIdResponse.to_json()

# convert the object into a dict
put_resource_type_resource_id_notes_note_id_response_dict = put_resource_type_resource_id_notes_note_id_response_instance.to_dict()
# create an instance of PutResourceTypeResourceIdNotesNoteIdResponse from a dict
put_resource_type_resource_id_notes_note_id_response_form_dict = put_resource_type_resource_id_notes_note_id_response.from_dict(put_resource_type_resource_id_notes_note_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


