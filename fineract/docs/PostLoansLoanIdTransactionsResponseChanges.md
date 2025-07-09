# PostLoansLoanIdTransactionsResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**reversal_external_id** | **str** |  | [optional] 
**transaction_amount** | **str** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_transactions_response_changes import PostLoansLoanIdTransactionsResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdTransactionsResponseChanges from a JSON string
post_loans_loan_id_transactions_response_changes_instance = PostLoansLoanIdTransactionsResponseChanges.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdTransactionsResponseChanges.to_json()

# convert the object into a dict
post_loans_loan_id_transactions_response_changes_dict = post_loans_loan_id_transactions_response_changes_instance.to_dict()
# create an instance of PostLoansLoanIdTransactionsResponseChanges from a dict
post_loans_loan_id_transactions_response_changes_form_dict = post_loans_loan_id_transactions_response_changes.from_dict(post_loans_loan_id_transactions_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


