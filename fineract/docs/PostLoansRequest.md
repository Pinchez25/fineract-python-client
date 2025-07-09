# PostLoansRequest

PostLoansRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_type** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**days_in_year_type** | **int** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**disbursement_data** | [**List[PostLoansDisbursementData]**](PostLoansDisbursementData.md) | List of PostLoansDisbursementData | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**grace_on_arrears_ageing** | **int** |  | [optional] 
**grace_on_interest_charged** | **int** |  | [optional] 
**grace_on_interest_payment** | **int** |  | [optional] 
**grace_on_principal_payment** | **int** |  | [optional] 
**interest_calculation_period_type** | **int** |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**loan_schedule_processing_type** | **str** |  | [optional] 
**loan_term_frequency** | **int** |  | [optional] 
**loan_term_frequency_type** | **int** |  | [optional] 
**loan_type** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_outstanding_loan_balance** | **float** | Maximum allowed outstanding balance | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **float** |  | [optional] 
**product_id** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | **int** |  | [optional] 
**repayments_starting_from_date** | **date** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_request import PostLoansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansRequest from a JSON string
post_loans_request_instance = PostLoansRequest.from_json(json)
# print the JSON string representation of the object
print(PostLoansRequest.to_json())

# convert the object into a dict
post_loans_request_dict = post_loans_request_instance.to_dict()
# create an instance of PostLoansRequest from a dict
post_loans_request_from_dict = PostLoansRequest.from_dict(post_loans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


