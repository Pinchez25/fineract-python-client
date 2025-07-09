# GetLoanProductsProductIdResponse

GetLoanProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mappings** | [**GetLoanAccountingMappings**](GetLoanAccountingMappings.md) |  | [optional] 
**accounting_rule** | [**GetLoanProductsAccountingRule**](GetLoanProductsAccountingRule.md) |  | [optional] 
**allow_approved_disbursed_amounts_over_applied** | **bool** |  | [optional] 
**allow_partial_period_interest_calculation** | **bool** |  | [optional] 
**allow_variable_installments** | **bool** |  | [optional] 
**amortization_type** | [**GetLoanProductsAmortizationType**](GetLoanProductsAmortizationType.md) |  | [optional] 
**annual_interest_rate** | **float** |  | [optional] 
**can_define_installment_amount** | **bool** |  | [optional] 
**can_use_for_topup** | **bool** |  | [optional] 
**charges** | **List[int]** |  | [optional] 
**credit_allocation** | [**List[CreditAllocationData]**](CreditAllocationData.md) |  | [optional] 
**currency** | [**GetLoanProductsCurrency**](GetLoanProductsCurrency.md) |  | [optional] 
**delinquency_bucket** | [**GetDelinquencyBucketsResponse**](GetDelinquencyBucketsResponse.md) |  | [optional] 
**delinquency_bucket_options** | [**List[GetDelinquencyBucketsResponse]**](GetDelinquencyBucketsResponse.md) |  | [optional] 
**description** | **str** |  | [optional] 
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
**id** | **int** |  | [optional] 
**in_arrears_tolerance** | **int** |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**interest_calculation_period_type** | [**GetLoansProductsInterestCalculationPeriodType**](GetLoansProductsInterestCalculationPeriodType.md) |  | [optional] 
**interest_rate_frequency_type** | [**GetLoanProductsInterestRateFrequencyType**](GetLoanProductsInterestRateFrequencyType.md) |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_rate_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**interest_recalculation_data** | [**GetLoanProductsInterestRecalculationData**](GetLoanProductsInterestRecalculationData.md) |  | [optional] 
**interest_type** | [**GetLoanProductsInterestTemplateType**](GetLoanProductsInterestTemplateType.md) |  | [optional] 
**is_floating_interest_rate_calculation_allowed** | **bool** |  | [optional] 
**is_interest_recalculation_enabled** | **bool** |  | [optional] 
**is_linked_to_floating_interest_rates** | **bool** |  | [optional] 
**is_rates_enabled** | **bool** |  | [optional] 
**loan_schedule_processing_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**loan_schedule_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**max_interest_rate_per_period** | **float** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal** | **float** |  | [optional] 
**max_tranche_count** | **int** |  | [optional] 
**maximum_gap** | **int** |  | [optional] 
**min_interest_rate_per_period** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal** | **float** |  | [optional] 
**minimum_gap** | **int** |  | [optional] 
**multi_disburse_loan** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_repayment_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**over_applied_calculation_type** | **str** |  | [optional] 
**over_due_days_for_repayment_event** | **int** |  | [optional] 
**overdue_days_for_npa** | **int** |  | [optional] 
**payment_allocation** | [**List[AdvancedPaymentData]**](AdvancedPaymentData.md) |  | [optional] 
**payment_channel_to_fund_source_mappings** | [**List[GetLoanPaymentChannelToFundSourceMappings]**](GetLoanPaymentChannelToFundSourceMappings.md) |  | [optional] 
**principal** | **float** |  | [optional] 
**principal_threshold_for_last_instalment** | **int** |  | [optional] 
**products_principal_variations_for_borrower_cycle** | [**List[GetLoanProductsPrincipalVariationsForBorrowerCycle]**](GetLoanProductsPrincipalVariationsForBorrowerCycle.md) |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | [**GetLoanProductsRepaymentFrequencyType**](GetLoanProductsRepaymentFrequencyType.md) |  | [optional] 
**repayment_start_date_type** | [**GetLoanProductsRepaymentStartDateType**](GetLoanProductsRepaymentStartDateType.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**supported_interest_refund_types** | [**List[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 
**transaction_processing_strategy_name** | **str** |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_product_id_response import GetLoanProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsProductIdResponse from a JSON string
get_loan_products_product_id_response_instance = GetLoanProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsProductIdResponse.to_json()

# convert the object into a dict
get_loan_products_product_id_response_dict = get_loan_products_product_id_response_instance.to_dict()
# create an instance of GetLoanProductsProductIdResponse from a dict
get_loan_products_product_id_response_form_dict = get_loan_products_product_id_response.from_dict(get_loan_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


