# JournalEntryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**accounting_rule_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**credits** | [**List[SingleDebitOrCreditEntryCommand]**](SingleDebitOrCreditEntryCommand.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**debits** | [**List[SingleDebitOrCreditEntryCommand]**](SingleDebitOrCreditEntryCommand.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**transaction_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.journal_entry_command import JournalEntryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryCommand from a JSON string
journal_entry_command_instance = JournalEntryCommand.from_json(json)
# print the JSON string representation of the object
print JournalEntryCommand.to_json()

# convert the object into a dict
journal_entry_command_dict = journal_entry_command_instance.to_dict()
# create an instance of JournalEntryCommand from a dict
journal_entry_command_form_dict = journal_entry_command.from_dict(journal_entry_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


