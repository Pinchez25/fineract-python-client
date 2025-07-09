# GetAccountRulesTemplateResponse

GetAccountRulesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_accounts** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**allowed_offices** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**system_defined** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_rules_template_response import GetAccountRulesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountRulesTemplateResponse from a JSON string
get_account_rules_template_response_instance = GetAccountRulesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountRulesTemplateResponse.to_json())

# convert the object into a dict
get_account_rules_template_response_dict = get_account_rules_template_response_instance.to_dict()
# create an instance of GetAccountRulesTemplateResponse from a dict
get_account_rules_template_response_from_dict = GetAccountRulesTemplateResponse.from_dict(get_account_rules_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


