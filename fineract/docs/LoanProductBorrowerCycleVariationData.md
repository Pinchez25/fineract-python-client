# LoanProductBorrowerCycleVariationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrower_cycle_number** | **int** |  | [optional] 
**default_value** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_product_param_type** | **str** |  | [optional] 
**loan_product_value_condition_type** | **str** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**param_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**value_condition_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_borrower_cycle_variation_data import LoanProductBorrowerCycleVariationData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductBorrowerCycleVariationData from a JSON string
loan_product_borrower_cycle_variation_data_instance = LoanProductBorrowerCycleVariationData.from_json(json)
# print the JSON string representation of the object
print LoanProductBorrowerCycleVariationData.to_json()

# convert the object into a dict
loan_product_borrower_cycle_variation_data_dict = loan_product_borrower_cycle_variation_data_instance.to_dict()
# create an instance of LoanProductBorrowerCycleVariationData from a dict
loan_product_borrower_cycle_variation_data_form_dict = loan_product_borrower_cycle_variation_data.from_dict(loan_product_borrower_cycle_variation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


