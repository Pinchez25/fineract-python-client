# GetSavingsProductsAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_receivable_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**income_from_fee_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**income_from_interest** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**income_from_penalty_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**interest_on_savings_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**interest_payable_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**overdraft_portfolio_control** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**penalty_receivable_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**savings_control_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**savings_reference_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**transfers_in_suspense_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 
**write_off_account** | [**GetSavingsProductsGlAccount**](GetSavingsProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_accounting_mappings import GetSavingsProductsAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsAccountingMappings from a JSON string
get_savings_products_accounting_mappings_instance = GetSavingsProductsAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsAccountingMappings.to_json())

# convert the object into a dict
get_savings_products_accounting_mappings_dict = get_savings_products_accounting_mappings_instance.to_dict()
# create an instance of GetSavingsProductsAccountingMappings from a dict
get_savings_products_accounting_mappings_from_dict = GetSavingsProductsAccountingMappings.from_dict(get_savings_products_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


