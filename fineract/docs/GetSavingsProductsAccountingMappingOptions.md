# GetSavingsProductsAccountingMappingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_account_options** | [**List[GetSavingsProductsAssetAccountOptions]**](GetSavingsProductsAssetAccountOptions.md) |  | [optional] 
**expense_account_options** | [**List[GetSavingsProductsExpenseAccountOptions]**](GetSavingsProductsExpenseAccountOptions.md) |  | [optional] 
**income_account_options** | [**List[GetSavingsProductsIncomeAccountOptions]**](GetSavingsProductsIncomeAccountOptions.md) |  | [optional] 
**liability_account_options** | [**List[GetSavingsProductsLiabilityAccountOptions]**](GetSavingsProductsLiabilityAccountOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_accounting_mapping_options import GetSavingsProductsAccountingMappingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsAccountingMappingOptions from a JSON string
get_savings_products_accounting_mapping_options_instance = GetSavingsProductsAccountingMappingOptions.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsAccountingMappingOptions.to_json())

# convert the object into a dict
get_savings_products_accounting_mapping_options_dict = get_savings_products_accounting_mapping_options_instance.to_dict()
# create an instance of GetSavingsProductsAccountingMappingOptions from a dict
get_savings_products_accounting_mapping_options_from_dict = GetSavingsProductsAccountingMappingOptions.from_dict(get_savings_products_accounting_mapping_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


