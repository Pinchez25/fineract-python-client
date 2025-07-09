# GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetRecurringDepositProductsProductIdFeeToIncomeAccountMappingsCharge**](GetRecurringDepositProductsProductIdFeeToIncomeAccountMappingsCharge.md) |  | [optional] 
**income_account** | [**GetRecurringDepositProductsProductIdFeeToIncomeAccountMappingsIncomeAccount**](GetRecurringDepositProductsProductIdFeeToIncomeAccountMappingsIncomeAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_fee_to_income_account_mappings import GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings from a JSON string
get_recurring_deposit_products_product_id_fee_to_income_account_mappings_instance = GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings.to_json())

# convert the object into a dict
get_recurring_deposit_products_product_id_fee_to_income_account_mappings_dict = get_recurring_deposit_products_product_id_fee_to_income_account_mappings_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings from a dict
get_recurring_deposit_products_product_id_fee_to_income_account_mappings_from_dict = GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings.from_dict(get_recurring_deposit_products_product_id_fee_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


