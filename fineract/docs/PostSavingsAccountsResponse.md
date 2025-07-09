# PostSavingsAccountsResponse

PostSavingsAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_accounts_response import PostSavingsAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountsResponse from a JSON string
post_savings_accounts_response_instance = PostSavingsAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(PostSavingsAccountsResponse.to_json())

# convert the object into a dict
post_savings_accounts_response_dict = post_savings_accounts_response_instance.to_dict()
# create an instance of PostSavingsAccountsResponse from a dict
post_savings_accounts_response_from_dict = PostSavingsAccountsResponse.from_dict(post_savings_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


