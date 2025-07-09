# GetProductsAccountingMappingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_account_options** | [**List[GetProductsAssetAccountOptions]**](GetProductsAssetAccountOptions.md) |  | [optional] 
**equity_account_options** | [**List[GetProductsEquityAccountOptions]**](GetProductsEquityAccountOptions.md) |  | [optional] 
**income_account_options** | [**List[GetProductsIncomeAccountOptions]**](GetProductsIncomeAccountOptions.md) |  | [optional] 
**liability_account_options** | [**List[GetProductsLiabilityAccountOptions]**](GetProductsLiabilityAccountOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_products_accounting_mapping_options import GetProductsAccountingMappingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsAccountingMappingOptions from a JSON string
get_products_accounting_mapping_options_instance = GetProductsAccountingMappingOptions.from_json(json)
# print the JSON string representation of the object
print(GetProductsAccountingMappingOptions.to_json())

# convert the object into a dict
get_products_accounting_mapping_options_dict = get_products_accounting_mapping_options_instance.to_dict()
# create an instance of GetProductsAccountingMappingOptions from a dict
get_products_accounting_mapping_options_from_dict = GetProductsAccountingMappingOptions.from_dict(get_products_accounting_mapping_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


