# GetPocketSavingAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_number** | **int** |  | [optional] 
**account_type** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**pocket_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_pocket_saving_accounts import GetPocketSavingAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetPocketSavingAccounts from a JSON string
get_pocket_saving_accounts_instance = GetPocketSavingAccounts.from_json(json)
# print the JSON string representation of the object
print GetPocketSavingAccounts.to_json()

# convert the object into a dict
get_pocket_saving_accounts_dict = get_pocket_saving_accounts_instance.to_dict()
# create an instance of GetPocketSavingAccounts from a dict
get_pocket_saving_accounts_form_dict = get_pocket_saving_accounts.from_dict(get_pocket_saving_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


