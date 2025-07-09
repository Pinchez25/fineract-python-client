# PageJournalEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[JournalEntryData]**](JournalEntryData.md) |  | [optional] 
**empty** | **bool** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.page_journal_entry_data import PageJournalEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of PageJournalEntryData from a JSON string
page_journal_entry_data_instance = PageJournalEntryData.from_json(json)
# print the JSON string representation of the object
print(PageJournalEntryData.to_json())

# convert the object into a dict
page_journal_entry_data_dict = page_journal_entry_data_instance.to_dict()
# create an instance of PageJournalEntryData from a dict
page_journal_entry_data_from_dict = PageJournalEntryData.from_dict(page_journal_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


