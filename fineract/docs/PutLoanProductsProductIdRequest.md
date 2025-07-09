# PutLoanProductsProductIdRequest

PutLoanProductsProductIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_moves_out_of_npa_only_on_arrears_completion** | **bool** |  | [optional] 
**accounting_rule** | **int** |  | [optional] 
**allow_approved_disbursed_amounts_over_applied** | **bool** |  | [optional] 
**allow_attribute_overrides** | [**AllowAttributeOverrides**](AllowAttributeOverrides.md) |  | [optional] 
**allow_compounding_on_eod** | **bool** |  | [optional] 
**allow_partial_period_interest_calcualtion** | **bool** |  | [optional] 
**allow_variable_installments** | **bool** |  | [optional] 
**amortization_type** | **int** |  | [optional] 
**can_define_installment_amount** | **bool** |  | [optional] 
**can_use_for_topup** | **bool** |  | [optional] 
**charge_off_expense_account_id** | **int** |  | [optional] 
**charge_off_fraud_expense_account_id** | **int** |  | [optional] 
**charges** | [**List[ChargeData]**](ChargeData.md) |  | [optional] 
**close_date** | **str** |  | [optional] 
**credit_allocation** | [**List[CreditAllocationData]**](CreditAllocationData.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**days_in_month_type** | **int** |  | [optional] 
**days_in_year_type** | **int** |  | [optional] 
**delinquency_bucket_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 
**disallow_expected_disbursements** | **bool** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**due_days_for_repayment_event** | **int** |  | [optional] 
**enable_accrual_activity_posting** | **bool** |  | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**fee_to_income_account_mappings** | [**List[GetLoanFeeToIncomeAccountMappings]**](GetLoanFeeToIncomeAccountMappings.md) |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**fund_id** | **int** |  | [optional] 
**fund_source_account_id** | **int** |  | [optional] 
**goodwill_credit_account_id** | **int** |  | [optional] 
**grace_on_arrears_ageing** | **int** |  | [optional] 
**grace_on_interest_payment** | **int** |  | [optional] 
**grace_on_principal_payment** | **int** |  | [optional] 
**hold_guarantee_funds** | **bool** |  | [optional] 
**in_arrears_tolerance** | **int** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**income_from_charge_off_fees_account_id** | **int** |  | [optional] 
**income_from_charge_off_interest_account_id** | **int** |  | [optional] 
**income_from_charge_off_penalty_account_id** | **int** |  | [optional] 
**income_from_fee_account_id** | **int** |  | [optional] 
**income_from_goodwill_credit_fees_account_id** | **int** |  | [optional] 
**income_from_goodwill_credit_interest_account_id** | **int** |  | [optional] 
**income_from_goodwill_credit_penalty_account_id** | **int** |  | [optional] 
**income_from_penalty_account_id** | **int** |  | [optional] 
**income_from_recovery_account_id** | **int** |  | [optional] 
**installment_amount_in_multiples_of** | **int** |  | [optional] 
**interest_calculation_period_type** | **int** |  | [optional] 
**interest_on_loan_account_id** | **int** |  | [optional] 
**interest_rate_frequency_type** | **int** |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_rate_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**interest_recalculation_compounding_method** | **int** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**is_arrears_based_on_original_schedule** | **bool** |  | [optional] 
**is_compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**is_equal_amortization** | **bool** |  | [optional] 
**is_interest_recalculation_enabled** | **bool** |  | [optional] 
**is_linked_to_floating_interest_rates** | **bool** |  | [optional] 
**loan_portfolio_account_id** | **int** |  | [optional] 
**loan_schedule_processing_type** | **str** |  | [optional] 
**loan_schedule_type** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_interest_rate_per_period** | **float** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal** | **float** |  | [optional] 
**max_tranche_count** | **int** |  | [optional] 
**min_interest_rate_per_period** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal** | **float** |  | [optional] 
**minimum_days_between_disbursal_and_first_repayment** | **int** |  | [optional] 
**multi_disburse_loan** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_repayment_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**over_applied_calculation_type** | **str** |  | [optional] 
**over_applied_number** | **int** |  | [optional] 
**over_due_days_for_repayment_event** | **int** |  | [optional] 
**overdue_days_for_npa** | **int** |  | [optional] 
**overpayment_liability_account_id** | **int** |  | [optional] 
**payment_allocation** | [**List[AdvancedPaymentData]**](AdvancedPaymentData.md) |  | [optional] 
**payment_channel_to_fund_source_mappings** | [**List[GetLoanPaymentChannelToFundSourceMappings]**](GetLoanPaymentChannelToFundSourceMappings.md) |  | [optional] 
**penalty_to_income_account_mappings** | [**List[ChargeToGLAccountMapper]**](ChargeToGLAccountMapper.md) |  | [optional] 
**pre_closure_interest_calculation_strategy** | **int** |  | [optional] 
**principal** | **float** |  | [optional] 
**principal_threshold_for_last_installment** | **int** |  | [optional] 
**principal_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**rates** | [**List[RateData]**](RateData.md) |  | [optional] 
**recalculation_compounding_frequency_interval** | **int** |  | [optional] 
**recalculation_compounding_frequency_on_day_type** | **int** |  | [optional] 
**recalculation_compounding_frequency_type** | **int** |  | [optional] 
**recalculation_rest_frequency_interval** | **int** |  | [optional] 
**recalculation_rest_frequency_type** | **int** |  | [optional] 
**receivable_fee_account_id** | **int** |  | [optional] 
**receivable_interest_account_id** | **int** |  | [optional] 
**receivable_penalty_account_id** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | **int** |  | [optional] 
**repayment_start_date_type** | **int** |  | [optional] 
**reschedule_strategy_method** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**supported_interest_refund_types** | **List[str]** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 
**transfers_in_suspense_account_id** | **int** |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 
**write_off_account_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_loan_products_product_id_request import PutLoanProductsProductIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoanProductsProductIdRequest from a JSON string
put_loan_products_product_id_request_instance = PutLoanProductsProductIdRequest.from_json(json)
# print the JSON string representation of the object
print PutLoanProductsProductIdRequest.to_json()

# convert the object into a dict
put_loan_products_product_id_request_dict = put_loan_products_product_id_request_instance.to_dict()
# create an instance of PutLoanProductsProductIdRequest from a dict
put_loan_products_product_id_request_form_dict = put_loan_products_product_id_request.from_dict(put_loan_products_product_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


