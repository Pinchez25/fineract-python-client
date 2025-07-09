# PostGLAccountsRequest

PostGLAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**tag_id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**usage** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_gl_accounts_request import PostGLAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGLAccountsRequest from a JSON string
post_gl_accounts_request_instance = PostGLAccountsRequest.from_json(json)
# print the JSON string representation of the object
print PostGLAccountsRequest.to_json()

# convert the object into a dict
post_gl_accounts_request_dict = post_gl_accounts_request_instance.to_dict()
# create an instance of PostGLAccountsRequest from a dict
post_gl_accounts_request_form_dict = post_gl_accounts_request.from_dict(post_gl_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


