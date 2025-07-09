# GetLoansLoanIdRepaymentSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**loan_term_in_days** | **int** |  | [optional] 
**periods** | [**List[GetLoansLoanIdRepaymentPeriod]**](GetLoansLoanIdRepaymentPeriod.md) |  | [optional] 
**total_fee_charges_charged** | **float** |  | [optional] 
**total_interest_charged** | **float** |  | [optional] 
**total_outstanding** | **float** |  | [optional] 
**total_paid_in_advance** | **float** |  | [optional] 
**total_paid_late** | **float** |  | [optional] 
**total_penalty_charges_charged** | **float** |  | [optional] 
**total_principal_disbursed** | **float** |  | [optional] 
**total_principal_expected** | **float** |  | [optional] 
**total_principal_paid** | **float** |  | [optional] 
**total_repayment_expected** | **float** |  | [optional] 
**total_waived** | **float** |  | [optional] 
**total_written_off** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_repayment_schedule import GetLoansLoanIdRepaymentSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdRepaymentSchedule from a JSON string
get_loans_loan_id_repayment_schedule_instance = GetLoansLoanIdRepaymentSchedule.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdRepaymentSchedule.to_json()

# convert the object into a dict
get_loans_loan_id_repayment_schedule_dict = get_loans_loan_id_repayment_schedule_instance.to_dict()
# create an instance of GetLoansLoanIdRepaymentSchedule from a dict
get_loans_loan_id_repayment_schedule_form_dict = get_loans_loan_id_repayment_schedule.from_dict(get_loans_loan_id_repayment_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


