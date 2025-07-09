# PostJournalEntriesResponse

PostJournalEntriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** | 1 | [optional] 
**transaction_id** | **str** | RS9MCISID4WK1ZM | [optional] 

## Example

```python
from fineract_client.models.post_journal_entries_response import PostJournalEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostJournalEntriesResponse from a JSON string
post_journal_entries_response_instance = PostJournalEntriesResponse.from_json(json)
# print the JSON string representation of the object
print PostJournalEntriesResponse.to_json()

# convert the object into a dict
post_journal_entries_response_dict = post_journal_entries_response_instance.to_dict()
# create an instance of PostJournalEntriesResponse from a dict
post_journal_entries_response_form_dict = post_journal_entries_response.from_dict(post_journal_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


