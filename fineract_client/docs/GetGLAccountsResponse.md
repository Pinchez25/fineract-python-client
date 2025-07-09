# GetGLAccountsResponse

GetGLAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**organization_running_balance** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**tag_id** | [**CodeValueData**](CodeValueData.md) |  | [optional] 
**type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**usage** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_gl_accounts_response import GetGLAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGLAccountsResponse from a JSON string
get_gl_accounts_response_instance = GetGLAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetGLAccountsResponse.to_json())

# convert the object into a dict
get_gl_accounts_response_dict = get_gl_accounts_response_instance.to_dict()
# create an instance of GetGLAccountsResponse from a dict
get_gl_accounts_response_from_dict = GetGLAccountsResponse.from_dict(get_gl_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


