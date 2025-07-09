# PostAccountsTypeResponse

PostAccountsTypeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_accounts_type_response import PostAccountsTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsTypeResponse from a JSON string
post_accounts_type_response_instance = PostAccountsTypeResponse.from_json(json)
# print the JSON string representation of the object
print PostAccountsTypeResponse.to_json()

# convert the object into a dict
post_accounts_type_response_dict = post_accounts_type_response_instance.to_dict()
# create an instance of PostAccountsTypeResponse from a dict
post_accounts_type_response_form_dict = post_accounts_type_response.from_dict(post_accounts_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


