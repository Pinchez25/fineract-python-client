# GetLoanProductsAccountingMappingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_account_options** | [**List[GetLoanProductsAssetAccountOptions]**](GetLoanProductsAssetAccountOptions.md) |  | [optional] 
**expense_account_options** | [**List[GetLoanProductsExpenseAccountOptions]**](GetLoanProductsExpenseAccountOptions.md) |  | [optional] 
**income_account_options** | [**List[GetLoanProductsIncomeAccountOptions]**](GetLoanProductsIncomeAccountOptions.md) |  | [optional] 
**liability_account_options** | [**List[GetLoanProductsLiabilityAccountOptions]**](GetLoanProductsLiabilityAccountOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_accounting_mapping_options import GetLoanProductsAccountingMappingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsAccountingMappingOptions from a JSON string
get_loan_products_accounting_mapping_options_instance = GetLoanProductsAccountingMappingOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsAccountingMappingOptions.to_json())

# convert the object into a dict
get_loan_products_accounting_mapping_options_dict = get_loan_products_accounting_mapping_options_instance.to_dict()
# create an instance of GetLoanProductsAccountingMappingOptions from a dict
get_loan_products_accounting_mapping_options_from_dict = GetLoanProductsAccountingMappingOptions.from_dict(get_loan_products_accounting_mapping_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


