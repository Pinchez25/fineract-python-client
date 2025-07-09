# PageCashierTransactionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[CashierTransactionData]**](CashierTransactionData.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.page_cashier_transaction_data import PageCashierTransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of PageCashierTransactionData from a JSON string
page_cashier_transaction_data_instance = PageCashierTransactionData.from_json(json)
# print the JSON string representation of the object
print PageCashierTransactionData.to_json()

# convert the object into a dict
page_cashier_transaction_data_dict = page_cashier_transaction_data_instance.to_dict()
# create an instance of PageCashierTransactionData from a dict
page_cashier_transaction_data_form_dict = page_cashier_transaction_data.from_dict(page_cashier_transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


