# PutRecurringDepositAccountsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_amount** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_accounts_changes import PutRecurringDepositAccountsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositAccountsChanges from a JSON string
put_recurring_deposit_accounts_changes_instance = PutRecurringDepositAccountsChanges.from_json(json)
# print the JSON string representation of the object
print(PutRecurringDepositAccountsChanges.to_json())

# convert the object into a dict
put_recurring_deposit_accounts_changes_dict = put_recurring_deposit_accounts_changes_instance.to_dict()
# create an instance of PutRecurringDepositAccountsChanges from a dict
put_recurring_deposit_accounts_changes_from_dict = PutRecurringDepositAccountsChanges.from_dict(put_recurring_deposit_accounts_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


