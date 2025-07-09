# AccountingTagRuleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tag** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**transaction_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.accounting_tag_rule_data import AccountingTagRuleData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingTagRuleData from a JSON string
accounting_tag_rule_data_instance = AccountingTagRuleData.from_json(json)
# print the JSON string representation of the object
print(AccountingTagRuleData.to_json())

# convert the object into a dict
accounting_tag_rule_data_dict = accounting_tag_rule_data_instance.to_dict()
# create an instance of AccountingTagRuleData from a dict
accounting_tag_rule_data_from_dict = AccountingTagRuleData.from_dict(accounting_tag_rule_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


