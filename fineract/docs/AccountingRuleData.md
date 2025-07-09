# AccountingRuleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_credit_entries** | **bool** |  | [optional] 
**allow_multiple_debit_entries** | **bool** |  | [optional] 
**allowed_accounts** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**allowed_credit_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_debit_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_offices** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**credit_accounts** | [**List[GLAccountDataForLookup]**](GLAccountDataForLookup.md) |  | [optional] 
**credit_tags** | [**List[AccountingTagRuleData]**](AccountingTagRuleData.md) |  | [optional] 
**debit_accounts** | [**List[GLAccountDataForLookup]**](GLAccountDataForLookup.md) |  | [optional] 
**debit_tags** | [**List[AccountingTagRuleData]**](AccountingTagRuleData.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**system_defined** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.accounting_rule_data import AccountingRuleData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingRuleData from a JSON string
accounting_rule_data_instance = AccountingRuleData.from_json(json)
# print the JSON string representation of the object
print AccountingRuleData.to_json()

# convert the object into a dict
accounting_rule_data_dict = accounting_rule_data_instance.to_dict()
# create an instance of AccountingRuleData from a dict
accounting_rule_data_form_dict = accounting_rule_data.from_dict(accounting_rule_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


