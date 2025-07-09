# SingleDebitOrCreditEntryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**comments_changed** | **bool** |  | [optional] 
**gl_account_id** | **int** |  | [optional] 
**gl_account_id_changed** | **bool** |  | [optional] 
**gl_amount_changed** | **bool** |  | [optional] 
**parameters_passed_in_request** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.single_debit_or_credit_entry_command import SingleDebitOrCreditEntryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SingleDebitOrCreditEntryCommand from a JSON string
single_debit_or_credit_entry_command_instance = SingleDebitOrCreditEntryCommand.from_json(json)
# print the JSON string representation of the object
print(SingleDebitOrCreditEntryCommand.to_json())

# convert the object into a dict
single_debit_or_credit_entry_command_dict = single_debit_or_credit_entry_command_instance.to_dict()
# create an instance of SingleDebitOrCreditEntryCommand from a dict
single_debit_or_credit_entry_command_from_dict = SingleDebitOrCreditEntryCommand.from_dict(single_debit_or_credit_entry_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


