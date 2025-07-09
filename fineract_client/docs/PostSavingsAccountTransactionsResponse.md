# PostSavingsAccountTransactionsResponse

PostSavingsAccountTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_account_transactions_response import PostSavingsAccountTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountTransactionsResponse from a JSON string
post_savings_account_transactions_response_instance = PostSavingsAccountTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(PostSavingsAccountTransactionsResponse.to_json())

# convert the object into a dict
post_savings_account_transactions_response_dict = post_savings_account_transactions_response_instance.to_dict()
# create an instance of PostSavingsAccountTransactionsResponse from a dict
post_savings_account_transactions_response_from_dict = PostSavingsAccountTransactionsResponse.from_dict(post_savings_account_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


