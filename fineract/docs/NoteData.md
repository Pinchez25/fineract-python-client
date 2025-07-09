# NoteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**created_by_id** | **int** |  | [optional] 
**created_by_username** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**deposit_account_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**loan_transaction_id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**note_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**saving_account_id** | **int** |  | [optional] 
**updated_by_id** | **int** |  | [optional] 
**updated_by_username** | **str** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 

## Example

```python
from fineract_client.models.note_data import NoteData

# TODO update the JSON string below
json = "{}"
# create an instance of NoteData from a JSON string
note_data_instance = NoteData.from_json(json)
# print the JSON string representation of the object
print NoteData.to_json()

# convert the object into a dict
note_data_dict = note_data_instance.to_dict()
# create an instance of NoteData from a dict
note_data_form_dict = note_data.from_dict(note_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


