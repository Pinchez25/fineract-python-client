# GLAccountData


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
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**equity_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**expense_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**income_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**liability_header_account_options** | [**List[GLAccountData]**](GLAccountData.md) |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**organization_running_balance** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**row_index** | **int** |  | [optional] 
**tag_id** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**usage** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**usage_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.gl_account_data import GLAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccountData from a JSON string
gl_account_data_instance = GLAccountData.from_json(json)
# print the JSON string representation of the object
print GLAccountData.to_json()

# convert the object into a dict
gl_account_data_dict = gl_account_data_instance.to_dict()
# create an instance of GLAccountData from a dict
gl_account_data_form_dict = gl_account_data.from_dict(gl_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


