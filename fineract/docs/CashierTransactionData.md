# CashierTransactionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_data** | [**CashierData**](CashierData.md) |  | [optional] 
**cashier_id** | **int** |  | [optional] 
**cashier_name** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**currency_options** | [**List[CurrencyData]**](CurrencyData.md) |  | [optional] 
**end_date** | **date** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 
**txn_amount** | **float** |  | [optional] 
**txn_date** | **date** |  | [optional] 
**txn_note** | **str** |  | [optional] 
**txn_type** | [**CashierTxnType**](CashierTxnType.md) |  | [optional] 

## Example

```python
from fineract_client.models.cashier_transaction_data import CashierTransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of CashierTransactionData from a JSON string
cashier_transaction_data_instance = CashierTransactionData.from_json(json)
# print the JSON string representation of the object
print(CashierTransactionData.to_json())

# convert the object into a dict
cashier_transaction_data_dict = cashier_transaction_data_instance.to_dict()
# create an instance of CashierTransactionData from a dict
cashier_transaction_data_from_dict = CashierTransactionData.from_dict(cashier_transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


