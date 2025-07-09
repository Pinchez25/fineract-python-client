# ExternalOwnerTransferJournalEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_data** | [**PageJournalEntryData**](PageJournalEntryData.md) |  | [optional] 
**transfer_data** | [**ExternalTransferData**](ExternalTransferData.md) |  | [optional] 

## Example

```python
from fineract_client.models.external_owner_transfer_journal_entry_data import ExternalOwnerTransferJournalEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalOwnerTransferJournalEntryData from a JSON string
external_owner_transfer_journal_entry_data_instance = ExternalOwnerTransferJournalEntryData.from_json(json)
# print the JSON string representation of the object
print(ExternalOwnerTransferJournalEntryData.to_json())

# convert the object into a dict
external_owner_transfer_journal_entry_data_dict = external_owner_transfer_journal_entry_data_instance.to_dict()
# create an instance of ExternalOwnerTransferJournalEntryData from a dict
external_owner_transfer_journal_entry_data_from_dict = ExternalOwnerTransferJournalEntryData.from_dict(external_owner_transfer_journal_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


