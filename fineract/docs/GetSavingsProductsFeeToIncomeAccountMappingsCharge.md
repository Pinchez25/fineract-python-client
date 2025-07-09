# GetSavingsProductsFeeToIncomeAccountMappingsCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_fee_to_income_account_mappings_charge import GetSavingsProductsFeeToIncomeAccountMappingsCharge

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsFeeToIncomeAccountMappingsCharge from a JSON string
get_savings_products_fee_to_income_account_mappings_charge_instance = GetSavingsProductsFeeToIncomeAccountMappingsCharge.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsFeeToIncomeAccountMappingsCharge.to_json()

# convert the object into a dict
get_savings_products_fee_to_income_account_mappings_charge_dict = get_savings_products_fee_to_income_account_mappings_charge_instance.to_dict()
# create an instance of GetSavingsProductsFeeToIncomeAccountMappingsCharge from a dict
get_savings_products_fee_to_income_account_mappings_charge_form_dict = get_savings_products_fee_to_income_account_mappings_charge.from_dict(get_savings_products_fee_to_income_account_mappings_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


