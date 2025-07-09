# GetFixedDepositAccountsAccountIdSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**currency** | [**GetFixedDepositAccountsAccountIdCurrency**](GetFixedDepositAccountsAccountIdCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_account_id_summary import GetFixedDepositAccountsAccountIdSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsAccountIdSummary from a JSON string
get_fixed_deposit_accounts_account_id_summary_instance = GetFixedDepositAccountsAccountIdSummary.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositAccountsAccountIdSummary.to_json()

# convert the object into a dict
get_fixed_deposit_accounts_account_id_summary_dict = get_fixed_deposit_accounts_account_id_summary_instance.to_dict()
# create an instance of GetFixedDepositAccountsAccountIdSummary from a dict
get_fixed_deposit_accounts_account_id_summary_form_dict = get_fixed_deposit_accounts_account_id_summary.from_dict(get_fixed_deposit_accounts_account_id_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


