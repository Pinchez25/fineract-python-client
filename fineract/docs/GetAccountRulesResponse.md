# GetAccountRulesResponse

GetAccountRulesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_multiple_credit_entries** | **bool** |  | [optional] 
**allow_multiple_debit_entries** | **bool** |  | [optional] 
**credit_tags** | [**List[AccountingTagRuleData]**](AccountingTagRuleData.md) |  | [optional] 
**debit_tags** | [**List[AccountingTagRuleData]**](AccountingTagRuleData.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**system_defined** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_rules_response import GetAccountRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountRulesResponse from a JSON string
get_account_rules_response_instance = GetAccountRulesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountRulesResponse.to_json())

# convert the object into a dict
get_account_rules_response_dict = get_account_rules_response_instance.to_dict()
# create an instance of GetAccountRulesResponse from a dict
get_account_rules_response_from_dict = GetAccountRulesResponse.from_dict(get_account_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


