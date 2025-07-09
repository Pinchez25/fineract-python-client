# GLAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[GLAccount]**](GLAccount.md) |  | [optional] 
**description** | **str** |  | [optional] 
**detail_account** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**header_account** | **bool** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**parent** | [**GLAccount**](GLAccount.md) |  | [optional] 
**tag_id** | [**CodeValue**](CodeValue.md) |  | [optional] 
**type** | **int** |  | [optional] 
**usage** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.gl_account import GLAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccount from a JSON string
gl_account_instance = GLAccount.from_json(json)
# print the JSON string representation of the object
print GLAccount.to_json()

# convert the object into a dict
gl_account_dict = gl_account_instance.to_dict()
# create an instance of GLAccount from a dict
gl_account_form_dict = gl_account.from_dict(gl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


