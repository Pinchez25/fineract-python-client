# GetLoanProductsIncomeAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**organization_running_balance** | **int** |  | [optional] 
**tag_id** | [**GetLoanProductsLiabilityTagId**](GetLoanProductsLiabilityTagId.md) |  | [optional] 
**type** | [**GetLoanProductsIncomeType**](GetLoanProductsIncomeType.md) |  | [optional] 
**usage** | [**GetLoanProductsLiabilityUsage**](GetLoanProductsLiabilityUsage.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_income_account_options import GetLoanProductsIncomeAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsIncomeAccountOptions from a JSON string
get_loan_products_income_account_options_instance = GetLoanProductsIncomeAccountOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsIncomeAccountOptions.to_json())

# convert the object into a dict
get_loan_products_income_account_options_dict = get_loan_products_income_account_options_instance.to_dict()
# create an instance of GetLoanProductsIncomeAccountOptions from a dict
get_loan_products_income_account_options_from_dict = GetLoanProductsIncomeAccountOptions.from_dict(get_loan_products_income_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


