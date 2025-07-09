# GetTransactionsPaymentDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_type** | [**GetPaymentTypeData**](GetPaymentTypeData.md) |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_transactions_payment_detail_data import GetTransactionsPaymentDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsPaymentDetailData from a JSON string
get_transactions_payment_detail_data_instance = GetTransactionsPaymentDetailData.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsPaymentDetailData.to_json())

# convert the object into a dict
get_transactions_payment_detail_data_dict = get_transactions_payment_detail_data_instance.to_dict()
# create an instance of GetTransactionsPaymentDetailData from a dict
get_transactions_payment_detail_data_from_dict = GetTransactionsPaymentDetailData.from_dict(get_transactions_payment_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


