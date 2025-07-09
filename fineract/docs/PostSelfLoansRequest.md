# PostSelfLoansRequest

PostSelfLoansRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_type** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**datatables** | [**List[PostSelfLoansDatatables]**](PostSelfLoansDatatables.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**disbursement_data** | [**List[PostSelfLoansDisbursementData]**](PostSelfLoansDisbursementData.md) |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**fixed_emi_amount** | **int** |  | [optional] 
**interest_calculation_period_type** | **int** |  | [optional] 
**interest_rate_per_period** | **int** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**link_account_id** | **int** |  | [optional] 
**loan_term_frequency** | **int** |  | [optional] 
**loan_term_frequency_type** | **int** |  | [optional] 
**loan_type** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_outstanding_loan_balance** | **int** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **float** |  | [optional] 
**product_id** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | **int** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_request import PostSelfLoansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansRequest from a JSON string
post_self_loans_request_instance = PostSelfLoansRequest.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansRequest.to_json()

# convert the object into a dict
post_self_loans_request_dict = post_self_loans_request_instance.to_dict()
# create an instance of PostSelfLoansRequest from a dict
post_self_loans_request_form_dict = post_self_loans_request.from_dict(post_self_loans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


