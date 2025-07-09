# GetLoanProductsInterestRecalculationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_compounding_on_eod** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_recalculation_compounding_frequency_type** | [**GetLoanProductsInterestRecalculationCompoundingFrequencyType**](GetLoanProductsInterestRecalculationCompoundingFrequencyType.md) |  | [optional] 
**interest_recalculation_compounding_type** | [**GetLoanProductsInterestRecalculationCompoundingType**](GetLoanProductsInterestRecalculationCompoundingType.md) |  | [optional] 
**is_arrears_based_on_original_schedule** | **bool** |  | [optional] 
**is_compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**pre_closure_interest_calculation_strategy** | [**GetLoanProductsPreClosureInterestCalculationStrategy**](GetLoanProductsPreClosureInterestCalculationStrategy.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**recalculation_compounding_frequency_interval** | **int** |  | [optional] 
**recalculation_compounding_frequency_on_day_type** | **int** |  | [optional] 
**recalculation_rest_frequency_interval** | **int** |  | [optional] 
**recalculation_rest_frequency_type** | [**GetLoanProductsInterestRecalculationCompoundingFrequencyType**](GetLoanProductsInterestRecalculationCompoundingFrequencyType.md) |  | [optional] 
**reschedule_strategy_type** | [**GetLoanProductsRescheduleStrategyType**](GetLoanProductsRescheduleStrategyType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_interest_recalculation_data import GetLoanProductsInterestRecalculationData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsInterestRecalculationData from a JSON string
get_loan_products_interest_recalculation_data_instance = GetLoanProductsInterestRecalculationData.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsInterestRecalculationData.to_json()

# convert the object into a dict
get_loan_products_interest_recalculation_data_dict = get_loan_products_interest_recalculation_data_instance.to_dict()
# create an instance of GetLoanProductsInterestRecalculationData from a dict
get_loan_products_interest_recalculation_data_form_dict = get_loan_products_interest_recalculation_data.from_dict(get_loan_products_interest_recalculation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


