# GetFixedDepositProductsResponse

GetFixedDepositProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | [**GetFixedDepositProductsAccountingRule**](GetFixedDepositProductsAccountingRule.md) |  | [optional] 
**currency** | [**GetFixedDepositProductsCurrency**](GetFixedDepositProductsCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetFixedDepositProductsInterestCalculationDaysInYearType**](GetFixedDepositProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetFixedDepositProductsInterestCalculationType**](GetFixedDepositProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetFixedDepositProductsInterestCompoundingPeriodType**](GetFixedDepositProductsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetFixedDepositProductsInterestPostingPeriodType**](GetFixedDepositProductsInterestPostingPeriodType.md) |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetFixedDepositProductsMaxDepositTermType**](GetFixedDepositProductsMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetFixedDepositProductsMinDepositTermType**](GetFixedDepositProductsMinDepositTermType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_response import GetFixedDepositProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsResponse from a JSON string
get_fixed_deposit_products_response_instance = GetFixedDepositProductsResponse.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositProductsResponse.to_json()

# convert the object into a dict
get_fixed_deposit_products_response_dict = get_fixed_deposit_products_response_instance.to_dict()
# create an instance of GetFixedDepositProductsResponse from a dict
get_fixed_deposit_products_response_form_dict = get_fixed_deposit_products_response.from_dict(get_fixed_deposit_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


