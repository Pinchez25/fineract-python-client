# GetRecurringDepositProductsProductIdResponse

GetRecurringDepositProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mappings** | [**GetRecurringDepositProductsProductIdAccountingMappings**](GetRecurringDepositProductsProductIdAccountingMappings.md) |  | [optional] 
**active_chart** | [**GetRecurringDepositProductsProductIdActiveChart**](GetRecurringDepositProductsProductIdActiveChart.md) |  | [optional] 
**currency** | [**GetRecurringDepositProductsProductIdCurrency**](GetRecurringDepositProductsProductIdCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**fee_to_income_account_mappings** | [**List[GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings]**](GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings.md) |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetRecurringDepositProductsInterestCalculationDaysInYearType**](GetRecurringDepositProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetRecurringDepositProductsInterestCalculationType**](GetRecurringDepositProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetRecurringDepositProductsProductIdInterestCompoundingPeriodType**](GetRecurringDepositProductsProductIdInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetRecurringDepositProductsInterestPostingPeriodType**](GetRecurringDepositProductsInterestPostingPeriodType.md) |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetRecurringDepositProductsProductIdMaxDepositTermType**](GetRecurringDepositProductsProductIdMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetRecurringDepositProductsProductIdMinDepositTermType**](GetRecurringDepositProductsProductIdMinDepositTermType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**penalty_to_income_account_mappings** | [**List[GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings]**](GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings.md) |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**pre_closure_penal_interest** | **float** |  | [optional] 
**pre_closure_penal_interest_on_type** | [**GetRecurringDepositProductsProductIdPreClosurePenalInterestOnType**](GetRecurringDepositProductsProductIdPreClosurePenalInterestOnType.md) |  | [optional] 
**recurring_deposit_frequency** | **int** |  | [optional] 
**recurring_deposit_frequency_type** | [**GetRecurringDepositProductsRecurringDepositFrequencyType**](GetRecurringDepositProductsRecurringDepositFrequencyType.md) |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_response import GetRecurringDepositProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdResponse from a JSON string
get_recurring_deposit_products_product_id_response_instance = GetRecurringDepositProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsProductIdResponse.to_json())

# convert the object into a dict
get_recurring_deposit_products_product_id_response_dict = get_recurring_deposit_products_product_id_response_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdResponse from a dict
get_recurring_deposit_products_product_id_response_from_dict = GetRecurringDepositProductsProductIdResponse.from_dict(get_recurring_deposit_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


