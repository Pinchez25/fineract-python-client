# GetFixedDepositProductsAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_accounting_rule import GetFixedDepositProductsAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsAccountingRule from a JSON string
get_fixed_deposit_products_accounting_rule_instance = GetFixedDepositProductsAccountingRule.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositProductsAccountingRule.to_json()

# convert the object into a dict
get_fixed_deposit_products_accounting_rule_dict = get_fixed_deposit_products_accounting_rule_instance.to_dict()
# create an instance of GetFixedDepositProductsAccountingRule from a dict
get_fixed_deposit_products_accounting_rule_form_dict = get_fixed_deposit_products_accounting_rule.from_dict(get_fixed_deposit_products_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


