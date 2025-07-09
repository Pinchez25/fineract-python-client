# GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse

GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 
**currency** | [**GetSelfSavingsTransactionCurrency**](GetSelfSavingsTransactionCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_detail_data** | [**GetSelfSavingsPaymentDetailData**](GetSelfSavingsPaymentDetailData.md) |  | [optional] 
**reversed** | **bool** |  | [optional] 
**running_balance** | **int** |  | [optional] 
**transaction_type** | [**GetSelfSavingsTransactionType**](GetSelfSavingsTransactionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_accounts_account_id_transactions_transaction_id_response import GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse from a JSON string
get_self_savings_accounts_account_id_transactions_transaction_id_response_instance = GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse.to_json()

# convert the object into a dict
get_self_savings_accounts_account_id_transactions_transaction_id_response_dict = get_self_savings_accounts_account_id_transactions_transaction_id_response_instance.to_dict()
# create an instance of GetSelfSavingsAccountsAccountIdTransactionsTransactionIdResponse from a dict
get_self_savings_accounts_account_id_transactions_transaction_id_response_form_dict = get_self_savings_accounts_account_id_transactions_transaction_id_response.from_dict(get_self_savings_accounts_account_id_transactions_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


