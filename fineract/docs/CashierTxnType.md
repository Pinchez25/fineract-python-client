# CashierTxnType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.cashier_txn_type import CashierTxnType

# TODO update the JSON string below
json = "{}"
# create an instance of CashierTxnType from a JSON string
cashier_txn_type_instance = CashierTxnType.from_json(json)
# print the JSON string representation of the object
print(CashierTxnType.to_json())

# convert the object into a dict
cashier_txn_type_dict = cashier_txn_type_instance.to_dict()
# create an instance of CashierTxnType from a dict
cashier_txn_type_from_dict = CashierTxnType.from_dict(cashier_txn_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


