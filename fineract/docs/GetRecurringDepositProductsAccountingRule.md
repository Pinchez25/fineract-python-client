# GetRecurringDepositProductsAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_accounting_rule import GetRecurringDepositProductsAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsAccountingRule from a JSON string
get_recurring_deposit_products_accounting_rule_instance = GetRecurringDepositProductsAccountingRule.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositProductsAccountingRule.to_json()

# convert the object into a dict
get_recurring_deposit_products_accounting_rule_dict = get_recurring_deposit_products_accounting_rule_instance.to_dict()
# create an instance of GetRecurringDepositProductsAccountingRule from a dict
get_recurring_deposit_products_accounting_rule_form_dict = get_recurring_deposit_products_accounting_rule.from_dict(get_recurring_deposit_products_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


