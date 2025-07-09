# PutRecurringDepositAccountsAccountIdResponse

PutRecurringDepositAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutRecurringDepositAccountsChanges**](PutRecurringDepositAccountsChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_accounts_account_id_response import PutRecurringDepositAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositAccountsAccountIdResponse from a JSON string
put_recurring_deposit_accounts_account_id_response_instance = PutRecurringDepositAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutRecurringDepositAccountsAccountIdResponse.to_json())

# convert the object into a dict
put_recurring_deposit_accounts_account_id_response_dict = put_recurring_deposit_accounts_account_id_response_instance.to_dict()
# create an instance of PutRecurringDepositAccountsAccountIdResponse from a dict
put_recurring_deposit_accounts_account_id_response_from_dict = PutRecurringDepositAccountsAccountIdResponse.from_dict(put_recurring_deposit_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


