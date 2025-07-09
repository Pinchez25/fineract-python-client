# GetSavingsProductsIncomeAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**tag_id** | **object** |  | [optional] 
**type** | [**GetSavingsProductsIncomeType**](GetSavingsProductsIncomeType.md) |  | [optional] 
**usage** | [**GetSavingsProductsLiabilityUsage**](GetSavingsProductsLiabilityUsage.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_income_account_options import GetSavingsProductsIncomeAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsIncomeAccountOptions from a JSON string
get_savings_products_income_account_options_instance = GetSavingsProductsIncomeAccountOptions.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsIncomeAccountOptions.to_json()

# convert the object into a dict
get_savings_products_income_account_options_dict = get_savings_products_income_account_options_instance.to_dict()
# create an instance of GetSavingsProductsIncomeAccountOptions from a dict
get_savings_products_income_account_options_form_dict = get_savings_products_income_account_options.from_dict(get_savings_products_income_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


