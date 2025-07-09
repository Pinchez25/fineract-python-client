# GetFixedDepositProductsProductIdAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_receivable_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**income_from_fee_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**income_from_penalty_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**interest_on_savings_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**interest_payable_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**penalty_receivable_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**savings_control_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**savings_reference_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 
**transfers_in_suspense_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_product_id_accounting_mappings import GetFixedDepositProductsProductIdAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsProductIdAccountingMappings from a JSON string
get_fixed_deposit_products_product_id_accounting_mappings_instance = GetFixedDepositProductsProductIdAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositProductsProductIdAccountingMappings.to_json())

# convert the object into a dict
get_fixed_deposit_products_product_id_accounting_mappings_dict = get_fixed_deposit_products_product_id_accounting_mappings_instance.to_dict()
# create an instance of GetFixedDepositProductsProductIdAccountingMappings from a dict
get_fixed_deposit_products_product_id_accounting_mappings_from_dict = GetFixedDepositProductsProductIdAccountingMappings.from_dict(get_fixed_deposit_products_product_id_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


