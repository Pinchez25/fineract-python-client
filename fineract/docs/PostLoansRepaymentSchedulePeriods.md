# PostLoansRepaymentSchedulePeriods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **date** |  | [optional] 
**fee_charges_due** | **int** |  | [optional] 
**fee_charges_outstanding** | **int** |  | [optional] 
**period** | **int** |  | [optional] 
**principal_disbursed** | **int** |  | [optional] 
**principal_loan_balance_outstanding** | **int** |  | [optional] 
**total_actual_cost_of_loan_for_period** | **int** |  | [optional] 
**total_due_for_period** | **int** |  | [optional] 
**total_original_due_for_period** | **int** |  | [optional] 
**total_outstanding_for_period** | **int** |  | [optional] 
**total_overdue** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_repayment_schedule_periods import PostLoansRepaymentSchedulePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansRepaymentSchedulePeriods from a JSON string
post_loans_repayment_schedule_periods_instance = PostLoansRepaymentSchedulePeriods.from_json(json)
# print the JSON string representation of the object
print(PostLoansRepaymentSchedulePeriods.to_json())

# convert the object into a dict
post_loans_repayment_schedule_periods_dict = post_loans_repayment_schedule_periods_instance.to_dict()
# create an instance of PostLoansRepaymentSchedulePeriods from a dict
post_loans_repayment_schedule_periods_from_dict = PostLoansRepaymentSchedulePeriods.from_dict(post_loans_repayment_schedule_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


