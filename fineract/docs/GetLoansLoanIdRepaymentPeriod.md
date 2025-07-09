# GetLoansLoanIdRepaymentPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** |  | [optional] 
**days_in_period** | **int** |  | [optional] 
**down_payment_period** | **bool** |  | [optional] 
**due_date** | **date** |  | [optional] 
**fee_charges_due** | **float** |  | [optional] 
**fee_charges_outstanding** | **float** |  | [optional] 
**fee_charges_paid** | **float** |  | [optional] 
**fee_charges_waived** | **float** |  | [optional] 
**fee_charges_written_off** | **float** |  | [optional] 
**from_date** | **date** |  | [optional] 
**interest_due** | **float** |  | [optional] 
**interest_original_due** | **float** |  | [optional] 
**interest_outstanding** | **float** |  | [optional] 
**interest_paid** | **float** |  | [optional] 
**interest_waived** | **float** |  | [optional] 
**interest_written_off** | **float** |  | [optional] 
**obligations_met_on_date** | **date** |  | [optional] 
**penalty_charges_due** | **float** |  | [optional] 
**penalty_charges_outstanding** | **float** |  | [optional] 
**penalty_charges_paid** | **float** |  | [optional] 
**penalty_charges_waived** | **float** |  | [optional] 
**penalty_charges_written_off** | **float** |  | [optional] 
**period** | **int** |  | [optional] 
**principal_due** | **float** |  | [optional] 
**principal_loan_balance_outstanding** | **float** |  | [optional] 
**principal_original_due** | **float** |  | [optional] 
**principal_outstanding** | **float** |  | [optional] 
**principal_paid** | **float** |  | [optional] 
**principal_written_off** | **float** |  | [optional] 
**total_actual_cost_of_loan_for_period** | **float** |  | [optional] 
**total_credits** | **float** |  | [optional] 
**total_due_for_period** | **float** |  | [optional] 
**total_installment_amount_for_period** | **float** |  | [optional] 
**total_original_due_for_period** | **float** |  | [optional] 
**total_outstanding_for_period** | **float** |  | [optional] 
**total_paid_for_period** | **float** |  | [optional] 
**total_paid_in_advance_for_period** | **float** |  | [optional] 
**total_paid_late_for_period** | **float** |  | [optional] 
**total_waived_for_period** | **float** |  | [optional] 
**total_written_off_for_period** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_repayment_period import GetLoansLoanIdRepaymentPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdRepaymentPeriod from a JSON string
get_loans_loan_id_repayment_period_instance = GetLoansLoanIdRepaymentPeriod.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdRepaymentPeriod.to_json()

# convert the object into a dict
get_loans_loan_id_repayment_period_dict = get_loans_loan_id_repayment_period_instance.to_dict()
# create an instance of GetLoansLoanIdRepaymentPeriod from a dict
get_loans_loan_id_repayment_period_form_dict = get_loans_loan_id_repayment_period.from_dict(get_loans_loan_id_repayment_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


