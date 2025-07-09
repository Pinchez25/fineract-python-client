# LoanProductInterestRecalculationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_compounding_on_eod** | **bool** |  | [optional] 
**arrears_based_on_original_schedule** | **bool** |  | [optional] 
**compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_recalculation_compounding_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**is_arrears_based_on_original_schedule** | **bool** |  | [optional] 
**is_compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**pre_closure_interest_calculation_strategy** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**recalculation_compounding_frequency_interval** | **int** |  | [optional] 
**recalculation_compounding_frequency_nth_day** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**recalculation_compounding_frequency_on_day** | **int** |  | [optional] 
**recalculation_compounding_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**recalculation_compounding_frequency_weekday** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**recalculation_rest_frequency_interval** | **int** |  | [optional] 
**recalculation_rest_frequency_nth_day** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**recalculation_rest_frequency_on_day** | **int** |  | [optional] 
**recalculation_rest_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**recalculation_rest_frequency_weekday** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**reschedule_strategy_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_interest_recalculation_data import LoanProductInterestRecalculationData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductInterestRecalculationData from a JSON string
loan_product_interest_recalculation_data_instance = LoanProductInterestRecalculationData.from_json(json)
# print the JSON string representation of the object
print(LoanProductInterestRecalculationData.to_json())

# convert the object into a dict
loan_product_interest_recalculation_data_dict = loan_product_interest_recalculation_data_instance.to_dict()
# create an instance of LoanProductInterestRecalculationData from a dict
loan_product_interest_recalculation_data_from_dict = LoanProductInterestRecalculationData.from_dict(loan_product_interest_recalculation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


