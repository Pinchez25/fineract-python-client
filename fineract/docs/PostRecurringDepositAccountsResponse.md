# PostRecurringDepositAccountsResponse

PostRecurringDepositAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_accounts_response import PostRecurringDepositAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositAccountsResponse from a JSON string
post_recurring_deposit_accounts_response_instance = PostRecurringDepositAccountsResponse.from_json(json)
# print the JSON string representation of the object
print PostRecurringDepositAccountsResponse.to_json()

# convert the object into a dict
post_recurring_deposit_accounts_response_dict = post_recurring_deposit_accounts_response_instance.to_dict()
# create an instance of PostRecurringDepositAccountsResponse from a dict
post_recurring_deposit_accounts_response_form_dict = post_recurring_deposit_accounts_response.from_dict(post_recurring_deposit_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


