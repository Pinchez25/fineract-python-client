# TransactionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_data** | [**GetResourceTypeResourceIdNotesResponse**](GetResourceTypeResourceIdNotesResponse.md) |  | [optional] 
**payment_details** | [**PaymentDetailData**](PaymentDetailData.md) |  | [optional] 
**transaction_id** | **int** |  | [optional] 
**transaction_type** | [**EnumOptionType**](EnumOptionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.transaction_details import TransactionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetails from a JSON string
transaction_details_instance = TransactionDetails.from_json(json)
# print the JSON string representation of the object
print TransactionDetails.to_json()

# convert the object into a dict
transaction_details_dict = transaction_details_instance.to_dict()
# create an instance of TransactionDetails from a dict
transaction_details_form_dict = transaction_details.from_dict(transaction_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


