# GetRecurringTransactionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approve_transfer** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**deposit** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**fee_deduction** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**initiate_transfer** | **bool** |  | [optional] 
**interest_posting** | **bool** |  | [optional] 
**overdraft_fee** | **bool** |  | [optional] 
**overdraft_interest** | **bool** |  | [optional] 
**reject_transfer** | **bool** |  | [optional] 
**withdraw_transfer** | **bool** |  | [optional] 
**withdrawal** | **bool** |  | [optional] 
**writtenoff** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_transaction_type import GetRecurringTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringTransactionType from a JSON string
get_recurring_transaction_type_instance = GetRecurringTransactionType.from_json(json)
# print the JSON string representation of the object
print(GetRecurringTransactionType.to_json())

# convert the object into a dict
get_recurring_transaction_type_dict = get_recurring_transaction_type_instance.to_dict()
# create an instance of GetRecurringTransactionType from a dict
get_recurring_transaction_type_from_dict = GetRecurringTransactionType.from_dict(get_recurring_transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


