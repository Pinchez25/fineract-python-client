# GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse

GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | [**GetRecurringTransactionsCurrency**](GetRecurringTransactionsCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_detail_data** | [**GetRecurringPaymentDetailData**](GetRecurringPaymentDetailData.md) |  | [optional] 
**reversed** | **bool** |  | [optional] 
**running_balance** | **int** |  | [optional] 
**transaction_type** | [**GetRecurringTransactionsTransactionType**](GetRecurringTransactionsTransactionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response import GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse from a JSON string
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response_instance = GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response_dict = get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response_instance.to_dict()
# create an instance of GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTransactionIdResponse from a dict
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response_form_dict = get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response.from_dict(get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


