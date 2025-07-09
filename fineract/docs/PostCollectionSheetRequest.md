# PostCollectionSheetRequest

PostCollectionSheetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_disbursement_date** | **str** |  | [optional] 
**bulk_disbursement_transactions** | **List[int]** |  | [optional] 
**bulk_repayment_transactions** | [**PostCollectionSheetBulkRepaymentTransactions**](PostCollectionSheetBulkRepaymentTransactions.md) |  | [optional] 
**bulk_savings_due_transactions** | **List[int]** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_collection_sheet_request import PostCollectionSheetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCollectionSheetRequest from a JSON string
post_collection_sheet_request_instance = PostCollectionSheetRequest.from_json(json)
# print the JSON string representation of the object
print PostCollectionSheetRequest.to_json()

# convert the object into a dict
post_collection_sheet_request_dict = post_collection_sheet_request_instance.to_dict()
# create an instance of PostCollectionSheetRequest from a dict
post_collection_sheet_request_form_dict = post_collection_sheet_request.from_dict(post_collection_sheet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


