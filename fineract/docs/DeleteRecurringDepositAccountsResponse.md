# DeleteRecurringDepositAccountsResponse

DeleteRecurringDepositAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_recurring_deposit_accounts_response import DeleteRecurringDepositAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRecurringDepositAccountsResponse from a JSON string
delete_recurring_deposit_accounts_response_instance = DeleteRecurringDepositAccountsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteRecurringDepositAccountsResponse.to_json()

# convert the object into a dict
delete_recurring_deposit_accounts_response_dict = delete_recurring_deposit_accounts_response_instance.to_dict()
# create an instance of DeleteRecurringDepositAccountsResponse from a dict
delete_recurring_deposit_accounts_response_form_dict = delete_recurring_deposit_accounts_response.from_dict(delete_recurring_deposit_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


