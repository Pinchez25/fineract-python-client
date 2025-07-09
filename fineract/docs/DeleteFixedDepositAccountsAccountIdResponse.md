# DeleteFixedDepositAccountsAccountIdResponse

DeleteFixedDepositAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_fixed_deposit_accounts_account_id_response import DeleteFixedDepositAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFixedDepositAccountsAccountIdResponse from a JSON string
delete_fixed_deposit_accounts_account_id_response_instance = DeleteFixedDepositAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteFixedDepositAccountsAccountIdResponse.to_json()

# convert the object into a dict
delete_fixed_deposit_accounts_account_id_response_dict = delete_fixed_deposit_accounts_account_id_response_instance.to_dict()
# create an instance of DeleteFixedDepositAccountsAccountIdResponse from a dict
delete_fixed_deposit_accounts_account_id_response_form_dict = delete_fixed_deposit_accounts_account_id_response.from_dict(delete_fixed_deposit_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


