# PutFixedDepositAccountsAccountIdRequest

PutFixedDepositAccountsAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_amount** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_accounts_account_id_request import PutFixedDepositAccountsAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositAccountsAccountIdRequest from a JSON string
put_fixed_deposit_accounts_account_id_request_instance = PutFixedDepositAccountsAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print PutFixedDepositAccountsAccountIdRequest.to_json()

# convert the object into a dict
put_fixed_deposit_accounts_account_id_request_dict = put_fixed_deposit_accounts_account_id_request_instance.to_dict()
# create an instance of PutFixedDepositAccountsAccountIdRequest from a dict
put_fixed_deposit_accounts_account_id_request_form_dict = put_fixed_deposit_accounts_account_id_request.from_dict(put_fixed_deposit_accounts_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


