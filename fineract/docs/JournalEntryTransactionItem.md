# JournalEntryTransactionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_by_user_name** | **str** |  | [optional] 
**created_date** | **date** |  | [optional] 
**currency** | [**CurrencyItem**](CurrencyItem.md) |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | [**EnumOptionType**](EnumOptionType.md) |  | [optional] 
**entry_type** | [**EnumOptionType**](EnumOptionType.md) |  | [optional] 
**gl_account_code** | **str** |  | [optional] 
**gl_account_id** | **int** |  | [optional] 
**gl_account_name** | **str** |  | [optional] 
**gl_account_type** | [**EnumOptionType**](EnumOptionType.md) |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entry** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**office_running_balance** | **float** |  | [optional] 
**organization_running_balance** | **float** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**running_balance_computed** | **bool** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**transaction_details** | [**TransactionDetails**](TransactionDetails.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.journal_entry_transaction_item import JournalEntryTransactionItem

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryTransactionItem from a JSON string
journal_entry_transaction_item_instance = JournalEntryTransactionItem.from_json(json)
# print the JSON string representation of the object
print(JournalEntryTransactionItem.to_json())

# convert the object into a dict
journal_entry_transaction_item_dict = journal_entry_transaction_item_instance.to_dict()
# create an instance of JournalEntryTransactionItem from a dict
journal_entry_transaction_item_from_dict = JournalEntryTransactionItem.from_dict(journal_entry_transaction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


