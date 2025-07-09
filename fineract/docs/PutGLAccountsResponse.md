# PutGLAccountsResponse

PutGLAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutGLAccountsResponsechangesSwagger**](PutGLAccountsResponsechangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_gl_accounts_response import PutGLAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutGLAccountsResponse from a JSON string
put_gl_accounts_response_instance = PutGLAccountsResponse.from_json(json)
# print the JSON string representation of the object
print PutGLAccountsResponse.to_json()

# convert the object into a dict
put_gl_accounts_response_dict = put_gl_accounts_response_instance.to_dict()
# create an instance of PutGLAccountsResponse from a dict
put_gl_accounts_response_form_dict = put_gl_accounts_response.from_dict(put_gl_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


