# GetJournalEntriesTransactionIdResponse

GetJournalEntriesTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[JournalEntryTransactionItem]**](JournalEntryTransactionItem.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_journal_entries_transaction_id_response import GetJournalEntriesTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetJournalEntriesTransactionIdResponse from a JSON string
get_journal_entries_transaction_id_response_instance = GetJournalEntriesTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetJournalEntriesTransactionIdResponse.to_json()

# convert the object into a dict
get_journal_entries_transaction_id_response_dict = get_journal_entries_transaction_id_response_instance.to_dict()
# create an instance of GetJournalEntriesTransactionIdResponse from a dict
get_journal_entries_transaction_id_response_form_dict = get_journal_entries_transaction_id_response.from_dict(get_journal_entries_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


