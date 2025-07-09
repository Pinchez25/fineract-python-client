# GetLoanProductsValueConditionTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_value_condition_type_options import GetLoanProductsValueConditionTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsValueConditionTypeOptions from a JSON string
get_loan_products_value_condition_type_options_instance = GetLoanProductsValueConditionTypeOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsValueConditionTypeOptions.to_json())

# convert the object into a dict
get_loan_products_value_condition_type_options_dict = get_loan_products_value_condition_type_options_instance.to_dict()
# create an instance of GetLoanProductsValueConditionTypeOptions from a dict
get_loan_products_value_condition_type_options_from_dict = GetLoanProductsValueConditionTypeOptions.from_dict(get_loan_products_value_condition_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


