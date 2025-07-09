# GetLoanProductsAccountingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_accounting_rule import GetLoanProductsAccountingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsAccountingRule from a JSON string
get_loan_products_accounting_rule_instance = GetLoanProductsAccountingRule.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsAccountingRule.to_json())

# convert the object into a dict
get_loan_products_accounting_rule_dict = get_loan_products_accounting_rule_instance.to_dict()
# create an instance of GetLoanProductsAccountingRule from a dict
get_loan_products_accounting_rule_from_dict = GetLoanProductsAccountingRule.from_dict(get_loan_products_accounting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


