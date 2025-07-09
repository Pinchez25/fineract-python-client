# DeleteGLAccountsRequest

DeleteGLAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_gl_accounts_request import DeleteGLAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGLAccountsRequest from a JSON string
delete_gl_accounts_request_instance = DeleteGLAccountsRequest.from_json(json)
# print the JSON string representation of the object
print DeleteGLAccountsRequest.to_json()

# convert the object into a dict
delete_gl_accounts_request_dict = delete_gl_accounts_request_instance.to_dict()
# create an instance of DeleteGLAccountsRequest from a dict
delete_gl_accounts_request_form_dict = delete_gl_accounts_request.from_dict(delete_gl_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


