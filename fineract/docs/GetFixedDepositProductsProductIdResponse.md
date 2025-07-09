# GetFixedDepositProductsProductIdResponse

GetFixedDepositProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mappings** | [**GetFixedDepositProductsProductIdAccountingMappings**](GetFixedDepositProductsProductIdAccountingMappings.md) |  | [optional] 
**active_chart** | [**GetFixedDepositProductsProductIdActiveChart**](GetFixedDepositProductsProductIdActiveChart.md) |  | [optional] 
**currency** | [**GetFixedDepositProductsProductIdCurrency**](GetFixedDepositProductsProductIdCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**fee_to_income_account_mappings** | [**List[GetFixedDepositProductsProductIdFeeToIncomeAccountMappings]**](GetFixedDepositProductsProductIdFeeToIncomeAccountMappings.md) |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetFixedDepositProductsInterestCalculationDaysInYearType**](GetFixedDepositProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetFixedDepositProductsInterestCalculationType**](GetFixedDepositProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetFixedDepositProductsProductIdInterestCompoundingPeriodType**](GetFixedDepositProductsProductIdInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetFixedDepositProductsInterestPostingPeriodType**](GetFixedDepositProductsInterestPostingPeriodType.md) |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetFixedDepositProductsProductIdMaxDepositTermType**](GetFixedDepositProductsProductIdMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetFixedDepositProductsProductIdMinDepositTermType**](GetFixedDepositProductsProductIdMinDepositTermType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**penalty_to_income_account_mappings** | [**List[GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings]**](GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings.md) |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**pre_closure_penal_interest** | **float** |  | [optional] 
**pre_closure_penal_interest_on_type** | [**GetFixedDepositProductsProductIdPreClosurePenalInterestOnType**](GetFixedDepositProductsProductIdPreClosurePenalInterestOnType.md) |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_product_id_response import GetFixedDepositProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsProductIdResponse from a JSON string
get_fixed_deposit_products_product_id_response_instance = GetFixedDepositProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositProductsProductIdResponse.to_json()

# convert the object into a dict
get_fixed_deposit_products_product_id_response_dict = get_fixed_deposit_products_product_id_response_instance.to_dict()
# create an instance of GetFixedDepositProductsProductIdResponse from a dict
get_fixed_deposit_products_product_id_response_form_dict = get_fixed_deposit_products_product_id_response.from_dict(get_fixed_deposit_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


