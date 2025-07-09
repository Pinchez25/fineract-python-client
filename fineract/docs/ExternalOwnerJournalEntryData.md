# ExternalOwnerJournalEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_data** | [**PageJournalEntryData**](PageJournalEntryData.md) |  | [optional] 
**owner_data** | [**ExternalTransferOwnerData**](ExternalTransferOwnerData.md) |  | [optional] 

## Example

```python
from fineract_client.models.external_owner_journal_entry_data import ExternalOwnerJournalEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalOwnerJournalEntryData from a JSON string
external_owner_journal_entry_data_instance = ExternalOwnerJournalEntryData.from_json(json)
# print the JSON string representation of the object
print ExternalOwnerJournalEntryData.to_json()

# convert the object into a dict
external_owner_journal_entry_data_dict = external_owner_journal_entry_data_instance.to_dict()
# create an instance of ExternalOwnerJournalEntryData from a dict
external_owner_journal_entry_data_form_dict = external_owner_journal_entry_data.from_dict(external_owner_journal_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


