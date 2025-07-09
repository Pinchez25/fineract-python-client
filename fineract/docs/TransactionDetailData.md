# TransactionDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_data** | [**NoteData**](NoteData.md) |  | [optional] 
**payment_details** | [**PaymentDetailData**](PaymentDetailData.md) |  | [optional] 
**transaction_id** | **int** |  | [optional] 
**transaction_type** | [**TransactionTypeEnumData**](TransactionTypeEnumData.md) |  | [optional] 

## Example

```python
from fineract_client.models.transaction_detail_data import TransactionDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetailData from a JSON string
transaction_detail_data_instance = TransactionDetailData.from_json(json)
# print the JSON string representation of the object
print TransactionDetailData.to_json()

# convert the object into a dict
transaction_detail_data_dict = transaction_detail_data_instance.to_dict()
# create an instance of TransactionDetailData from a dict
transaction_detail_data_form_dict = transaction_detail_data.from_dict(transaction_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


