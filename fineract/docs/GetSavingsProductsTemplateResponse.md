# GetSavingsProductsTemplateResponse

GetSavingsProductsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_mapping** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 
**accounting_mapping_options** | [**GetSavingsProductsAccountingMappingOptions**](GetSavingsProductsAccountingMappingOptions.md) |  | [optional] 
**accounting_rule** | [**GetSavingsProductsTemplateAccountingRule**](GetSavingsProductsTemplateAccountingRule.md) |  | [optional] 
**accounting_rule_options** | [**List[GetSavingsProductsTemplateAccountingRule]**](GetSavingsProductsTemplateAccountingRule.md) |  | [optional] 
**charge_options** | [**List[GetSavingsProductsChargeOptions]**](GetSavingsProductsChargeOptions.md) |  | [optional] 
**currency** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 
**currency_options** | [**List[GetSavingsCurrency]**](GetSavingsCurrency.md) |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetSavingsProductsInterestCalculationDaysInYearType**](GetSavingsProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_days_in_year_type_options** | [**List[GetSavingsProductsInterestCalculationDaysInYearType]**](GetSavingsProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetSavingsProductsInterestCalculationType**](GetSavingsProductsInterestCalculationType.md) |  | [optional] 
**interest_calculation_type_options** | [**List[GetSavingsProductsInterestCalculationType]**](GetSavingsProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetSavingsProductsInterestCompoundingPeriodType**](GetSavingsProductsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_compounding_period_type_options** | [**List[GetSavingsProductsInterestCompoundingPeriodType]**](GetSavingsProductsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetSavingsProductsInterestPostingPeriodType**](GetSavingsProductsInterestPostingPeriodType.md) |  | [optional] 
**interest_posting_period_type_options** | [**List[GetSavingsProductsInterestPostingPeriodType]**](GetSavingsProductsInterestPostingPeriodType.md) |  | [optional] 
**lockin_period_frequency_type_options** | [**List[GetSavingsProductsLockinPeriodFrequencyTypeOptions]**](GetSavingsProductsLockinPeriodFrequencyTypeOptions.md) |  | [optional] 
**payment_type_options** | [**List[GetSavingsProductsPaymentTypeOptions]**](GetSavingsProductsPaymentTypeOptions.md) |  | [optional] 
**withdrawal_fee_type_options** | [**List[GetSavingsProductsWithdrawalFeeTypeOptions]**](GetSavingsProductsWithdrawalFeeTypeOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_template_response import GetSavingsProductsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsTemplateResponse from a JSON string
get_savings_products_template_response_instance = GetSavingsProductsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsTemplateResponse.to_json()

# convert the object into a dict
get_savings_products_template_response_dict = get_savings_products_template_response_instance.to_dict()
# create an instance of GetSavingsProductsTemplateResponse from a dict
get_savings_products_template_response_form_dict = get_savings_products_template_response.from_dict(get_savings_products_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


