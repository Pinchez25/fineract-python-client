# PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse

PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostRecurringChanges**](PostRecurringChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse from a JSON string
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response_instance = PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse.to_json())

# convert the object into a dict
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response_dict = post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response_instance.to_dict()
# create an instance of PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse from a dict
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response_from_dict = PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsResponse.from_dict(post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


