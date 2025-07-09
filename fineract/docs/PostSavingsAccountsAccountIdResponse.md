# PostSavingsAccountsAccountIdResponse

PostSavingsAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_accounts_account_id_response import PostSavingsAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountsAccountIdResponse from a JSON string
post_savings_accounts_account_id_response_instance = PostSavingsAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(PostSavingsAccountsAccountIdResponse.to_json())

# convert the object into a dict
post_savings_accounts_account_id_response_dict = post_savings_accounts_account_id_response_instance.to_dict()
# create an instance of PostSavingsAccountsAccountIdResponse from a dict
post_savings_accounts_account_id_response_from_dict = PostSavingsAccountsAccountIdResponse.from_dict(post_savings_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


