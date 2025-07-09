# PutFixedDepositAccountsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_amount** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_accounts_changes import PutFixedDepositAccountsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositAccountsChanges from a JSON string
put_fixed_deposit_accounts_changes_instance = PutFixedDepositAccountsChanges.from_json(json)
# print the JSON string representation of the object
print(PutFixedDepositAccountsChanges.to_json())

# convert the object into a dict
put_fixed_deposit_accounts_changes_dict = put_fixed_deposit_accounts_changes_instance.to_dict()
# create an instance of PutFixedDepositAccountsChanges from a dict
put_fixed_deposit_accounts_changes_from_dict = PutFixedDepositAccountsChanges.from_dict(put_fixed_deposit_accounts_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


