# PutLoansLoanIdRequest

PutLoansLoanIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_type** | **int** |  | [optional] 
**charges** | [**List[PutLoansLoanIdChanges]**](PutLoansLoanIdChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**collateral** | [**List[PutLoansLoanIdCollateral]**](PutLoansLoanIdCollateral.md) |  | [optional] 
**create_standing_instruction_at_disbursement** | **bool** |  | [optional] 
**date_format** | **str** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**disbursement_data** | [**List[PutLoansLoanIdDisbursementData]**](PutLoansLoanIdDisbursementData.md) |  | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**fraud** | **bool** |  | [optional] 
**grace_on_arrears_ageing** | **int** |  | [optional] 
**interest_calculation_period_type** | **int** |  | [optional] 
**interest_charged_from_date** | **str** |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**is_equal_amortization** | **bool** |  | [optional] 
**is_topup** | **bool** |  | [optional] 
**link_account_id** | **int** |  | [optional] 
**loan_id_to_close** | **int** |  | [optional] 
**loan_schedule_processing_type** | **str** |  | [optional] 
**loan_term_frequency** | **int** |  | [optional] 
**loan_term_frequency_type** | **int** |  | [optional] 
**loan_type** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_outstanding_loan_balance** | **int** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_day_of_week_type** | **int** |  | [optional] 
**repayment_frequency_nth_day_type** | **int** |  | [optional] 
**repayment_frequency_type** | **int** |  | [optional] 
**repayments_starting_from_date** | **str** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_request import PutLoansLoanIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdRequest from a JSON string
put_loans_loan_id_request_instance = PutLoansLoanIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutLoansLoanIdRequest.to_json())

# convert the object into a dict
put_loans_loan_id_request_dict = put_loans_loan_id_request_instance.to_dict()
# create an instance of PutLoansLoanIdRequest from a dict
put_loans_loan_id_request_from_dict = PutLoansLoanIdRequest.from_dict(put_loans_loan_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


