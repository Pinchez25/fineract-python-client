# GetSelfLoanIdSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_disburse** | **bool** |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**disbursement_details** | [**List[GetLoansLoanIdDisbursementDetails]**](GetLoansLoanIdDisbursementDetails.md) |  | [optional] 
**emi_amount_variations** | **List[object]** |  | [optional] 
**fee_charges_charged** | **float** |  | [optional] 
**fee_charges_due_at_disbursement_charged** | **float** |  | [optional] 
**fee_charges_outstanding** | **float** |  | [optional] 
**fee_charges_overdue** | **float** |  | [optional] 
**fee_charges_paid** | **float** |  | [optional] 
**fee_charges_waived** | **float** |  | [optional] 
**fee_charges_written_off** | **float** |  | [optional] 
**fixed_emi_amount** | **float** |  | [optional] 
**in_arrears** | **bool** |  | [optional] 
**interest_charged** | **float** |  | [optional] 
**interest_outstanding** | **float** |  | [optional] 
**interest_overdue** | **float** |  | [optional] 
**interest_paid** | **float** |  | [optional] 
**interest_waived** | **float** |  | [optional] 
**interest_written_off** | **float** |  | [optional] 
**is_npa** | **bool** |  | [optional] 
**linked_account** | [**GetLoansLoanIdLinkedAccount**](GetLoansLoanIdLinkedAccount.md) |  | [optional] 
**max_outstanding_loan_balance** | **float** |  | [optional] 
**overdue_charges** | [**List[GetLoansLoanIdOverdueCharges]**](GetLoansLoanIdOverdueCharges.md) |  | [optional] 
**overdue_since_date** | **date** |  | [optional] 
**penalty_charges_charged** | **float** |  | [optional] 
**penalty_charges_outstanding** | **float** |  | [optional] 
**penalty_charges_overdue** | **float** |  | [optional] 
**penalty_charges_paid** | **float** |  | [optional] 
**penalty_charges_waived** | **float** |  | [optional] 
**penalty_charges_written_off** | **float** |  | [optional] 
**principal_adjustments** | **float** |  | [optional] 
**principal_disbursed** | **float** |  | [optional] 
**principal_outstanding** | **float** |  | [optional] 
**principal_overdue** | **float** |  | [optional] 
**principal_paid** | **float** |  | [optional] 
**principal_written_off** | **float** |  | [optional] 
**total_charge_adjustment** | **float** |  | [optional] 
**total_charge_adjustment_reversed** | **float** |  | [optional] 
**total_chargeback** | **float** |  | [optional] 
**total_cost_of_loan** | **float** |  | [optional] 
**total_credit_balance_refund** | **float** |  | [optional] 
**total_credit_balance_refund_reversed** | **float** |  | [optional] 
**total_expected_cost_of_loan** | **float** |  | [optional] 
**total_expected_repayment** | **float** |  | [optional] 
**total_goodwill_credit** | **float** |  | [optional] 
**total_goodwill_credit_reversed** | **float** |  | [optional] 
**total_merchant_refund** | **float** |  | [optional] 
**total_merchant_refund_reversed** | **float** |  | [optional] 
**total_outstanding** | **float** |  | [optional] 
**total_overdue** | **float** |  | [optional] 
**total_payout_refund** | **float** |  | [optional] 
**total_payout_refund_reversed** | **float** |  | [optional] 
**total_repayment** | **float** |  | [optional] 
**total_repayment_transaction** | **float** |  | [optional] 
**total_repayment_transaction_reversed** | **float** |  | [optional] 
**total_waived** | **float** |  | [optional] 
**total_written_off** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loan_id_summary import GetSelfLoanIdSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoanIdSummary from a JSON string
get_self_loan_id_summary_instance = GetSelfLoanIdSummary.from_json(json)
# print the JSON string representation of the object
print(GetSelfLoanIdSummary.to_json())

# convert the object into a dict
get_self_loan_id_summary_dict = get_self_loan_id_summary_instance.to_dict()
# create an instance of GetSelfLoanIdSummary from a dict
get_self_loan_id_summary_from_dict = GetSelfLoanIdSummary.from_dict(get_self_loan_id_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


