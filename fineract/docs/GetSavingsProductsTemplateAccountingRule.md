# GetSavingsProductsTemplateAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_template_accounting_rule import GetSavingsProductsTemplateAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsTemplateAccountingRule from a JSON string
get_savings_products_template_accounting_rule_instance = GetSavingsProductsTemplateAccountingRule.from_json(json)
# print the JSON string representation of the object
print GetSavingsProductsTemplateAccountingRule.to_json()

# convert the object into a dict
get_savings_products_template_accounting_rule_dict = get_savings_products_template_accounting_rule_instance.to_dict()
# create an instance of GetSavingsProductsTemplateAccountingRule from a dict
get_savings_products_template_accounting_rule_form_dict = get_savings_products_template_accounting_rule.from_dict(get_savings_products_template_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


