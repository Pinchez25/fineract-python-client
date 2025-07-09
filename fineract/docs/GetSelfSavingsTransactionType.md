# GetSelfSavingsTransactionType


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
from fineract_client.models.get_self_savings_transaction_type import GetSelfSavingsTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsTransactionType from a JSON string
get_self_savings_transaction_type_instance = GetSelfSavingsTransactionType.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsTransactionType.to_json())

# convert the object into a dict
get_self_savings_transaction_type_dict = get_self_savings_transaction_type_instance.to_dict()
# create an instance of GetSelfSavingsTransactionType from a dict
get_self_savings_transaction_type_from_dict = GetSelfSavingsTransactionType.from_dict(get_self_savings_transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


