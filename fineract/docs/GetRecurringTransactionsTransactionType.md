# GetRecurringTransactionsTransactionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**deposit** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**fee_deduction** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_posting** | **bool** |  | [optional] 
**withdrawal** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_transactions_transaction_type import GetRecurringTransactionsTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringTransactionsTransactionType from a JSON string
get_recurring_transactions_transaction_type_instance = GetRecurringTransactionsTransactionType.from_json(json)
# print the JSON string representation of the object
print(GetRecurringTransactionsTransactionType.to_json())

# convert the object into a dict
get_recurring_transactions_transaction_type_dict = get_recurring_transactions_transaction_type_instance.to_dict()
# create an instance of GetRecurringTransactionsTransactionType from a dict
get_recurring_transactions_transaction_type_from_dict = GetRecurringTransactionsTransactionType.from_dict(get_recurring_transactions_transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


