# GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappingsCharge**](GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappingsCharge.md) |  | [optional] 
**income_account** | [**GetFixedDepositProductsGlAccount**](GetFixedDepositProductsGlAccount.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_product_id_penalty_to_income_account_mappings import GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings from a JSON string
get_fixed_deposit_products_product_id_penalty_to_income_account_mappings_instance = GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings.to_json())

# convert the object into a dict
get_fixed_deposit_products_product_id_penalty_to_income_account_mappings_dict = get_fixed_deposit_products_product_id_penalty_to_income_account_mappings_instance.to_dict()
# create an instance of GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings from a dict
get_fixed_deposit_products_product_id_penalty_to_income_account_mappings_from_dict = GetFixedDepositProductsProductIdPenaltyToIncomeAccountMappings.from_dict(get_fixed_deposit_products_product_id_penalty_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


