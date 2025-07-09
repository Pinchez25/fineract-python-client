# GetClientsSavingsAccountsDepositType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_savings_accounts_deposit_type import GetClientsSavingsAccountsDepositType

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsSavingsAccountsDepositType from a JSON string
get_clients_savings_accounts_deposit_type_instance = GetClientsSavingsAccountsDepositType.from_json(json)
# print the JSON string representation of the object
print GetClientsSavingsAccountsDepositType.to_json()

# convert the object into a dict
get_clients_savings_accounts_deposit_type_dict = get_clients_savings_accounts_deposit_type_instance.to_dict()
# create an instance of GetClientsSavingsAccountsDepositType from a dict
get_clients_savings_accounts_deposit_type_form_dict = get_clients_savings_accounts_deposit_type.from_dict(get_clients_savings_accounts_deposit_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


