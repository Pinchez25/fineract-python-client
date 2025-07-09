# GetRecurringDepositProductsResponse

GetRecurringDepositProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | [**GetRecurringDepositProductsAccountingRule**](GetRecurringDepositProductsAccountingRule.md) |  | [optional] 
**currency** | [**GetRecurringDepositProductsCurrency**](GetRecurringDepositProductsCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetRecurringDepositProductsInterestCalculationDaysInYearType**](GetRecurringDepositProductsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetRecurringDepositProductsInterestCalculationType**](GetRecurringDepositProductsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetRecurringDepositProductsInterestCompoundingPeriodType**](GetRecurringDepositProductsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetRecurringDepositProductsInterestPostingPeriodType**](GetRecurringDepositProductsInterestPostingPeriodType.md) |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetRecurringDepositProductsMaxDepositTermType**](GetRecurringDepositProductsMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetRecurringDepositProductsMinDepositTermType**](GetRecurringDepositProductsMinDepositTermType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**recurring_deposit_frequency** | **int** |  | [optional] 
**recurring_deposit_frequency_type** | [**GetRecurringDepositProductsRecurringDepositFrequencyType**](GetRecurringDepositProductsRecurringDepositFrequencyType.md) |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_response import GetRecurringDepositProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsResponse from a JSON string
get_recurring_deposit_products_response_instance = GetRecurringDepositProductsResponse.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositProductsResponse.to_json()

# convert the object into a dict
get_recurring_deposit_products_response_dict = get_recurring_deposit_products_response_instance.to_dict()
# create an instance of GetRecurringDepositProductsResponse from a dict
get_recurring_deposit_products_response_form_dict = get_recurring_deposit_products_response.from_dict(get_recurring_deposit_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


