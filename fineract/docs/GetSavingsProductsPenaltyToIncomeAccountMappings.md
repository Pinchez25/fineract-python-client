# GetSavingsProductsPenaltyToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetSavingsProductsPenaltyToIncomeAccountMappingsCharge**](GetSavingsProductsPenaltyToIncomeAccountMappingsCharge.md) |  | [optional] 
**income_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_penalty_to_income_account_mappings import GetSavingsProductsPenaltyToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsPenaltyToIncomeAccountMappings from a JSON string
get_savings_products_penalty_to_income_account_mappings_instance = GetSavingsProductsPenaltyToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsPenaltyToIncomeAccountMappings.to_json()

# convert the object into a dict
get_savings_products_penalty_to_income_account_mappings_dict = get_savings_products_penalty_to_income_account_mappings_instance.to_dict()
# create an instance of GetSavingsProductsPenaltyToIncomeAccountMappings from a dict
get_savings_products_penalty_to_income_account_mappings_form_dict = get_savings_products_penalty_to_income_account_mappings.from_dict(get_savings_products_penalty_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


