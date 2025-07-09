# GetProductsAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_accounting_rule import GetProductsAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsAccountingRule from a JSON string
get_products_accounting_rule_instance = GetProductsAccountingRule.from_json(json)
# print the JSON string representation of the object
print GetProductsAccountingRule.to_json()

# convert the object into a dict
get_products_accounting_rule_dict = get_products_accounting_rule_instance.to_dict()
# create an instance of GetProductsAccountingRule from a dict
get_products_accounting_rule_form_dict = get_products_accounting_rule.from_dict(get_products_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


