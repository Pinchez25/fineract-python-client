# GetStandingInstructionHistoryFromAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instruction_history_from_account import GetStandingInstructionHistoryFromAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionHistoryFromAccount from a JSON string
get_standing_instruction_history_from_account_instance = GetStandingInstructionHistoryFromAccount.from_json(json)
# print the JSON string representation of the object
print(GetStandingInstructionHistoryFromAccount.to_json())

# convert the object into a dict
get_standing_instruction_history_from_account_dict = get_standing_instruction_history_from_account_instance.to_dict()
# create an instance of GetStandingInstructionHistoryFromAccount from a dict
get_standing_instruction_history_from_account_from_dict = GetStandingInstructionHistoryFromAccount.from_dict(get_standing_instruction_history_from_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


