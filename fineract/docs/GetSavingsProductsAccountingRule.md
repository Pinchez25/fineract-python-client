# GetSavingsProductsAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_accounting_rule import GetSavingsProductsAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsAccountingRule from a JSON string
get_savings_products_accounting_rule_instance = GetSavingsProductsAccountingRule.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsAccountingRule.to_json())

# convert the object into a dict
get_savings_products_accounting_rule_dict = get_savings_products_accounting_rule_instance.to_dict()
# create an instance of GetSavingsProductsAccountingRule from a dict
get_savings_products_accounting_rule_from_dict = GetSavingsProductsAccountingRule.from_dict(get_savings_products_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


