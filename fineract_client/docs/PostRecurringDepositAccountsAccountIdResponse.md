# PostRecurringDepositAccountsAccountIdResponse

PostRecurringDepositAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_accounts_account_id_response import PostRecurringDepositAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositAccountsAccountIdResponse from a JSON string
post_recurring_deposit_accounts_account_id_response_instance = PostRecurringDepositAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositAccountsAccountIdResponse.to_json())

# convert the object into a dict
post_recurring_deposit_accounts_account_id_response_dict = post_recurring_deposit_accounts_account_id_response_instance.to_dict()
# create an instance of PostRecurringDepositAccountsAccountIdResponse from a dict
post_recurring_deposit_accounts_account_id_response_from_dict = PostRecurringDepositAccountsAccountIdResponse.from_dict(post_recurring_deposit_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


