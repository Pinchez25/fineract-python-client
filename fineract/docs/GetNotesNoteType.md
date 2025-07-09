# GetNotesNoteType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_notes_note_type import GetNotesNoteType

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotesNoteType from a JSON string
get_notes_note_type_instance = GetNotesNoteType.from_json(json)
# print the JSON string representation of the object
print GetNotesNoteType.to_json()

# convert the object into a dict
get_notes_note_type_dict = get_notes_note_type_instance.to_dict()
# create an instance of GetNotesNoteType from a dict
get_notes_note_type_form_dict = get_notes_note_type.from_dict(get_notes_note_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


