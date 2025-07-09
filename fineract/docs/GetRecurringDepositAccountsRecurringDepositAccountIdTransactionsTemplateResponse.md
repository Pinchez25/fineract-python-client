# GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse

GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency** | [**GetRecurringCurrency**](GetRecurringCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_type_options** | **List[int]** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**transaction_type** | [**GetRecurringTransactionType**](GetRecurringTransactionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response import GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse from a JSON string
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response_instance = GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response_dict = get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response_instance.to_dict()
# create an instance of GetRecurringDepositAccountsRecurringDepositAccountIdTransactionsTemplateResponse from a dict
get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response_form_dict = get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response.from_dict(get_recurring_deposit_accounts_recurring_deposit_account_id_transactions_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


