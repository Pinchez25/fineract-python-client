# PostCollectionSheetBulkRepaymentTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_id** | **int** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **int** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.post_collection_sheet_bulk_repayment_transactions import PostCollectionSheetBulkRepaymentTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of PostCollectionSheetBulkRepaymentTransactions from a JSON string
post_collection_sheet_bulk_repayment_transactions_instance = PostCollectionSheetBulkRepaymentTransactions.from_json(json)
# print the JSON string representation of the object
print(PostCollectionSheetBulkRepaymentTransactions.to_json())

# convert the object into a dict
post_collection_sheet_bulk_repayment_transactions_dict = post_collection_sheet_bulk_repayment_transactions_instance.to_dict()
# create an instance of PostCollectionSheetBulkRepaymentTransactions from a dict
post_collection_sheet_bulk_repayment_transactions_from_dict = PostCollectionSheetBulkRepaymentTransactions.from_dict(post_collection_sheet_bulk_repayment_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


