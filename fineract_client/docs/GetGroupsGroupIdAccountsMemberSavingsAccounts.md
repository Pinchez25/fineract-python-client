# GetGroupsGroupIdAccountsMemberSavingsAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**account_type** | [**GetGroupsGroupIdAccountsMemberLoanType**](GetGroupsGroupIdAccountsMemberLoanType.md) |  | [optional] 
**currency** | [**GetGroupsGroupIdAccountsSavingCurrency**](GetGroupsGroupIdAccountsSavingCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetGroupsGroupIdAccountsSavingStatus**](GetGroupsGroupIdAccountsSavingStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_member_savings_accounts import GetGroupsGroupIdAccountsMemberSavingsAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsMemberSavingsAccounts from a JSON string
get_groups_group_id_accounts_member_savings_accounts_instance = GetGroupsGroupIdAccountsMemberSavingsAccounts.from_json(json)
# print the JSON string representation of the object
print(GetGroupsGroupIdAccountsMemberSavingsAccounts.to_json())

# convert the object into a dict
get_groups_group_id_accounts_member_savings_accounts_dict = get_groups_group_id_accounts_member_savings_accounts_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsMemberSavingsAccounts from a dict
get_groups_group_id_accounts_member_savings_accounts_from_dict = GetGroupsGroupIdAccountsMemberSavingsAccounts.from_dict(get_groups_group_id_accounts_member_savings_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


