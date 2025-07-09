# GetLoanProductsTemplateResponse

GetLoanProductsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mapping_options** | [**GetLoanProductsAccountingMappingOptions**](GetLoanProductsAccountingMappingOptions.md) |  | [optional] 
**accounting_rule** | [**GetLoanProductsAccountingRule**](GetLoanProductsAccountingRule.md) |  | [optional] 
**accounting_rule_options** | [**List[GetLoanProductsAccountingRule]**](GetLoanProductsAccountingRule.md) |  | [optional] 
**advanced_payment_allocation_future_installment_allocation_rules** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**advanced_payment_allocation_transaction_types** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**advanced_payment_allocation_types** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**amortization_type** | [**GetLoanProductsAmortizationType**](GetLoanProductsAmortizationType.md) |  | [optional] 
**amortization_type_options** | [**List[GetLoanProductsAmortizationType]**](GetLoanProductsAmortizationType.md) |  | [optional] 
**charge_options** | [**List[GetLoanProductsChargeOptions]**](GetLoanProductsChargeOptions.md) |  | [optional] 
**credit_allocation_allocation_types** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**credit_allocation_transaction_types** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**currency** | [**GetLoanProductsTemplateCurrency**](GetLoanProductsTemplateCurrency.md) |  | [optional] 
**currency_options** | [**List[GetLoanProductsCurrencyOptions]**](GetLoanProductsCurrencyOptions.md) |  | [optional] 
**days_in_month_type** | [**GetLoansProductsDaysInMonthTemplateType**](GetLoansProductsDaysInMonthTemplateType.md) |  | [optional] 
**days_in_month_type_options** | [**List[GetLoansProductsDaysInMonthTemplateType]**](GetLoansProductsDaysInMonthTemplateType.md) |  | [optional] 
**days_in_year_type** | [**GetLoanProductsDaysInYearTemplateType**](GetLoanProductsDaysInYearTemplateType.md) |  | [optional] 
**days_in_year_type_options** | [**List[GetLoanProductsInterestTemplateType]**](GetLoanProductsInterestTemplateType.md) |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**interest_calculation_period_type** | [**GetLoansProductsInterestCalculationPeriodType**](GetLoansProductsInterestCalculationPeriodType.md) |  | [optional] 
**interest_calculation_period_type_options** | [**List[GetLoansProductsInterestCalculationPeriodType]**](GetLoansProductsInterestCalculationPeriodType.md) |  | [optional] 
**interest_rate_frequency_type** | [**GetLoanProductsInterestRateTemplateFrequencyType**](GetLoanProductsInterestRateTemplateFrequencyType.md) |  | [optional] 
**interest_rate_frequency_type_options** | [**List[GetLoanProductsInterestRateTemplateFrequencyType]**](GetLoanProductsInterestRateTemplateFrequencyType.md) |  | [optional] 
**interest_rate_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**interest_recalculation_compounding_type_options** | [**List[GetLoanProductsInterestRecalculationCompoundingType]**](GetLoanProductsInterestRecalculationCompoundingType.md) |  | [optional] 
**interest_recalculation_data** | [**GetLoanProductsInterestRecalculationTemplateData**](GetLoanProductsInterestRecalculationTemplateData.md) |  | [optional] 
**interest_recalculation_frequency_type_options** | [**List[GetLoanProductsInterestRecalculationCompoundingFrequencyType]**](GetLoanProductsInterestRecalculationCompoundingFrequencyType.md) |  | [optional] 
**interest_type** | [**GetLoanProductsInterestTemplateType**](GetLoanProductsInterestTemplateType.md) |  | [optional] 
**interest_type_options** | [**List[GetLoanProductsInterestTemplateType]**](GetLoanProductsInterestTemplateType.md) |  | [optional] 
**is_interest_recalculation_enabled** | **bool** |  | [optional] 
**loan_schedule_processing_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**loan_schedule_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**number_of_repayment_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**payment_type_options** | [**List[GetLoanProductsPaymentTypeOptions]**](GetLoanProductsPaymentTypeOptions.md) |  | [optional] 
**pre_closure_interest_calculation_strategy_options** | [**List[GetLoanProductsPreClosureInterestCalculationStrategy]**](GetLoanProductsPreClosureInterestCalculationStrategy.md) |  | [optional] 
**principal_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**repayment_frequency_type** | [**GetLoanProductsRepaymentTemplateFrequencyType**](GetLoanProductsRepaymentTemplateFrequencyType.md) |  | [optional] 
**repayment_frequency_type_options** | [**List[GetLoanProductsRepaymentTemplateFrequencyType]**](GetLoanProductsRepaymentTemplateFrequencyType.md) |  | [optional] 
**repayment_start_date_type_options** | [**List[GetLoanProductsRepaymentStartDateType]**](GetLoanProductsRepaymentStartDateType.md) |  | [optional] 
**reschedule_strategy_type_options** | [**List[GetLoanProductsRescheduleStrategyType]**](GetLoanProductsRescheduleStrategyType.md) |  | [optional] 
**supported_interest_refund_types** | [**List[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**supported_interest_refund_types_options** | [**List[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**transaction_processing_strategy_options** | [**List[GetLoanProductsTransactionProcessingStrategyOptions]**](GetLoanProductsTransactionProcessingStrategyOptions.md) |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 
**value_condition_type_options** | [**List[GetLoanProductsValueConditionTypeOptions]**](GetLoanProductsValueConditionTypeOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_template_response import GetLoanProductsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsTemplateResponse from a JSON string
get_loan_products_template_response_instance = GetLoanProductsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsTemplateResponse.to_json())

# convert the object into a dict
get_loan_products_template_response_dict = get_loan_products_template_response_instance.to_dict()
# create an instance of GetLoanProductsTemplateResponse from a dict
get_loan_products_template_response_from_dict = GetLoanProductsTemplateResponse.from_dict(get_loan_products_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


