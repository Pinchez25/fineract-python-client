# GetSavingsProductsResponse

GetSavingsProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | [**GetSavingsProductsAccountingRule**](GetSavingsProductsAccountingRule.md) |  | [optional] 
**currency** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetSavingsProductsInterestCalculationDaysInYearType**](GetSavingsProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetSavingsProductsInterestCalculationType**](GetSavingsProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetSavingsProductsInterestCompoundingPeriodType**](GetSavingsProductsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetSavingsProductsInterestPostingPeriodType**](GetSavingsProductsInterestPostingPeriodType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**short_name** | **str** |  | [optional] 
**withdrawal_fee_for_transfers** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_response import GetSavingsProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsResponse from a JSON string
get_savings_products_response_instance = GetSavingsProductsResponse.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsResponse.to_json()

# convert the object into a dict
get_savings_products_response_dict = get_savings_products_response_instance.to_dict()
# create an instance of GetSavingsProductsResponse from a dict
get_savings_products_response_form_dict = get_savings_products_response.from_dict(get_savings_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


