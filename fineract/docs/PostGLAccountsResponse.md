# PostGLAccountsResponse

PostGLAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_gl_accounts_response import PostGLAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGLAccountsResponse from a JSON string
post_gl_accounts_response_instance = PostGLAccountsResponse.from_json(json)
# print the JSON string representation of the object
print PostGLAccountsResponse.to_json()

# convert the object into a dict
post_gl_accounts_response_dict = post_gl_accounts_response_instance.to_dict()
# create an instance of PostGLAccountsResponse from a dict
post_gl_accounts_response_form_dict = post_gl_accounts_response.from_dict(post_gl_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


