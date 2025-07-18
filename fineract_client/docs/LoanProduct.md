# LoanProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_moves_out_of_npa_only_on_arrears_completion** | **bool** |  | [optional] 
**accounting_disabled** | **bool** |  | [optional] 
**accounting_rule** | **int** |  | [optional] 
**allow_approved_disbursed_amounts_over_applied** | **bool** |  | [optional] 
**allow_variabe_installments** | **bool** |  | [optional] 
**arrears_based_on_original_schedule** | **bool** |  | [optional] 
**borrower_cycle_variations** | [**List[LoanProductBorrowerCycleVariations]**](LoanProductBorrowerCycleVariations.md) |  | [optional] 
**can_define_installment_amount** | **bool** |  | [optional] 
**can_use_for_topup** | **bool** |  | [optional] 
**cash_based_accounting_enabled** | **bool** |  | [optional] 
**charges** | [**List[Charge]**](Charge.md) |  | [optional] 
**close_date** | **date** |  | [optional] 
**credit_allocation_rules** | [**List[LoanProductCreditAllocationRule]**](LoanProductCreditAllocationRule.md) |  | [optional] 
**currency** | [**MonetaryCurrency**](MonetaryCurrency.md) |  | [optional] 
**delinquency_bucket** | [**DelinquencyBucket**](DelinquencyBucket.md) |  | [optional] 
**description** | **str** |  | [optional] 
**disallow_expected_disbursements** | **bool** |  | [optional] 
**due_days_for_repayment_event** | **int** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**equal_amortization** | **bool** |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**floating_rates** | [**LoanProductFloatingRates**](LoanProductFloatingRates.md) |  | [optional] 
**fund** | [**Fund**](Fund.md) |  | [optional] 
**hold_guarantee_funds** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**installment_amount_in_multiples_of** | **int** |  | [optional] 
**interest_period_frequency_type** | **str** |  | [optional] 
**interest_recalculation_enabled** | **bool** |  | [optional] 
**linked_to_floating_interest_rate** | **bool** |  | [optional] 
**loan_configurable_attributes** | [**LoanProductConfigurableAttributes**](LoanProductConfigurableAttributes.md) |  | [optional] 
**loan_product_guarantee_details** | [**LoanProductGuaranteeDetails**](LoanProductGuaranteeDetails.md) |  | [optional] 
**loan_product_min_max_constraints** | [**LoanProductMinMaxConstraints**](LoanProductMinMaxConstraints.md) |  | [optional] 
**loan_product_related_detail** | [**LoanProductRelatedDetail**](LoanProductRelatedDetail.md) |  | [optional] 
**loan_product_tranche_details** | [**LoanProductTrancheDetails**](LoanProductTrancheDetails.md) |  | [optional] 
**max_nominal_interest_rate_per_period** | **float** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal_amount** | [**Money**](Money.md) |  | [optional] 
**min_nominal_interest_rate_per_period** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal_amount** | [**Money**](Money.md) |  | [optional] 
**minimum_days_between_disbursal_and_first_repayment** | **int** |  | [optional] 
**multi_disburse_loan** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**nominal_interest_rate_per_period** | **float** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**over_applied_calculation_type** | **str** |  | [optional] 
**over_applied_number** | **int** |  | [optional] 
**over_due_days_for_repayment_event** | **int** |  | [optional] 
**overdue_days_for_npa** | **int** |  | [optional] 
**payment_allocation_rules** | [**List[LoanProductPaymentAllocationRule]**](LoanProductPaymentAllocationRule.md) |  | [optional] 
**periodic_accrual_accounting_enabled** | **bool** |  | [optional] 
**principal_amount** | [**Money**](Money.md) |  | [optional] 
**principal_threshold_for_last_installment** | **float** |  | [optional] 
**product_interest_recalculation_details** | [**LoanProductInterestRecalculationDetails**](LoanProductInterestRecalculationDetails.md) |  | [optional] 
**rates** | [**List[Rate]**](Rate.md) |  | [optional] 
**repayment_start_date_type** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**sync_expected_with_disbursement_date** | **bool** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 
**transaction_processing_strategy_name** | **str** |  | [optional] 
**upfront_accrual_accounting_enabled** | **bool** |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 
**variable_installment_config** | [**LoanProductVariableInstallmentConfig**](LoanProductVariableInstallmentConfig.md) |  | [optional] 

## Example

```python
from fineract_client.models.loan_product import LoanProduct

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProduct from a JSON string
loan_product_instance = LoanProduct.from_json(json)
# print the JSON string representation of the object
print(LoanProduct.to_json())

# convert the object into a dict
loan_product_dict = loan_product_instance.to_dict()
# create an instance of LoanProduct from a dict
loan_product_from_dict = LoanProduct.from_dict(loan_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


