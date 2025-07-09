# GetLoansLoanIdDelinquencySummary

Delinquent data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_disbursement_amount** | **float** |  | [optional] 
**delinquency_pause_periods** | [**List[GetLoansLoanIdDelinquencyPausePeriod]**](GetLoansLoanIdDelinquencyPausePeriod.md) | List of GetLoansLoanIdDelinquencyPausePeriod | [optional] 
**delinquent_amount** | **float** |  | [optional] 
**delinquent_date** | **date** |  | [optional] 
**delinquent_days** | **int** |  | [optional] 
**delinquent_fee** | **float** |  | [optional] 
**delinquent_interest** | **float** |  | [optional] 
**delinquent_penalty** | **float** |  | [optional] 
**delinquent_principal** | **float** |  | [optional] 
**installment_level_delinquency** | [**List[GetLoansLoanIdLoanInstallmentLevelDelinquency]**](GetLoansLoanIdLoanInstallmentLevelDelinquency.md) | List of GetLoansLoanIdLoanInstallmentLevelDelinquency | [optional] 
**last_payment_amount** | **float** |  | [optional] 
**last_payment_date** | **date** |  | [optional] 
**last_repayment_amount** | **float** |  | [optional] 
**last_repayment_date** | **date** |  | [optional] 
**next_payment_due_date** | **date** |  | [optional] 
**past_due_days** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_delinquency_summary import GetLoansLoanIdDelinquencySummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdDelinquencySummary from a JSON string
get_loans_loan_id_delinquency_summary_instance = GetLoansLoanIdDelinquencySummary.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdDelinquencySummary.to_json())

# convert the object into a dict
get_loans_loan_id_delinquency_summary_dict = get_loans_loan_id_delinquency_summary_instance.to_dict()
# create an instance of GetLoansLoanIdDelinquencySummary from a dict
get_loans_loan_id_delinquency_summary_from_dict = GetLoansLoanIdDelinquencySummary.from_dict(get_loans_loan_id_delinquency_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


