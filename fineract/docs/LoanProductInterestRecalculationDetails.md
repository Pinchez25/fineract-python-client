# LoanProductInterestRecalculationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrears_based_on_original_schedule** | **bool** |  | [optional] 
**compounding_frequency_nth_day** | **int** |  | [optional] 
**compounding_frequency_on_day** | **int** |  | [optional] 
**compounding_frequency_type** | **str** |  | [optional] 
**compounding_frequency_weekday** | **int** |  | [optional] 
**compounding_interval** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_recalculation_compounding_method** | **int** |  | [optional] 
**is_compounding_to_be_posted_as_transaction** | **bool** |  | [optional] 
**new** | **bool** |  | [optional] 
**reschedule_strategy_method** | **int** |  | [optional] 
**rest_frequency_nth_day** | **int** |  | [optional] 
**rest_frequency_on_day** | **int** |  | [optional] 
**rest_frequency_type** | **str** |  | [optional] 
**rest_frequency_weekday** | **int** |  | [optional] 
**rest_interval** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_interest_recalculation_details import LoanProductInterestRecalculationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductInterestRecalculationDetails from a JSON string
loan_product_interest_recalculation_details_instance = LoanProductInterestRecalculationDetails.from_json(json)
# print the JSON string representation of the object
print LoanProductInterestRecalculationDetails.to_json()

# convert the object into a dict
loan_product_interest_recalculation_details_dict = loan_product_interest_recalculation_details_instance.to_dict()
# create an instance of LoanProductInterestRecalculationDetails from a dict
loan_product_interest_recalculation_details_form_dict = loan_product_interest_recalculation_details.from_dict(loan_product_interest_recalculation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


