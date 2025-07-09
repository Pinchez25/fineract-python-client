# PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest

PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request import PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest from a JSON string
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request_instance = PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.to_json())

# convert the object into a dict
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request_dict = post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request_instance.to_dict()
# create an instance of PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest from a dict
post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request_from_dict = PostRecurringDepositAccountsRecurringDepositAccountIdTransactionsRequest.from_dict(post_recurring_deposit_accounts_recurring_deposit_account_id_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


