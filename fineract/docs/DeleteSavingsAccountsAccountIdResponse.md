# DeleteSavingsAccountsAccountIdResponse

DeleteSavingsAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_savings_accounts_account_id_response import DeleteSavingsAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSavingsAccountsAccountIdResponse from a JSON string
delete_savings_accounts_account_id_response_instance = DeleteSavingsAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteSavingsAccountsAccountIdResponse.to_json()

# convert the object into a dict
delete_savings_accounts_account_id_response_dict = delete_savings_accounts_account_id_response_instance.to_dict()
# create an instance of DeleteSavingsAccountsAccountIdResponse from a dict
delete_savings_accounts_account_id_response_form_dict = delete_savings_accounts_account_id_response.from_dict(delete_savings_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


