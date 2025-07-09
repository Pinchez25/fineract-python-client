# GetClientsSavingsAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**currency** | [**GetClientsSavingsAccountsCurrency**](GetClientsSavingsAccountsCurrency.md) |  | [optional] 
**deposit_type** | [**GetClientsSavingsAccountsDepositType**](GetClientsSavingsAccountsDepositType.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**short_product_name** | **str** |  | [optional] 
**status** | [**GetClientsSavingsAccountsStatus**](GetClientsSavingsAccountsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_savings_accounts import GetClientsSavingsAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsSavingsAccounts from a JSON string
get_clients_savings_accounts_instance = GetClientsSavingsAccounts.from_json(json)
# print the JSON string representation of the object
print(GetClientsSavingsAccounts.to_json())

# convert the object into a dict
get_clients_savings_accounts_dict = get_clients_savings_accounts_instance.to_dict()
# create an instance of GetClientsSavingsAccounts from a dict
get_clients_savings_accounts_from_dict = GetClientsSavingsAccounts.from_dict(get_clients_savings_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


