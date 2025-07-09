# GetRecurringDepositProductsProductIdAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_receivable_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**income_from_fee_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**income_from_penalty_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**interest_on_savings_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**interest_payable_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**penalty_receivable_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**savings_control_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 
**transfers_in_suspense_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_accounting_mappings import GetRecurringDepositProductsProductIdAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdAccountingMappings from a JSON string
get_recurring_deposit_products_product_id_accounting_mappings_instance = GetRecurringDepositProductsProductIdAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsProductIdAccountingMappings.to_json())

# convert the object into a dict
get_recurring_deposit_products_product_id_accounting_mappings_dict = get_recurring_deposit_products_product_id_accounting_mappings_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdAccountingMappings from a dict
get_recurring_deposit_products_product_id_accounting_mappings_from_dict = GetRecurringDepositProductsProductIdAccountingMappings.from_dict(get_recurring_deposit_products_product_id_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


