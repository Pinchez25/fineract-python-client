# LoanProductBorrowerCycleVariations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrower_cycle_number** | **int** |  | [optional] 
**default_value** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**new** | **bool** |  | [optional] 
**param_type** | **str** |  | [optional] 
**value_condition_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_borrower_cycle_variations import LoanProductBorrowerCycleVariations

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductBorrowerCycleVariations from a JSON string
loan_product_borrower_cycle_variations_instance = LoanProductBorrowerCycleVariations.from_json(json)
# print the JSON string representation of the object
print LoanProductBorrowerCycleVariations.to_json()

# convert the object into a dict
loan_product_borrower_cycle_variations_dict = loan_product_borrower_cycle_variations_instance.to_dict()
# create an instance of LoanProductBorrowerCycleVariations from a dict
loan_product_borrower_cycle_variations_form_dict = loan_product_borrower_cycle_variations.from_dict(loan_product_borrower_cycle_variations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


