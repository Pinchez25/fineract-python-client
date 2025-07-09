# PutGLAccountsRequest

PutGLAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**tag_id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**usage** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_gl_accounts_request import PutGLAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGLAccountsRequest from a JSON string
put_gl_accounts_request_instance = PutGLAccountsRequest.from_json(json)
# print the JSON string representation of the object
print PutGLAccountsRequest.to_json()

# convert the object into a dict
put_gl_accounts_request_dict = put_gl_accounts_request_instance.to_dict()
# create an instance of PutGLAccountsRequest from a dict
put_gl_accounts_request_form_dict = put_gl_accounts_request.from_dict(put_gl_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


