# PutSavingsAccountsAccountIdResponse

PutSavingsAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSavingsAccountsChanges**](PutSavingsAccountsChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_accounts_account_id_response import PutSavingsAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsAccountsAccountIdResponse from a JSON string
put_savings_accounts_account_id_response_instance = PutSavingsAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutSavingsAccountsAccountIdResponse.to_json())

# convert the object into a dict
put_savings_accounts_account_id_response_dict = put_savings_accounts_account_id_response_instance.to_dict()
# create an instance of PutSavingsAccountsAccountIdResponse from a dict
put_savings_accounts_account_id_response_from_dict = PutSavingsAccountsAccountIdResponse.from_dict(put_savings_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


