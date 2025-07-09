# PostJournalEntriesTransactionIdRequest

PostJournalEntriesTransactionIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** | 1 | [optional] 

## Example

```python
from fineract_client.models.post_journal_entries_transaction_id_request import PostJournalEntriesTransactionIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostJournalEntriesTransactionIdRequest from a JSON string
post_journal_entries_transaction_id_request_instance = PostJournalEntriesTransactionIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostJournalEntriesTransactionIdRequest.to_json())

# convert the object into a dict
post_journal_entries_transaction_id_request_dict = post_journal_entries_transaction_id_request_instance.to_dict()
# create an instance of PostJournalEntriesTransactionIdRequest from a dict
post_journal_entries_transaction_id_request_from_dict = PostJournalEntriesTransactionIdRequest.from_dict(post_journal_entries_transaction_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


