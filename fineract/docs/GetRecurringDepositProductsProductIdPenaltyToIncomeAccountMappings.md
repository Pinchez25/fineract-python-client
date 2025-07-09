# GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappingsCharge**](GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappingsCharge.md) |  | [optional] 
**income_account** | [**GetRecurringDepositProductsGlAccount**](GetRecurringDepositProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_penalty_to_income_account_mappings import GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings from a JSON string
get_recurring_deposit_products_product_id_penalty_to_income_account_mappings_instance = GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings.to_json()

# convert the object into a dict
get_recurring_deposit_products_product_id_penalty_to_income_account_mappings_dict = get_recurring_deposit_products_product_id_penalty_to_income_account_mappings_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings from a dict
get_recurring_deposit_products_product_id_penalty_to_income_account_mappings_form_dict = get_recurring_deposit_products_product_id_penalty_to_income_account_mappings.from_dict(get_recurring_deposit_products_product_id_penalty_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


