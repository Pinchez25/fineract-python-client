# PostLoansLoanIdTransactionsRequest

PostLoansLoanIdTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**charge_off_reason_id** | **int** |  | [optional] 
**check_number** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**frequency_number** | **int** |  | [optional] 
**frequency_type** | **str** |  | [optional] 
**loan_charge_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**number_of_installments** | **int** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**reversal_external_id** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **str** |  | [optional] 
**writeoff_reason_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_transactions_request import PostLoansLoanIdTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdTransactionsRequest from a JSON string
post_loans_loan_id_transactions_request_instance = PostLoansLoanIdTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdTransactionsRequest.to_json()

# convert the object into a dict
post_loans_loan_id_transactions_request_dict = post_loans_loan_id_transactions_request_instance.to_dict()
# create an instance of PostLoansLoanIdTransactionsRequest from a dict
post_loans_loan_id_transactions_request_form_dict = post_loans_loan_id_transactions_request.from_dict(post_loans_loan_id_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


