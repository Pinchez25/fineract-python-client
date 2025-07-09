# GetLoanProductsPrincipalVariationsForBorrowerCycle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borrower_cycle_number** | **int** |  | [optional] 
**default_value** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**param_type** | [**GetLoanProductsParamType**](GetLoanProductsParamType.md) |  | [optional] 
**value_condition_type** | [**GetLoanProductsValueConditionType**](GetLoanProductsValueConditionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_principal_variations_for_borrower_cycle import GetLoanProductsPrincipalVariationsForBorrowerCycle

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsPrincipalVariationsForBorrowerCycle from a JSON string
get_loan_products_principal_variations_for_borrower_cycle_instance = GetLoanProductsPrincipalVariationsForBorrowerCycle.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsPrincipalVariationsForBorrowerCycle.to_json()

# convert the object into a dict
get_loan_products_principal_variations_for_borrower_cycle_dict = get_loan_products_principal_variations_for_borrower_cycle_instance.to_dict()
# create an instance of GetLoanProductsPrincipalVariationsForBorrowerCycle from a dict
get_loan_products_principal_variations_for_borrower_cycle_form_dict = get_loan_products_principal_variations_for_borrower_cycle.from_dict(get_loan_products_principal_variations_for_borrower_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


