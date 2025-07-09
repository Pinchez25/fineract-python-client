# PutFixedDepositAccountsAccountIdResponse

PutFixedDepositAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutFixedDepositAccountsChanges**](PutFixedDepositAccountsChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_accounts_account_id_response import PutFixedDepositAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositAccountsAccountIdResponse from a JSON string
put_fixed_deposit_accounts_account_id_response_instance = PutFixedDepositAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutFixedDepositAccountsAccountIdResponse.to_json())

# convert the object into a dict
put_fixed_deposit_accounts_account_id_response_dict = put_fixed_deposit_accounts_account_id_response_instance.to_dict()
# create an instance of PutFixedDepositAccountsAccountIdResponse from a dict
put_fixed_deposit_accounts_account_id_response_from_dict = PutFixedDepositAccountsAccountIdResponse.from_dict(put_fixed_deposit_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


