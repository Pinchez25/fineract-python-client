# PutRecurringDepositAccountsAccountIdRequest

PutRecurringDepositAccountsAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_amount** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_accounts_account_id_request import PutRecurringDepositAccountsAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositAccountsAccountIdRequest from a JSON string
put_recurring_deposit_accounts_account_id_request_instance = PutRecurringDepositAccountsAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutRecurringDepositAccountsAccountIdRequest.to_json())

# convert the object into a dict
put_recurring_deposit_accounts_account_id_request_dict = put_recurring_deposit_accounts_account_id_request_instance.to_dict()
# create an instance of PutRecurringDepositAccountsAccountIdRequest from a dict
put_recurring_deposit_accounts_account_id_request_from_dict = PutRecurringDepositAccountsAccountIdRequest.from_dict(put_recurring_deposit_accounts_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


