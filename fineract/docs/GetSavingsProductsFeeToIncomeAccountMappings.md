# GetSavingsProductsFeeToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetSavingsProductsFeeToIncomeAccountMappingsCharge**](GetSavingsProductsFeeToIncomeAccountMappingsCharge.md) |  | [optional] 
**income_account** | [**GetSavingsProductsFeeToIncomeAccountMappingsIncomeAccount**](GetSavingsProductsFeeToIncomeAccountMappingsIncomeAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_fee_to_income_account_mappings import GetSavingsProductsFeeToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsFeeToIncomeAccountMappings from a JSON string
get_savings_products_fee_to_income_account_mappings_instance = GetSavingsProductsFeeToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsFeeToIncomeAccountMappings.to_json())

# convert the object into a dict
get_savings_products_fee_to_income_account_mappings_dict = get_savings_products_fee_to_income_account_mappings_instance.to_dict()
# create an instance of GetSavingsProductsFeeToIncomeAccountMappings from a dict
get_savings_products_fee_to_income_account_mappings_from_dict = GetSavingsProductsFeeToIncomeAccountMappings.from_dict(get_savings_products_fee_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


