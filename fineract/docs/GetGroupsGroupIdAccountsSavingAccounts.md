# GetGroupsGroupIdAccountsSavingAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**account_type** | [**GetGroupsGroupIdAccountsSavingAccountType**](GetGroupsGroupIdAccountsSavingAccountType.md) |  | [optional] 
**currency** | [**GetGroupsGroupIdAccountsSavingCurrency**](GetGroupsGroupIdAccountsSavingCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetGroupsGroupIdAccountsSavingStatus**](GetGroupsGroupIdAccountsSavingStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_saving_accounts import GetGroupsGroupIdAccountsSavingAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsSavingAccounts from a JSON string
get_groups_group_id_accounts_saving_accounts_instance = GetGroupsGroupIdAccountsSavingAccounts.from_json(json)
# print the JSON string representation of the object
print GetGroupsGroupIdAccountsSavingAccounts.to_json()

# convert the object into a dict
get_groups_group_id_accounts_saving_accounts_dict = get_groups_group_id_accounts_saving_accounts_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsSavingAccounts from a dict
get_groups_group_id_accounts_saving_accounts_form_dict = get_groups_group_id_accounts_saving_accounts.from_dict(get_groups_group_id_accounts_saving_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


