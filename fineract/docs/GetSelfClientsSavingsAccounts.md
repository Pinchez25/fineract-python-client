# GetSelfClientsSavingsAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**currency** | [**GetSelfClientsSavingsAccountsCurrency**](GetSelfClientsSavingsAccountsCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetSelfClientsSavingsAccountsStatus**](GetSelfClientsSavingsAccountsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_savings_accounts import GetSelfClientsSavingsAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsSavingsAccounts from a JSON string
get_self_clients_savings_accounts_instance = GetSelfClientsSavingsAccounts.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsSavingsAccounts.to_json()

# convert the object into a dict
get_self_clients_savings_accounts_dict = get_self_clients_savings_accounts_instance.to_dict()
# create an instance of GetSelfClientsSavingsAccounts from a dict
get_self_clients_savings_accounts_form_dict = get_self_clients_savings_accounts.from_dict(get_self_clients_savings_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


