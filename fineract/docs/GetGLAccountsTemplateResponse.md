# GetGLAccountsTemplateResponse

GetGLAccountsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**allowed_assets_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_equity_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_expenses_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_income_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**allowed_liabilities_tag_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**asset_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**equity_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**expense_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**liability_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**usage** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**usage_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_gl_accounts_template_response import GetGLAccountsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGLAccountsTemplateResponse from a JSON string
get_gl_accounts_template_response_instance = GetGLAccountsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetGLAccountsTemplateResponse.to_json())

# convert the object into a dict
get_gl_accounts_template_response_dict = get_gl_accounts_template_response_instance.to_dict()
# create an instance of GetGLAccountsTemplateResponse from a dict
get_gl_accounts_template_response_from_dict = GetGLAccountsTemplateResponse.from_dict(get_gl_accounts_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


